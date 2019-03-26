#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:53:49 2019

@author: gopi
"""


from datetime import datetime
from UDFunctions import getAge ,getChilds,getBirthdate,dates_within
from datetime import date


##############################       FUNCTIONS  START      #######################################

#print(dates_within(datetime.strptime('2018-05-04',"%Y-%m-%d"), datetime.strptime('2011-05-04',"%Y-%m-%d"), 0, 15, 'years'))    
##############################       FUNCTIONS  START      #######################################




##############################       IMPLEMENTING  USER STORIES  START      #######################################

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
                report_error('ERROR',error_type, error_descrip, error_location)
                return_flag = False
                
        if family.divorced!="NA":
            if family.divorced>today: 
                    error_descrip = "Divorce date (" + str(family.divorced) + \
                        ") should not occur after today (" + str(today)+")" 
                    error_location = [family.uid, family.husbandID, family.wifeID]
                    print('nError User Story Description" "Location')
                    print(('-' * 150)) 
                    report_error('ERROR',error_type, error_descrip, error_location)
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
                report_error('ERROR',error_type, error_descrip, error_location)
                return_flag = False
                
        if individual.deathDate!='NA':
            if individual.deathDate > today: 
                    error_descrip = "Death date (" + str(individual.deathDate) + \
                        ") should not occur after today (" + str(today)+")" 
                    error_location = [individual.uid]
                    print('nError User Story Description" "Location')
                    print(('-' * 150)) 
                    report_error('ERROR',error_type, error_descrip, error_location)
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
                        print("\nError     User Story                            Description                                    "
                            "                             Location")
                        print(('-' * 150)) 
                        report_error('ERROR',error_type, error_descrip, error_location)
                        return_flag = False
                if individual.uid == family.husbandID:
                    if individual.birthday > family.married:
                        error_descrip = "Birth of Husband ("+str(individual.birthday)+") occurs before his marriage ("+str(family.married)+")"
                        error_location = [husband]
                        print("\nError    User Story                            Description                                   "
                            "                                   Location")
                        print(('-' * 150)) 
                        report_error('ERROR',error_type, error_descrip, error_location)
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
                #print('nError User Story Description" "Location')
                #print(('-' * 150)) 
                report_error('ERROR',error_type, error_descrip, error_location)
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
                #print("\nError       User Story                            Description                         "
                #     "                             Location")
                #print(('-' * 150))
                report_error('ERROR', error_type,
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
                        error_descrip = "Death of wife (" + str( wife.deathDate) + ") occurs before her marriage (" + str(family.married)+")"
                        error_location = [wife.uid]
                        report_error('ERROR', error_type,error_descrip, error_location)
                        return_flag = False
            if husband != None:
                if husband.alive == False:
                    if family.married > husband.deathDate:
                        error_descrip = "Death of Husband ("+str(husband.deathDate)+") occurs before his marriage ("+str(family.married)+")"
                        error_location = [husband.uid] 
                        report_error('ERROR', error_type,error_descrip, error_location)
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
                            #print("\nError       User Story                            Description                         "
                            #      "                             Location")
                            #print(('-' * 150))
                            report_error('ERROR', error_type,
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
        
                            report_error('ERROR', error_type,error_descrip, error_location)
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
            report_error('ERROR', error_type, error_descrip, error_location)
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
                        report_error('ERROR',error_type, error_descrip, error_location)
                        return_flag = False
                
    return return_flag

#------------------------------------ US 08 END -------------------------------------------
    

#------------------------------------ US 09 START [KRUTARTH]-------------------------------


#------------------------------------ US 09 END -------------------------------------------
    


#------------------------------------ US 10 START [Dhaval]---------------------------------
def US10_marriage_age_14(individuals,families):
    return_flag = True
    error_type = "US10"
    #today=datetime.date.today()
    for family in families:   
      if family.married != 'NA':
        #if family.deathDate!='NA' and individual.birthday!='NA':
         #   if individual.birthday > individual.deathDate: 
        for individual in individuals:
            if individual.uid==family.husbandID:
                return_flag =  not dates_within(getBirthdate(individual.uid),getFamily(individual.uid).married ,0,13,'years')
                if return_flag==True:
                    error_descrip = "Age during marriage less than 14 for husband! birth:"+str(getBirthdate(individual.uid))+" marriage:"+str(getFamily(individual.uid).married) 
                    error_location = [individual.uid]
                    report_error('ERROR',error_type, error_descrip, error_location)

        for individual in individuals:
            if individual.uid==family.wifeID:
                return_flag =  not dates_within(getBirthdate(individual.uid),getFamily(individual.uid).married ,0,13,'years')
                if return_flag==True:
                    error_descrip = "Age during marriage less than 14 for wife! birth"+str(getBirthdate(individual.uid))+" marriage:"+str(getFamily(individual.uid).married) 
                    error_location = [individual.uid]
                    report_error('ERROR',error_type, error_descrip, error_location)
                    return_flag = False

    return return_flag

#------------------------------------ US 10 END -------------------------------------------
    


#------------------------------------ US 11 START [Dhaval]---------------------------------
def US11_no_bigamy(individuals,families):
    return_flag = True
    error_type = "US11"
    #today=datetime.date.today()
    for family in families:   
      if family.married != 'NA':
        currentFamId=family.uid
        for family2 in families:
          if currentFamId!=family2.uid:
            if family.husbandID==family2.husbandID or family.wifeID==family2.wifeID:
              if family.married<family2.married:
                if family.divorced!='NA' and family.divorced>family2.married:
                  return_flag==False
                  error_descrip = "Bigamy detected!"
                  error_location = [family.uid,family2.uid]
                  report_error('ERROR',error_type, error_descrip, error_location)


              if family.married>family2.married:
                if family.divorced!='NA' and family.divorced<family2.married:
                  return_flag==False
                  error_descrip = "Bigamy detected!"
                  error_location = [family.uid,family2.uid]
                  report_error('ERROR',error_type, error_descrip, error_location)

    return return_flag

#------------------------------------ US 11 END -------------------------------------------
    

    
#------------------------------------ US 12 START [GOPI]----------------------------------NEW AFTER REFACTORING

## US12	Parents not too old	---Mother should be less than 60 years older than her children and father should be less than 80 years older than his children

def US12_parents_not_too_old(individuals, families):
    
    return_flag = True
    error_type = "US12"
  
    for family in families:
        birthday_husband=getBirthdate(family.husbandID)
        birthday_wife=getBirthdate(family.wifeID)
        childs=(family.children)
        birthday_childs={}
      
        for child in childs:
            birthday=getBirthdate(child)
            birthday_childs[child]=birthday
        
        for childID,childBirthday in birthday_childs.items():
                return_flag =  not dates_within(birthday_husband,childBirthday ,0,79,'years')
                
                if return_flag==False:
                    error_descrip = "Husband (Id, Age: " + family.husbandID + ', ' + str(getAge(family.husbandID)) + ") is elder than 80 years than his children(Id, Age: " + childID + ', ' + str(getAge(childID)) + ')\n'
                    error_location = [family.husbandID]
                    report_error('ERROR',error_type, error_descrip, error_location)
                
                return_flag = not dates_within(birthday_wife,childBirthday,0,59,'years')
                if return_flag==False:
                    error_descrip = "Wife (Id, Age: "+ family.wifeID + ', '  + str(getAge(family.wifeID)) + ") is elder than 60 years than her children (Id, Age: " + childID + ', ' + str(getAge(childID)) + ')\n'
                    error_location = [family.wifeID]
                    report_error('ERROR',error_type, error_descrip, error_location)
  
    return return_flag
#----------------------------------- US 12 END -------------------------------------------
    

#------------------------------------ US 13 START [GOPI]-----------------------------------NEW AFTER REFACTORING
    
def US13_siblings_spacing(individuals, families):
    return_flag = True
    error_type = "US13"
    for family in families:
        childs=family.children
        birthdayOfChilds={}
        for individual in individuals:
            for child in childs:
                if child==individual.uid:
                    birthdayOfChilds[individual.uid]=getBirthdate(child)
        childslen=len(birthdayOfChilds);
        for i in range(0,childslen):
            for j in range (i+1,childslen):
                return_flag = dates_within(birthdayOfChilds[childs[i]],birthdayOfChilds[childs[j]],2,243,'days')
                if return_flag==False:
                    error_descrip = "Child (ID: " +str(childs[i])+", B'day: " +str(birthdayOfChilds[childs[i]]) + ") is not 8 months apart from his/her sibling (ID: " +str(childs[j]) +", B'day: " +str(birthdayOfChilds[childs[j]]) + ")";
                    error_location = [childs[i]]
                    report_error('ERROR',error_type, error_descrip, error_location)
    return return_flag

#------------------------------------ US 13 END ------------------------------------------
    

#------------------------------------ US 14 START [DEEP]----------------------------------
def US14_Multiple_births(individuals, families):
    return_flag = True
    error_type = "US14"

    for family in families:
        birthdays = []
        children = family.children
        Number_of_children = len(children)
        if Number_of_children > 6:
            for child in children:
                for individual in individuals:
                    if (child==individual.uid):
                        birthdays.append(individual.birthday)
            pre = ""
            count =0
            for birthday in birthdays:
                if(birthday==prev):
                    count=count + 1

                pre = birthday

            if count > 6:
                error_descrip = "Multiple births"
                error_location = [family.uid]
                print("\nError       User Story                            Description                         "                            "                             Location")
                print(('-' * 150))
                StoryValidation.report_error('ERROR', error_type, error_descrip, error_location)
                return_flag = False 

    return return_flag


#------------------------------------ US 15 END ------------------------------------------
    
#------------------------------------ US 15 START [DEEP]----------------------------------
def US15_Fewer_than_15_siblings(families):
    return_flag = True
    error_type = "US15"

    for family in families:
        child = family.children
        Number_of_children=len(child)
        if Number_of_children > 15:
            error_descrip = "More than 15 siblings"
            error_location = [family.uid]
            print("\nError       User Story                            Description                         "
                "                             Location")
            print(('-' * 150))
            StoryValidation.report_error('ERROR', error_type, error_descrip, error_location)
            return_flag = False

    return return_flag

#------------------------------------ US 15 END -------------------------------------------
    
#------------------------------------ US 16 START [KRUTARTH]--------------------------------


##############################       IMPLEMENTING  USER STORIES  END      ########################################

##############################       REPORTING ERRORS  START      #########################################
error_locations = []

def report_error(rtype, error_type, description, locations):

        if isinstance(locations, list):
            locations = ','.join(locations)

        estr = '{:10.10s} {:15.15s}  {:100.100s}    {:50.50s}' \
            .format(rtype, error_type, description, locations)
        print(estr)
        error_locations.extend(locations)

##############################       REPORTING ERRORS  END      #########################################


