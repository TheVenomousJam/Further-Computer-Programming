from scipy.stats import norm
import random
import time
import matplotlib.pyplot as plt
peopleDictionary = []
class Person():
    def __init__(self, startingImmunity):
        if random.randint(0,100)<startingImmunity:
            self.immunity = True
        else:
            self.immunity = False
        self.contagiousness = 0
        self.contagiousDays = 0
        self.friends = int((norm.rvs(size=1,loc=0.5,scale=0.15)[0]*10).round(0)) #use a gaussian distribution for avg friends
        
def initiateSim():
    numPeople = 100000
    startingImmunity = 1
    startingInfecters = 1
    for x in range(0,numPeople):
        peopleDictionary.append(Person(startingImmunity))
    for x in range(0,startingInfecters):
        peopleDictionary[random.randint(0,len(peopleDictionary)-1)].contagiousness = int((norm.rvs(size=1,loc=0.5,scale=0.15)[0]*10).round(0)*10)
    daysContagious = 7
    lockdownDay1 = 9
    lockdownDay2 = 17
    lockdownDay3 = 26
    lockdownDay4 = 35
    lockdownDay5 = 44
    lockdownEnd1 = 14
    lockdownEnd2 = 23
    lockdownEnd3 = 30
    lockdownEnd4 = 41
    lockdownEnd5 = 50
    return daysContagious, lockdownDay1, lockdownDay2, lockdownDay3, lockdownDay4, lockdownDay5, lockdownEnd1, lockdownEnd2, lockdownEnd3, lockdownEnd4, lockdownEnd5
def runDay(daysContagious, lockdown):
    #simulates the spread of covid
    for person in [person for person in peopleDictionary if person.contagiousness>0 and person.friends>0]:
        peopleCouldMeetToday = int(person.friends)
        if peopleCouldMeetToday > 0:
            peopleMetToday = random.randint(0,peopleCouldMeetToday)
        else:
            peopleMetToday = 0    
        if lockdown == True:
            peopleMetToday = 0    
        for x in range(0,peopleMetToday):
            friendInQuestion = peopleDictionary[random.randint(0,len(peopleDictionary)-1)]
            if random.randint(0,100)<person.contagiousness and friendInQuestion.contagiousness == 0 and friendInQuestion.immunity==False:
                friendInQuestion.contagiousness = int((norm.rvs(size=1,loc=0.5,scale=0.15)[0]*10).round(0)*10)          
    for person in [person for person in peopleDictionary if person.contagiousness>0]:
        person.contagiousDays += 1
        if person.contagiousDays > daysContagious:
            person.immunity = True
            person.contagiousness = 0
            
lockdown = False
daysContagious, lockdownDay1, lockdownDay2, lockdownDay3, lockdownDay4, lockdownDay5, lockdownEnd1, lockdownEnd2, lockdownEnd3, lockdownEnd4, lockdownEnd5 = initiateSim()

for x in range(0,100):
    if x==lockdownDay1:
        lockdown = True
    elif x==lockdownEnd1:
        lockdown = False
    elif x==lockdownDay2:
        lockdown = True
    elif x==lockdownEnd2:
        lockdown = False
    elif x==lockdownDay3:
        lockdown = True
    elif x==lockdownEnd3:
        lockdown = False
    elif x==lockdownDay4:
         lockdown = True
    elif x==lockdownEnd4:
         lockdown = False
    elif x==lockdownDay5:
         lockdown = True
    elif x==lockdownEnd5:
         lockdown = False
   
        
    print("DAY ", x)
    runDay(daysContagious,lockdown)
    coviddata = open("coviddata.txt", "a")
    write = str(len([person for person in peopleDictionary if person.contagiousness>0])) + "\n"
    coviddata.write(write)
    print(len([person for person in peopleDictionary if person.contagiousness>0]), " people are contagious on this day.")
    
coviddata.close()

contagious = []
f = open('coviddata.txt', 'r')
contagious = []
for line in f:
    line = line.split()
    if line:
        line = [int(i) for i in line]
        contagious.append(line)




