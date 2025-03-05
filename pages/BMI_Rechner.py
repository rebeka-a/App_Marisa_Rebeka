import streamlit as st

st.title("BMI Rechner")
height = st.number_input("Geben Sie Ihre Größe in cm ein:", min_value=0.0, format="%.2f")
weight = st.number_input("Geben Sie Ihr Gewicht in kg ein:", min_value=0.0, format="%.2f")

if st.button("BMI berechnen"):
    if height > 0 and weight > 0:
        bmi = weight / ((height / 100) ** 2)
        st.write(f"Ihr BMI ist: {bmi:.2f}")
        if bmi < 18.5:
            st.write("Sie sind untergewichtig.")
        elif 18.5 <= bmi < 24.9:
            st.write("Sie haben ein normales Gewicht.")
        elif 25 <= bmi < 29.9:
            st.write("Sie sind übergewichtig.")
        else:
            st.write("Sie sind adipös.")
    else:
        st.write("Bitte geben Sie gültige Werte für Größe und Gewicht ein.")

st.image(
        "https://www.zurrose.ch/sites/default/files/styles/media_w1166/public/media/images/ZRS_ADIPOSITAS_1%20%282%29.png.webp?h=e53d47f6&itok=XTap7IX1",
        caption=None,
        width=None,
        use_column_width=None,
        clamp=False,
        channels="RGB",
        output_format="auto",
        use_container_width=False
    )
