from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, Tool, AgentType

from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotel
from tools.place_tool import get_places
from tools.weather_tool import get_weather
from tools.budget_tool import calculate_budget

import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

tools = [
    Tool(
        name="Flight Search",
        func=lambda q: str(search_flights(*q.split(","))),
        description="Find flights using source,destination"
    ),

    Tool(
        name="Hotel Recommendation",
        func=recommend_hotel,
        description="Find best hotel by city"
    ),

    Tool(
        name="Places Discovery",
        func=get_places,
        description="Find attractions in a city"
    ),

    Tool(
        name="Weather Lookup",
        func=lambda city: str(get_weather()),
        description="Get weather forecast"
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_travel_agent(source, destination, days):
    prompt = f"""
    Plan a {days}-day trip from {source} to {destination}.

    Include:

    1. Best Flight
    2. Best Hotel
    3. Weather
    4. Top Attractions
    5. Day-wise itinerary
    6. Budget estimate
    7. Why recommendations were selected
    """

    return agent.run(prompt)