import streamlit as st
import pandas

st.title("My Parents New Healthy Diner")

st.header("Breakfast Menu")
st.text(" 🥣 Omega 3 & Blueberry Oatmeal")
st.text(" 🥗 Kale, Spinach & Rocket Smoothie")
st.text(" 🐔 Hard-Boiled Free-Range Egg")
st.text(" 🥑🍞 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
