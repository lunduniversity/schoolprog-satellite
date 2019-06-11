# 2. Inläsning av mer data
import api
data = api.get_station_data()
print(list(data.keys()))
print(type(list(data.keys())))

lund = data["Lund"]
print(lund[:10])

temps = []
for day in lund:
    temps.append(day[3])

#api.plot(y=temps, fname="plot_2_no_time.png")

times = []
for datum in lund:
    (y, m, d, t) = datum
    times.append(y+((m-1)*30+d)/365)

#api.plot(x=times, y=temps, fname="plot_2_years.png")

# 3. Temperaturförändring under ett år

def data_by_year(year, city_data):
    result = []
    for datum in city_data:
        if datum[0] == year:
            result.append(datum[3])
    return result

lund2016 = data_by_year(2016, lund)
#api.plot(y=lund2016, fname="plot_3.png")

# 4. Medeltemperaturen för varje år

def avg(data):
    summa = 0
    for tal in data:
        summa += tal
    medel = summa / len(data)
    return medel
   
years = []
avg_temps = []
for year in range(1961, 2018):
    years.append(year)
    avg_temps.append(avg(data_by_year(year, lund)))

#api.plot(x=years, y=avg_temps, fname="plot_4.png")    

# 5. Medeltemperaturen för hela Sverige

def mean_by_year(city, year):
    city_data = data[city]
    year_temps = data_by_year(year, city_data)
    return avg(year_temps)

total_mean = []
years = []
for year in range(1961, 2018):
    cities = list(data.keys())
    city_means = []
    for city in cities:
        city_means.append(mean_by_year(city, year))
    total_mean.append(avg(city_means))
    years.append(year)
api.plot(x=years, y=total_mean, fname="plot_5")


