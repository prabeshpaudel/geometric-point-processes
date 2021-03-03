import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import collections as mc
import math
import csv

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
num = 100 # number of points
trial = 1000 # number of trials
edge_num = int(num * (num - 1) / 2) # number of edges

with open('results.csv','w', newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(list(range(1,num)))

t = 0
while t < trial:
    ### INITIATION ###
    x = np.random.uniform(-100,100,num) # uniform distribution for x
    y = np.random.uniform(-100,100,num) # uniform distribution for y

    dist_mat = np.zeros((num,num)) # empty space to store distance matrix
    sorted_dist_mat = np.zeros((num,num)) # empty space to store sorted distance matrix
    edges = np.zeros(edge_num) # empty space to store all edge length
    edges_critical = np.zeros(edge_num) # empty space to store 
    sorted_edge_mat = np.zeros((edge_num,num)) # empty space to store sorted edge matrix (critical distance at each degree for all edges)
    # critical distance: the distance at which the edge/vertex appears in the rips complex, given the degree
    edges_dist = {} # edge dictionary to store edge and corresponding vertices

    # Distance Matrix, Sorted Edges, and Distance dictionary
    i = 0
    k = 0
    while i < num:
        j = i + 1
        while j < num:
            dist_mat[j,i] = dist_mat[i,j] = edges[k] = distance(i,j)  # store distance
            edges_dist[edges[k]]= (i,j) # store the corresponding vertices for the edge
            j += 1
            k += 1
        i += 1
    edges = np.sort(edges) # sort edges
    # print(dist_mat) # print distance matrix
    # print(edges) # print sorted edges
    # print(edges_dist) # print edge dictionary

    # Sorted Distance Matrix
    i = 0
    while i < num:
        sorted_dist_mat[i,] = np.sort(dist_mat[i,]) # sort distance matrix by row
        i += 1
    # print(sorted_dist_mat) # print sorted distance matrix

    # Sorted Edge Matrix
    filler = [] # emtpy array
    i = 0
    while i < edge_num: # loop through all edges
        j = 0
        while j < num: # loop through number of degrees
            points = edges_dist[edges[i]] # two vertices associated with the edge
            one = sorted_dist_mat[points[0],j] # critical distance for vertex 1
            two = sorted_dist_mat[points[1],j] # critical distance for vertex 2
            sorted_edge_mat[i,j] = max(one,two,edges[i]) # critical distance for the edge
            j += 1
        filler = np.unique(sorted_edge_mat[i,]) # unique critical distances for the edge
        edges_critical[i] = len(filler) # length of unique critical distances or the number of critical points
        i += 1
    # print(sorted_edge_mat) # print sorted edge matrix

    ### RESULTS ###
    #print(np.array(np.unique(edges_critical, return_counts=True)).T)
    results = np.unique(edges_critical, return_counts=True) # counts for # of edges given # of critical points
    # print(results)
    # print(results[1].tolist())

    with open('results.csv','a', newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(results[1].tolist())

    t += 1

# fig = plt.figure() # print figure
# ax = fig.add_axes([0,0,1,1]) # add axis
# ax.bar(results[0],results[1]) # plot results
# plt.show() # show plot