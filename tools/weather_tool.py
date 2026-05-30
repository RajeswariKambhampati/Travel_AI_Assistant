import requests

def get_weather():

    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=15.2993"
            "&longitude=74.1240"
            "&daily=temperature_2m_max"
            "&timezone=auto"
        )

        response = requests.get(url)
        data = response.json()

        temp = data["daily"]["temperature_2m_max"][0]

        return {
            "condition": "Forecast",
            "temperature": f"{temp}°C"
        }

    except Exception as e:
        return {
            "condition": "Unavailable",
            "temperature": str(e)
        }


if __name__ == "__main__":
    print(get_weather())