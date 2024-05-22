import requests
from geopy.geocoders import Nominatim

class WeatherInfo:
    @staticmethod
    def get_weather(city_name):
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode(city_name)
        if location:
            lat, lon = location.latitude, location.longitude
            api_key = "37708956d0dc4535299a5e30e44d92d6"
            url=f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data   # Directly returning raw data
            else:
                print("Error:", response.status_code)
                return None

        else:
            print('Location not found')
            return None

# weather_data = WeatherInfo.get_weather('Kolkata')

# if weather_data:
#     print("Temperature:", weather_data["list"][0]["main"]["temp"])
#     print("Feels like:", weather_data["list"][0]["main"]["feels_like"])
#     print("Minimum Temperature:", weather_data["list"][0]["main"]["temp_min"])
#     print("Maximum Temperature:", weather_data["list"][0]["main"]["temp_max"])
#     print("Atmospheric Pressure:", weather_data["list"][0]["main"]["pressure"])
#     print("Sea Level:", weather_data["list"][0]["main"]["sea_level"])
#     print("Humidity:", weather_data["list"][0]["main"]["humidity"])
