from dotenv import load_dotenv
from pathlib import Path
import os

# Load .env file
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

print("KEY FOUND:", "YES" if os.getenv("GROQ_API_KEY") else "NO")

from langchain_groq import ChatGroq

# Updated Groq model
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
You are a professional AI Travel Planning Assistant.

Source City: {source}
Destination City: {destination}
Trip Duration: {days} days

Flight Details:
{flight}

Hotel Details:
{hotel}

Places:
{places}

Weather:
{weather}

Budget:
{budget}

Generate:

1. Trip Summary
2. Flight Recommendation
3. Hotel Recommendation
4. Day-wise itinerary
5. Weather Overview
6. Budget Breakdown
7. Why these recommendations were selected

Format the response professionally.
"""

    response = llm.invoke(prompt)

    return response.content