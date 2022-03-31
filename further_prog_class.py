# -*- coding: utf-8 -*-
import networkx as nx 
import matplotlib.pyplot as plt
import random


names = ["A","B","C","D","E"]
positions = [(1,1),(1,4),(4,4),(4,1),(3,3)]
#positions =[]
POP = [1000,10000,5000,20000,4000]
POPDEN = [100,4000,500,2000,40]
Connect = [("B","D"),("A","B"),("C","E"),("D","E"),("B","E"),("A","E")]
labels={}
areas =[]

g =nx.Graph()

if not positions:
    for i in range(0,len(names)):
        a = random.randint(0,len(names))
        b = random.randint(0,len(names)) 
        positions.append((a,b))

class Airport:
    #include edges
    def __init__(self,name,position,POP=None,POPDEN=None,Connect=None):
        self.name = name
        self.position = position
        self.POP = POP
        self.POPDEN = POPDEN
        self.Connect = Connect
    def size(S): 
        size = (S.POP/S.POPDEN)*40
        return size
    def names(NA):
        labels[NA.name] = NA.name
    def Nodes(NO):
        g.add_node(NO.name,pos=NO.position)
        
    def edges(ED):
        g.add_edge((ED.name,ED.connect))

    def Make_graph(self): 
        for n in self.name:
            (i.Nodes())
            areas.append(i.size())
            i.names()

def Add_edges(Connect):
    for C  in Connect:
        g.add_edge(C[0],C[1])

for i in range(0,(len(names))):
    (i) = Airport(names[i],positions[i],POP[i],POPDEN[i])
    i.Make_graph()

Add_edges(Connect)


pos=nx.get_node_attributes(g,'pos')
nx.draw(g,pos,node_size=areas,labels=labels,with_labels=(True))
#connectionstyle='arc3,rad=0.1'    changes to curves
plt.show()






        
    