#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:22:14 2019

@author: gopi
"""
import GedcomParser 
from datetime import datetime
FILENAME='My-Family_EditedByGopi_Errors.ged'
individuals, families = GedcomParser.gedcomParser(FILENAME)

import math

def getIndividiual(individual_uid):
    for i in individuals:
        if i.uid==individual_uid:
           return i 


def getFamily(individual_uid):
    for f in families:
       if f.husbandID==individual_uid or f.wifeID==individual_uid:
            return f 
       

def getChilds(individual_uid):
    childs=[]
    family=getFamily(individual_uid)
    childs.append(family.children)
    return childs
    
  

def getAge(individual_uid):
    individual=getIndividiual(individual_uid)
    todayDate=datetime.now()
    birthDate=individual.birthday
    age= abs(int(todayDate.strftime("%Y"))-int(birthDate.strftime("%Y")))
    return age
    

def getBirthdate(individual_uid):
    individual=getIndividiual(individual_uid)
    if individual!=None:
        birthDay=individual.birthday
        return birthDay
    
    
def dates_within(date1,date2,startLimit,endLimit,units):
    conversion={'days':1,'months':30.4,'years':365.25}
    datesDiff=abs((date1-date2).days)/conversion[units]
    returnFlag=  False if (datesDiff>=startLimit and datesDiff<=endLimit) else True
    return returnFlag

    
    
if __name__ == '__main__':     
    getChilds('@I2@')
    getChilds('@I3@') 
    getAge('@I1@')
    print(999<float(math.inf))
    getBirthdate('@I7@')