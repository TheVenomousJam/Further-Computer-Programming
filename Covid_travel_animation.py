#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jacke
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import networkx  as nx
import random as r
#from furprog_planemap import *


infection_period = 1 #the number of days one person can infect another
plane_size = 100 #number of people on plane
airports = ['A','B','C','D','E']
#100 days is about 14weeks
weeks = 100
week = list(range(weeks+1))

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



FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='red circles following edges')
writer = FFMpegWriter(fps=30, metadata=metadata)
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
    
    for z in range(weeks):
        plot1 = plt.figure(1)
        plt.plot(week[z:z+2],PIA[z:z+2])
        writer.grab_frame()
        plt.plot(week[z:z+2],PIB[z:z+2])
        writer.grab_frame()
        plt.plot(week[z:z+2],PIC[z:z+2])
        writer.grab_frame()
        plt.plot(week[z:z+2],PID[z:z+2])
        writer.grab_frame()
        plt.plot(week[z:z+2],PIE[z:z+2])
        plt.legend(airports)
        writer.grab_frame()
#    for z in range(weeks):
 #       plot2 = plt.figure(2)
  #      plt.plot(week[z:z+2],PIB[z:z+2])
   #     writer.grab_frame()
    #for z in range(weeks):
     #   plot3 = plt.figure(3)
      #  plt.plot(week[z:z+2],PIC[z:z+2])
       # writer.grab_frame()
    #for z in range(weeks):
     #   plot4 = plt.figure(4)
      #  plt.plot(week[z:z+2],PIE[z:z+2])
       # writer.grab_frame()
#    for z in range(weeks):        
 #       plot5 = plt.figure(5)
  #      plt.plot(week[z:z+2],PIE[z:z+2])
   #     plt.legend(airports)
    #    plt.xlabel('Days')
     #   plt.ylabel('percentage of population infected')
      #  writer.grab_frame()
    plt.show()








with writer.saving(fig, "writer_test.mp4", 100):
    infection_proportion()