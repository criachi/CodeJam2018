#!/usr/bin/env python
import osmnx as ox 
 
ox.config(log_file=True, log_console=True, use_cache=True)

G = ox.graph_from_place("Chicago, Illinois, USA", network_type = "drive_service")
ox.plot_graph(G)


G2 = ox.load_graphml('network.graphml')
fig, ax = ox.plot_graph(G2)
