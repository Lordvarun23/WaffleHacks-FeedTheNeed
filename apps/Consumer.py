import streamlit as st
import pandas as pd
import csv
users = []
def app():
    with st.form(key = "form1"):
        UserName = st.text_input("Enter Your Name:")
        UserMail = st.text_input("Enter Your Email id:")
        UserZip = st.text_input("Enter Your Zip Code:")
        UserCity = st.text_input("Enter Your City:")
        UserCountry = st.text_input("Enter Your Country:")
        UserChoice = st.text_input("Enter your needs(Raw Materials/Food):")
        users.append([UserName, UserMail, UserZip, UserCity, UserCountry, UserChoice])
        submit = st.form_submit_button(label = "Submit")



    filename = "Request.csv"

    # writing to csv file

    with open(filename, 'a') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(users)
