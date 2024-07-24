import requests, json
from os import getenv


def getGeoData(city_name, api_key):
    return requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}')

def getWeatherData(lat, lon, api_key):
    return requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')

def kalvinsToCelsius():
    return 0


API_KEY = getenv('API_KEY')

geo_data = getGeoData(input(), API_KEY).json()
weather_data = getWeatherData(geo_data[0]["lat"], geo_data[0]["lon"], API_KEY).json()

print(json.dumps(geo_data, indent=2))
print(json.dumps(weather_data, indent=2))
