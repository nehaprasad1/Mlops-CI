import streamlit as st

#UI
st.title("power calculator")
st.write("enter the number to calculate powers")

#user input
num = st.number_input("enter an integer",value = 1 , step =1)

#result
square = num ** 2
cube = num **3
fifth_pow = num ** 5

#show result
st.write(f"the square of {num} is: {square}")
st.write(f"the cube of {num} is:  {cube}")
st.write(f"the fifth power of {num} is:  {fifth_pow}")





