import streamlit

streamlit.title ('My Parents New Healthy Diner')

streamlit.header (' Breakfast Menue')
streamlit.text ('🥣 Omega 3 & Blueberry OatMeal')
streamlit.text (' 🥗 Kale Spainach and Rocket Smoothie')
streamlit.text (' 🐔  Hard Boiled free-Range Egg')
streamlit.text ('🥑🍞 Avacado and toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv ("https//:https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
