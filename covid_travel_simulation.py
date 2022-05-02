#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:39:41 2022

@author: guyanderson
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import networkx  as nx
import random as r
#from furprog_planemap import *

'''
=========================
Changeable info for graph
=========================
'''
infection_period = 1 #the number of days one person can infect another
plane_size = 100 #number of people on plane
airports = ['A','B','C','D','E']
#100 days is about 14weeks
weeks = 100
week = list(range(weeks+1))
print(week)
#just to create a list of week numbers to use for the graph
#print(week)
#PIx = Proportion of people who are infected with covid in x
PIA = [0.00]
PIB = [0.01]
PIC = [0.02]
PID = [0.04]
PIE = [0.07]
#PCL = proportion of people with covid that causes a lockdown
PCL = 0.15
#RVx = R value for x
RVA = 1.00
RVB = 0.95
RVC = 1.05
RVD = 1.10
RVE = 0.90
#RVL = the R value during a lockdown
RVL = 0.6
#start_list & end_list act as a flight log to use for the animation
start_list = []
end_list = []

'''
=========================
'''
'''
=========================
Changeable info for animation
=========================
'''
# at the moment this is commented out so that the network diagram 
# doesnt overlap with the graph, need to find a way to make this not happen.
'''
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
nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True),node_color=[node_colours[a],node_colours[b],node_colours[c],node_colours[d],node_colours[e]])  
red_circle1, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
'''
'''
=========================
'''
FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='red circles following edges')
writer = FFMpegWriter(fps=60, metadata=metadata)
fig = plt.figure()
def infection_proportion():
    for i in range(weeks):
    # inf_x = proportion of infected people in x on day i
    # inf_x = PIx[i] + (PIx[i] * RVx) - PIx[i], so PIx[i] cancel to simplify
    # this works because I'm using weeks rather than days
    # so the infectious period is only 1 interation in the loop
    # this assumes no-one has long covid
#lockdown        
        if PIA[i] > PCL:
            #lockdown enforced
            inf_A = (PIA[i] * RVL)
        else:
            inf_A = (PIA[i] * RVA) 
        if PIB[i] > PCL:
            #lockdown enforced
            inf_B = (PIB[i] * RVL)
        else:
            inf_B = (PIB[i] * RVB) 
        if PIC[i] > PCL:
            #lockdown enforced
            inf_C = (PIC[i] * RVL)
        else:        
            inf_C = (PIC[i] * RVC)
        if PID[i] > PCL:
            #lockdown enforced
            inf_D = (PID[i] * RVL)
        else:        
            inf_D = (PID[i] * RVD)
        if PIE[i] > PCL:
            #lockdown enforced
            inf_E = (PIE[i] * RVL)
        else:        
            inf_E = (PIE[i] * RVE)
#flight paths
        weekly_flights = r.randint(0,5)
        print(weekly_flights, 'flights on week',i)
        for x in range(weekly_flights):
            start_index = r.randint(0,4)
            end_index = r.randint(1,4)
            start_point = airports[start_index]
            end_point = airports[start_index - end_index]
            # doing it this way guarantees that the planes can't go from A to A etc.
            start_list.append(start_point)
            end_list.append(end_point)
            # creating these lists is so we have the data for the animation
            # this long if statement is adding the covid from the flights to the current infection rates.
            if start_point == 'A':
                if end_point == 'B':
                    inf_B += PIA[i]*RVA/10
                elif end_point == 'C':
                    inf_C += PIA[i]*RVA/10
                elif end_point == 'D':
                    inf_D += PIA[i]*RVA/10 
                elif end_point == 'E':
                    inf_E += PIA[i]*RVA/10
            elif start_point == 'B':
                if end_point == 'A':
                    inf_A += PIB[i]*RVB/10 
                elif end_point == 'C':
                    inf_C += PIB[i]*RVB/10
                elif end_point == 'D':
                    inf_D += PIB[i]*RVB/10 
                elif end_point == 'E':
                    inf_E += PIB[i]*RVB/10
            elif start_point == 'C':
                if end_point == 'A':
                    inf_A += PIC[i]*RVC/10
                elif end_point == 'B':
                    inf_B += PIC[i]*RVC/10
                elif end_point == 'D':
                    inf_D += PIC[i]*RVC/10
                elif end_point == 'E':
                    inf_E += PIC[i]*RVC/10
            elif start_point == 'D':
                if end_point == 'A':
                    inf_A += PID[i]*RVD/10
                elif end_point == 'B':
                    inf_B += PID[i]*RVD/10
                elif end_point == 'C':
                    inf_C += PID[i]*RVD/10
                elif end_point == 'E':
                    inf_E += PID[i]*RVD/10
            elif start_point == 'E':
                if end_point == 'A':
                    inf_A += PIE[i]*RVE/10
                elif end_point == 'B':
                    inf_B += PIE[i]*RVE/10
                elif end_point == 'C':
                    inf_C += PIE[i]*RVE/10
                elif end_point == 'D':
                    inf_D += PIE[i]*RVE/10
            print('plane journey from', start_point, 'to', end_point)
            #/10 as number of people on plane is far less than total pop.
            #probably should be more than /10, plane size/pop = 1/100
            #but making it 1/100 makes the infection increase pretty small
        PIA.append(inf_A)
        PIB.append(inf_B)
        PIC.append(inf_C)
        PID.append(inf_D)
        PIE.append(inf_E)

        
    plt.plot(week,PIA)
    plt.plot(week,PIB)
    plt.plot(week,PIC)
    plt.plot(week,PID)
    plt.plot(week,PIE)
    plt.legend(airports)
    plt.show()
           # PIA.append(inf_A)
            #PIB.append(inf_B)
          #  PIC.append(inf_C)
           # PID.append(inf_D)
           # PIE.append(inf_E)
       # print(i,PIA[i])
        #for s in range(1):
         #   writer.grab_frame()


    #print('A', PIA,'\nB', PIB,'\nC', PIC,'\nD', PID,'\nE', PIE)     
