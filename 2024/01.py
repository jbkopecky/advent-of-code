data = open("./data/01_0.txt", "r")
data = data.readlines()
data = [x.replace("\n", "").split("    ") for x in data]

a = [int(x[0]) for x in data]
b = [int(x[1]) for x in data]

print(sum([abs(i-j) for i, j in zip(sorted(a), sorted(b))]))
print(sum([i * sum([j == i for j in b]) for i in a]))
