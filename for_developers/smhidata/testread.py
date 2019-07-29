from readdata import *

#stations = get_station_list("file.txt")
#print(stations)

station_data = get_station_data("result18.txt")
for station in list(station_data.keys()):
    datapoints = station_data[station]
    length = len(datapoints)
    print(station + " has " + str(length) + " data points")
    print("First point is " + str(datapoints[0]))
    print("Last point is " + str(datapoints[length-1]))
    print()
