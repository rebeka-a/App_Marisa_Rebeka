import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# Initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="App_Marisa_Rebeka")  # switch drive

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# Load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value=pd.DataFrame(), 
    parse_dates=['timestamp']
)
st.title("Unsere erste Streamlit App -- ein BMI-Rechner!")
st.write("Diese App wurde von Marisa und Rebeka im Rahmen des BMLD-Studiums entwickelt.")
st.write("Durch diese App kannst du ganz leicht deinen BMI berechnen.")
st.write("Der BMI ist eine bestimmte Grösse, welche das Verhältniss zwischen Gewicht und Körpergrösse angibt. Durch den BMI kann man heruas finden, ob man einen gesundes Gewicht hat oder nicht.")
st.write("Viel Spass beim Ausprobieren!")


st.title("Unsere Kontaktdaten:")
st.write("Marisa von Fellenberg: vonfemar@students.zhaw.ch")
st.write("Rebeka Ammann: ammanre1@students.zhaw.ch")