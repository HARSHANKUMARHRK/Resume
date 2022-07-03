import streamlit as st
import pandas as pd

st.title("Resume")
st.subheader("About Me")

menu=["","Educational Details","Skill Summary","Work Experience","Projects","Contact"]
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
    m1=["","Hand Writing (Good or Bad Prediction)","Face Recognition and Absentees Notifying Model","Data Mining","Virtual Chatbot","College Symposium QR code generator","AI word annotator","Unsupervised K-Means clustering","Web Apps"]
    ch=st.sidebar.selectbox("projects",m1)
    if(ch=="Hand Writing (Good or Bad Prediction)"):
        st.subheader("Hand Writing Predictor Model")
        st.write("🟡 Using trained images, this algorithm predicts the best and worst handwriting based on accuracy (trained image is standard English Alphabets). The predicted model will return good handwriting if its accuracy is the highest, and terrible handwriting if its accuracy is the lowest. I employed Tensorflow, Scikit-Learn, Numpy, and Ml Flow ")
        st.subheader("Technology Stack")
        st.write("1.Tensor Flow")
        st.write("2.Scikit-Learn")
        st.write("3.Flask")
        st.write("4.Ml-Flow")
        st.write("5.Matplotlib")
        st.subheader("Source Code")
        st.write("I have pushed all of my codes to github in my github handle by private repository. Please contact me via email if you want collaborator access.")
        st.write("check out my github handle [link] https://github.com/HARSHANKUMARHRK")

    if(ch=="Face Recognition and Absentees Notifying Model"):
        st.subheader("Face Recognition Model")
        st.write("🟢Due to my increased interest in this field due to the positive growth of machine learning, I began developing a face recognition model. I trained the model using student images as the training dataset, and I tested it using a webcam to see if the faces matched. If they did, the model returned the present and return the time and date of entry, name of the student. If somebody is absent, the absentees dataset will be displayed, and the absentees record will automatically be delivered to the class teacher via e-mail.")
        st.subheader("Technology Stack")
        st.write("1.open CV")
        st.write("2.Flask")
        st.write("3.Numpy")
        st.write("4.MongoDB")
        st.write("5.other local modules")
        st.subheader("Source Code")
        st.write("I have pushed all of my codes to github in my github handle by private repository. Please contact me via email if you want collaborator access.")
        st.write("check out my github handle [link] https://github.com/HARSHANKUMARHRK")


    if(ch=="Data Mining"):
        st.subheader("Data Mining")
        st.write("🟦I chose an IPL Match Dataset and performed EDA (Exploratory Data Analysis) on this data set because I believe that analysing and delving ever further into an area creates and nurtures a great interest in that field. and regressions, which predicted some data.")
        st.subheader("Modules Used")
        st.write("1.plotly")
        st.write("2.matplotlib")
        st.write("Numpy")
        st.write("Pandas")
        st.subheader("Source Code")
        st.write("I have pushed all of my codes to github in my github handle by private repository. Please contact me via email if you want collaborator access.")
        st.write("check out my github handle [link] https://github.com/HARSHANKUMARHRK")


    if(ch=="Virtual Chatbot"):
        st.subheader("Virtual chatbot using RASA BOT")
        st.write("🟤Virtual bots are becoming more and more like humans these days thanks to the integration of AI in everything. I've done  a virtual chat bot for clarifying queries about hotels and their availability, local cuisine, location, etc. where a lot of data is thrown out as questions and pertinent responses are taught appropriately.")
        st.subheader("Technolgy Used")
        st.write("1.RASA BOT")
        st.subheader("Source Code")
        st.write("I have pushed all of my codes to github in my github handle by private repository. Please contact me via email if you want collaborator access.")
        st.write("check out my github handle [link] https://github.com/HARSHANKUMARHRK")


    if(ch=="College Symposium QR code generator"):
        st.subheader("Basic details form and QR code generator in Streamlit")
        st.write("🟩Our college is hosting a symposium, so my team and I volunteered to support our seniors with the building of a web app to collect basic registration information. Once registered, information is then exported to a CSV file for future use, and all information is stored in a QR code. Then the enrolled candidate is subsequently sent the QR code through registered mail ID.")
    
        st.subheader("Technology Used")
        st.write("1.Streamlit")
        st.write("2.QR Code")
        st.subheader("Source Code")
        st.write("I have pushed all of my codes to github in my github handle by private repository. Please contact me via email if you want collaborator access.")
        st.write("check out my github handle [link] https://github.com/HARSHANKUMARHRK")

    if(ch=="AI word annotator"):
        st.subheader("AI word annotator")
        st.write("🟥A tool similar to Grammarly, AI Word Annotator uses natural language processing (textblob) and is applied in a web application to fix misspelt words that are related to the word in dispute.")
        st.subheader("Technology Used")
        st.write("1.Streamlit")
        st.write("2.Textblob")
        st.write("3.text_annotator")
        st.subheader("Source Code")
        st.write("I have pushed all of my codes to github in my github handle by private repository. Please contact me via email if you want collaborator access.")
        st.write("check out my github handle [link] https://github.com/HARSHANKUMARHRK")

    if(ch=="Unsupervised K-Means clustering"):
        st.subheader("K-means clustering")
        st.write("🟪K-Means clustering transforms unlabeled groups of data into labelled groups of data. It is an unsupervised machine learning technique. I converted an unlabeled mall dataset into labelled data by determining the K-Means value.")
        st.subheader("Technology Used")
        st.write("1.K-Means")
        st.write("2.Regressions")
        st.write("3.Matplotlib")
        st.write("4.Seaborn")
        st.write("5.Pandas")
        st.subheader("Source Code")
        st.write("I have pushed all of my codes to github in my github handle by private repository. Please contact me via email if you want collaborator access.")
        st.write("check out my github handle [link] https://github.com/HARSHANKUMARHRK")


if(choice=="Contact"):
    st.subheader("Contact Details")
    st.image("github.png",width=60)
    if st.button("github profile"):
        st.write("https://github.com/HARSHANKUMARHRK")
    st.image("med.png",width=120)
    if st.button("blog page link"):
        st.write("https://medium.com/@harshankumarhrk")
    st.image("mai.jpg",width=60)
    if st.button("mail id"):
        st.success("harshankumarhrk@gmail.com")
    st.image("linkedin.png",width=120)
    if st.button("linkedin profile"):
        st.write("https://www.linkedin.com/in/kishore-harshan-kumar-388279224/")
    st.image("ph.png",width=60)
    if st.button("number"):
        st.write("7540081803")
    st.image("Instagram.png",width=80)
    if st.button("Handle"):
        st.write("https://www.instagram.com/harshankumarhrk/")



        


