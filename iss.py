#!/usr/bin/env python
import requests
import time
__author__ = 'Elijah Webster'


def astros():
    astroData = requests.get("http://api.open-notify.org/astros.json").json()

    print("Total Astronauts in Space: ", astroData.get(
        "number"), "\n****************************************\n")
    for people in astroData.get("people"):
        print("Name: ", people.get("name"),
              "\nSpacecraft: ", people.get("craft"), "\n_________________________\n")
    return astroData


def issLocate():
    issData = requests.get("http://api.open-notify.org/iss-now.json").json()
    print("International Space Station Locator\n*********************************************\n\n",
          "Latitude: ", issData.get("iss_position").get("latitude"), "\nLongitude: ", issData.get("iss_position").get("longitude"), "\nTimestamp: ", issData.get("timestamp"))
    return issData


def issPass(location):
    issPassData = requests.get(
        "http://api.open-notify.org/iss-pass.json", params={"lat": location[0], "lon": location[1]})
    print("\nISS will pass over ", location, " on ", time.ctime(
        issPassData.json().get("response")[0].get("risetime")))


def main():
    astros()
    issLocate()
    issPass([39.791000, -86.148003])
    pass


if __name__ == '__main__':
    main()
