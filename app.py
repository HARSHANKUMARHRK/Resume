import streamlit as st
import pandas as pd

st.title("Resume")
st.subheader("About Me")

menu=["","Educational Details","Skill Summary","Work Experience","Projects"]
choice=st.sidebar.selectbox("Menu",menu)
if(choice=="Educational Details"):
    a = st.container()
    b = st.container()
    with a:
        st.title("College Details and School Details")
    
    with b:
        data= pd.read_csv("edu.csv")
        data2=pd.read_csv("sch.csv")
        st.table(data)
        st.table(data2)

if(choice=="Projects"):
    m1=["Linear Regression(Bitcoin Prediction)","Face Recognition and Absentees Notifying Model"]
    ch=st.sidebar.selectbox("projects",m1)