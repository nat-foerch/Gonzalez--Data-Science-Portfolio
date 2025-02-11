import streamlit as st
import pandas as pd

st.title('Penguin Exploration!')  # This creates an app title

st.write('This is an app that will explore penguin demographics that include three different species and their island, sex, body mass, and more! Scroll through the data and use the dropdown menu to filter through species!.')
# This creates a description for the app. 
st.subheader ("Now, let's look at some data!")
# Creates a subheader

def load_data():  # Importing data from local folder to streamlit.
    return pd.read_csv("C:/Users/nglez/OneDrive/Documents/GitHub/Gonzalez--Data-Science-Portfolio/basic_streamlit-app/data/penguins.csv")

data = load_data() #displays data

st.dataframe(data) # Creates a table of the data on the app. Users can scroll through the app.

Pen_species = st.selectbox("Select a Species!", data['species'].unique()) # Creates a dropdown menu of different penguin species. 

filtered_df = data[data["species"] == Pen_species] # Creates filtered data frame for users

st.write(f"{Pen_species} Penguins:") # Heading
st.dataframe(filtered_df) # Displaying filtered results