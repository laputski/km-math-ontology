# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:29:28 2015

@author: MetaLHeaD
"""

try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx

G=nx.Graph()

pos={0:(0,0),
     1:(1,0),
     2:(0,1),
     3:(1,1),
     4:(0.5,2.0)}

elist=[(1,4,1),(0,4,1),(0,3,1),(1,2,1),(2,3,1)]
G.add_weighted_edges_from(elist)

nx.draw_networkx_nodes(G,pos,node_size=3000,nodelist=[4])
nx.draw_networkx_nodes(G,pos,node_size=3000,nodelist=[0,1,2,3],node_color='b')
nx.draw_networkx_edges(G,pos)
plt.axis('off')

plt.show() 