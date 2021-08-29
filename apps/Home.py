# Import Libraries
import streamlit as st
import folium
from math import sin, cos, sqrt, atan2, radians
from streamlit_folium import folium_static
import pandas as pd
from geopy.geocoders import Nominatim
# Layout in StreamLit

def calc_dist(la1,lo1,la2,lo2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(la1)
    lon1 = radians(lo1)
    lat2 = radians(la2)
    lon2 = radians(lo2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return round(distance,2)
def app():
# User Details

    UserName = st.text_input("Enter Donor's Name:")
    UserMail = st.text_input("Enter Donor's Email id:")
    UserCity = st.text_input("Enter Your City:")
    UserCountry = st.text_input("Enter Your Country:")
    if len(UserCity)>0:
        geolocator = Nominatim(user_agent="Arun")
        loc = geolocator.geocode(UserCity)
        Userlat = loc.latitude
        Userlong = loc.longitude


    # Asking the user whether he needs to send raw materials or cooked food
    st.write('Select any one:')
    option_r = st.checkbox('Raw Materials')
    option_c = st.checkbox('Food')

    # If user wants to ship the raw materials he/she can ship to any countries of his wish
    if option_r:
        C = folium.Map(location=[20,0], zoom_start=3)
        data = pd.read_csv("Request.csv")
        City = list(data["City"][data["Food/Raw"] == 'Raw Materials'])
        Name = list(data["Name"][data["Food/Raw"] == 'Raw Materials'])
        mail_id = list(data["Email Id"][data["Food/Raw"] == 'Raw Materials'])
        tooltip = "Click me!"
        folium.Marker([Userlat, Userlong], popup="User Location",tooltip=tooltip,icon=folium.Icon(color="green")).add_to(C)

        for i in range(len(City)):
            from geopy.geocoders import Nominatim
            geolocator = Nominatim(user_agent="Varun")
            temp=City[i].title()
            name = Name[i].title()
            mail = mail_id[i]
            loc = geolocator.geocode(temp)
            tooltip = "Click me!"
            folium.Marker([loc.latitude, loc.longitude], popup=f"<i>Name:{name},Mail_Id:{mail}</i>", tooltip=tooltip).add_to(C)
        folium_static(C)
        request_id = st.text_input("Enter Receiver's Mail Id:")
        from geopy.geocoders import Nominatim
        geolocator = Nominatim(user_agent="Varun")
        temp = City[mail_id.index(request_id)]
        loc = geolocator.geocode(temp)
        loc = [(loc.latitude, loc.longitude),
               (Userlat, Userlong)]

        folium.PolyLine(loc,
                        color='red',
                        weight=15,
                        opacity=0.8).add_to(C)
        folium_static(C)
        dis= calc_dist(loc.latitude,loc.longitude,Userlat,Userlong)
        st.write(f"The Distance between you and the Needed Person is::{dis} KM")
        st.write(f"The Estimated Time Taken to reach is {round(dis/45,2)} hours.")

    elif option_c:
        C = folium.Map(location=[20, 0], zoom_start=3)
        data = pd.read_csv("Request.csv")
        City = list(data["City"][data["Food/Raw"] == 'Food'])
        Name = list(data["Name"][data["Food/Raw"] == 'Food'])
        mail_id = list(data["Email Id"][data["Food/Raw"] == 'Food'])
        tooltip = "Click me!"
        folium.Marker([Userlat, Userlong], popup="Your Location",tooltip=tooltip,icon=folium.Icon(color="green")).add_to(C)
        for i in range(len(City)):
            from geopy.geocoders import Nominatim

            geolocator = Nominatim(user_agent="Varun")
            temp = City[i].title()
            name = Name[i].title()
            mail = mail_id[i]
            loc = geolocator.geocode(temp)
            tooltip = "Click me!"
            folium.Marker([loc.latitude, loc.longitude], popup=f"<i>Name:{name},Mail_Id:{mail}</i>",
                          tooltip=tooltip).add_to(C)
        folium_static(C)
        request_id = st.text_input("Enter Receiver's Mail Id:")
        from geopy.geocoders import Nominatim

        geolocator = Nominatim(user_agent="Varun")
        temp = City[mail_id.index(request_id)]
        loc = geolocator.geocode(temp)
        dis = calc_dist(loc.latitude, loc.longitude, Userlat, Userlong)
        loc = [(loc.latitude,loc.longitude),
               (Userlat, Userlong)]

        folium.PolyLine(loc,
                        color='red',
                        weight=15,
                        opacity=0.8).add_to(C)
        folium_static(C)
        st.write(f"The Distance between you and the Needed Person is {dis} KM.")
        st.write(f"The Estimated Time Taken to reach is {round(dis/45,2)} hours.")