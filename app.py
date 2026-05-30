from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotel
from tools.place_tool import get_places
from tools.weather_tool import get_weather
from tools.budget_tool import calculate_budget

from agent.travel_agent import generate_travel_plan

import streamlit as st

st.set_page_config(
    page_title="Agentic AI Travel Planning Assistant",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Agentic AI Travel Planning Assistant")

source = st.text_input("Source City")
destination = st.text_input("Destination City")

days = st.number_input(
    "Number of Days",
    min_value=1,
    max_value=15,
    value=3
)

budget = st.number_input(
    "Budget (₹)",
    min_value=1000,
    value=10000
)

if st.button("Generate Travel Plan"):

    flight = search_flights(source, destination)

    if isinstance(flight, str):
        st.error(flight)
        st.stop()

    hotel = recommend_hotel(destination)

    places = get_places(destination)

    weather = get_weather()

    budget_data = calculate_budget(
        flight["price"],
        hotel["price_per_night"],
        days
    )

    st.subheader("✈ Flight Details")
    st.write(flight)

    st.subheader("🏨 Hotel Details")
    st.write(hotel)

    st.subheader("📍 Places")
    st.write(places)

    st.subheader("🌤 Weather")
    st.write(weather)

    st.subheader("💰 Budget")
    st.write(budget_data)

    st.subheader("🤖 AI Travel Plan")

    ai_output = generate_travel_plan(
        source=source,
        destination=destination,
        days=days,
        flight=flight,
        hotel=hotel,
        places=places,
        weather=weather,
        budget=budget_data
    )

    st.markdown(ai_output)