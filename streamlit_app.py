import streamlit as st
import pandas as pd
import requests
import snowflake.connector


def get_frutyvice_fruit_info(fruit_name):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_name)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized


def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM fruit_load_list")
        return my_cur.fetchall()


# Add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("INSERT INTO fruit_load_list values ('{new_fruit}')")
        return "thanks for adding " + new_fruit
    

st.title("My Parents New Healthy Diner")

st.header("Breakfast Menu")
st.text(" 🥣 Omega 3 & Blueberry Oatmeal")
st.text(" 🥗 Kale, Spinach & Rocket Smoothie")
st.text(" 🐔 Hard-Boiled Free-Range Egg")
st.text(" 🥑🍞 Avocado Toast")

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

st.dataframe(fruits_to_show)

# API response
st.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = st.text_input('What fruit would you like information about?')
    if not fruit_choice:
        st.warning('Please enter a fruit')
    else:
        fruityvice_normalized = get_frutyvice_fruit_info(fruit_choice)
        st.dataframe(fruityvice_normalized)
except:
    st.error()


# Testing snowflake + streamlit
st.header("The fruit load list contains:")
if st.button("Ger Fruit Load List"):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    st.dataframe(my_data_rows)

    
add_my_fruit = st.text_input('What fruit would you like to add?')
if st.button("Add Fruit"):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_data_rows = insert_row_snowflake(add_my_fruit)
    st.text(my_data_rows)
