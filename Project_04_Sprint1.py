#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import unittest
from datetime import datetime
from gedcomParser import gedcomParser
"""
Created on Fri Feb 22 22:30:29 2019



SSW 555 Agile Methods for Software Development Project 4

Purpose: Perform first sprint Assignment:

From now on all project work will be done in teams. Only one member of the team needs to submit work for each assignment.

There are 4 parts to this assignment:

    Executing Sprint 1

    Demonstrating the results of Sprint 1

    Reviewing Sprint 1

    Planning Sprint 2

1. Executing Sprint 1:

    Perform the tasks and complete the user stories as identified for this sprint. Record actual sizes and times and copy those where appropriate on the Project Backlog page.

    Update the Burndown sheet and calculate your velocities for the sprint.

    Make sure that you create a line-oriented application that does something for demonstration to the customer.

    Make sure that you commit the completed version of your source code to your GitHub repository.

2. Demonstrating Sprint 1:

    Execute your system on the acceptance test file.

    Capture the output in a separate Test Results file. This is the demonstration for the customer.

3. Reviewing Sprint 1:

    At a team meeting review the results of the sprint.

    Make 2 lists:

        things you want to keep doing

        things that you want to avoid doing in the future

    Record the lists at the bottom of the Sprint1 sheet

4. Planning Sprint 2:

    At a team meeting decide which user stories will be completed in the next sprint.

    Update the Backlog sheet and the Sprint 2 sheet to show this, including ownership and estimates of all tasks and user stories for Sprint 2.

Submit your Project Sprint Report, your acceptance test file and your Test Results from Sprint 1 as a single zipped archive file to the Project 04 Canvas assignment. Make sure that the name of your GitHub repository is included on the Team sheet of your Project Sprint Report. The instructor needs this to review your source code.

Please see the Sprint Checklist for an example of the format of output and the information to include in your submission.

@author: Gopi Miyani
         Deep Chokshi
         Krutarth Trivedi
         Dhaval Dongre

###  GOPI MIYANI : USER STORIES ###
         
         US04	Marriage before divorce	Marriage should occur before divorce of spouses, and divorce can only occur after marriage
         US05	Marriage before death	Marriage should occur before death of either spouse

"""

## FOR MY REFERENCE:
'''
# --------------------------- CLASS: INDIVIDUAL PERSON ---------------------------
class individualClass(object):

    def __init__(self, uid):
        self.uid = uid  
        self.name = 'NA' 
        self.gender = 'NA'  
        self.birthday = 'NA'  
        self.deathDate = 'NA'  
        self.alive = True
        self.famc = []
        self.fams = [] 

# ----------------------------- CLASS: FAMILY ------------------------------------
class familyClass(object):

    def __init__(self, uid):
        self.uid = uid
        self.married = 'NA'  
        self.divorced = 'NA'  
        self.husbandID = 'NA'  
        self.husbandName = 'NA'  
        self.wifeID = 'NA'  
        self.wifeName = 'NA'  
        self.children = [] 
      

'''
FILENAME = 'SSW-555-Agile-Project-01_UserStories.ged'
#FILENAME = 'SSW-555-Agile-Project-01_UserStories_Err.ged'
error_locations = []
#from datetime import date


##############################       IMPLEMENTING  USER STORIES  START      ########################################


#------------------------------------ US 01 START ----------------------------------------


#------------------------------------ US 01 END ------------------------------------------


#------------------------------------ US 02 START ----------------------------------------

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
                        report_error('ERROR',error_type, error_descrip, error_location)
                        return_flag = False
                if individual.uid == family.husbandID:
                    if individual.birthday > family.married:
                        error_descrip = "Birth of Husband ("+str(individual.birthday)+") occurs before his marriage ("+str(family.married)+")"
                        error_location = [husband]
                        print("\nError       User Story                            Description                         "
                            "                             Location")
                        print(('-' * 150)) 
                        report_error('ERROR',error_type, error_descrip, error_location)
                        return_flag = False
    return return_flag

#------------------------------------ US 02 END ------------------------------------------

#------------------------------------ US 03 START ----------------------------------------

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
                report_error('ERROR',error_type, error_descrip, error_location)
                return_flag = False
    return return_flag

#------------------------------------ US 03 END -----------------------------------------


#------------------------------------ US 04 START -----------------------------------------

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
                report_error('ERROR', error_type,
                             error_descrip, error_location)
                return_flag = False
    return return_flag


#------------------------------------ US 04 END ------------------------------------------


