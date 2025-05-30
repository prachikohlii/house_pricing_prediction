import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.set_page_config("rooftop values",layout="wide")

custom_css='''<style> 
#rooftop-values-house-pricing-prediction{
    text-align: center;
}

</style>'''
st.markdown(custom_css,unsafe_allow_html=True)




st.header("RoofTop Values : House Pricing Prediction")

with st.form("Enter the credentials:"):
    c1,c2,c3=st.columns(3)
    with c1:
        furnishingstatus=st.number_input("Furnishing Status (Unfurnished:0 , Semi-furnished:1 , Furnished:2)",min_value=0,max_value=2)
        prefarea=st.number_input("Preferred Area (Yes:1 , No:0)",min_value=0,max_value=1)
        parking=st.number_input("Parking",min_value=0,max_value=1000)
        airconditioning=st.number_input("Air Conditioning (Yes:1 , No:0)",min_value=0,max_value=1)

    with c2:
        hotwaterheating=st.number_input("Hot Water Heating (Yes:1 , No:0)",min_value=0,max_value=1)
        guestroom=st.number_input("GuestRoom (Yes:1 , No:0)",min_value=0,max_value=1)
        basement=st.number_input("Basement (Yes:1 , No:0)",min_value=0,max_value=1)
        mainroad=st.number_input("Mainroad (Yes:1 , No:0)",min_value=0,max_value=1)
    with c3:
        storeys=st.number_input("Storeys",min_value=0,max_value=1000)
        bathrooms=st.number_input("Bathrooms",min_value=0,max_value=100)
        bedrooms=st.number_input("Bedrooms",min_value=0,max_value=100)
        area=st.number_input("Area",min_value=0,max_value=10000000)

    model=pickle.load(open("priceprediction.pkl","rb"))
    lt=[area,bedrooms,bathrooms,storeys,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus]
    z=pd.DataFrame([lt])
    x=model.predict(z)
    x=int(x[0])
    
  
    
    
    
    
   
    


    button=st.form_submit_button("Predict")
    if button:
        st.write("Predicted Value:")
        st.success(x)
 
