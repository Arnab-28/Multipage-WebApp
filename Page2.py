import streamlit as st

def page2(navigate):
    st.title("Page 2")
    st.write("This is the final page.")

    st.button("← Back", on_click=lambda: navigate("Page1"))
