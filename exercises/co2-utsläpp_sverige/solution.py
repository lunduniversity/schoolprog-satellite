import matplotlib.pyplot as plt
import numpy as np

with open("utslapp3.txt", "r") as f:
    data = f.read()

data = data.split("\n")

"""
with open("utslapp3.txt", "w") as f:
    for i in range(len(data)):
        f.write(data[i])
        if(i != len(data)-1):
            f.write("\n")
"""
raw_data = []
for line in data:
    raw_data.append(line.split("\t"))
    print(raw_data[-1])

raw_data = raw_data[1:]

data_by_category = {}
for measure in raw_data:
    if(measure[1] not in data_by_category):
        data_by_category[measure[1]]=[]
    data_by_category[measure[1]].append(float(measure[3]))

years = [i for i in range(1990, 2018)]
y = data_by_category['NATIONELL TOTAL (exklusive LULUCF, inklusive internationella transporter)']

plt.plot(years, y)
plt.ylim(0, 110000)

bars = []
width=0.5

def plot_bars():
    categories = list(data_by_category.keys())
    categories = categories[1:]
    bottoms = np.zeros(28)
    for category in categories:
        bars.append(plt.bar(years, data_by_category[category], width, bottom=bottoms))
        bottoms = np.array(data_by_category[category]) + bottoms

    

plot_bars()
plt.legend(tuple(list(map(lambda x:x[0], bars))[::-1]), tuple(list(data_by_category.keys())[1:][::-1]))

plt.show()
#print(data_by_category.keys())

