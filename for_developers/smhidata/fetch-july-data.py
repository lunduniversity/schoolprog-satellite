# Create files in julydir
# Will extract data from SMHI files
# Will extract July temperatures from those stations where there are data points
#  for all days in July for all three years 2016, 2017, and 2018.
# Will store each such July in a separate textfile in julydir.
# Names will be mangled to not include blanks, Å, Ä, Ö, å, ä, ö
# The SMHI station number is included in the file name as well.
import sys
from wrap_smhi_api import *
from collections import defaultdict
start_year = 2016
end_year = 2018
try:
    os.stat('julydir')
except:
    os.mkdir('julydir')
def print_temps(i, name, temps, yearstring):
    filename = asciiname(name) + "_" + str(i) + "_july_" + yearstring + ".txt"
    path = os.path.join("julydir", filename)
    if not os.path.isfile(path): # Write file if it does not already exist
        with open(path, 'w') as f:
            for e in range(len(temps)-1):
                f.write(str(temps[e])+"\n")
            f.write(str(temps[-1]))
    sys.stderr.write(filename + '\n')
def asciiname(name):
    n = name.replace(" ", "_")
    n = n.replace("Å", "AA")
    n = n.replace("Ä", "AE")
    n = n.replace("Ö", "OE")
    n = n.replace("å", "aa")
    n = n.replace("ä", "ae")
    n = n.replace("ö", "oe")
    return n
stations = get_stations()
days = list(range(1,32))
for i, name in stations:
    sys.stderr.write(str(i) + "; " + name + '\n')
    data = list(get_data(i))
    temp2016 = []
    days2016 = []
    temp2017 = []
    days2017 = []
    temp2018 = []
    days2018 = []
    for (y, m, d), t in data:
        if y==2016 and m==7:
            temp2016.append(t)
            days2016.append(d)
        if y==2017 and m==7:
            temp2017.append(t)
            days2017.append(d)
        if y==2018 and m==7:
            temp2018.append(t)
            days2018.append(d)
    if days2016 == days and days2017 == days and days2018 == days:
        print_temps(i, name, temp2016, "2016")
        print_temps(i, name, temp2017, "2017")
        print_temps(i, name, temp2018, "2018")

#     station_lines = [] # Text lines to output for this station
#     station_lines.append("{} {}".format(i, name))
#     for (y, m, d), t in data:
#         # Use only data points between start and end year, inclusive
#         if y>=start_year and y<=end_year:
#             station_lines.append("{} {} {} {}".format(y, m, d, t))
#     (y1, m1, d1, t1) = station_lines[1].split() # First data point
#     (y2, m2, d2, t2) = station_lines[-1].split() # Last data point
#     # Skip stations that don't start and end at the desired dates
#     if (y1, m1, d1)==(str(start_year), "1", "1") and (y2, m2, d2)==(str(end_year), "12", "31"):
#         # Skip stations with too few data points in the desired years
#         if len(station_lines)>min_no_of_data_points:
#             all_lines += station_lines
#             all_lines.append('')
#             num_saved_stations += 1
#             sys.stderr.write("Saved\n")
# print('\n'.join(all_lines))
# sys.stderr.write("Saved a total of " + str(num_saved_stations) + " stations")
