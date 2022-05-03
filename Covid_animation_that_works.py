#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: guy james nic jack
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

infection_period = int(input("length of infection period\n")) #the number of days one person can infect another
plane_size = int(input("enter plane size\n")) #number of people on plane
airports = ['A','B','C','D','E']
#100 days is about 14weeks
weeks = int(input("enter number of weeks simulation will run\n"))
week = list(range(weeks+1))
print(week)
#just to create a list of week numbers to use for the graph
#print(week)
#PIx = Proportion of people who are infected with covid in x



PIA = float(input("enter airport A proportion of infected\n"))
PIB = float(input("enter airport B proportion of infected\n"))
PIC = float(input("enter airport C proportion of infected\n"))
PID = float(input("enter airport D proportion of infected\n"))
PIE = float(input("enter airport E proportion of infected\n"))
PIA = [PIA]
PIB = [PIB]
PIC = [PIC]
PID = [PID]
PIE = [PIE]

# =============================================================================
# PIA = [0.00]
# PIB = [0.01]
# PIC = [0.02]
# PID = [0.04]
# PIE = [0.07]
# =============================================================================
#PCL = proportion of people with covid that causes a lockdown
#0.15
PCL = float(input("proportion of infected to trigger lockdown\n"))
#RVx = R value for x
#[1.00,0.95,1.05,1.10,0.90]
RVA = float(input("R value for A"))
RVB = float(input("R value for B"))
RVC = float(input("R value for C"))
RVD = float(input("R value for D"))
RVE = float(input("R value for E"))
#RVL = the R value during a lockdown
RVL = float(input("R value during lockdown"))
#start_list & end_list act as a flight log to use for the animation
start_list = []
end_list = []

node_colours = ['#5cb200','#c6f808','#fdff38','#fc824a','#ec2d01']
#'''
#=========================
'''
'''
#=========================
#Changeable info for animation
#=========================
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

#'''
#'''
#=========================
#'''


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

        



    #print('A', PIA,'\nB', PIB,'\nC', PIC,'\nD', PID,'\nE', PIE)     
# these functions create the path for the plane to follow
def flight1():
    global a,b,c,d,e
    if PIA[weeks] == 0:
        a = a
    elif 0 <PIA[weeks]< 0.025:
        a += 1
    elif 0.025 < PIA[weeks]< 0.075:
        a += 2 
    elif 0.075 < PIA[weeks]< 0.125:
        a += 3
    elif 0.125 < PIA[weeks]< 0.175:
        a += 4
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color=[node_colours[a],node_colours[b],node_colours[c],node_colours[d],node_colours[e]])  

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
    global a,b,c,d,e
  
    if PIB[weeks] == 0:
        b=b
    elif 0 <PIB[weeks]< 0.025:
        b+=1
    elif 0.025 < PIB[weeks]< 0.075:
        b+=2
    elif 0.075 < PIB[weeks]< 0.125:
        b+=3
    elif 0.125 < PIB[weeks]< 0.175:
        b+=4
    nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color=[node_colours[a],node_colours[b],node_colours[c],node_colours[d],node_colours[e]])  
    for i in range(10):
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
        global a,b,c,d,e
      
        if PIC[weeks] == 0:
            c+=1
        elif 0 <PIC[weeks]< 0.025:
            c+=1
        elif 0.025 < PIC[weeks]< 0.075:
            c+=1
        elif 0.075 < PIC[weeks]< 0.125:
            c+=1
        elif 0.125 < PIC[weeks]< 0.175:
            c+=1
        nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color=[node_colours[a],node_colours[b],node_colours[c],node_colours[d],node_colours[e]])  

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
        global a,b,c,d,e    
  
        if PID[weeks] == 0:
            d+=1
        elif 0 <PID[weeks]< 0.025:
            d+=1
        elif 0.025 < PID[weeks]< 0.075:
            d+=1
        elif 0.075 < PID[weeks]< 0.125:
            d+=1
        elif 0.125 < PID[weeks]< 0.175:
            d+=1
        nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color=[node_colours[a],node_colours[b],node_colours[c],node_colours[d],node_colours[e]])  

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
      
        if PIE[weeks] == 0:
            e+=1
        elif 0 <PIE[weeks]< 0.025:
            e+=1
        elif 0.025 < PIE[weeks]< 0.075:
            e+=1
        elif 0.075 < PIE[weeks]< 0.125:
            e+=1
        elif 0.125 < PIE[weeks]< 0.175:
            e+=1
        nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color=[node_colours[a],node_colours[b],node_colours[c],node_colours[d],node_colours[e]])  
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
           
def node_animation():
    colours_A = []
    colours_B = []
    colours_C = []
    colours_D = []
    colours_E = []

    for a in range(weeks):  
        if PIA[a] == 0:
            ch = 'green'
        elif 0 <PIA[a]< 0.025:
            ch = '#5cb200'
        elif 0.025 < PIA[a]< 0.075:
            ch = '#c6f808'
        elif 0.075 < PIA[a]< 0.125:
            ch = '#fdff38'
        elif 0.125 < PIA[a]< 0.175:
            ch = '#fc824a'
        nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(False),node_color=[ch])  
        for i in range(60):
            writer.grab_frame()


    
graph_or_animation = input('Do you want to see a graph or an animation?\nType g or a\n')
if graph_or_animation == 'g':
        infection_proportion()
        plt.plot(week,PIA)
        plt.plot(week,PIB)
        plt.plot(week,PIC)
        plt.plot(week,PID)
        plt.plot(week,PIE)
        plt.legend(airports)
        plt.show()
elif graph_or_animation == 'a':
    with writer.saving(fig, "writer_test.mp4", 100):    
        for i in range (0,len(populations)):
            areas.append((populations[i]/popdensity[i])*100)
            labels[names[i]] = f"airport {i+1}"     

        for i in range (0,5):
            g.add_node(names[i],pos=pos[i],)


        g.add_edges_from([("B","C"),("A","B"),("C","D"),("D","E"),("B","E"),("A","E")])
        g.add_edges_from([("D","A"),("C","E")])
        pos=nx.get_node_attributes(g,'pos')
        nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True),node_color=[node_colours[a],node_colours[b],node_colours[c],node_colours[d],node_colours[e]])  
        red_circle1, = plt.plot([], [], 'ro', markersize = 15, linewidth = 50, label = ("plane"))
        infection_proportion()
        flight1()
