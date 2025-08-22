import streamlit as st

st.write("## Student reg page, Karan Bhat")

name = st.text_input(label="Enter your name", )
age = st.number_input(label="Enter your age", min_value=1, max_value=100, step=1)
mob_no = st.text_input(label="Enter your mobile number")
email = st.text_input(label="Enter your email id")
dob = st.date_input(label="Enter your date of birth")
cgpa = st.slider(label="Enter your cgpa", min_value=0.0, max_value=10.0, step=0.1)
remarks = st.text_area(label="Enter your remarks")


if st.button(label="Submit application"):
    st.write("Application submitted successfully")
    st.write("Name: ", name)
    st.write("Age: ", age)
    st.write("Mobile Number: ", mob_no)
    st.write("Email ID: ", email)
    st.write("Date of Birth: ", dob)
    st.write("CGPA: ", cgpa)
    st.write("Remarks: ", remarks)


import numpy as np
x = np.arange(0,100)
y = x**2

st.line_chart(data=y, width=0, height=0, use_container_width=True)

