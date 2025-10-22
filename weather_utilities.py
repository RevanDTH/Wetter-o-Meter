import requests as rs
import json

api_key = "013fca169287728e32de33e9ed823df0"

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
    weather_score = 0 ##Zero is the default score


