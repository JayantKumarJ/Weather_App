from pymongo import *
import sam1, sam2
from weather2 import *


uri = "mongodb://localhost:27017"
client = MongoClient(uri)
database = client["Weather_app"]
collection = database["weather"]


weather_data = sam2.WeatherInfo.get_weather('Kolkata')
temp = weather_data["list"][0]["main"]["temp"]
feel = weather_data["list"][0]["main"]["feels_like"]
min_temp = weather_data["list"][0]["main"]["temp_min"]
max_temp = weather_data["list"][0]["main"]["temp_max"]
atm_p = weather_data["list"][0]["main"]["pressure"]
sea_level = weather_data["list"][0]["main"]["sea_level"]
humidi = weather_data["list"][0]["main"]["humidity"]

document_list = [
   { "Temperature" : temp },
   { "Feels like" : feel },
   { "Minimum Temperature" : min_temp },
   { "Maximum Temperature" : max_temp },
   { "Atmospheric Pressure" : atm_p },
   { "Sea Level" : sea_level },
   { "Humidity" : humidi }
]
result = collection.insert_many(document_list)
print(result.acknowledged)







 #{ "Feels like" : {weather_data["list"][0]["main"]["feels_like"]}},
 #{ "Minimum Temperature" : {weather_data["list"][0]["main"]["temp_min"]}},
 #{ "Maximum Temperature" : {weather_data["list"][0]["main"]["temp_max"]}},
 #{ "Atmospheric Pressure" : {weather_data["list"][0]["main"]["pressure"]}},
 #{ "Sea Level" : {weather_data["list"][0]["main"]["sea_level"]}},
 #{ "Humidity" : {weather_data["list"][0]["main"]["humidity"]}}
 


print(client)