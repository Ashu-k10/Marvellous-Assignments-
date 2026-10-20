# Develop a streamlit Application that accepts a Principal Amount . Rate of Interest and Time Period. Provide a Calculate button to calculate and display the simple interest

import streamlit as st 

st.title("Simple Marvellous Calculator")

#Accept input from the user

p = st.number_input("Enter Principal Amount",min_value=0.0,value=1000.0)
r = st.number_input("Enter Rate of Interest(%)",min_value=0.0,value=5.0)
s = st.number_input("Enter Time Period (Years)",min_value=0.0,value=2.0)

# Calculate button
if st.button("Calculate"):
    si = (p * r * s) / 100
    st.success(f"Simple Interest is: ₹{si:.2f}")

    total = p + si
    st.info(f"Total Amount is: ₹{total:.2f}")
