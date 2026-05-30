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
st.markdown(
"Plan your trip intelligently using AI-powered recommendations."
)

source = st.text_input("🏙 Source City")
destination = st.text_input("📍 Destination City")

days = st.number_input(
"📅 Number of Days",
min_value=1,
max_value=15,
value=3
)

budget = st.number_input(
"💰 Budget (₹)",
min_value=1000,
value=10000
)

if st.button("🚀 Generate Travel Plan"):
  if not source or not destination:
    st.warning(
        "Please enter Source City and Destination City."
    )
    st.stop()

with st.spinner("Generating Travel Plan..."):

    flight = search_flights(source, destination)

    if isinstance(flight, str):
        st.error(flight)
        st.stop()

    hotel = recommend_hotel(destination)

    if isinstance(hotel, str):
        st.error(hotel)
        st.stop()

    places = get_places(destination)

    weather = get_weather()

    budget_data = calculate_budget(
        flight["price"],
        hotel["price_per_night"],
        days
    )

    # -------------------------
    # Flight Section
    # -------------------------

    st.subheader("✈ Flight Recommendation")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Airline",
            flight["airline"]
        )

    with col2:
        st.metric(
            "Price",
            f"₹{flight['price']}"
        )

    with col3:
        st.metric(
            "Route",
            f"{source} → {destination}"
        )

    # -------------------------
    # Hotel Section
    # -------------------------

    st.subheader("🏨 Hotel Recommendation")

    if "name" in hotel:
        st.write(f"🏨 Hotel Name: {hotel['name']}")

    st.write(f"⭐ Rating: {hotel['stars']} Stars")
    st.write(
        f"💰 Price Per Night: ₹{hotel['price_per_night']}"
    )

    # -------------------------
    # Places Section
    # -------------------------

    st.subheader("📍 Top Attractions")

    for place in places:

        st.write(
            f"✅ {place['name']} "
            f"({place['type']}) "
            f"⭐ {place['rating']}"
        )

    # -------------------------
    # Weather Section
    # -------------------------

    st.subheader("🌤 Weather Forecast")

    try:

        for day in weather:

            st.write(
                f"📅 {day['date']} | "
                f"🌡 {day['temperature']}°C"
            )

    except Exception:
        st.write(weather)

    # -------------------------
    # Budget Section
    # -------------------------

    st.subheader("💰 Budget Breakdown")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Flight",
            f"₹{budget_data['flight_cost']}"
        )

    with col2:
        st.metric(
            "Hotel",
            f"₹{budget_data['hotel_cost']}"
        )

    with col3:
        st.metric(
            "Food",
            f"₹{budget_data['food_cost']}"
        )

    with col4:
        st.metric(
            "Transport",
            f"₹{budget_data['transport_cost']}"
        )

    st.success(
        f"Estimated Total Cost: ₹{budget_data['total_cost']}"
    )

    st.divider()

    # -------------------------
    # AI Travel Report
    # -------------------------

    st.subheader("🤖 AI Generated Travel Report")

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

    st.download_button(
        label="📄 Download Travel Report",
        data=ai_output,
        file_name="travel_report.txt",
        mime="text/plain"
    )