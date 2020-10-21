import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import collections as mc
import math

def distance(a,b):
    return(abs(math.sqrt((x[a] - x[b]) ** 2 + (y[a] - y[b]) ** 2)))

# uniform
num = 5
x = np.random.uniform(-100,100,num)
y = np.random.uniform(-100,100,num)

dist_mat = np.zeros((num,num))
sorted_dist_mat = np.zeros((num,num))

i = 0
while i < num:
    j = i + 1
    while j < num:
        dist_mat[j,i] = dist_mat[i,j] = distance(i,j)
        j += 1
    i += 1
print(dist_mat)

i = 0
while i < num:
    sorted_dist_mat[i,] = np.sort(dist_mat[i,])
    i += 1
print(sorted_dist_mat)

def rips (degree, distance):
    vertices = []
    i = 0
    while i < num:
        if sorted_dist_mat[i,degree] <= distance:
            vertices.append(i)
        i += 1
    return(vertices)

degree = 0
distance = 0
while(degree >= 0 and distance >= 0):
    degree = int(input("Enter degree: "))
    distance = int(input("Enter distance: "))
    keeps = rips(degree, distance)
    edges = []
    i = 0
    while i < len(keeps):
        j = i + 1
        a = keeps[i]
        while j < len(keeps):
            b = keeps[j]
            if dist_mat[a,b] <= distance:
                edges.append([(x[a],y[a]),(x[b],y[b])])
            j += 1
        i += 1
    # print(keeps)
    # print(edges)

    lc = mc.LineCollection(edges, linewidths=2)
    fig, ax = plt.subplots()
    ax.add_collection(lc)

    ax.set_xlim(-100,100)
    ax.set_ylim(-100,100)
    ax.margins(0.1)
    plt.scatter(x[keeps],y[keeps],s=10)
    plt.show()