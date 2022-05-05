from scipy.stats import norm
import random
import time
import matplotlib.pyplot as plt
import numpy as np

def AIRPORT1():
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
        
    def CovidSimulation():
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
        lockdownDay5 = 42
        lockdownDay6 = 51
        lockdownDay7 = 64
        lockdownEnd1 = 14
        lockdownEnd2 = 23
        lockdownEnd3 = 30
        lockdownEnd4 = 39
        lockdownEnd5 = 46
        lockdownEnd6 = 56
        lockdownEnd7 = 70
        return daysContagious, lockdownDay1, lockdownDay2, lockdownDay3, lockdownDay4, lockdownDay5, lockdownDay6, lockdownDay7, lockdownEnd1, lockdownEnd2, lockdownEnd3, lockdownEnd4, lockdownEnd5, lockdownEnd6, lockdownEnd7
    def CovidSpread(daysContagious, lockdown):
        for person in [person for person in peopleDictionary if person.contagiousness>0 and person.friends>0]:
            peopleCouldMeetToday = int(person.friends/2)
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
    daysContagious, lockdownDay1, lockdownDay2, lockdownDay3, lockdownDay4, lockdownDay5, lockdownDay6, lockdownDay7, lockdownEnd1, lockdownEnd2, lockdownEnd3, lockdownEnd4, lockdownEnd5, lockdownEnd6, lockdownEnd7 = CovidSimulation()

    for x in range(0,101):
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
        elif x==lockdownDay6:
            lockdown = True
        elif x==lockdownEnd6:
            lockdown = False
   
        
        print("DAY ", x)
        CovidSpread(daysContagious,lockdown)
        coviddata_AP1 = open("coviddata_AP1.txt", "a")
        write = str(len([person for person in peopleDictionary if person.contagiousness>0])) + "\n"
        coviddata_AP1.write(write)
        print(len([person for person in peopleDictionary if person.contagiousness>0]), " people are contagious on this day.")
    
    coviddata_AP1.close()


def AIRPORT2():
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
        
    def CovidSimulation():
        numPeople = 234500
        startingImmunity = 10
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
        lockdownDay5 = 42
        lockdownDay6 = 51
        lockdownDay7 = 64
        lockdownEnd1 = 14
        lockdownEnd2 = 23
        lockdownEnd3 = 30
        lockdownEnd4 = 39
        lockdownEnd5 = 46
        lockdownEnd6 = 56
        lockdownEnd7 = 70
        return daysContagious, lockdownDay1, lockdownDay2, lockdownDay3, lockdownDay4, lockdownDay5, lockdownDay6, lockdownDay7, lockdownEnd1, lockdownEnd2, lockdownEnd3, lockdownEnd4, lockdownEnd5, lockdownEnd6, lockdownEnd7
    def CovidSpread(daysContagious, lockdown):
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
    daysContagious, lockdownDay1, lockdownDay2, lockdownDay3, lockdownDay4, lockdownDay5, lockdownDay6, lockdownDay7, lockdownEnd1, lockdownEnd2, lockdownEnd3, lockdownEnd4, lockdownEnd5, lockdownEnd6, lockdownEnd7 = CovidSimulation()

    for x in range(0,101):
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
        CovidSpread(daysContagious,lockdown)
        coviddata_AP2 = open("coviddata_AP2.txt", "a")
        write = str(len([person for person in peopleDictionary if person.contagiousness>0])) + "\n"
        coviddata_AP2.write(write)
        print(len([person for person in peopleDictionary if person.contagiousness>0]), " people are contagious on this day.")
    
    coviddata_AP2.close()


    



