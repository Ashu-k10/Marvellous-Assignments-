#Develop a streamlit application that accepts two numbers from the user using input fields.Provide an Add button to calculate and display the addition of the entered numbers
import streamlit as st

st.title("Addition Calculation")

#Accepting the two number 
num1 = st.number_input("Enter the first Number :",value=0.0)
num2 = st.number_input("Enter the Second Number :",value=0.0)

if st.button("Add"):
    result = num1 + num2
    st.success(f"Addition is:{result}")

