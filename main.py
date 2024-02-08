import streamlit as st
import plotly.express as px # dir(px)

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2024-02-09", "2024-02-10", "2024-02-11"]
    temperatures = [10, 11, 9]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x" : "Date", "y" : "Temperature (C)"})
st.plotly_chart(figure)
