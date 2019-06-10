
temps = []

with open("data_april_2017_lund.txt", "r") as f:
#    print(f.read().split("\n")[:-1])
    temps = list(map(lambda x: float(x.split()[3]), f.read().split("\n")[:-1]))

print(temps)
with open("temps_april_2017_lund.txt", "w") as f:
    for temp in temps:
        f.write(str(temp) + "\n")
