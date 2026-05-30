from langchain.tools import Tool

from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotel
from tools.place_tool import get_places
from tools.weather_tool import get_weather


flight_tool = Tool(
    name="Flight Search",
    func=lambda x: search_flights(*x.split(",")),
    description="Search flights between source and destination city. Input format: source,destination"
)

hotel_tool = Tool(
    name="Hotel Search",
    func=recommend_hotel,
    description="Find best hotel in destination city"
)

places_tool = Tool(
    name="Places Search",
    func=get_places,
    description="Find tourist attractions in destination city"
)

weather_tool = Tool(
    name="Weather Search",
    func=lambda x: get_weather(),
    description="Get weather forecast"
)

TOOLS = [
    flight_tool,
    hotel_tool,
    places_tool,
    weather_tool
]