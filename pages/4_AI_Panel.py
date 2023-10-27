import streamlit as st
from  functions.login import get_loginform
from functions.pagesetup import set_title, set_page_overview


st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

if 'authenticated' not in st.session_state:
    get_loginform()
elif not st.session_state.authenticated:
    get_loginform()
else:
    set_title("FEOC", "AI Panel")
    set_page_overview("Overview", "Interact with AI and Autonomous Agents.")