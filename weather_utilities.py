import requests as rs

api_key = "013fca169287728e32de33e9ed823df0"

def get_place(place):
    print(place)

    url="http://api.openweathermap.org/geo/1.0/zip?zip="+place+",CH&appid="+api_key

    print(url)
    response = rs.get(url=url)

    return response.text


def get_weather(lat,lon):

    url="https://api.openweathermap.org/data/3.0/onecall?lat="+lat+"&lon="+lon+"&appid="+api_key

    response = rs.get(url=url)

    return response.text