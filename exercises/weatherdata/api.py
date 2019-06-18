import gzip
import matplotlib.pyplot as plt


def get_station_data():
    result = {}
    with gzip.open('1961.all.ssv.gz', 'rt') as f:
        raw_data = f.read().split('\n\n')
        for s in raw_data:
            station_data = s.split('\n')
            name = ' '.join(station_data[0].split()[1:])
            data = []
            for entry in station_data[1:]:
                y, m, d, t = entry.split()
                data.append((int(y), int(m), int(d), float(t)))
            if(len(name) > 0):
                result[name] = data
    return result


def plot(x=None, y=None, fname="plot.png"):
    if x: 
        plt.plot(x, y)
    else:
        plt.plot(y)
    plt.savefig(fname)
    plt.show()

