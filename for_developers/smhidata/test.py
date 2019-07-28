#import sys
from wrap_smhi_api import *
#from collections import defaultdict

def print_stations():
  stations = get_stations()
  for station in stations:
    print(station)

def print_station(id):
  station_data = get_data(53430)
  for d in station_data:
    print(d)

# Examples
print_stations()
print_station(53430)
