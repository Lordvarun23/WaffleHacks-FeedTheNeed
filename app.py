import streamlit as st
from multiapp import MultiApp
from apps import Home, Consumer # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Donor's Dashboard", Home.app)
app.add_app("Consumer's DashBoard", Consumer.app)

# The main app
app.run()