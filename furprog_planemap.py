# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:09:32 2022

@author: jacke
"""
import networkx as nx 
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
f = 1000
n = 1000
g =nx.Graph()
pos=nx.get_node_attributes(g,'pos')
FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='a red circle following a blue sine wave')
writer = FFMpegWriter(fps=140, metadata=metadata)

fig = plt.figure()
populations = [10000,23450,30000,50000,100000]#changes size of nodes
popdensity = [5000,2000,8000,10000,6000]#changes size of nodes
names = ["A","B","C","D","E"]
pos=[(1,1),(1,1000),(1000,1000),(1000,1),(500,500)]

nodeSize = []
labels={}
areas = []
for i in range (0,len(populations)):
    areas.append((populations[i]/popdensity[i])*100)
    labels[names[i]] = f"port {i+1}"     

for i in range (0,5):
    g.add_node(names[i],pos=pos[i],)


g.add_edges_from([("B","C"),("A","B"),("C","D"),("D","E"),("B","E"),("A","E")])
g.add_edges_from([("D","A"),("C","E")])
pos=nx.get_node_attributes(g,'pos')
print(pos)
nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True), node_color='blue')
red_circle1, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
red_circle2, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
red_circle3, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
red_circle4, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
red_circle5, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(n):
        red_circle1.set_data([1],[i])
        red_circle2.set_data([i],[1000])
        red_circle3.set_data([1000],[i])
        red_circle4.set_data([i],[i])
        writer.grab_frame()
    for i in range(n):
        while f > 1:
            f = f-1
            red_circle5.set_data([f],[1])
            red_circle1.set_marker(None)
            writer.grab_frame()


# Next make markers disappear after finished


#next try and change color over time after markers disappear



#next bar chart, and number of infected










