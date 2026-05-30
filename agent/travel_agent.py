from dotenv import load_dotenv
from pathlib import Path

# Load .env file
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3
)

def generate_travel_plan(
    source,
    destination,
    days,
    flight,
    hotel,
    places,
    weather,
    budget
):

    prompt = f"""
You are a Professional Travel Consultant and AI Travel Planner.

Generate a professional travel report using proper Markdown formatting.

Use the following sections:

# 🌍 Trip Summary

Provide a short summary of the trip.

# ✈ Flight Recommendation

Mention:
- Airline
- Route
- Estimated Cost

# 🏨 Hotel Recommendation

Mention:
- Hotel Name
- Cost Per Night
- Why it is recommended

# 📍 Top Places To Visit

List important tourist attractions with short descriptions.

# 🌦 Weather Forecast

Provide a simple weather overview.

# 💰 Budget Breakdown

Show:
- Flight Cost
- Hotel Cost
- Food Cost
- Transport Cost
- Total Estimated Cost

# 📅 Day-Wise Itinerary

Create a detailed itinerary for each day.

Example:

Day 1
- Visit attraction
- Lunch suggestion
- Evening activity

Day 2
- Visit attraction
- Shopping
- Dinner suggestion

# ✅ Why These Recommendations Were Selected

Explain:
- Why this flight was selected
- Why this hotel was selected
- Why these attractions were selected

IMPORTANT RULES:

- Do NOT print Python dictionaries.
- Do NOT print JSON.
- Do NOT print raw data structures.
- Format everything professionally.
- Use bullet points.
- Make the report look like a real travel consultant prepared it.

Travel Information:

Source City:
{source}

Destination City:
{destination}

Trip Duration:
{days} Days

Flight Information:
{flight}

Hotel Information:
{hotel}

Places Information:
{places}

Weather Information:
{weather}

Budget Information:
{budget}
"""

    response = llm.invoke(prompt)

    return response.content