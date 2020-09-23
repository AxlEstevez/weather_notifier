#/usr/bin/python3
#-*- coding: utf-8 -*-

import requests
from pynotifier import Notification

url = "http://api.openweathermap.org/data/2.5/weather?q="
cityname = "Mexico City, MX"

api_key = ''

data = requests.get(url+cityname+'&appid='+api_key).json()
city = data['name']
country = data['sys']['country']
temperature = data['main']['temp_max'] - 273.15
weather = data['weather'][0]['main']
wind_speed = float(data['wind']['speed'])
humidity = data['main']['humidity']
pressure = data['main']['pressure']

if data["cod"] != '404':
    Notification(
        title= city+","+country,
        description=f'{temperature}°C {weather} Wind Speed {wind_speed}\n'+
        f'Humidity {humidity}\n ressure {pressure}',
        duration=50,
        icon_path='./icons/weather.ico',
        urgency=Notification.URGENCY_CRITICAL
    ).send()
else:
    print("City not found")