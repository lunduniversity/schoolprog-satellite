import matplotlib.pyplot as plt

# 1. Inläsning från fil
with open("april_2017.txt", "r") as f:
    data = f.read()
print(data)

print(type(data))

data = data.split("\n")
print(data)
print(type(data))

data = [float(x) for x in data]
print(data)
print(type(data))

plt.plot(data)
plt.savefig("april_2017.png")

