
temps = []

with open("data_april_2017_lund.txt", "r") as f:
#    print(f.read().split("\n")[:-1])
    temps = list(map(lambda x: float(x.split()[3]), f.read().split("\n")[:-1]))

print(temps)
with open("temps_april_2017_lund.txt", "w") as f:
    for i in range(len(temps)):
        if(i < len(temps)-1):
            f.write(str(temps[i]) + "\n")
        else:
            f.write(str(temps[i]))
