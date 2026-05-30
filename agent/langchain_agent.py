from agent.travel_agent import generate_travel_plan

def run_travel_agent(query):
    return generate_travel_plan(
        source="Hyderabad",
        destination="Goa",
        days=3,
        flight="Flight Selected",
        hotel="Hotel Selected",
        places="Tourist Places",
        weather="Sunny",
        budget="15000"
    )