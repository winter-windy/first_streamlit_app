
import streamlit
import requests
import pandas


streamlit.title('My parents healthy food diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocked Smoothie')
streamlit.text('🐔 Hard-boiled Rree Range Egg')
streamlit.text('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

