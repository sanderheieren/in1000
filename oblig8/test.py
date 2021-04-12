import random
rad = 3
kolonne = 3
rutenett = []
for i in range(rad):
    radMatrix = []
    for j in range(kolonne):
        radMatrix.append(j)
    rutenett.append(radMatrix)

print(random.randint(1,2))
    

print(rutenett[0][1])