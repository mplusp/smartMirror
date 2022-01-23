import requests
import re

API_KEY = "INSERT_YOUR_API_KEY_HERE"


def city_current(city):
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q="
        + city
        + "&units=metric&APPID="
        + API_KEY
    )
    return response.json()


def city_forecast(city):
    currentData = city_current(city)
    lat = currentData["coord"]["lat"]
    lon = currentData["coord"]["lon"]

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall?lat="
        + str(lat)
        + "&lon="
        + str(lon)
        + "&exclude=current,minutely,hourly,alerts"
        + "&units=metric&appid="
        + API_KEY
    )
    return response.json()
