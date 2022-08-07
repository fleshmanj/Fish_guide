import time
import json
import ast
import datetime

import requests
from bs4 import BeautifulSoup
from Constants import NAVARRE


def get_forcast():
    lat, long = NAVARRE

    url = f"https://api.weather.gov/points/{lat},{long}"

    response = requests.get(url)

    byte_str = response.content

    dict_str = byte_str.decode("UTF-8")
    my_data = ast.literal_eval(dict_str)

    forcast_url = my_data["properties"]["forecast"]

    forecast = requests.get(forcast_url)
    data = forecast.json()
    return data


days = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}

now = datetime.datetime.now()
day_of_the_week = datetime.datetime.today().weekday()


day = None

if __name__ == "__main__":

    data = get_forcast()

    for value in data["properties"]["periods"]:
        if type(value) == dict:
            if value["name"] is not None:
                day = value["name"]
            if day == "This Morning" or day == "This Afternoon" or day == "Tonight" or day == "Today":
                for vkey, vvalue in value.items():
                    print(vkey, vvalue)
