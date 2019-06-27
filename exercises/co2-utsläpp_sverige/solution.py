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
plt.figure(figsize=(10,10))
plt.grid(True)
plt.plot(years, y)
plt.ylim(0, 110000)

categories = list(data_by_category.keys())
categories = categories[1:]

bars = []
bottoms = np.zeros(28)
plt.figure(figsize=(15,10))
for category in categories:
    bar = plt.bar(years, data_by_category[category], 0.5, bottom=bottoms)
    bars.append(bar)
    bottoms = np.array(data_by_category[category]) + bottoms
plt.grid(True)
plt.ylim(0, 110000)
plt.legend(tuple(map(lambda x:x[0], bars))[::-1], tuple(categories[::-1]))
plt.show()
#print(data_by_category.keys())