def AIRPORT3():
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
        
    def CovidSimulation():
        numPeople = 300000
        startingImmunity = 5
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
        lockdownDay5 = 42
        lockdownDay6 = 51
        lockdownDay7 = 64
        lockdownEnd1 = 14
        lockdownEnd2 = 23
        lockdownEnd3 = 30
        lockdownEnd4 = 39
        lockdownEnd5 = 46
        lockdownEnd6 = 56
        lockdownEnd7 = 70
        return daysContagious, lockdownDay1, lockdownDay2, lockdownDay3, lockdownDay4, lockdownDay5, lockdownDay6, lockdownDay7, lockdownEnd1, lockdownEnd2, lockdownEnd3, lockdownEnd4, lockdownEnd5, lockdownEnd6, lockdownEnd7
    def CovidSpread(daysContagious, lockdown):
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
    daysContagious, lockdownDay1, lockdownDay2, lockdownDay3, lockdownDay4, lockdownDay5, lockdownDay6, lockdownDay7, lockdownEnd1, lockdownEnd2, lockdownEnd3, lockdownEnd4, lockdownEnd5, lockdownEnd6, lockdownEnd7 = CovidSimulation()

    for x in range(0,101):
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
        CovidSpread(daysContagious,lockdown)
        coviddata_AP3 = open("coviddata_AP3.txt", "a")
        write = str(len([person for person in peopleDictionary if person.contagiousness>0])) + "\n"
        coviddata_AP3.write(write)
        print(len([person for person in peopleDictionary if person.contagiousness>0]), " people are contagious on this day.")
    
    coviddata_AP3.close()


    



def AIRPORT4():
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
        
    def CovidSimulation():
        numPeople = 500000
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
        lockdownDay5 = 42
        lockdownDay6 = 51
        lockdownDay7 = 64
        lockdownEnd1 = 14
        lockdownEnd2 = 23
        lockdownEnd3 = 30
        lockdownEnd4 = 39
        lockdownEnd5 = 46
        lockdownEnd6 = 56
        lockdownEnd7 = 70
        return daysContagious, lockdownDay1, lockdownDay2, lockdownDay3, lockdownDay4, lockdownDay5, lockdownDay6, lockdownDay7, lockdownEnd1, lockdownEnd2, lockdownEnd3, lockdownEnd4, lockdownEnd5, lockdownEnd6, lockdownEnd7
    def CovidSpread(daysContagious, lockdown):
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
    daysContagious, lockdownDay1, lockdownDay2, lockdownDay3, lockdownDay4, lockdownDay5, lockdownDay6, lockdownDay7, lockdownEnd1, lockdownEnd2, lockdownEnd3, lockdownEnd4, lockdownEnd5, lockdownEnd6, lockdownEnd7 = CovidSimulation()

    for x in range(0,101):
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
        CovidSpread(daysContagious,lockdown)
        coviddata_AP4 = open("coviddata_AP4.txt", "a")
        write = str(len([person for person in peopleDictionary if person.contagiousness>0])) + "\n"
        coviddata_AP4.write(write)
        print(len([person for person in peopleDictionary if person.contagiousness>0]), " people are contagious on this day.")
    
    coviddata_AP4.close()


    



def AIRPORT5():
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
        
    def CovidSimulation():
        numPeople = 1000000
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
        lockdownDay5 = 42
        lockdownDay6 = 51
        lockdownDay7 = 64
        lockdownEnd1 = 14
        lockdownEnd2 = 23
        lockdownEnd3 = 30
        lockdownEnd4 = 39
        lockdownEnd5 = 46
        lockdownEnd6 = 56
        lockdownEnd7 = 70
        return daysContagious, lockdownDay1, lockdownDay2, lockdownDay3, lockdownDay4, lockdownDay5, lockdownDay6, lockdownDay7, lockdownEnd1, lockdownEnd2, lockdownEnd3, lockdownEnd4, lockdownEnd5, lockdownEnd6, lockdownEnd7
    def CovidSpread(daysContagious, lockdown):
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
    daysContagious, lockdownDay1, lockdownDay2, lockdownDay3, lockdownDay4, lockdownDay5, lockdownDay6, lockdownDay7, lockdownEnd1, lockdownEnd2, lockdownEnd3, lockdownEnd4, lockdownEnd5, lockdownEnd6, lockdownEnd7 = CovidSimulation()

    for x in range(0,101):
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
        CovidSpread(daysContagious,lockdown)
        coviddata_AP5 = open("coviddata_AP5.txt", "a")
        write = str(len([person for person in peopleDictionary if person.contagiousness>0])) + "\n"
        coviddata_AP5.write(write)
        print(len([person for person in peopleDictionary if person.contagiousness>0]), " people are contagious on this day.")
    
    coviddata_AP5.close()


    

