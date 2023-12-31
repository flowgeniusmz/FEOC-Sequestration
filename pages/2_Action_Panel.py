import streamlit as st
from  functions.login import get_loginform
from functions.pagesetup import set_title, set_page_overview


st.set_page_config(layout="wide")

if 'authenticated' not in st.session_state:
    get_loginform()
elif not st.session_state.authenticated:
    get_loginform()
else:
    set_title("FEOC", "Action Panel")
    set_page_overview("Overview", "The Action Panel contains standard FEOC actions that parties can utilize related to their certificate. Use the tabs below. ")