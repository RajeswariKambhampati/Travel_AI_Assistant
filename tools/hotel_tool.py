import json

def recommend_hotel(city):

    with open("data/hotels.json", "r") as file:
        hotels = json.load(file)

    city_hotels = [
        hotel for hotel in hotels
        if hotel["city"].lower() == city.lower()
    ]

    if not city_hotels:
        return "No hotels found"

    best_hotel = sorted(
        city_hotels,
        key=lambda x: (-x["stars"], x["price_per_night"])
    )[0]

    return best_hotel


if __name__ == "__main__":
    result = recommend_hotel("Goa")
    print(result)