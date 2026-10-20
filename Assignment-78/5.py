# Develop a Streamlit application that accepts temperature in Celsius. Provide a Convert button to convert the entered temperature into Fahrenheit and display the result

import streamlit as st

st.title("Temperature Converter")

#Accept temperature in Celcius
Celcius = st.number_input("Enter temperature in Celcius", value=0.0)

# Convert button
if st.button("Convert"):
    fahrenheit = (Celcius * 9/5) + 32

    st.success(f"Temperature in Fahrenheit: {fahrenheit:.2f} °F")
