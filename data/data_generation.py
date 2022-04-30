# Importing Libraries 
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import snap
import igraph
import copy
import powerlaw
import time
import csv


def Node_information(G, filename):
    t = time.time()
    betweenness = np.array(list(nx.betweenness_centrality(G).values()))
    print(f"Time for Betweenness: {time.time() - t}")
    t = time.time()
    
    closeness = np.array(list(nx.closeness_centrality(G).values()))
    print(f"Time for Closeness: {time.time() - t}")
    t = time.time()

    pagerank = np.array(list(nx.pagerank(G).values()))
    print(f"Time for Pagerank: {time.time() - t}")
    t = time.time()

    clustering_coefficient = np.array(list(nx.clustering(G).values()))
    print(f"Time for Clustering COefficient: {time.time() - t}")
    t = time.time()

    hubs, authorities = nx.hits(G)
    hubs, authorities = np.array(list(hubs.values())), np.array(list(authorities.values()))
    print(f"Time for HITS1: {time.time() - t}")
    t = time.time()
    
    csvwriter = csv.writer(open(filename, 'w'))
    csvwriter.writerow(["Nodes", "Betweennness", "Closeness", "Clustering_Coefficient", "Pagerank", "Hubs", "Authorities"])    
    csvwriter.writerows(np.array([G.Nodes(), betweenness, closeness, clustering_coefficient, pagerank, hubs, authorities]).T)
    print(f"Time for Writing: {time.time() - t}")


# Creating Barabasi-Albert Graph
nodes = random.randint(20000, 100000)
initial_nodes = random.randint(3, 20)
# n1 = 20000
# p1 = 0.5
# G = nx.erdos_renyi_graph(n1, p1)
name = "edgelist_ba_" + str(nodes) + "_" + str(initial_nodes) + ".txt"
start = time.time()
print(f"Nodes: {nodes}, Initial_nodes: {initial_nodes}")
edges = np.ceil(initial_nodes * nodes * (nodes - 1) / 2)
G = snap.GenPrefAttach(nodes, initial_nodes)
print(f"Time for creating: {time.time() - start}")
t = time.time()
snap.SaveEdgeList(G, name)
print(f"Time consumed for {nodes} nodes: {time.time() - t}")
t = time.time()
# Computing
# comments = f"Nodes: {nodes} and initial_nodes: {initial_nodes}"
Node_information(G, "ba_" + str(nodes) + "_" + str(initial_nodes) + ".csv")
print(f"Time for computing Info: {time.time() - t}")
print(f"Total time: {time.time() - start}")