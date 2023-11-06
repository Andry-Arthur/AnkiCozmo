import random

def sample(population, likelihood):

    population = []
    likelihood = []

    sum = 0

    for i in likelihood:
       sum += likelihood[i]

    x = len(population)

    probab = []

    for i in range(x):
       probab.append(likelihood[i] / sum)

    # print(probab)
    cumProb = [probab[0]]

    for i in (n+1 for n in range(x)):
        cumProb.append(cumProb[i - 1] + probab[i])

    cumProb[x - 1] = 1.0

    newPopulation = [None] * x

    for i in range(x):
        v = random.random()
        idx = x - 1
        while idx > 0 and v < cumProb[idx - 1]:
            idx -= 1
            newPopulation[i] = population[idx]
            
    return newPopulation[0]