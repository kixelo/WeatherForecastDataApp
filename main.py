import streamlit as st
import plotly.express as px # dir(px)
from backend import get_data
from datetime import datetime

# Add title, text input, slider, selectobox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place.capitalize()}")

# Get the temperature/sky data
if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
        # Create a temperature plot
            temperatures = [(i["main"]["temp"]-273.15) for i in filtered_data]
            dates = [i['dt_txt'] for i in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x" : "Date", "y" : "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear" : "images/clear.png", "Clouds" : "images/cloud.png", "Rain" : "images/rain.png", "Snow" : "images/snow.png"}
            sky_conditions = [i['weather'][0]['main'] for i in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            dt = [i['dt'] for i in filtered_data]
            dt_formatted = [datetime.utcfromtimestamp(i).strftime(('%a, %d-%m-%Y %H:%M')) for i in dt]
            st.image(image_paths, width=115, caption=dt_formatted)

    except KeyError:
        st.subheader(f":red[Sorry we do not have '{place.capitalize()}' in our database!!!]")