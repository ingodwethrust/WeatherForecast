import requests
from dateutil.parser import parse
import argparse
import pprint


APIKEY  = ""
CITY_ID = {"Moscow": 524901}

class APIRequest:

    def __init__(self):
       self._city_caсhe = {}       

    def get(self, city="Moscow"):
        if city in self._city_caсhe:
            return self._city_caсhe[city]
        city_id = CITY_ID[city]
        url = f" http://api.openweathermap.org/data/2.5/forecast?id={city_id}&APPID=d3f1d3de84ecef66312ed51d46a344bc"
        print("не работаеш")
        data  = requests.get(url).json()
        forecast_data = data["list"][0]["main"]
        # kelvin to celsius:
        forecast = forecast_data["temp"] - 273.15
        self._city_caсhe[city] = forecast
        return forecast

class CityInfo:

    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or APIRequest()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city) 


def _main(city_name="Moscow"):
    weather_forecast = APIRequest()
    for _ in range(5):
        city_info = CityInfo(city_name, weather_forecast=weather_forecast)
        forecast = city_info.weather_forecast()
    pprint.pprint("За окном - {0:.1f} по Цельсию".format(forecast))

    
if __name__ == "__main__":
    _main()
