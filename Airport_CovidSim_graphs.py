import numpy as np
import matplotlib.pyplot as plt
from Airports_CovidSim import *

AIRPORT1()
AIRPORT2()
AIRPORT3()
AIRPORT4()
AIRPORT5()

contagious1 = np.genfromtxt('coviddata_AP1.txt')
contagious2 = np.genfromtxt('coviddata_AP2.txt')
contagious3 = np.genfromtxt('coviddata_AP3.txt')
contagious4 = np.genfromtxt('coviddata_AP4.txt')
contagious5 = np.genfromtxt('coviddata_AP5.txt')

plt.plot(contagious1, color='red', label = 'Airport1')
plt.plot(contagious2, color='orange', label = 'Airport2')
plt.plot(contagious3, color='yellow', label = 'Airport3')
plt.plot(contagious4, color='green', label = 'Airport4')
plt.plot(contagious5, color='blue', label = 'Airport5')
plt.legend()
plt.show()

coviddata_AP1 = open('coviddata_AP1.txt','r+')
coviddata_AP1.truncate(0)
coviddata_AP1.close()

coviddata_AP2 = open('coviddata_AP2.txt','r+')
coviddata_AP2.truncate(0)
coviddata_AP2.close()

coviddata_AP3 = open('coviddata_AP3.txt','r+')
coviddata_AP3.truncate(0)
coviddata_AP3.close()

coviddata_AP4 = open('coviddata_AP4.txt','r+')
coviddata_AP4.truncate(0)
coviddata_AP4.close()

coviddata_AP5 = open('coviddata_AP5.txt','r+')
coviddata_AP5.truncate(0)
coviddata_AP5.close()

