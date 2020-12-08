import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import collections as mc
import math

### FUNCTIONS ###
def distance(a,b): # function that returns distance between two points
    return(abs(math.sqrt((x[a] - x[b]) ** 2 + (y[a] - y[b]) ** 2)))

def rips (degree, distance): # function that returns vertices present in the rips complex given degree and distance
    vertices = []
    i = 0
    while i < num:
        if sorted_dist_mat[i,degree] <= distance:
            vertices.append(i)
        i += 1
    return(vertices)

### PARAMETERS ###
num = 5 # number of points
x = np.random.uniform(-100,100,num) # uniform distribution for x
y = np.random.uniform(-100,100,num) # uniform distribution for y

### INITIATION ###
dist_mat = np.zeros((num,num)) # empty space to store distance matrix
sorted_dist_mat = np.zeros((num,num)) # empty space to store sorted distance matrix
edges = np.zeros(int(num * (num - 1) / 2)) # empty space to store all edge length

# Distance Matrix and Sorted Edges
i = 0
k = 0
while i < num:
    j = i + 1
    while j < num:
        dist_mat[j,i] = dist_mat[i,j] = edges[k] = distance(i,j) # store distance
        j += 1
        k += 1
    i += 1
edges = np.sort(edges) # sort edges
edges = np.insert(edges,0,0) # add 0 to the front of edges
print(dist_mat) # print distance matrix
print(edges) # print sorted edges

# Sorted Distance Matrix
i = 0
while i < num:
    sorted_dist_mat[i,] = np.sort(dist_mat[i,]) # sort distance matrix by row
    i += 1
print(sorted_dist_mat) # print sorted distane matrix

### GRAPHING ###
fig, ax = plt.subplots(int(1+num*(num-1)/2), num, sharex=True, sharey=True) # create all subplots sharing x and y vertices
degree = 0
while degree < num: # loop for all degrees
    dist_index = int(num*(num-1)/2) # start with the largest distance
    for distance in edges: # loop for all distances at critical points
        keeps = rips(degree, distance) # get vertices in the rips complex
        keep_edges = [] # empty array to store the edges in the rips complex
        i = 0
        while i < len(keeps): # loop for all vertices in the rips complex
            j = i + 1
            a = keeps[i]
            while j < len(keeps):
                b = keeps[j]
                if dist_mat[a,b] <= distance: # if edge in the rips complex
                    keep_edges.append([(x[a],y[a]),(x[b],y[b])]) # add edge
                j += 1
            i += 1
        ax[dist_index,num-1-degree].scatter(x[keeps],y[keeps],s=10) # add vertices to the scatterplot
        lc = mc.LineCollection(keep_edges, linewidths=1) # create edges
        ax[dist_index,num-1-degree].add_collection(lc) # add edges to the scatterplot
        ax[dist_index,num-1-degree].set_xlim(-100,100) # set x limit for scatterplot
        ax[dist_index,num-1-degree].set_ylim(-100,100) # set y limit for scatterplot
        ax[dist_index,num-1-degree].margins(0.1) # set margins for scatterplot
        #ax[dist_index,num-1-degree].xaxis.set_visible(False) # disable x axis
        #ax[dist_index,num-1-degree].yaxis.set_visible(False) # disable y axis
        plt.setp(ax[-1,num-1-degree],xlabel=degree) # setup x labels for the plot
        plt.setp(ax[dist_index,0],ylabel=int(distance)) # set up y labels for the plot
        dist_index -= 1 # decrease distance index

    degree += 1

plt.show() # show plot