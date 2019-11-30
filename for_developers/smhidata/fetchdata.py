import sys
from wrap_smhi_api import *
from collections import defaultdict
start_year = 1961
end_year = 2018
margin = 100 # Allowed missed data points
min_no_of_data_points = (end_year - start_year + 1)*365.25 - 200
stations = get_stations()
all_lines = [] # Text lines to output
num_saved_stations = 0
for i, name in stations:
    sys.stderr.write(str(i) + "; " + name + '\n')
    data = list(get_data(i))
    if len(data)>1:
        sys.stderr.write("First data point: " + str(data[0]) + "\n")
        sys.stderr.write("Last data point: " + str(data[-1]) + "\n")
        sys.stderr.write("Number of data points: " + str(len(data)) + "\n")
        (y1, m1, d1), t1 = data[0]
        (y2, m2, d2), t2 = data[-1]
        datapoints_per_year = len(data)//(y2-y1+1)
        sys.stderr.write("Average data points per year: " + str(datapoints_per_year) + "\n")

    # Skip stations with too few data points overall
    if len(data) < min_no_of_data_points: continue

    # Skip stations that start measuring later than start year
    (y, m, d), t = data[0]
    if y>start_year: continue

    station_lines = [] # Text lines to output for this station
    station_lines.append("{} {}".format(i, name))
    for (y, m, d), t in data:
        # Use only data points between start and end year, inclusive
        if y>=start_year and y<=end_year:
            station_lines.append("{} {} {} {}".format(y, m, d, t))
    (y1, m1, d1, t1) = station_lines[1].split() # First data point
    (y2, m2, d2, t2) = station_lines[-1].split() # Last data point
    # Skip stations that don't start and end at the desired dates
    if (y1, m1, d1)==(str(start_year), "1", "1") and (y2, m2, d2)==(str(end_year), "12", "31"):
        # Skip stations with too few data points in the desired years
        if len(station_lines)>min_no_of_data_points:
            all_lines += station_lines
            all_lines.append('')
            num_saved_stations += 1
            sys.stderr.write("Saved\n")
print('\n'.join(all_lines))
sys.stderr.write("Saved a total of " + str(num_saved_stations) + " stations")
