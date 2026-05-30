import requests

def get_weather():

    latitude = 15.2993
    longitude = 74.1240

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&daily=temperature_2m_max"
        f"&timezone=auto"
    )

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            dates = data["daily"]["time"]
            temps = data["daily"]["temperature_2m_max"]

            weather_data = []

            for date, temp in zip(dates[:3], temps[:3]):
                weather_data.append({
                    "date": date,
                    "temperature": temp
                })

            return weather_data

        return []

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    print(get_weather())