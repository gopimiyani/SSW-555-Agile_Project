#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:53:49 2019

@author: gopi
"""


from datetime import datetime
import StoryValidation
from datetime import date

##############################       IMPLEMENTING  USER STORIES  START      ########################################

#------------------------------------ US 01 START [Dhaval]--------------------------------

def US01_dates_before_currentDate(individuals,families):
    return_flag = True
    error_type = "US01"
    today=date.today()
    #print("yoyoyoyoyo")

    for family in families:   
        if family.married != 'NA':
           if family.married > today: 
                error_descrip = "Marriage date (" + str(family.married) + \
                    ") should not occur after today (" + str(today)+")" 
                error_location = [family.uid, family.husbandID, family.wifeID]
                print('nError User Story Description" "Location')
                print(('-' * 150)) 
                StoryValidation.report_error('ERROR',error_type, error_descrip, error_location)
                return_flag = False
                
        if family.divorced!="NA":
            if family.divorced>today: 
                    error_descrip = "Divorce date (" + str(family.divorced) + \
                        ") should not occur after today (" + str(today)+")" 
                    error_location = [family.uid, family.husbandID, family.wifeID]
                    print('nError User Story Description" "Location')
                    print(('-' * 150)) 
                    StoryValidation.report_error('ERROR',error_type, error_descrip, error_location)
                    return_flag = False                

    for individual in individuals:   
        if individual.birthday!='NA':
                #print("test"+return_flag)
            if individual.birthday > today: 
                error_descrip = "Birthday date (" + str(individual.birthday) + \
                    ") should not occur after today (" + str(today)+")" 
                error_location = [individual.uid]
                print('nError User Story Description" "Location')
                print(('-' * 150)) 
                StoryValidation.report_error('ERROR',error_type, error_descrip, error_location)
                return_flag = False
                
        if individual.deathDate!='NA':
            if individual.deathDate > today: 
                    error_descrip = "Death date (" + str(individual.deathDate) + \
                        ") should not occur after today (" + str(today)+")" 
                    error_location = [individual.uid]
                    print('nError User Story Description" "Location')
                    print(('-' * 150)) 
                    StoryValidation.report_error('ERROR',error_type, error_descrip, error_location)
                    return_flag = False                

    #print("test"+return_flag)

    return return_flag
#------------------------------------ US 01 END ------------------------------------------


#------------------------------------ US 02 START [Krutarth]------------------------------

## US02 All BIRTH DATES MUST BE BEFORE MARRIAGE 
def US02_birth_before_marriage(individuals,families):
    return_flag = True
    error_type = "US02"
    for family in families:
        if family.married != 'NA':
            husband = family.husbandID
            wife = family.wifeID
            for individual in individuals:                  
                if individual.uid == wife:
                    if individual.birthday > family.married:
                        error_descrip = "Birth of wife (" + str(individual.birthday) + ") occurs before her marriage (" +str(family.married)+")"
                        error_location = [wife]
                        print("\nError       User Story                            Description                         "
                            "                             Location")
                        print(('-' * 150)) 
                        StoryValidation.report_error('ERROR',error_type, error_descrip, error_location)
                        return_flag = False
                if individual.uid == family.husbandID:
                    if individual.birthday > family.married:
                        error_descrip = "Birth of Husband ("+str(individual.birthday)+") occurs before his marriage ("+str(family.married)+")"
                        error_location = [husband]
                        print("\nError       User Story                            Description                         "
                            "                             Location")
                        print(('-' * 150)) 
                        StoryValidation.report_error('ERROR',error_type, error_descrip, error_location)
                        return_flag = False
    return return_flag

#------------------------------------ US 02 END ------------------------------------------

#------------------------------------ US 03 START [Krutarth]------------------------------

## US03 All BIRTH DATES MUST BE BEFORE DEATH DATE
def US03_birth_before_death(individuals):
    return_flag = True
    error_type = "US03"
    for individual in individuals:   
        if individual.deathDate!='NA' and individual.birthday!='NA':
            if individual.birthday > individual.deathDate: 
                error_descrip = "Death (" + str(individual.deathDate) + ") occurs before Birthday (" +str(individual.birthday)+")" 
                error_location = [individual.uid]
                print('nError User Story Description" "Location')
                print(('-' * 150)) 
                StoryValidation.report_error('ERROR',error_type, error_descrip, error_location)
                return_flag = False
    return return_flag

#------------------------------------ US 03 END -----------------------------------------


#------------------------------------ US 04 START [Gopi]---------------------------------

## US04 All MARRIAGE DATES MUST BE BEFORE DIVORCE DATE

def US04_marriage_before_divorce(families):
    return_flag = True
    error_type = "US04"
    for family in families:
        if family.married != 'NA' and family.divorced != 'NA':
            if family.married > family.divorced:
                error_descrip = "Divorce (" + str(family.divorced) + \
                    ") occurs before marriage (" + str(family.married)+")"
                error_location = [family.uid, family.husbandID, family.wifeID]
                print("\nError       User Story                            Description                         "
                      "                             Location")
                print(('-' * 150))
                StoryValidation.report_error('ERROR', error_type,
                             error_descrip, error_location)
                return_flag = False
    return return_flag


#------------------------------------ US 04 END ------------------------------------------


#------------------------------------ US 05 START [Gopi]-----------------------------------------

## US05 All MARRIAGE DATES MUST BE BEFORE DEATH DATE

def US05_marriage_before_death(individuals, families):
    return_flag = True
    error_type = "US05"
    for family in families:
        if family.married:
            husband = None
            wife = None
            for indiv in individuals:
                if indiv.uid == family.husbandID:
                    husband = indiv
                if indiv.uid == family.wifeID:
                    wife = indiv
            if wife != None:
                if wife.alive == False:
                    if family.married > wife.deathDate:
                        error_descrip = "Death of wife (" + str(
                            wife.deathDate) + ") occurs before her marriage (" + str(family.married)+")"
                        error_location = [wife.uid]
                        print("\nError       User Story                            Description                         "
                              "                             Location")
                        print(('-' * 150))
                        StoryValidation.report_error('ERROR', error_type,
                                     error_descrip, error_location)
                        return_flag = False
            if husband != None:
                if husband.alive == False:
                    if family.married > husband.deathDate:
                        error_descrip = "Death of Husband ("+str(
                            husband.deathDate)+") occurs before his marriage ("+str(family.married)+")"
                        error_location = [husband.uid]
                        print("\nError       User Story                            Description                         "
                              "                             Location")
                        print(('-' * 150))
                        StoryValidation.report_error('ERROR', error_type,
                                     error_descrip, error_location)
                        return_flag = False
    return return_flag

#------------------------------------ US 05 END -------------------------------------------


#------------------------------------ US 06 START [Deep]-----------------------------------------

def US06_Divorce_before_death(individual, families):
    return_flag = True
    error_type = "US06"
    for line in families:

        if(line.divorced != 'NA'):
            for linei in individual:
                if line.husbandID == linei.uid:
                    if linei.deathDate == 'NA':
                        return_flag = True

                    else:
                        divorce = str(line.divorced).split('-')
                        d_Date = str(linei.deathDate).split('-')

                        if(int(d_Date[0])-int(divorce[0])) > 0:
                            return_flag = True

                        elif d_Date[0] == divorce[0] and (d_Date[1]-divorce[1]) > 0:
                            return_flag = True

                        elif d_Date[0] == divorce[0] and d_Date[1] == divorce[1] and (d_Date[2]-divorce[2]) > 0:
                            return_flag = True

                        else:
                            error_descrip = "Divorce after death"
                            error_location = [linei.uid]
                            print("\nError       User Story                            Description                         "
                                  "                             Location")
                            print(('-' * 150))
                            StoryValidation.report_error('ERROR', error_type,
                                         error_descrip, error_location)
                            return_flag = False

                if line.wifeID == linei.uid:
                    if linei.deathDate == 'NA':
                        return_flag = True

                    else:
                        divorce = str(line.divorced).split('-')
                        d_Date = str(linei.deathDate).split('-')
                        if(int(d_Date[0])-int(divorce[0])) > 0:
                            return_flag = True

                        elif d_Date[0] == divorce[0] and (d_Date[1]-divorce[1]) > 0:
                            return_flag = True

                        elif d_Date[0] == divorce[0] and d_Date[1] == divorce[1] and (d_Date[2]-divorce[2]) > 0:
                            return_flag = True

                        else:
                            error_descrip = "Divorce after death"
                            error_location = [linei.uid]
                            print("\nError       User Story                            Description                         "
                                  "                             Location")
                            print(('-' * 150))
                            StoryValidation.report_error('ERROR', error_type,
                                         error_descrip, error_location)
                            return_flag = False
    return return_flag

#------------------------------------ US 06 END -------------------------------------------


#------------------------------------ US 07 START [Deep]-----------------------------------------

def US07(individuals):
    return_flag = True
    error_type = "US07"
    for individual in individuals:
        birthDate = individual.birthday
        arg = birthDate
        x = datetime.now()
        a = int(x.strftime("%Y")) - int(arg.strftime("%Y"))
        arg1 = int(arg.strftime("%m"))
        if (arg1 > int(x.strftime("%m"))) and int(arg.strftime("%d")) > int(x.strftime("%d")):
            age = a
        else:
            age = a-1

        if age > 150:
            error_descrip = "Age is more than 150"
            error_location = [individual.uid]
            print("\nError       User Story                            Description                         "
                  "                             Location")
            print(('-' * 150))
            StoryValidation.report_error('ERROR', error_type, error_descrip, error_location)
            return_flag = False
    return return_flag

#------------------------------------ US 07 END -------------------------------------------


#------------------------------------ US 08 START [Dhaval]---------------------------------

def US08_childbirth_after_marriage(individuals,families):
    return_flag = True
    error_type = "US08"
    for family in families:
        if family.married != 'NA' and family.children:
            husband = family.husbandID
            wife = family.wifeID
            for individual in individuals:                  
                if individual.uid in family.children:
                    if individual.birthday < family.married:
                        error_descrip = "Birth of child (" + str(individual.birthday) + ")"+str(individual.name)+ "cannot occur before marriage (" +str(family.married)+")"
                        error_location = [individual.uid,family.uid]
                        print("\nError       User Story                            Description                         "
                            "                             Location")
                        print(('-' * 150)) 
                        StoryValidation.report_error('ERROR',error_type, error_descrip, error_location)
                        return_flag = False
                
    return return_flag

#------------------------------------ US 08 END -------------------------------------------
    

#------------------------------------ US 09 START [KRUTARTH]-------------------------------


#------------------------------------ US 09 END -------------------------------------------
    


#------------------------------------ US 10 START [Dhaval]---------------------------------


#------------------------------------ US 10 END -------------------------------------------
    


#------------------------------------ US 11 START [Dhaval]---------------------------------


#------------------------------------ US 11 END -------------------------------------------
    


#------------------------------------ US 12 START [GOPI]----------------------------------


#------------------------------------ US 12 END -------------------------------------------
    
#------------------------------------ US 13 START [GOPI]-----------------------------------


#------------------------------------ US 13 END ------------------------------------------
    
#------------------------------------ US 14 START [DEEP]----------------------------------


#------------------------------------ US 15 END ------------------------------------------
    
#------------------------------------ US 15 START [DEEP]----------------------------------


#------------------------------------ US 16 END -------------------------------------------
    
#------------------------------------ US 16 START [KRUTARTH]--------------------------------


##############################       IMPLEMENTING  USER STORIES  END      ########################################



