import requests as rs
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

def get_place(place):
    print(place)

    url="http://api.openweathermap.org/geo/1.0/zip?zip="+place+",CH&appid="+api_key

    response = rs.get(url=url)

    return response.text


def get_weather(lat,lon):

    url="https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+api_key

    response = rs.get(url=url)

    return response.text


def analyse_weather(weather_obj):
    weather = json.loads(weather_obj)
    feels_like_weather = float(weather["main"]["feels_like"]) - 273.15
    weather_score = 0.0 ##Zero is the default score, higher score means better weather

    ##checking main weather state
    match weather["weather"][0]["main"]:
        case "clear sky":
            weather_score += 3
        case "few clouds":
            weather_score += 2
        case "scattered clouds":
            weather_score += 1
        case "broken clouds":
            weather_score += 0
        case "shower rain":
            weather_score -= 1
        case "rain":
            weather_score -= 2
        case "thunderstorm":
            weather_score -= 3
        case "snow":
            weather_score -= 4
        case "mist":
            weather_score -= 1


    ##Some ugly ass if statement, I will rewrite this I promise
    if feels_like_weather >= 40.0:
        weather_score += 5
    elif feels_like_weather >= 35.0 and feels_like_weather <= 39.9:
        weather_score += 4
    elif feels_like_weather >= 30.0 and feels_like_weather <= 34.9:
        weather_score += 3
    elif feels_like_weather >= 25.0 and feels_like_weather <= 29.9:
        weather_score += 2
    elif feels_like_weather >= 20.0 and feels_like_weather <= 24.9:
        weather_score += 1
    elif feels_like_weather >= 15.0 and feels_like_weather <= 19.9:
        weather_score += 0
    elif feels_like_weather >= 10.0 and feels_like_weather <= 14.9:
        weather_score -= 1
    elif feels_like_weather >= 5.0 and feels_like_weather <= 9.9:
        weather_score -= 2
    elif feels_like_weather >= 0.0 and feels_like_weather <= 4.9:
        weather_score -= 3
    elif feels_like_weather < 0.0:
        weather_score -= 4

    return weather_score


    ## Later on I will add some more stuff to check the weather
