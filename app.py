import streamlit as st
import pandas as pd

st.title("Resume")
m2=["About Me","Menu"]
ch2=st.selectbox("Informations",m2)
if(ch2=="About Me"):
    st.image("mine.jpeg")
    st.title("About Me")

    st.subheader("Myself, R.Kishore Harshan Kumar im currently pursuing BTech.Artificial Intelligence And Data Science in St Joseph's College Of Engineering. i have done my schoolings in Kamlavati Senior Secondary School (CBSE). im from BIO stream background therefore didn't initially have much knowledge of computer science and its various branches. I'm quite happy to be working in this profession and eager to learn more technical information. These technical issues always require me to start my searches over. As a student of computer science, I'm quite excited to go on this path of new experiences.")

if(ch2=="Menu"):
    menu=["","Educational Details","Skill Summary","Work Experience","Technolgies Worked On","Projects","Online course certifications","Articles","Contact"]
    choice=st.sidebar.selectbox("Menu",menu)
    if(choice=="Educational Details"):
        a = st.container()
        b = st.container()
        with a:
            st.title("College Details,School Details and additional course completion")
    
        with b:
            data= pd.read_csv("edu.csv")
            data2=pd.read_csv("sch.csv")
            data3=pd.read_csv("ext.csv")
            st.table(data)
            st.table(data2)
            st.table(data3)

    if(choice=="Projects"):
        m1=["","Hand Writing (Good or Bad Prediction)","Face Recognition and Absentees Notifying Model","Data Mining","Virtual Chatbot","College Symposium QR code generator","AI word annotator","Unsupervised K-Means clustering","Web Apps"]
        ch=st.selectbox("projects",m1)
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


    if(choice=="Online course certifications"):
        st.title("Certifications")
        st.subheader("Google Data Analytics:")
        st.image("google.jpeg")
        st.subheader("AWS:")
        st.image("AWS.jpeg")
        st.subheader("Diploma In Step Into RPA:")
        st.image("RPA.jpeg")
        st.subheader("K-Means:")
        st.image("kmeans.jpeg")
        st.subheader("MongoDB:")
        st.image("mongodb.jpeg")
        st.subheader("QR Project:")
        st.image("qr.jpeg")
        st.subheader("LINUX:")
        st.image("linux.jpeg")
        st.subheader("Credit Card Fraud Detection:")
        st.image("credit.jpeg")
        st.subheader("Flask:")
        st.image("flask.jpeg")
        st.subheader("Data Mining:")
        st.image("data.jpeg")
        st.subheader("Pygame:")
        st.image("pygame.jpeg")
        st.subheader("ChatBOT:")
        st.image("chatbot.jpeg")
        st.subheader("Textblob")
        st.image("text.jpeg")
        st.subheader("Webinar on Bilding ChatBOT:")
        st.image("webinar.jpeg")
        st.subheader("Nestle Virtual Internship:")
        st.image("nestle.jpeg")

    if(choice=="Articles"):
        st.title("Medium Articles")  
        st.warning("Follow Me on Medium For More Technical Stuffs")
        st.image("med.png",width=120)
        if st.button("blog page link"):
            st.write("https://medium.com/@harshankumarhrk")
        df=pd.read_csv("med.csv")
        st.table(df)  

    if(choice=="Work Experience"):
        st.title("Work Experience")
        st.subheader("Internships:")
        st.subheader("**TactLabs**")
     
        st.image("tactlabs.jpeg",width=500)
        st.subheader("Role-Developer Intern") 
        st.write("The Canadian company TactLabs is a technological organisation with a small research team that specialises in MLOps (MaaMs) and ML-related activities. In this organisation, I learned a lot of technical information (priorly on machine learning). More than that, I had great team members and a senior leader who helped us learn more. This platform makes more opportunities available to Tamil Nadu's public school children. We interns will conduct knowledge transfer sessions for these students, which will increase their interest both technically and emotionally.")
        st.subheader("**National Engineering Olympiad**")
        st.image("neo.png",width=150)
        st.write("Gained knowledge about digital marketing and learned to do marketing in different ideas and innovations ")
    
    

   



        


