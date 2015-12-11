from hipchat import Hipchat
from foodtruck import FoodTruckFiesta
import json


def notify(*args, **kwargs):
    config = load_config()
    foodtruck = FoodTruckFiesta()
    hipchat = Hipchat(config.get('token'), config.get('room_id'))
    locations = config.get('locations', [])
    for location in locations:
        truck_list = foodtruck.get_truck_list(location)
        hipchat.hipchat_trucks(location, truck_list)

def load_config():
    with open('config.json') as f:
        return json.load(f)
