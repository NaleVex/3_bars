import json
from math import sqrt

seatsMax = 0
seatsMaxBarName = ''
seatsMin = 0
seatsMinBarName = ''
bar = None
locationA = None
locationB = None
nearestBar = None
nearestBarRange = None


def load_data():
    f_address = input("Where is your JSON file: ")
    try:
        with open(f_address) as bars_data:
            global bars
            bars = json.load(bars_data)
    except FileNotFoundError:
        print("Cannot find file, try again")
        load_data()


def get_biggest_bar():
    global bars, seatsMax, seatsMaxBarName
    for bar in bars:
        if bar['SeatsCount'] > seatsMax:
            seatsMax = bar['SeatsCount']
            seatsMaxBarName = bar['Name']
            # print('-max- ' + seatsMaxBarName + ' ' + str(seatsMax))


def get_smallest_bar():
    global bars, seatsMin, seatsMinBarName
    for bar in bars:
        if bar['SeatsCount'] < seatsMin:
            seatsMin = bar['SeatsCount']
            seatsMinBarName = bar['Name']
            # print('-min- ' + seatsMinBarName + ' ' + str(seatsMin))


def get_closest_bar():
    global bars, nearestBar, nearestBarRange
    for bar in bars:
        range_finded = find_range(float(bar['geoData']['coordinates'][0]), float(bar['geoData']['coordinates'][1]))
        if range_finded < nearestBarRange:
            nearestBar = bar['Name']
            nearestBarRange = range_finded


def find_range(bar_loc_a, bar_loc_b):
    global locationA
    global locationB
    range = sqrt(((bar_loc_a - locationA) ** 2) + ((bar_loc_b - bar_loc_a) ** 2))
    return range


if __name__ == '__main__':
    load_data()
    inputCoords = input('Enter your coordinates, divide with space : ')
    locationA = float(inputCoords.split(' ')[0])
    locationB = float(inputCoords.split(' ')[1])
    seatsMin = bars[0]['SeatsCount']
    seatsMinBarName = bars[0]['Name']
    nearestBarRange = 9999999999999
    # print('-min- ' + seatsMinBarName + ' ' + str(seatsMin))

    get_biggest_bar()
    get_smallest_bar()
    get_closest_bar()
    print('Most seats in bar ' + seatsMaxBarName + ' with ' + str(seatsMax) + ' seats')
    print('Minimum seats in bar ' + seatsMinBarName + ' with ' + str(seatsMin) + ' seats')
    print('Nearest bar is ' + str(nearestBar))
