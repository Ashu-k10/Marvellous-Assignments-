# Develop a streamlit Application that accepts a students name and marks in three subjects. Calculate total marks , percentage and display whether the student has passed or failed. Consider 40 Marks out of 100 as the minimum passing marks in each subject

import streamlit as st

st.title("Marvellous Result Calculator")

name = st.text_input("Enter Student name")

m1 = st.number_input("Enter marks in Subject 1",min_value=0, max_value=100, step=1)
m2 = st.number_input("Enter marks in Subject 2",min_value=0, max_value=100, step=1)
m3 = st.number_input("Enter marks in Subject 3",min_value=0, max_value=100, step=1)

# Calculate result
if st.button("Calculate Result"):

    total = m1 + m2 + m3
    percentage = (total / 300) * 100

    st.write("Student Name:", name)
    st.write("Total Marks:", total, "/ 300")
    st.write("Percentage:", round(percentage, 2), "%")

    # Check pass or fail
    if m1 >= 40 and m2 >= 40 and m3 >= 40:
        st.success("Result: PASS")
    else:
        st.error("Result: FAIL")
