import streamlit as st
from utils.data_manager import DataManager
from datetime import datetime

from App_Marisa_Rebeka.utils.data_manager import DataManager

# Page Configuration
st.set_page_config(page_title="BMI Rechner", page_icon="📄", layout="wide")

# Title
st.title("BMI Rechner 🏋️‍♂️")

# User Input for Height and Weight
height = st.number_input("Geben Sie Ihre Grösse in cm ein:", min_value=0.0, format="%.2f")
weight = st.number_input("Geben Sie Ihr Gewicht in kg ein:", min_value=0.0, format="%.2f")

# Calculate BMI
if st.button("BMI berechnen"):
    if height > 0 and weight > 0:
        bmi = weight / ((height / 100) ** 2)
        st.write(f"### Ihr BMI ist: **{bmi:.2f}**")

        # BMI Classification
        if bmi < 18.5:
            st.warning("🔸 Sie sind **untergewichtig**.")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ Sie haben ein **normales Gewicht**. Gut gemacht! 🎉")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ Sie sind **übergewichtig**.")
        else:
            st.error("❌ Sie sind **adipös**. Bitte sprechen Sie mit einem Arzt.")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create result dictionary with timestamp
        result = {
            "timestamp": timestamp,
            "height": height,
            "weight": weight,
            "bmi": bmi,
        }

    else:
        st.error("Bitte geben Sie gültige Werte für Größe und Gewicht ein.")

# BMI Image
st.image(
    "https://www.zurrose.ch/sites/default/files/styles/media_w1166/public/media/images/ZRS_ADIPOSITAS_1%20%282%29.png.webp?h=e53d47f6&itok=XTap7IX1",
    use_container_width=True)

# Define the result dictionary with relevant data
result = {
    "height": height,
    "weight": weight,
    "bmi": bmi if 'bmi' in locals() else None
}
# update data in session state and save to persistent storage
DataManager().append_record(session_state_key='data_df', record_dict=result)
