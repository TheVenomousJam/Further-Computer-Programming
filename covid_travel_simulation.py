#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:39:41 2022

@author: guyanderson
"""
import numpy as np
import matplotlib.pyplot as plt
import random as r


pop = {'A': 10000,'B': 10000,'C': 10000}
infected = [0.0,0.0,0.02]
rvalue = [1.2,1,1.1] #R value
infection_period = 1 #the number of days one person can infect another
plane_size = 100 #number of people on plane
airports = ['A','B','C']
paths = [('A','B'),('A','C'),('B','C')]
#100 days is about 14weeks
weeks = 14
week = list(range(weeks+1))
#just to create a list of week numbers to use for the graph
print(week)
#PIx = Proportion of people who are infected with covid in x
PIA = [0.10]
PIB = [0.15]
PIC = [0.05]
#PCL = proportion of people with covid that causes a lockdown
PCL = 0.3
#RVx = R value for x
RVA = 1.13
RVB = 0.98
RVC = 1.07
#RVL = the R value during a lockdown
RVL = 0.6

def infection_proportion():
    for i in range(weeks):
    #inf_x = proportion of infected people in x on day i
    #inf_x = PIx[i] + (PIx[i] * RVx) - PIx[i], so PIx[i] cancel to simplify
    #this works because I'm using weeks rather than days
    #so the infectious period is only 1 interation in the loop
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
    #flight path
        start_index = r.randint(0,2)
        end_index = r.randint(1,2)
        start_point = airports[start_index]
        end_point = airports[start_index - end_index]
        print('plane journey from', start_point, 'to', end_point)
        # doing it this way guarantees that the planes can't go from A to A etc.
        if start_point == 'A':
            if end_point == 'B':
                inf_B += PIA[i]*RVA/10
            elif end_point == 'C':
                inf_C += PIA[i]*RVA/10   
        elif start_point == 'B':
            if end_point == 'A':
                inf_A += PIB[i]*RVB/10
            elif end_point == 'C':
                inf_C += PIB[i]*RVB/10
        elif start_point == 'C':
            if end_point == 'B':
                inf_B += PIC[i]*RVC/10
            elif end_point == 'A':
                inf_A += PIC[i]*RVC/10
        #so the proportion of people cannot exceed 1
        if inf_A > 1:
            inf_A = 1
        if inf_B > 1:
            inf_B = 1
        if inf_C > 1:
            inf_C = 1
        PIA.append(inf_A)
        PIB.append(inf_B)
        PIC.append(inf_C)
    print('A', PIA)
    print('B', PIB)
    print('C', PIC)
    plt.plot(week,PIA)
    plt.plot(week,PIB)
    plt.plot(week,PIC)
    plt.legend(['A','B','C'])
    plt.show()
    

infection_proportion()

        
'''
def flight_path():
flight_path()
'''





'''
def infection_count():
    global infected
    for i in range(days):
        for count,inf in enumerate(infected):
            new_inf = inf + inf*rvalue[count]
            if count > 10:
                new_inf = new_inf[i] - new_inf[i-10]
            if new_inf > 1:
                new_inf = 1
            infected = infected[:count] + [new_inf] + infected[count+1:]
            print(infected)
            
infection_count()    
'''



'''        
        if i == 0:
            inf_A = PIA[i] + (PIA[i] * RVA)
            inf_B = PIB[i] + (PIB[i] * RVB)
            inf_C = PIC[i] + (PIC[i] * RVC)
        else:
            
        inf_A = PIA[i] + (PIA[i] * RVA) - PIA[i]
        inf_B = PIB[i] + (PIB[i] * RVB) - PIB[i]
        inf_C = PIC[i] + (PIC[i] * RVC) - PIC[i]                



inf_B = (PIB[i] * RVB) + (PIA[i]*(RVA*(plane_size/pop[0][1])))
'''



