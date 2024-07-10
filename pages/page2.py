from navigation import make_sidebar
import streamlit as st
from time import sleep

make_sidebar()

st.markdown("# Data Input")
        # Add data input components here
        # File uploader
uploaded_file1 = st.file_uploader("Upload the Training Dataset", type=['csv', 'xlsx'], key="file1")
uploaded_file2 = st.file_uploader("Upload the Testing Dataset", type=['csv', 'xlsx'], key="file2")

        # Train button
if uploaded_file1 and uploaded_file2:
   
    if st.button("Train", type="primary"):
        st.session_state.logged_in = True  # Assuming you have this session_state variable set elsewhere
        st.success("Training started!")
        sleep(0.5)
        st.switch_page("pages/page3.py")
