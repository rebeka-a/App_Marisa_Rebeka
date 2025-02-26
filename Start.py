import streamlit as st
import pandas as pd

st.title("Meine erste Streamlit App")

st.write("Diese App wurde von Marisa und Rebeka entwickelt.")
st.write("Marisa von Fellenberg: vonfemar@students.zhaw.ch") 
st.write("Rebeka Ammann: ammanre1@students.zhaw.ch")
st.write("Durch diese App wird es ihnen möglich ihre Daten zu organisieren und abzurufen.")
if st.button("Welt retten", icon="🌍") :
    st.write("Booooom! 🌎💥🔥")
