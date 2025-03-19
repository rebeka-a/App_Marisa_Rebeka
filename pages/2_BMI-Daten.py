import streamlit as st
import pandas as pd

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

st.title("BMI-Daten")

st.write("Diese Seite zeigt Ihre BMI-Daten an.")


data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine BMI Daten vorhanden. Berechnen Sie Ihren BMI auf der Startseite.')
    st.stop()

# Ensure 'timestamp' is in datetime format
data_df['timestamp'] = pd.to_datetime(data_df['timestamp'], errors='coerce')

# Sort dataframe by timestamp
data_df = data_df.sort_values('timestamp', ascending=False)

# Round BMI to one decimal place
data_df['bmi'] = data_df['bmi'].round(1)

# Add BMI category
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Untergewicht"
    elif 18.5 <= bmi < 24.9:
        return "Normalgewicht"
    elif 25 <= bmi < 29.9:
        return "Übergewicht"
    else:
        return "Adipositas"

data_df['Kategorie'] = data_df['bmi'].apply(categorize_bmi)

# Rename columns for display
data_df = data_df.rename(columns={
    'timestamp': 'Datum und Uhrzeit',
    'height': 'Körpergrösse (cm)',
    'weight': 'Gewicht (kg)',
    'bmi': 'BMI'
})

# Display table
st.dataframe(data_df)