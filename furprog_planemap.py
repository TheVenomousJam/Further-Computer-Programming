# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:09:32 2022

@author: jacke
"""
import networkx as nx 
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
n = 1000
g =nx.Graph()
pos=nx.get_node_attributes(g,'pos')
FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='a red circle following a blue sine wave')
writer = FFMpegWriter(fps=240, metadata=metadata)


fig = plt.figure()
populations = [10000,23450,30000,50000,100000]
popdensity = [5000,2000,8000,10000,6000]
names = ["A","B","C","D","E"]
pos=[(1,1),(1,1000),(1000,1000),(1000,1),(500,500)]

nodeSize = []
labels={}
areas = []
for i in range (0,len(populations)):
    areas.append((populations[i]/popdensity[i])*100)
    labels[names[i]] = f"port {i+1}"     

for i in range (0,5):
    g.add_node(names[i],pos=pos[i])


g.add_edges_from([("B","C"),("A","B"),("C","D"),("D","E"),("B","E"),("A","E")])
g.add_edges_from([("D","A"),("C","E")])
pos=nx.get_node_attributes(g,'pos')
print(pos)
nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True))
red_circle, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(n):
        red_circle.set_data([1],[i])
        writer.grab_frame()
    for i in range(n):
        red_circle.set_data([i],[1000])
        writer.grab_frame()
        
    for i in range(n):
        red_circle.set_data([1000],[i])
        writer.grab_frame()
    for i in range(n):
        red_circle.set_data([i],[1])
        writer.grab_frame()
    for i in range(1000,1):
        red_circle.set_data([i],[1])
        writer.grab_frame()
#last for loop isnt working
#increase n maybe?
#put all markers moving at once

    

#next try and change color over time



#next bar chart, and number of infected










