#! python3
# umbrellaReminder.py - Texts a reminder to bring an umbrella if rain is due today

APPID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
LOCATION = 'Sheffield, GB'

import json, requests, textmyself

def getWeather():
    url='https://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=3&appid=%s'\
    % (LOCATION,APPID)
    response=requests.get(url)
    response.raise_for_status()
    weatherData=json.loads(response.text)
    w=weatherData['list']
    return w

def checkForRain():
    w = getWeather()
    if w[0]['weather'][0]['main'] == 'Rain':
        textmyself.textmyself('Bring an umbrella, Giorgio. Rain is due today!')

checkForRain()
