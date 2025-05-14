import requests

#  Replace this with your OpenWeatherMap API key
API_KEY = "fb69556dc93086566dee889e799de4b2"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to get and display weather info
def get_weather(city):
    # Prepare query parameters for API call
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        # Send GET request to the API
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Handle error response (e.g., city not found)
        if data.get("cod") != 200:
            print(f"Error: {data.get('message', 'Unknown error').capitalize()}")
            return

        # Extract relevant weather data
        name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].capitalize()

        # Output formatted weather info
        print(f"\nWeather in {name}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")

    except requests.exceptions.RequestException as e:
        # Handle network issues or bad requests
        print(f"Network error: {e}")

# Main program entry
if __name__ == "__main__":
    print("=== Weather App ===")
    city_name = input("Enter city name: ").strip()
    get_weather(city_name)
