#Importing required libraries
import streamlit as st
import pandas as pd
import pickle as pkl

#Reading the Dataset
cars = pd.read_csv("cleaned_cars.csv")

#Fetching all the unique companies, car model names, years, a fuel types
company = cars['company'].unique()
name = cars['name'].unique()
year = sorted(cars['year'].unique(),reverse=True)
fuel_type = cars['fuel_type'].unique()

st.title("USED CAR PRICE PREDICTOR")
st.subheader("Enter the details of car: ")

#Taking user inputs
col1, col2 = st.columns(2)
with col1:
    
    selected_company = st.selectbox('Select Company:',company)
    
with col2:
    
    selected_company_models = []
    for i in list(name):
        if i.startswith(selected_company):
            selected_company_models.append(i)
            
    selected_model = st.selectbox('Select Model Name:',selected_company_models)
    
col3, col4 = st.columns(2)
with col3:
    selected_year = st.selectbox('Select Year:',year)
    
with col4:
    selected_fuel_type = st.selectbox('Select Fuel Type:',fuel_type)

selected_km_driven = st.number_input("Enter Kilometers Driven: ")

btn = st.button('Submit Info')

if btn:
    #Loading trained machine learning model via pickle
    with open('LinearRegressionModel.pkl', 'rb') as file:
        model = pkl.load(file)
    
    #Predicting the result
    prediction = model.predict(pd.DataFrame([[selected_model, selected_company, selected_year, selected_km_driven,selected_fuel_type]], columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']))
    
    #Showing Results
    st.subheader(round(prediction[0],2))