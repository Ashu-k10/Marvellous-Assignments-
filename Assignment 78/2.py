# Develop a streamlit Application that accepts an integers from the user. Provide a check button to determine whether the entered number is even or odd and display the result

import streamlit as st

st.title("Even or Odd Checker")

# Accept an integer from the user 
num = st.number_input("Enter an integer",value=0, step=1)

# Check button
if st.button("Check"):
    if num % 2 == 0:
        st.success("The number is Even")
    else:
        st.warning("The Number is Odd")

