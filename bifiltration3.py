import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import collections as mc
import math

# function for distance
def distance(a,b):
    return(round(abs(math.sqrt((x[a] - x[b]) ** 2 + (y[a] - y[b]) ** 2)),3))

# function to build vertices of the rips complex given degree and distance
def rips (degree, distance):
    vertices = []
    i = 0
    while i < num:
        if sorted_dist_mat[i,degree] <= distance:
            vertices.append(i)
        i += 1
    return(vertices)

# initation
num = 5
edge_num = int(num * (num - 1) / 2)
x = np.random.uniform(-100,100,num)
y = np.random.uniform(-100,100,num)

dist_mat = np.zeros((num,num))
sorted_dist_mat = np.zeros((num,num))
edges = np.zeros(edge_num)
edges_critical = np.zeros(edge_num)
sorted_edge_mat = np.zeros((edge_num,num))
edges_dist = {}

# distance matrix and sorted edges
i = 0
k = 0
while i < num:
    j = i + 1
    while j < num:
        dist_mat[j,i] = dist_mat[i,j] = edges[k] = distance(i,j)
        edges_dist[edges[k]]= (i,j)
        j += 1
        k += 1
    i += 1
edges = np.sort(edges)
print(dist_mat)
print(edges)
print(edges_dist)

# sorted distance matrix
i = 0
while i < num:
    sorted_dist_mat[i,] = np.sort(dist_mat[i,])
    i += 1
print(sorted_dist_mat)

# sorted edge matrix
filler = []
i = 0
while i < edge_num:
    j = 0
    while j < num:
        points = edges_dist[edges[i]]
        one = sorted_dist_mat[points[0],j]
        two = sorted_dist_mat[points[1],j]
        sorted_edge_mat[i,j] = max(one,two,edges[i])
        j += 1
    filler = np.unique(sorted_edge_mat[i,])
    edges_critical[i] = len(filler)
    i += 1
print(sorted_edge_mat)

#print(np.array(np.unique(edges_critical, return_counts=True)).T)
results = np.unique(edges_critical, return_counts=True)
print(results)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(results[0],results[1])
plt.show()