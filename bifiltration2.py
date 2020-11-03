import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import collections as mc
import math

def distance(a,b):
    return(abs(math.sqrt((x[a] - x[b]) ** 2 + (y[a] - y[b]) ** 2)))

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
x = np.random.uniform(-100,100,num)
y = np.random.uniform(-100,100,num)

dist_mat = np.zeros((num,num))
sorted_dist_mat = np.zeros((num,num))
edges = np.zeros(int(num * (num - 1) / 2))

# distance matrix and sorted edges
i = 0
k = 0
while i < num:
    j = i + 1
    while j < num:
        dist_mat[j,i] = dist_mat[i,j] = edges[k] = distance(i,j)
        j += 1
        k += 1
    i += 1
edges = np.sort(edges)
edges = np.insert(edges,0,0)
print(dist_mat)
print(edges)

# sorted distance matrix
i = 0
while i < num:
    sorted_dist_mat[i,] = np.sort(dist_mat[i,])
    i += 1
print(sorted_dist_mat)

# sorted index matrix
# sorted_index_mat = np.zeros((num,num))
# i = 0
# while i < num:
#     j = 0
#     while j < num:
#         sorted_index_mat[i,j] = dist_mat[i,].tolist().index(sorted_dist_mat[i,j])
#         j += 1
#     i += 1
# sorted_index_mat = sorted_index_mat.astype(np.int)
# print(sorted_index_mat)

# printing bifiltrations
# degree = 0
# while degree < num:
#     for distance in edges:
#         keeps = rips(degree, distance)
#         keep_edges = []
#         i = 0
#         while i < len(keeps):
#             j = i + 1
#             a = keeps[i]
#             while j < len(keeps):
#                 b = keeps[j]
#                 if dist_mat[a,b] <= distance:
#                     keep_edges.append([(x[a],y[a]),(x[b],y[b])])
#                 j += 1
#             i += 1
#         lc = mc.LineCollection(keep_edges, linewidths=2)
#         fig, ax = plt.subplots()
#         ax.add_collection(lc)

#         ax.set_xlim(-100,100)
#         ax.set_ylim(-100,100)
#         ax.margins(0.1)
#         plt.scatter(x[keeps],y[keeps],s=10)
#         plt.show()
#     degree += 1

fig, ax = plt.subplots(11, 5, sharex=True, sharey=True)
degree = 0
while degree < num:
    dist_index = 10
    for distance in edges:
        keeps = rips(degree, distance)
        keep_edges = []
        i = 0
        while i < len(keeps):
            j = i + 1
            a = keeps[i]
            while j < len(keeps):
                b = keeps[j]
                if dist_mat[a,b] <= distance:
                    keep_edges.append([(x[a],y[a]),(x[b],y[b])])
                j += 1
            i += 1
        ax[dist_index,num-1-degree].scatter(x[keeps],y[keeps],s=10)
        lc = mc.LineCollection(keep_edges, linewidths=1)
        ax[dist_index,num-1-degree].add_collection(lc)
        ax[dist_index,num-1-degree].set_xlim(-100,100)
        ax[dist_index,num-1-degree].set_ylim(-100,100)
        ax[dist_index,num-1-degree].margins(0.1)
        #ax[dist_index,num-1-degree].xaxis.set_visible(False)
        #ax[dist_index,num-1-degree].yaxis.set_visible(False)
        plt.setp(ax[-1,num-1-degree],xlabel=degree)
        plt.setp(ax[dist_index,0],ylabel=int(distance))
        dist_index -= 1

    degree += 1

plt.show()