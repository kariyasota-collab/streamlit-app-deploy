import streamlit as st
from datetime import datetime

st.set_page_config(page_title="CHECK_8503")
st.title("CHECK_8503")
st.write("APP LOADED")
st.caption(f"loaded from: {__file__}")
st.caption(f"rendered at: {datetime.now():%Y-%m-%d %H:%M:%S}")