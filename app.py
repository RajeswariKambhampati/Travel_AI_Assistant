from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotel
from tools.place_tool import get_places
from tools.weather_tool import get_weather
from tools.budget_tool import calculate_budget

from agent.travel_agent import generate_travel_plan

import streamlit as st

st.set_page_config(
    page_title="Smart Travel Planner",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #334155
    );
}

h1 {
    text-align: center;
    color: white;
}

[data-testid="stMetric"] {
    background-color: rgba(255,255,255,0.08);
    padding: 15px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.1);
}

.stButton button {
    width: 100%;
    border-radius: 10px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.title("🌍 Smart Travel Planner")

st.markdown("""
Plan your perfect trip with AI-powered recommendations for
flights, hotels, attractions, weather forecasts, and budget planning.
""")

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
        st.warning("Please enter Source City and Destination City.")
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

        # Trip Overview
        st.subheader("📊 Trip Overview")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Destination", destination)

        with col2:
            st.metric("Days", days)

        with col3:
            st.metric("Budget", f"₹{budget}")

        st.divider()

        # Flight Recommendation
        st.subheader("✈ Flight Recommendation")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Airline", flight["airline"])

        with col2:
            st.metric("Price", f"₹{flight['price']}")

        with col3:
            st.metric(
                "Route",
                f"{source} → {destination}"
            )

        # Hotel Recommendation
        st.subheader("🏨 Hotel Recommendation")

        st.success(
            f"""
🏨 Hotel Name: {hotel.get('name', 'Recommended Hotel')}

⭐ Rating: {hotel['stars']} Stars

💰 Price Per Night: ₹{hotel['price_per_night']}
"""
        )

        # Top Attractions
        st.subheader("📍 Top Attractions")

        for place in places:
            st.info(
                f"""
📍 {place['name']}

🏷 Category: {place['type']}

⭐ Rating: {place['rating']}
"""
            )

        # Weather Forecast
        st.subheader("🌤 Weather Forecast")

        if isinstance(weather, dict):

            st.success(
                f"""
🌤 Current Weather: {weather.get('condition', 'Clear Sky')}

🌡 Temperature: {weather.get('temperature', '32°C')}
"""
            )

        else:

            st.success(
                """
🌤 Current Weather: Clear Sky

🌡 Temperature: 32°C
"""
            )

        # Budget Breakdown
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

        # AI Generated Travel Report
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

st.divider()

st.caption(
    "Powered by Groq LLM | Streamlit | AI Travel Planning System"
)