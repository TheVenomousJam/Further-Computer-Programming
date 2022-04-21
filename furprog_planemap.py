# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:09:32 2022

@author: jacke
"""
import networkx as nx 
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import random as r
f = 100
n = 101
g =nx.Graph()
pos=nx.get_node_attributes(g,'pos')
FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='red circles following edges')
writer = FFMpegWriter(fps=60, metadata=metadata)

fig = plt.figure()
populations = [10000,23450,30000,50000,100000]#changes size of nodes
popdensity = [5000,2000,8000,10000,6000]#changes size of nodes
names = ["A","B","C","D","E"]
pos=[(1,1),(1,100),(100,100),(100,1),(50,50)]

node_colours = ['#5cb200','#c6f808','#fdff38','#fc824a','#ec2d01']
#node colours are: kermit green, greeny yellow, lemon yellow, orange ish, tomato red
#these variables will be the index values for node_colours for each node a = node 1 etc.
a = 0
b = 0
c = 0
d = 0
e = 0

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
#the one commented out is the one to make James' code work
#nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True),node_color={'#fcfcfc', '#ff0000', '#ffffff' ,'#fefefe' ,'#fdfdfd'})
nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True),node_color=[node_colours[a],node_colours[b],node_colours[c],node_colours[d],node_colours[e]])  
red_circle1, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
red_circle2, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
red_circle3, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
red_circle4, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
red_circle5, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
red_circle6, = plt.plot([50], [70], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
plane = plt.text(50,70,'Planes')

'''
with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(n):
        red_circle1.set_data([1],[i])
        red_circle2.set_data([i],[100])
        red_circle3.set_data([100],[i])
        red_circle4.set_data([i],[i])
        red_circle5.set_data([i/2],[i/2])
        writer.grab_frame()
    for i in range(15):
        writer.grab_frame()
    for i in range(n):
        while f > 1:
            f = f-1
            red_circle5.set_data([f],[1])
            red_circle3.set_data([f],[100])
            red_circle4.set_data([f],[f])
            writer.grab_frame()
        red_circle1.set_marker(None)
        red_circle2.set_marker(None)
        red_circle3.set_marker(None)
        red_circle4.set_marker(None)
        red_circle5.set_marker(None)# makes plot disappear
        writer.grab_frame()
    red_circle6.set_marker(None)
    plane.remove()
    writer.grab_frame()

    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffffff' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffeded' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffecec' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffebeb' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffeaea' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffe9e9' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffe8e8' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffe7e7' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffe6e6' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffe5e5' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffe4e4' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffe3e3' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffe2e2' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffe1e1' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffe0e0' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffdddd' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffdcdc' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffd9d9' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffd6d6' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffd2d2' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffd0d0' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffcccc' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffc7c7' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffc3c3' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffb8b8' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ffa6a6' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ff9191' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ff8585' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ff7979' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ff6767' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ff5c5c' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ff5151' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ff4545' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ff3131' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ff2727' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color={'#fcfcfc', '#ff0000', '#ff1b1b' ,'#fefefe' ,'#fdfdfd'})
    for i in range(60):
        writer.grab_frame()
# need to learn to remove graph
#colour changes are now smoother just need more suitable colours for the changes
#


#next bar chart, and number of infected

'''


def flight1():
#    with writer.saving(fig, "writer_test.mp4", 100):
        global a,b,c,d,e
        a += 1
        for i in range (1):
            nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True),node_color=[node_colours[a],node_colours[b],node_colours[c],node_colours[d],node_colours[e]])  
            writer.grab_frame()
        for i in range(30):
            writer.grab_frame()
        destination = r.randint(1,5)
        if destination == 1: 
            flight1()
        elif destination == 2:
            for i in range(n):
                red_circle1.set_data([0],[i])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight2()
        elif destination == 3:
            for i in range(n):
                red_circle1.set_data([i],[i])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight3()
        elif destination == 4:
            for i in range(n):
                red_circle1.set_data([i],[0])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight4()
        elif destination == 5:
            for i in range(n):
                red_circle1.set_data([i/2],[i/2])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight5()


def flight2():
#    with writer.saving(fig, "writer_test.mp4", 100):
        global a,b,c,d,e
        b+=1
        for i in range (1):
            nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True),node_color=[node_colours[a],node_colours[b],node_colours[c],node_colours[d],node_colours[e]])  
            writer.grab_frame()
        for i in range(30):
            writer.grab_frame()
        destination = r.randint(1,5)
        if destination == 1: 
            for i in range(n):
                red_circle1.set_data([0],[100-i])
                writer.grab_frame()    
        elif destination == 2:
            flight2()
        elif destination == 3:
            for i in range(n):
                red_circle1.set_data([i],[100])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight3()
        elif destination == 4:
            for i in range(n):
                red_circle1.set_data([i],[100-i])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight4()
        elif destination == 5:
            for i in range(n):
                red_circle1.set_data([i/2],[100-(i/2)])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight5()
        for i in range(120):
            writer.grab_frame()
            
def flight3():
#    with writer.saving(fig, "writer_test.mp4", 100):
        global a,b,c,d,e
        c+=1
        for i in range (1):
            nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True),node_color=[node_colours[a],node_colours[b],node_colours[c],node_colours[d],node_colours[e]])  
            writer.grab_frame()
        for i in range(30):
            writer.grab_frame()
        destination = r.randint(1,5)
        if destination == 1: 
            for i in range(n):
                red_circle1.set_data([100-i],[100-i])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight1()
        elif destination == 2:
            for i in range(n):
                red_circle1.set_data([100-i],[100])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight2()
        elif destination == 3:
            flight3()
        elif destination == 4:
            for i in range(n):
                red_circle1.set_data([100],[100-i])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight4()
        elif destination == 5:
            for i in range(n):
                red_circle1.set_data([100-(i/2)],[100-(i/2)])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight5()
        for i in range(120):
            writer.grab_frame()
            
def flight4():
#    with writer.saving(fig, "writer_test.mp4", 100):
        global a,b,c,d,e
        d+=1
        for i in range(1):
            nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True),node_color=[node_colours[a],node_colours[b],node_colours[c],node_colours[d],node_colours[e]])  
            writer.grab_frame()
        for i in range(30):
            writer.grab_frame()
        destination = r.randint(1,5)
        if destination == 1: 
            for i in range(n):
                red_circle1.set_data([100-i],[0])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight1()
        elif destination == 2:
            for i in range(n):
                red_circle1.set_data([100-i],[i])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight2()
        elif destination == 3:
            for i in range(n):
                red_circle1.set_data([100],[i])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight3()
        elif destination == 4:
            for i in range(n):
                flight4()
        elif destination == 5:
            for i in range(n):
                red_circle1.set_data([100-(i/2)],[i/2])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight5()
        for i in range(120):
            writer.grab_frame()
            
def flight5():
#    with writer.saving(fig, "writer_test.mp4", 100):
        global a,b,c,d,e
        e+=1
        for i in range (1):
            nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True),node_color=[node_colours[a],node_colours[b],node_colours[c],node_colours[d],node_colours[e]])  
            writer.grab_frame()
        for i in range(30):
            writer.grab_frame()
        destination = r.randint(1,5)
        if destination == 1: 
            for i in range(n):
                red_circle1.set_data([50-(i/2)],[50-(i/2)])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight1()
        elif destination == 2:
            for i in range(n):
                red_circle1.set_data([50-(i/2)],[50+i/2])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight2()
        elif destination == 3:
            for i in range(n):
                red_circle1.set_data([50+i/2],[50+i/2])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight3()
        elif destination == 4:
            for i in range(n):
                red_circle1.set_data([50+i/2],[50-(i/2)])
                writer.grab_frame()
            for i in range(30):
                writer.grab_frame()
            flight4()
        elif destination == 5:
            flight5()
        for i in range(120):
            writer.grab_frame()

with writer.saving(fig, "writer_test.mp4", 100):
    flight1()

#need to press the red square on the console when you want it to end, otherwise it'll carry on forever. :)

#next thing to work out is how to avoid the colours changing more than once due to the plane staying on the node. (when random number = node number)



