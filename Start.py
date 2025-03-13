import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="App_Marisa_Rebeka_Data")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value=pd.DataFrame(), 
    parse_dates=['timestamp']
)

st.sidebar.image(
    "https://cdn2.iconfinder.com/data/icons/health-colored/160/7-512.png",
    use_container_width=True
)

st.title("Unsere erste Streamlit App -- ein BMI-Rechner!")
st.write("Diese App wurde von Marisa und Rebeka im Rahmen des BMLD-Studiums entwickelt.")
st.write("Durch diese App kannst du ganz leicht deinen BMI berechnen.")

st.title("Unsere Kontaktdaten:")
st.write("Marisa von Fellenberg: vonfemar@students.zhaw.ch")
st.write("Rebeka Ammann: ammanre1@students.zhaw.ch")