with open("data.txt", "r") as f:
    data=f.read()
data = data.split("\n")
years=[]
co2=[]
trend=[]
co2_dict={}
trend_dict={}
for line in data:
    splitted = line.split()
    years.append(float(splitted[2]))
    co2.append(float(splitted[4]))
    trend.append(float(splitted[5]))
    co2_dict[(int(splitted[0]), int(splitted[1]))] = float(splitted[4]) 
    trend_dict[(int(splitted[0]), int(splitted[1]))] = float(splitted[5])

import matplotlib.pyplot as plt
"""
#Plotta bara co2:
plt.plot(years, co2, color="red", linestyle="solid", marker="o", markersize=1.5, linewidth=0.5)
plt.savefig("keeling.png")

"""
"""
#Plotta co2 och trenden:
plt.plot(years, co2, color="red", linewidth=0.5)
plt.plot(years, trend, color="blue", linewidth=0.7)
plt.savefig("keeling.png")
"""

"""
#Plotta med fler inställningar
plt.plot(years, co2, color="red", linewidth=0.5)
plt.plot(years, trend, color="blue", linewidth=0.7)
plt.xlabel("År")
plt.ylabel("ppm CO2")
plt.title("Keelingkurvan")
plt.legend(["CO2", "Trend"])
plt.grid(True)
plt.savefig("keeling.png")
"""
def avg_year(year):
    total = 0
    values = 0
    for i in range(1,13):
        if((year,i) in co2_dict):
            total += co2_dict[(year,i)]
            values += 1
    return total/values

mean_year = []
for i in range(1958,2020):
    mean_year.append(avg_year(i))

actual_years = [i+0.5 for i in range(1958, 2020)]
"""
#Plotta förskjutna årsmedelvärdet
plt.plot(years, co2, color="red", linewidth=0.5)
plt.plot(actual_years, mean_year, color="blue", linewidth=0.7)
plt.xlabel("År")
plt.ylabel("ppm CO2")
plt.title("Keelingkurvan")
plt.legend(["CO2", "Årsmedelvärde"])
plt.grid(True)
plt.savefig("year_mean.png")
"""

mean_diff = []
for i in range(1958,2018):
    diff = avg_year(i+1)-avg_year(i)
    mean_diff.append(diff)
"""
#Plotta differanserna
plt.plot(range(1958,2018), mean_diff)
plt.savefig("mean_diff.png")
"""

def plot_co2_year(year):
    co2_year = []
    trend_year = []
    for i in range(1, 13):
        co2_year.append(co2_dict[(year, i)])
        trend_year.append(trend_dict[(year, i)])
    plt.plot(range(1, 13), co2_year, color="red", linewidth=2, marker="o")
    plt.plot(range(1, 13), trend_year, color="blue", linewidth=2, marker="^")
    plt.xlabel("Månad")
    plt.ylabel("ppm CO2")
    plt.title("Keelingkurvan 2018")
    plt.legend(["CO2", "Trend"])
    plt.grid(True)
    plt.savefig("month_mean.png")

"""
#Plotta co2 under året 2018
plot_co2_year(2018)
"""



