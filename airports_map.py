#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 18:48:45 2022

3author: guyanderson
"""
import networkx as nx 
import matplotlib.pyplot as plt
import pandas as pd


fig = plt.figure(1, figsize=(36, 18), dpi=90)
g =nx.Graph()
pos=nx.get_node_attributes(g,'coords')


columns = ['name','lat_deg','lon_deg']
info = pd.read_csv('airports.csv', usecols=columns)
#print(info) this will print the whole spreadsheet
x = 0
for i in range(0,len(info)):
    g.add_node(info['name'].values[x],coords=(info['lon_deg'].values[x],info['lat_deg'].values[x]))
    x+=1
#have to use x as using i as the index doesnt work, idk why
print(x)

nx.draw(g)

