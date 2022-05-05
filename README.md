# Further-Computer-Programming

 
   
--- read me --- 
Our code uses a node network to show how air travel 
during a pandemic can affect transmission of covid 
as well as the affect of lockdowns on the spread. 
It highlights the need for stricter regulations early 
on in the pandemic to prevent smaller countries from becoming
overrun with cases.

--- requirements to run the code --- 

maplotlib.pyplot
maplotlib.animation 
networkx 
random 
numpy
from scipy.stats, norm

--- instructions --- 

input all variables as you wish and choose between an animation   
or graph, graph just produces a graph, if choosing aimation allow code to run 
and find writer_test.mp4 which should contain the animation.

These were the values we used to produce the graph shown in the report:
Number of weeks = 26

PIx = Proportion of people who are infected with covid in country x
PIA = 0.05
PIB = 0.01
PIC = 0.02
PID = 0.04
PIE = 0.07

PCL = proportion of people with covid that causes a lockdown
PCL = 0.15

RVx = R value for country x
RVA = 1.00
RVB = 0.95
RVC = 1.05
RVD = 1.10
RVE = 0.90

RVL = the R value during a lockdown
RVL = 0.6

plane_size = number of peope on the planes

--- instructions for running Airport_CovidSim_graphs --- 

Running this code will produce a graph with all 5 locations
covid journey. Each airport has a 10x bigger population than
the populations used in the covid travel animations
to make it more realistic.

To edit any variables please open Airports_CovidSim as this is 
the bulk of the code.

The variables are all currently set the same as to keep it fair
between each location. However, you could change the variables
startingImmunity to give a higher number of people who could never 
contract the virus and startingInfecters to increase the speed in which 
the virus is passed through the population.
