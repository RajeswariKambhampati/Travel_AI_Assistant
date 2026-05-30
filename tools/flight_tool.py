import json

def search_flights(source, destination):

    with open("data/flights.json", "r") as file:
        flights = json.load(file)

    matching_flights = [
        flight for flight in flights
        if flight["from"].lower() == source.lower()
        and flight["to"].lower() == destination.lower()
    ]

    if not matching_flights:
        return "No flights found"

    cheapest = min(matching_flights, key=lambda x: x["price"])

    return cheapest


if __name__ == "__main__":
    result = search_flights("Hyderabad", "Goa")
    print(result)