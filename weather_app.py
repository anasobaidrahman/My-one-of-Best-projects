import json
from time import strftime

import requests
import datetime

import urllib3

print('🌤 Welcome to the Weather App!')
print('Type any time "q" to quit')
API_KEY = '<your API key>'
while True:
    city = input('Enter City Name: ').strip()
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
    url = f'{BASE_URL}q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)

    if city.lower() == "q":
        print("Goodbye! 👋 Check your weather history in 'weather_history.txt'.")
        break
    try:
        if response.status_code == 200:
            data = response.json()
            print(data)
            Condition = data['weather'][0]['main']
            weather_icon = data['weather'][0]['icon']
            description = data['weather'][0]['description']
            Temperature = data['main']['temp']
            feel_like = data['main']['feels_like']
            icon_url= f'http://openweathermap.org/img/wn/{weather_icon}@2x.png'
            max_temp = data['main']['temp_max']
            min_temp = data['main']['temp_min']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind_gust = data['wind']['gust']
            wind_speed_ms = data['wind']['speed']
            wind_speed=f' {wind_speed_ms*(18/5)}Km/h'
            visibility_m = data['visibility']
            visibility = f'{visibility_m * (10 ** -3)}Km'
            wind_direction = data['wind']['deg']
            if wind_direction == 0:
                wind_direction_str=f'Wind blowing from South to North in {wind_direction} degrees '
            elif 90>wind_direction >0:
                wind_direction_str=f'Wind blowing from southwest top northeast in {wind_direction} degrees '
            elif wind_direction == 90:
                wind_direction_str=f'Wind is blowing from west to east in {wind_direction} degrees '
            elif 180>wind_direction >90:
                wind_direction_str=f'Wind blowing from northwest to southeast in {wind_direction} degrees '
            elif wind_direction == 180:
                wind_direction_str=f'Wind is blowing from North to south in {wind_direction} degrees '
            elif 270>wind_direction >180:
                wind_direction_str=f'Wind is blowing from northeast to southwest in {wind_direction} degrees '
            elif wind_direction == 270:
                wind_direction_str=f'Wind is blowing from East to west in {wind_direction} degrees '
            elif wind_direction>270:
                wind_direction_str=f'Wind is blowing from southeast to northwest in {wind_direction} degrees '

            up_time = data['dt']
            sunset = data['sys']['sunset']
            sunrise = data['sys']['sunrise']
            times = [up_time, sunset, sunrise]
            times_ap= ['current time','Sunset','Sunrise']
            converted_times = {}
            for times,label in zip(times,times_ap):

                Time = datetime.datetime.fromtimestamp(times).strftime('Time:%I:%M %p    Date:%d/%m/%Y')
                converted_times[label] = Time
            sunrise_time = converted_times['Sunrise']
            sunset_time = converted_times['Sunset']
            current_time = converted_times['current time']

            weather_report = (
                f'\033[94m {city.title()}\033[0m \n'
                f'Weather Report for {current_time}\n'
                f'Weather Condition: {Condition} {icon_url}| Description:{description}\n'
                f'Temperature: {Temperature}℃\n'
                f'Humidity: {humidity}%\n'
                f'Pressure: {pressure}hPa\n'
                f'Wind Speed: {wind_speed} | Wind gust: {wind_gust}\n'
                f'Wind Direction: {wind_direction_str}\n'
                f'visibilty: {visibility}\n'
                f'Sunset: {sunset_time}\n'
                f'Sunrise: {sunrise_time}\n'

            )
            print(weather_report)


        elif response.status_code == 404:
            print('❌ City Name Not Found,please check your spelling')
        else:
            print(f'API Error: {response.status_code}')


    except requests.exceptions.Timeout:
        print('⏳ Request timeout,please check your internet connection')
    except requests.exceptions.RequestException as e:
        print('An error accurred as {e}')
    except urllib3.exceptions.MaxRetryError:
        print('⏳ Request timeout,please check your internet connection')
    except requests.exceptions.Timeout:
        print("⏳ The request timed out. Try again later.")

    except requests.exceptions.HTTPError as err:
        print(f"⚠️ HTTP error occurred: {err}")

    except Exception as e:
        print(f"Unexpected error: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f' An unexpected error occurred: {e}')