#------------------------------------ US 05 START -----------------------------------------

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
                        report_error('ERROR', error_type,
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
                        report_error('ERROR', error_type,
                                     error_descrip, error_location)
                        return_flag = False
    return return_flag

#------------------------------------ US 05 END -------------------------------------------


#------------------------------------ US 06 START -----------------------------------------

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
                            print("\nError       User Story                            Description                         "
                                  "                             Location")
                            print(('-' * 150))
                            report_error('ERROR', error_type,
                                         error_descrip, error_location)
                            return_flag = False
    return return_flag

#------------------------------------ US 06 END -------------------------------------------


#------------------------------------ US 07 START -----------------------------------------

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
            report_error('ERROR', error_type, error_descrip, error_location)
            return_flag = False
    return return_flag

#------------------------------------ US 07 END -------------------------------------------


#------------------------------------ US 08 START -----------------------------------------


#------------------------------------ US 08 END -------------------------------------------


##############################       IMPLEMENTING  USER STORIES  END      ########################################


##############################       VALIDATING USER STORIES  START      #########################################
def story_validation(individuals, families):

    print('\n================================================ Validating User Stories ===================================================\n')

    returnFlag_US02 = US02_birth_before_marriage(individuals,families)
    returnFlag_US03 = US03_birth_before_death(individuals)
    returnFlag_US04 = US04_marriage_before_divorce(families)
    returnFlag_US05 = US05_marriage_before_death(individuals, families)
    returnFlag_US06 = US06_Divorce_before_death(individuals, families)
    returnFlag_US07 = US07(individuals)

    if returnFlag_US02==True:
        print('\n\nUS02 >> No Bugs Encountered.')
    else:
        print('\n\nUS02 >> Errors Found!!\n')
    if returnFlag_US03==True:
        print('\n\nUS03 >> No Bugs Encountered.')
    else:
        print('\n\nUS03 >> Errors Found!!\n')
    if returnFlag_US04 == True:
        print('\n\nUS04 >> No Bugs Encountered.')
    else:
        print('\n\nUS04 >> Errors Found!!\n')

    if returnFlag_US05 == True:

        print('\nUS05 >> No Bugs Encountered.')
    else:
        print('\nUS05 >> Errors Found!!\n')

    if returnFlag_US06 == True:

        print('\nUS06 >> No Bugs Encountered.')
    else:
        print('\nUS06 >> Errors Found!!\n')

    if returnFlag_US07 == True:

        print('\nUS07 >> No Bugs Encountered.')
    else:
        print('\nUS07 >> Errors Found!!\n')
    #print("\n* * * * * * * * * * * * * * * *  * * * * * * * * * *         ERRORS         * * * * * * * * * * * * * * * * * * * * * * * \n")


##############################       VALIDATING USER STORIES  END      #########################################


##############################       REPORTING ERRORS  START      #########################################

def report_error(rtype, error_type, description, locations):

        if isinstance(locations, list):
            locations = ','.join(locations)

        estr = '{:13.6s} {:15.15s}  {:80.80s}    {:70.70s}' \
            .format(rtype, error_type, description, locations)
        print(estr)
        error_locations.extend(locations)

##############################       REPORTING ERRORS  END      #########################################


##############################       UNIT TEST  START      #########################################

#from gedcomParser import gedcomParser

cur_path = os.path.dirname(__file__)

passFile = "SSW-555-Agile-Project-01_UserStories.ged"
failFile = "SSW-555-Agile-Project-01_UserStories_Err.ged"


class test_UserStories(unittest.TestCase):
# ------------------------------- TESTING US_02 -------------------------------------
    def test_US02(self):
        print("\n======================Performing Unit test on User Stories ================\n")
        print('TESTING US_02...')
        individuals, families = gedcomParser(passFile)
        self.assertEqual(US02_birth_before_marriage(individuals,families), True)
        individuals, families = gedcomParser(failFile)
        self.assertEqual(US02_birth_before_marriage(individuals,families), False)

# ------------------------------- TESTING US_03 -------------------------------------

    def test_US03(self):
        print('TESTING US_03...')
        individuals, families = gedcomParser(passFile)
        self.assertEqual(US03_birth_before_death(individuals), True)
        individuals, families = gedcomParser(failFile)
        self.assertEqual(US03_birth_before_death(individuals), False)
     # ------------------------------- TESTING US_04 -------------------------------------
    def test_US04(self):
        print('TESTING US_04...')
        individuals, families = gedcomParser(failFile)
        #self.assertTrue(US04_marriage_before_divorce(families))
        self.assertNotEqual(US04_marriage_before_divorce(families), True)

    # --------------------------- TESTING US_05 -------------------------------------------

    def test_US05(self):
        print('TESTING US_05...')
        individuals, families = gedcomParser(passFile)
        #self.assertFalse(US05_marriage_before_death(individuals, families))
        #self.assertContains(response, 'pagination', html=True)
        self.assertNotEqual(US05_marriage_before_death(
            individuals, families), True)
 # --------------------------- TESTING US_05 -------------------------------------------

    def test_US06(self):
        print('TESTING US_06...')
        individuals, families = gedcomParser(passFile)
        self.assertTrue(US06_Divorce_before_death(individuals, families))
        individuals, families = gedcomParser(failFile)
        self.assertFalse(US06_Divorce_before_death(individuals, families))

    def test_US07(self):
        print('TESTING US_07...')
        individuals, families = gedcomParser(passFile)
        self.assertTrue(US07(individuals))
        individuals, families = gedcomParser(failFile)
        self.assertFalse(US07(individuals))
    


##############################       UNIT TEST  END      #########################################


##############################       MAIN METHOD START    #########################################

if __name__ == '__main__':
    #countErrors=0
    individuals, families = gedcomParser(FILENAME)
    story_validation(individuals, families)
    unittest.main()


##############################       MAIN METHOD END    #########################################