# these functions create the path for the plane to follow
def flight_from_A():
    if end_list[f] == 'B':
        for b in range(n):
            red_circle1.set_data([0],[b])
            writer.grab_frame()
    elif end_list[f] == 'C':
        for b in range(n):
            red_circle1.set_data([b],[b])
            writer.grab_frame()
    elif end_list[f] == 'D':
        for b in range(n):
            red_circle1.set_data([b],[0])
            writer.grab_frame()
    elif end_list[f] == 'E':
        for b in range(n):
            red_circle1.set_data([b/2],[b/2])
            writer.grab_frame()
            
def flight_from_B():
    if end_list[f] == 'A':
        for b in range(n):
            red_circle1.set_data([0],[100-b])
            writer.grab_frame()
    elif end_list[f] == 'C':
        for b in range(n):
            red_circle1.set_data([b],[100])
            writer.grab_frame()
    elif end_list[f] == 'D':
        for b in range(n):
            red_circle1.set_data([b],[100-b])
            writer.grab_frame()
    elif end_list[f] == 'E':
        for b in range(n):
            red_circle1.set_data([b/2],[100-(b/2)])
            writer.grab_frame()
            
def flight_from_C():
    if end_list[f] == 'A':
        for b in range(n):
            red_circle1.set_data([100-b],[100-b])
            writer.grab_frame()
    elif end_list[f] == 'B':
        for b in range(n):
            red_circle1.set_data([100-b],[100])
            writer.grab_frame()
    elif end_list[f] == 'D':
        for b in range(n):
            red_circle1.set_data([100],[100-i])
            writer.grab_frame()
    elif end_list[f] == 'E':
        for b in range(n):
            red_circle1.set_data([100-(b/2)],[100-(b/2)])
            writer.grab_frame()
            
def flight_from_D():
    if end_list[f] == 'A':
        for b in range(n):
            red_circle1.set_data([100-b],[0])
            writer.grab_frame()
    elif end_list[f] == 'B':
        for b in range(n):
            red_circle1.set_data([100-b],[b])
            writer.grab_frame()
    elif end_list[f] == 'C':
        for b in range(n):
            red_circle1.set_data([100],[b])
            writer.grab_frame()
    elif end_list[f] == 'E':
        for b in range(n):
            red_circle1.set_data([100-(b/2)],[b/2])
            writer.grab_frame()
            
def flight_from_E():
    if end_list[f] == 'A':
        for b in range(n):
            red_circle1.set_data([50-(b/2)],[50-(b/2)])
            writer.grab_frame()
    elif end_list[f] == 'B':
        for b in range(n):
            red_circle1.set_data([50-(b/2)],[50+(b/2)])
            writer.grab_frame()
    elif end_list[f] == 'C':
        for b in range(n):
            red_circle1.set_data([50+(b/2)],[50+(b/2)])
            writer.grab_frame()
    elif end_list[f] == 'D':
        for b in range(n):
            red_circle1.set_data([50+(b/2)],[50-(b/2)])
            writer.grab_frame()
            
def node_animation():
    colours_A = []
    colours_B = []
    colours_C = []
    colours_D = []
    colours_E = []
    for a in range(weeks):
        colours_A.append(PIA[a]*255)
        colours_B.append(PIB[a]*255)
        colours_C.append(PIC[a]*255)
        colours_D.append(PID[a]*255)
        colours_E.append(PIE[a]*255)
        nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True),node_color=[node_colours[colours_A[week]],node_colours[colours_B[week]],node_colours[colours_C[week]],node_colours[colours_D[week]],node_colours[colours_E[week]]])  
        writer.grab_frame()
    for f in len(start_list):
        if start_list[f] == 'A':              
            flight_from_A()
        if start_list[f] == 'B':
            flight_from_B()
        if start_list[f] == 'C':
            flight_from_C()
        if start_list[f] == 'D':
            flight_from_D()
        if start_list[f] == 'E':
            flight_from_E()

    
graph_or_animation = input('Do you want to see a graph or an animation?\nType g or a\n')
if graph_or_animation == 'g':
        infection_proportion()
elif graph_or_animation == 'a':
    with writer.saving(fig, "writer_test.mp4", 100):    
        node_animation()



