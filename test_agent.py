from agent.travel_agent import generate_travel_plan

result = generate_travel_plan(
    source="Hyderabad",
    destination="Goa",
    days=3,
    flight="IndiGo - ₹7299",
    hotel="Sea View Resort - ₹3000/night",
    places=["Baga Beach", "Calangute Beach", "Fort Aguada"],
    weather="Sunny 31°C",
    budget="₹15000"
)

print(result)