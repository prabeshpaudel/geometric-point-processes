import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import collections as mc
from queue import PriorityQueue
import math
import csv

# np.random.seed(3)

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
num = 40 # number of points
trial = 1 # number of trials
edge_num = int(num * (num - 1) / 2) # number of edges
connected_sum = pd.DataFrame(0, index = list(range(edge_num,-1,-1)), columns = list(range(num-1,-1,-1)))

# interested points
num_yellow = 5
yellow_degree = [2, 3, 3, 4, 4]
yellow_distance = [727, 732, 739, 719, 729]
yellow_con = pd.DataFrame(np.zeros((num_yellow, trial)))

t = 0
while t < trial:
    print(t)
    ### INITIATION ###
    x = np.random.uniform(-100,100,num) # uniform distribution for x
    y = np.random.uniform(-100,100,num) # uniform distribution for y

    dist_mat = np.zeros((num,num)) # empty space to store distance matrix
    sorted_dist_mat = np.zeros((num,num)) # empty space to store sorted distance matrix
    edges = np.zeros(edge_num) # empty space to store all edge length
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
    # print("\nDistance Matrix")
    # print(dist_mat) # print distance matrix
    # print(edges_dist) # print edge dictionary

    # Sorted Distance Matrix
    i = 0
    while i < num:
        sorted_dist_mat[i,] = np.sort(dist_mat[i,]) # sort distance matrix by row
        i += 1
    # print("\nSorted Distance Matrix")
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
        i += 1
    # print("\nSorted Edge Matrix")
    # print(sorted_edge_mat) # print sorted edge matrix

    # Connected Components Matrix
    connected = pd.DataFrame(-1, index = np.flip(sorted_edge_mat[:,0]), columns = list(range(num-1,-1,-1)))
    connected.loc[0] = np.full((num),0) # add the row for distance 0

    for deg in range(0,num):
        q = PriorityQueue() # create priority queue
        j = 0
        for i in range(0,edge_num): # loop for all edges
            while j < num: # loop for all vertices
                q.put((sorted_dist_mat[j,deg],-j)) # add vertices to queue
                j += 1
            q.put((sorted_edge_mat[i,deg],sorted_edge_mat[i,0])) # add edges to queue

        visited = np.full((num),num) # the number of clusters for all vertices
        cluster_num = 0 # total number of clusters
        clusters = [] # list of numpy arrays, each containing a cluster of vertices

        while not q.empty():
            next_item = q.get() # get the node/edge with the least critical bi-grade distance
            if next_item[1] <= 0: # if it is a node
                ind = next_item[1] * -1 # get the index for the node
                visited[ind] = cluster_num # assign a new cluster number
                clusters.append([ind]) # append node into cluster
            else: # if it is an edge
                points = edges_dist[next_item[1]] # get the two associated nodes
                if visited[points[0]] != visited[points[1]]: # if in two different clusters
                    min_cluster_num = min(visited[points[0]],visited[points[1]]) # get the cluster with smaller id
                    max_cluster_num = max(visited[points[0]],visited[points[1]]) # get the cluster with bigger id
                    for node in clusters[max_cluster_num]:
                        visited[node] = min_cluster_num # combine the clusters in visited
                        clusters[min_cluster_num].append(node) # combine the clusters
                    clusters.pop(max_cluster_num) # delete the other cluster
                    while max_cluster_num < len(clusters):
                        for node in clusters[max_cluster_num]:
                            visited[node] -= 1 # decrease the cluster number for all other clusters
                        max_cluster_num += 1
            cluster_num = len(clusters) # get current number of clusters
            connected.at[next_item[0],deg] = cluster_num # add the number of connected components to matrix

    for deg in range(0,num): # fill in the blanks (loop through degree)
        for i in range(edge_num,0,-1): # loop through distance
            if connected.iloc[i-1,deg] == -1: # if not a critical bi-grade
                connected.iloc[i-1,deg] = connected.iloc[i,deg] # follow the previous critical bigrade

    # print points and connected matrix to txt
    # if t < 10:
    #     with open('bi6_results.txt', 'a') as file:
    #         content_x = str(x)
    #         content_y = str(y)
    #         file.write(content_x)
    #         file.write('\n')
    #         file.write(content_y)
    #         file.write('\n')
    #         file.write(
    #             connected.to_string()
    #         )
    #         file.write('\n')
    #         file.write('\n')

    connected.reset_index(drop=True, inplace=True) # delete index for connected
    connected_sum = connected_sum.add(connected, axis = 1) # add to the sum of connected matrices

    # for yellow in range(0,num_yellow):
    #     yellow_con.at[yellow,t] = connected.at[yellow_distance[yellow],yellow_degree[yellow]]
        # print(connected.at[yellow_distance[yellow],yellow_degree[yellow]])
    
    t += 1

with open('yellow.txt', 'a') as file:
    file.write(yellow_con.to_string())
# connected_sum.to_csv('bi6_results.csv', index=False)

