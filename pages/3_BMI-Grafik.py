# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# === BMI Grafik ===
import streamlit as st

st.title('BMI Verlauf')

st.write('Hier sehen Sie Ihren BMI und Ihr Gewicht über die Zeit, in einer übersichtlichen Graphik dargestellt.')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine BMI Daten vorhanden. Berechnen Sie Ihren BMI auf der Startseite.')
    st.stop()

# Weight over time
st.line_chart(data=data_df.set_index('timestamp')['weight'], 
                use_container_width=True)
st.caption('Gewicht über Zeit (kg)')


# BMI over time
st.line_chart(data=data_df.set_index('timestamp')['bmi'],
                use_container_width=True)
st.caption('BMI über Zeit')
