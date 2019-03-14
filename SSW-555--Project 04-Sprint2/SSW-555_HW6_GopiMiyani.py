#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:32:10 2019

@author: Gopi Miyani 10437266
"""

def dates_within(date1,date2,limit,units):
    conversion={'days':1,'months':30.4,'years':365.25}
    datesDiff=abs((date1-date2).days)/conversion[units]
    returnFlag=  False if (datesDiff<=limit) else True
    return returnFlag
    
#------------------------------------ US 13 START [GOPI]-----------------------------------NEW AFTER REFACTORING
    
def US13_siblings_spacing__NEW(individuals, families):
    return_flag = True
    error_type = "US13"
    
    for family in families:
        childs=[]
        for child  in family.children:
            childs.append(child)
        birthdayOfChilds={}
        for individual in individuals:
            for child in childs:
                if child==individual.uid:
                    birthday_child=individual.birthday
                    birthdayOfChilds[individual.uid]=birthday_child
        childslen=len(birthdayOfChilds);
        for i in range(0,childslen):
            for j in range (i+1,childslen):
                    
                        return_flag = dates_within(birthdayOfChilds[childs[i]],birthdayOfChilds[childs[j]],8,'months')
                        error_descrip = "Child (ID: " +str(childs[i])+", B'day: " +str(birthdayOfChilds[childs[i]]) + ") violates Sibling Space with other child (ID: " +str(childs[j]) +", B'day: " +str(birthdayOfChilds[childs[j]]) + ")";
                        
                        error_location = [family.wifeID]
                       
                        report_error('ERROR',error_type, error_descrip, error_location)
                        
                    
    return return_flag



#------------------------------------ US 13 START [GOPI]-----------------------------------OLD WITH BAD SMELLS

## US13	Siblings spacing ----Birth dates of siblings should be more than 8 months apart or less than 2 days apart (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)

def US13_siblings_spacing__OLD(individuals, families):
    return_flag = True
    error_type = "US13"
    
    for family in families:
        childs=[]
        for child  in family.children:
            childs.append(child)
        birthdayOfChilds={}
        for individual in individuals:
            for child in childs:
                if child==individual.uid:
                    birthday_child=individual.birthday
                    birthdayOfChilds[individual.uid]=birthday_child
        childslen=len(birthdayOfChilds);
        for i in range(0,childslen):
            for j in range (i+1,childslen):
                    birthdayDiff=abs((birthdayOfChilds[childs[i]]-birthdayOfChilds[childs[j]]).days)    
                   
                    if birthdayDiff>1 and birthdayDiff<240:
                        error_descrip = "Child (ID: " +str(childs[i])+", B'day: " +str(birthdayOfChilds[childs[i]]) + ") violates Sibling Space with other child (ID: " +str(childs[j]) +", B'day: " +str(birthdayOfChilds[childs[j]]) + ")";
                        
                        error_location = [family.wifeID]
                       
                        report_error('ERROR',error_type, error_descrip, error_location)
                        return_flag = False
                    
    return return_flag

#------------------------------------ US 13 END ------------------------------------------
    

##############################       REPORTING ERRORS  START      #########################################
error_locations = []

def report_error(rtype, error_type, description, locations):

        if isinstance(locations, list):
            locations = ','.join(locations)

        estr = '{:10.6s} {:13.15s}  {:100.130s}    {:70.70s}' \
            .format(rtype, error_type, description, locations)
        print(estr)
        error_locations.extend(locations)

##############################       REPORTING ERRORS  END      #########################################

