
def get_station_data(textfilename):
    # Returns a dict from station name to list of (y, m, d, t) tuples
    result = {}
    with open(textfilename, "r") as f:
        # Stations are separated by a blank line
        raw_data = f.read().split('\n\n')
        for s in raw_data:
            # The first line for a station is the id and its name (which may contain blanks)
            station_data = s.split('\n')
            name = ' '.join(station_data[0].split()[1:])
            # The remaining lines contain the temperature data
            data = []
            for entry in station_data[1:]:
                y, m, d, t = entry.split()
                data.append((int(y), int(m), int(d), float(t)))
            if(len(name) > 0):
                result[name] = data
    return result

def get_station_list(textfilename):
    # Returns a list of (id:str, name:str) tuples for the stations
    result = []
    with open(textfilename, "r") as f:
        # Stations are separated by a blank line
        raw_data = f.read().split('\n\n')
        for s in raw_data:
            # The first line for a station is the id and its name (which may contain blanks)
            station_data = s.split('\n')
            id = station_data[0].split()[0]
            name = ' '.join(station_data[0].split()[1:])
            result.append((id, name))
    return result
