import streamlit as st

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

    else:
        st.error("Bitte geben Sie gültige Werte für Größe und Gewicht ein.")

# BMI Image
st.image(
    "https://www.zurrose.ch/sites/default/files/styles/media_w1166/public/media/images/ZRS_ADIPOSITAS_1%20%282%29.png.webp?h=e53d47f6&itok=XTap7IX1",
    use_container_width=True
)
