import time
import streamlit as st
st.title('Pomodoro Timer')


my_time = 25
while my_time > 0:
    st.title(f'{my_time}')
    time.sleep(1)
    my_time -= 1
