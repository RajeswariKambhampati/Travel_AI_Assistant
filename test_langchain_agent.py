from agent.langchain_agent import run_travel_agent

query = """
Plan a 3-day trip to Goa.
Find flights.
Recommend hotels.
Suggest tourist attractions.
Provide weather information.
Estimate budget.
"""

result = run_travel_agent(query)

print(result)