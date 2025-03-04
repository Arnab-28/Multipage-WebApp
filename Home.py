import streamlit as st

def home_page(navigate):
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
    
    # Navigation button at the bottom
    st.button("Next →", on_click=lambda: navigate("Page1"))
