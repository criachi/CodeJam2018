import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import osmnx as ox

centers = []


G = ox.graph_from_place('Chicago, Illinois, USA',network_type="drive")
fig, ax = ox.plot_graph(G, show=False, close=False, node_zorder=0)\



file = open("out.csv",'r')

for i in [i.split(",")[1:] for i in file.read().split("\n")[1:-1]]:

    centers.append([float(i[-1]),float(i[-2])])


X = np.array(centers)

#plt.scatter(X[:,0],X[:,1], label='True Position')
#plt.show()

kmeans = KMeans(n_clusters=10)  
kmeans.fit(X)

 

plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black', zorder=4)

plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow', s=4, zorder=2)



plt.show()