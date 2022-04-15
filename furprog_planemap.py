# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:09:32 2022

@author: jacke
"""
import networkx as nx 
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
f = 100
n = 101
g =nx.Graph()
pos=nx.get_node_attributes(g,'pos')
FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='red circles following edges')
writer = FFMpegWriter(fps=30, metadata=metadata)

fig = plt.figure()
populations = [10000,23450,30000,50000,100000]#changes size of nodes
popdensity = [5000,2000,8000,10000,6000]#changes size of nodes
names = ["A","B","C","D","E"]
pos=[(1,1),(1,100),(100,100),(100,1),(50,50)]

nodeSize = []
labels={}
areas = []
for i in range (0,len(populations)):
    areas.append((populations[i]/popdensity[i])*100)
    labels[names[i]] = f"airport {i+1}"     

for i in range (0,5):
    g.add_node(names[i],pos=pos[i],)


g.add_edges_from([("B","C"),("A","B"),("C","D"),("D","E"),("B","E"),("A","E")])
g.add_edges_from([("D","A"),("C","E")])
pos=nx.get_node_attributes(g,'pos')
print(pos)
nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True),node_color='green')  
red_circle1, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
red_circle2, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
red_circle3, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
red_circle4, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
red_circle5, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
red_circle6, = plt.plot([50], [70], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
plane = plt.text(50,70,'Planes')


with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(n):
        red_circle1.set_data([1],[i])
        red_circle2.set_data([i],[100])
        red_circle3.set_data([100],[i])
        red_circle4.set_data([i],[i])
        writer.grab_frame()
    for i in range(n):
        while f > 1:
            f = f-1
            red_circle5.set_data([f],[1])
            red_circle1.set_marker(None)
            red_circle2.set_marker(None)
            red_circle3.set_marker(None)
            red_circle4.set_marker(None)
            writer.grab_frame()
        red_circle5.set_marker(None)# makes plot disappear
        writer.grab_frame()
    red_circle6.set_marker(None)
    plane.remove()
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'whitesmoke', 'red', 'black' ,'blue' ,'green'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color='gainsboro')
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color='lightgray')
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color='lightgrey')
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color='silver')
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color='darkgray')
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color='darkgrey')
    for i in range(60):
        writer.grab_frame()
    colors = [i/len(g.nodes) for i in range(len(g.nodes))]
    nx.draw(g, pos,node_size=areas, node_color=colors)
    for i in range(60):
        writer.grab_frame()
# need to learn to remove graph
#colour changes are now smoother just need more suitable colours for the changes
#


#next bar chart, and number of infected










