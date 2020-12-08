import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import collections as mc
import math

def distance(a,b): # function that returns distance between two points
    return(abs(math.sqrt((x[a] - x[b]) ** 2 + (y[a] - y[b]) ** 2)))

num = 5 # number of points
x = np.random.uniform(-100,100,num) # uniform distribution for x
y = np.random.uniform(-100,100,num) # uniform distribution for y

dist_mat = np.zeros((num,num)) # empty space to store distance matrix
sorted_dist_mat = np.zeros((num,num)) # empty space to store sorted distance matrix

i = 0
while i < num:
    j = i + 1
    while j < num:
        dist_mat[j,i] = dist_mat[i,j] = distance(i,j) # store distance into distance matrix
        j += 1
    i += 1
print(dist_mat) # print distance matrix

i = 0
while i < num:
    sorted_dist_mat[i,] = np.sort(dist_mat[i,]) # sort distance matrix by row
    i += 1
print(sorted_dist_mat) # print sorted distance matrix

def rips (degree, distance): # function that returns vertices present in the rips complex given degree and distance
    vertices = [] # empty array to store vertices
    i = 0
    while i < num:
        if sorted_dist_mat[i,degree] <= distance: # check if vertex present in the complex
            vertices.append(i) # add vertex
        i += 1
    return(vertices)

# Graph the rips complex
degree = 0
distance = 0
while(degree >= 0 and distance >= 0): # loop for input
    degree = int(input("Enter degree: ")) # input degree
    distance = int(input("Enter distance: ")) # input distance
    keeps = rips(degree, distance) # vertices present given degree and distance
    edges = [] # empty array to store edges
    i = 0
    while i < len(keeps):
        j = i + 1
        a = keeps[i] # i-th vertex
        while j < len(keeps):
            b = keeps[j] # j-th vertex
            if dist_mat[a,b] <= distance: # if edge is present in the complex
                edges.append([(x[a],y[a]),(x[b],y[b])]) # add edge
            j += 1
        i += 1
    # print(keeps)
    # print(edges)

    lc = mc.LineCollection(edges, linewidths=2) # create edges
    fig, ax = plt.subplots() # subplots
    ax.add_collection(lc) # add edges in the graph

    ax.set_xlim(-100,100) # set graph x limit
    ax.set_ylim(-100,100) # set graph y limit
    ax.margins(0.1) # set graph margins
    plt.scatter(x[keeps],y[keeps],s=10) # plot the points
    plt.show() # show graph