import json

def get_places(city):

    with open("data/places.json", "r") as file:
        places = json.load(file)

    city_places = [
        place for place in places
        if place["city"].lower() == city.lower()
    ]

    top_places = sorted(
        city_places,
        key=lambda x: x["rating"],
        reverse=True
    )

    return top_places[:5]


if __name__ == "__main__":
    result = get_places("Goa")
    print(result)