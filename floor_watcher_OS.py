import winsound
import requests
import re
import time
import json


def get_floor(collection_name):
    url = f"https://api.opensea.io/api/v1/collection/{collection_name}"
    response = requests.request("GET", url)
    string = response.text
    dict = json.loads(string)
    global floor_price
    floor_price = dict["collection"]["stats"]["floor_price"]
    return floor_price

def beep():
    print("Processing ... ")
    while floor_price > floor_min:
        get_floor(collection_name)
        time.sleep(0.5)
    while True:
        print("Price is down...")
        winsound.Beep(440, 900)

collection_name = input("Creat a price alert! \n collection name : ")
floor_min = float(input("When floor price falls bellow: "))

get_floor(collection_name)
beep()

