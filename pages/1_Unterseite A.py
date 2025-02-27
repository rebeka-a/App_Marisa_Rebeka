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

