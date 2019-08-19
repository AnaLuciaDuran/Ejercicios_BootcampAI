import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
#importar los datos y ver como están
x = pd.read_csv("iris.csv")
x.head()
#Calcular la distancia euclideana
def euc_dist(x1, x2, length):
    distance = 0
    for x in range(length):
        distance += np-square((x1[x] - x2[x]))
    return np.sqrt(distance)
def getNeighbors(trainingSet, testInstance, k):
    distances = {}
    sort={}
    
    length = len(testInstance)-1
    
    for x in range(len(trainingSet)):
        dist = euc_dist(testInstance, trainingSet.iloc[x], length)
        distances[x] = dist[0]
    sortdist = sorted(distances.items(), key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(sortdist[x][0])
    return neighbors

def getResponse(neighbors):
    Votes = {}
    for x in range(len(neighbors)):
        response = trainingSet.iloc[neighbors[x]][-1]
        if response in Votes:
            Votes[response] += 1
        else:
            Votes[response] = 1
    sortvotes = sorted(Votes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

testSet = [[6.8, 3.4, 4.8, 2.4]]
test = pd.DataFrame(testSet)
k = 15
k1 = 35
result,neigh = knn(data, test, k)
result1,neigh1 = knn(data, test, k1)
print(result)
print(neigh)
print(result1)
print(neigh1)