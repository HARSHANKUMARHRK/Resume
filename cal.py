import streamlit as st
import pandas as pd
st.title("GPA Calculator")


st.write("Enter your English Grade ")
a=st.selectbox("Grade",("O","A+","A","B+","B","C+","C"))
if(a=="O"):
    b=10*3
elif(a=="A+"):
    b=9*3
elif(a=="A"):
    b=8*3
elif(a=="B+"):
    b=7*3
elif(a=="B"):
    b=6*3
elif(a=="C+"):
    b=5*3
else:
    b=4*3
st.write("You selected",a)
st.write("Your grade point",b)

st.write("Enter Your Maths GRADE")
c=st.selectbox("Maths Grade",("O","A+","A","B+","B","C+","C"))
if(c=="O"):
    d=10*4
elif(c=="A+"):
    d=9*4
elif(c=="A"):
    d=8*4
elif(c=="B+"):
    d=7*4
elif(c=="B"):
    d=6*4
elif(c=="C+"):
    d=5*4
else:
    d=4*4

st.write("You selected",c)
st.write("Your grade point",d)

st.write("Enter Your EVS GRADE")
e=st.selectbox("EVS Grade",("O","A+","A","B+","B","C+","C"))
if(e=="O"):
    f=10*3
elif(e=="A+"):
    f=9*3
elif(e=="A"):
    f=8*3
elif(e=="B+"):
    f=7*3
elif(e=="B"):
    f=6*3
elif(e=="C+"):
    f=5*3
else:
    f=4*3
st.write("You selected",e)
st.write("Your grade point",f)

st.write("Enter Your Pysics GRADE")
g=st.selectbox("Physics Grade",("O","A+","A","B+","B","C+","C"))
if(g=="O"):
    h=10*3
elif(g=="A+"):
    h=9*3
elif(g=="A"):
    h=8*3
elif(g=="B+"):
    h=7*3
elif(g=="B"):
    h=6*3
elif(g=="C+"):
    h=5*3
else:
    h=4*3

st.write("You selected",g)
st.write("Your grade point",h)

st.write("Enter Your C  GRADE")
i=st.selectbox("C Grade",("O","A+","A","B+","B","C+","C"))
if(i=="O"):
    j=10*3
elif(i=="A+"):
    j=9*3
elif(i=="A"):
    j=8*3
elif(i=="B+"):
    j=7*3
elif(i=="B"):
    j=6*3
elif(i=="C+"):
    j=5*3
else:
    j=4*3

st.write("You selected",i)
st.write("Your grade point",j)

st.write("Enter Your BEEE GRADE")
k=st.selectbox("EG Grade",("O","A+","A","B+","B","C+","C"))
if(k=="O"):
    l=10*3
elif(k=="A+"):
    l=9*3
elif(k=="A"):
    l=8*3
elif(k=="B+"):
    l=7*3
elif(k=="B"):
    l=6*3
elif(k=="C+"):
    l=5*3
else:
    l=4*3

st.write("You selected",k)
st.write("Your grade point",l)

st.write("Enter Your EP Laboratory GradE")
o=st.selectbox("EP ",("O","A+","A","B+","B","C+","C"))
if(o=="O"):
    p=10*2
elif(o=="A+"):
    p=9*2
elif(o=="A"):
    p=8*2
elif(o=="B+"):
    p=7*2
elif(o=="B"):
    p=6*2
elif(o=="C+"):
    p=5*2
else:
    p=4*2

st.write("You selected",o)
st.write("Your grade point",p)

st.write("Enter Your C Laboratory Grade Mark")
q=st.selectbox("C laboratory Grade",("O","A+","A","B+","B","C+","C"))
if(q=="O"):
    r=10*2
elif(q=="A+"):
    r=9*2
elif(q=="A"):
    r=8*2
elif(q=="B+"):
    r=7*2
elif(q=="B"):
    r=6*2
elif(q=="C+"):
    r=5*2
else:
    r=4*2

st.write("You selected",q)
st.write("Your grade point",r)


m=(b+d+f+h+j+l+p+r)
res=m/23
st.subheader("GPA")
st.success(res)