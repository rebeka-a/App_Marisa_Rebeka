import streamlit as st
from datetime import datetime
from utils.data_manager import DataManager

st.set_page_config(page_title="BMI Rechner", page_icon="📄", layout="wide")  # Nur einmal aufrufen!

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# Initialisiere DataManager
data_manager = DataManager()

if "data_df" not in st.session_state:
    data_manager.load_app_data(session_state_key="data_df", file_name="data.csv", initial_value=[])

# Entferne diesen doppelten Aufruf!
# st.set_page_config(page_title="BMI Rechner", page_icon="📄", layout="wide")

st.title("BMI Rechner 🏋️‍♂️")
st.write("Willst auch du deinen BMI wissen? Trag deine Daten ein, klikke auf den Button und finde es heraus!")

height = st.number_input("Geben Sie Ihre Grösse in cm ein:", min_value=0.0, format="%.2f")
weight = st.number_input("Geben Sie Ihr Gewicht in kg ein:", min_value=0.0, format="%.2f")

bmi = None
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Zeitstempel wird IMMER gesetzt

if st.button("BMI berechnen"):
    if height > 0 and weight > 0:
        bmi = weight / ((height / 100) ** 2)
        st.write(f"### Ihr BMI ist: **{bmi:.2f}**")

        if bmi < 18.5:
            st.warning("🔸 Sie sind **untergewichtig**.")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ Sie haben ein **normales Gewicht**. Gut gemacht! 🎉")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ Sie sind **übergewichtig**.")
        else:
            st.error("❌ Sie sind **adipös**. Bitte sprechen Sie mit einem Arzt.")

    else:
        st.error("Bitte geben Sie gültige Werte für Größe und Gewicht ein.")

st.image(
    "https://www.zurrose.ch/sites/default/files/styles/media_w1166/public/media/images/ZRS_ADIPOSITAS_1%20%282%29.png.webp?h=e53d47f6&itok=XTap7IX1",
    use_container_width=True
)

# Ergebnis-Dictionary enthält IMMER 'timestamp'
result = {
    "timestamp": timestamp,
    "height": height,
    "weight": weight,
    "bmi": bmi
}

# Speichere Daten nur, wenn eine gültige Eingabe gemacht wurde
if bmi is not None:
    data_manager.append_record(session_state_key="data_df", record_dict=result)