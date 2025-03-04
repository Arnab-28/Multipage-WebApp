import streamlit as st

def page1(navigate):
    st.title("Page 1")
    st.write("This is Page 1.")

    col1, col2 = st.columns([1,1])
    
    with col1:
        st.button("← Back", on_click=lambda: navigate("Home"))
    
    with col2:
        st.button("Next →", on_click=lambda: navigate("Page2"))
