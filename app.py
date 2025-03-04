import streamlit as st
from Home import home_page
from Page1 import page1
from Page2 import page2

# Initialize session state for navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Function to navigate between pages
def navigate(page):
    st.session_state.current_page = page
    
# Render pages based on session state
if st.session_state.current_page == "Home":
    home_page(navigate)
elif st.session_state.current_page == "Page1":
    page1(navigate)
elif st.session_state.current_page == "Page2":
    page2(navigate)
