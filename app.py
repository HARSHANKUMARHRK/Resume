import streamlit as st

st.title("Resume")
st.subheader("About Me")
menu=["","Educational Details","Skill Summary","Work Experience","Projects"]
choice=st.sidebar.selectbox("Menu",menu)