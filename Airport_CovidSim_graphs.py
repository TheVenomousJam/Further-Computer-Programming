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
plt.show()

