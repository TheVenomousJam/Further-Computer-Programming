#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:39:41 2022

@author: guyanderson
"""
import numpy as np
import matplotlib.pyplot as plt


pop = [10000,10000,10000]
airports = ['A','B','C']
infected = [0.0,0.0,0.02]
rvalue = [1.2,1,1.1] #R value
infection_period = 1 #the number of days one person can infect another
#100 people per flight
paths = [('A','B'),('A','C'),('B','C')]
#100 days is about 14weeks
weeks = 14
week = [0] 
#just to create a list of week numbers to use for the graph
for i in range(weeks):
    week.append(i+1)

def infection_proportion():
    #PIx = Proportion of people who are infected with covid in x
    PIA = [0.10]
    PIB = [0.15]
    PIC = [0.05]
    #PCL = proportion of people with covid that causes a lockdown
    PCL = 0.3
    #RVx = R value for x
    RVA = 1.13
    RVB = 0.98
    RVC = 1.1
    #RVL = the R value during a lockdown
    RVL = 0.6
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
    plt.legend(['A', 'B','C'])
    plt.show()
    

infection_proportion()

        

        
        # if i == 0:
        #     inf_A = PIA[i] + (PIA[i] * RVA)
        #     inf_B = PIB[i] + (PIB[i] * RVB)
        #     inf_C = PIC[i] + (PIC[i] * RVC)
        # else:
            
        # inf_A = PIA[i] + (PIA[i] * RVA) - PIA[i]
        # inf_B = PIB[i] + (PIB[i] * RVB) - PIB[i]
        # inf_C = PIC[i] + (PIC[i] * RVC) - PIC[i]                




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