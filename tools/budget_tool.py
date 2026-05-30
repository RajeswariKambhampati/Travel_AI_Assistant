def calculate_budget(
        flight_price,
        hotel_price_per_night,
        days):

    hotel_cost = hotel_price_per_night * days

    food_cost = days * 800

    local_transport = days * 500

    total = (
        flight_price
        + hotel_cost
        + food_cost
        + local_transport
    )

    return {
        "flight_cost": flight_price,
        "hotel_cost": hotel_cost,
        "food_cost": food_cost,
        "transport_cost": local_transport,
        "total_cost": total
    }


if __name__ == "__main__":

    result = calculate_budget(
        flight_price=7299,
        hotel_price_per_night=1232,
        days=3
    )

    print(result)