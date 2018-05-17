import json
import urllib.request
import urllib.parse


def get_json_data(URL):
    with urllib.request.urlopen(URL) as response:
        return json.loads(response.read().decode('utf-8'))


def get_location_id(location_name):
    URL = f'https://www.metaweather.com/api/location/search/?query={location_name}'
    data = get_json_data(URL)
    try:
        return data[0]['woeid']
    except IndexError:
        return None


def print_weather(location_name):
    location_id = get_location_id(location_name)
    weather_URL = f'https://www.metaweather.com/api/location/{location_id}'
    weather = get_json_data(weather_URL)['consolidated_weather'][0]
    print(
        f'Weather: {weather["weather_state_name"]}, temperature: {weather["the_temp"]}, air pressure: {weather["air_pressure"]}')


if __name__ == '__main__':
    location = input('Location? ')
    print_weather(location)
