# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:09:32 2022

@author: jacke
"""
import networkx as nx 
import matplotlib.pyplot as plt
g =nx.Graph()
pos=nx.get_node_attributes(g,'pos')

populations = [10000,23450,30000,50000,100000]
popdensity = [5000,2000,8000,10000,6000]
names = ["A","B","C","D","E"]
pos=[(1,1),(1,4),(4,4),(4,1),(3,3)]

nodeSize = []
labels={}
areas =[]
for i in range (0,len(populations)):
    areas.append((populations[i]/popdensity[i])*100)
    labels[names[i]] = f"port {i+1}"     

for i in range (0,5):
    g.add_node(names[i],pos=pos[i])


g.add_edges_from([("B","D"),("A","B"),("C","E"),("D","E"),("B","E"),("A","E")])
pos=nx.get_node_attributes(g,'pos')
print(pos)

nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True))
#next try and change color over time



#next bar chart, and number of infected










