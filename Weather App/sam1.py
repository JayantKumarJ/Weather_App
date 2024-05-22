import requests
import json
import geocoder
from geopy.geocoders import Nominatim

def city(city_name="delhi"):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city_name)
    if location:  
        lat = location.latitude
        lon = location.longitude
        return lat, lon
    

lat, lon = city()


api_key = "37708956d0dc4535299a5e30e44d92d6"

url=f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={api_key}"

response=requests.get(url)

class getinfo:
    def __init__(self):
        self()
    def tmp():
        if response.status_code==200:
            data=response.json()
            return data["list"][0]["main"]["temp"]
            #print(data["list"][0]["main"]["temp"])
        else:
            print("error", response.status_code)

    def feellike():
        if response.status_code==200:
            data=response.json()
            return data["list"][0]["main"]["feels_like"]
        else:
            print("error", response.status_code)

    def mintmp():
        if response.status_code==200:
            data=response.json()
            return data["list"][0]["main"]["temp_min"]
            print("Minimum Temperature:" ,temp_min)
        else:
            print("error", response.status_code)

    def maxtmp():
        if response.status_code==200:
            data=response.json()
            return data["list"][0]["main"]["temp_max"]
        else:
            print("error", response.status_code)

    def pressure():
        if response.status_code==200:
            data=response.json()
            return data["list"][0]["main"]["pressure"]
        else:
            print("error", response.status_code)

    def sea_level():
        if response.status_code==200:
            data=response.json()
            return data["list"][0]["main"]["sea_level"]
        else:
            print("error", response.status_code)

    def humidity():
        if response.status_code==200:
            data=response.json()
            return data["list"][0]["main"]["humidity"]
        else:
            print("error", response.status_code)

    if __name__ == '__main__':
        app = tmp()
        app = feellike()
        app = mintmp()
        app = maxtmp()
        app = pressure()
        app = sea_level()
        app = humidity()


