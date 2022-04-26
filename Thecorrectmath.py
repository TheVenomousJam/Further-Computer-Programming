# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:34:43 2022

@author: jacke
"""

#planes move, numbers, 
POP = [10000,10000,10000]
airport  = ["A","B","C"] 
infected = [0,0,0.02]
rval = [1.2,1,1.1]
#"plane" flies between changing infection rate
paths = [("A","B"),("C","A"),("B","C")] 
#100 people per flight 

Ainf = [0]
Binf = [0] 
Cinf = [0.2] 

Ar = 1.2
Br = 1
Cr = 1.1


#100 days
days  = 100
print(infected)
length = len(airport)

for i in range (days): 
    if i > 9 : 
        print(i)
        j = i -10 
        anewinf = Ainf[i]*Ar - Ainf[j]
    
        if anewinf >1: 
            anewinf = 1
            Ainf.append(anewinf)
        else:
            Ainf.append(anewinf)
        bnewinf = Binf[i]*Br - Binf[j]
        if bnewinf >1 :
            bnewinf = 1 
        
            Binf.append(bnewinf)
        else: 
            Binf.append(bnewinf)

        cnewinf = Cinf[i]*Cr - Cinf[j]
        if cnewinf > 1 : 
            cnewinf = 1
            Cinf.append(cnewinf)
        else: 
            Cinf.append(cnewinf)
     
        
    else:
        print(i)
        anewinf = Ainf[i]*Ar 
        if anewinf >1: 
            anewinf = 1
            Ainf.append(anewinf)
        else:
                Ainf.append(anewinf)
        bnewinf = Binf[i]*Br
        if bnewinf >1 :
                bnewinf = 1 
        
                Binf.append(bnewinf)
        else: 
            Binf.append(bnewinf)

        cnewinf = Cinf[i]*Cr
        if cnewinf > 1 : 
            cnewinf = 1
            Cinf.append(cnewinf)
        else: 
            Cinf.append(cnewinf)





for inf in Cinf:
    print(inf)
# =============================================================================
# for i in range (days): 
#     for count,inf in enumerate(infected): 
#         newinf = inf*rval[count]
#         if newinf > 1: 
#             newinf = 1
#         infected = infected[:count]+[newinf]+infected[count+1:] 
#         
# 
# =============================================================================
        
            



#introduce variable 
