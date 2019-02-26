#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
from gedcomParser import gedcomParser
FILENAME = 'SSW-555-Agile-Project-01_UserStories.ged'
error_locations = []
#from datetime import date

from datetime import datetime


##############################        USER STORIES        ########################################


# ------------------- US04 All MARRIAGE DATES MUST BE BEFORE DIVORCE DATE ---------------

def US04_marriage_before_divorce(families):
   
    return_flag = True
    error_type = "US04"
    for family in families:
        if family.married!='NA' and family.divorced!='NA':
          
            
            if family.married > family.divorced:
                error_descrip = "Divorce (" + str(family.divorced) + ") occurs before marriage (" +str(family.married)+")" 
                error_location = [family.uid, family.husbandID, family.wifeID]
                
                print("\nError       User Story                            Description                         "
                              "                             Location")
                print(('-' * 150)) 
                report_error('ERROR',error_type, error_descrip, error_location)
                return_flag = False
    return return_flag


# ------------------- US05 All MARRIAGE DATES MUST BE BEFORE DEATH DATE ---------------
def US05_marriage_before_death(individuals,families):

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

            if wife!=None:
                
                if wife.alive == False:
                    if family.married > wife.deathDate:
                       
                        error_descrip = "Death of wife (" + str(wife.deathDate) + ") occurs before her marriage (" +str(family.married)+")"
                        error_location = [wife.uid]
                        print("\nError       User Story                            Description                         "
                              "                             Location")
                        print(('-' * 150)) 
                        report_error('ERROR',error_type, error_descrip, error_location)
                        return_flag = False
                        
                        
                        
                        
                        
            if husband!=None:
                if husband.alive == False:
                    if  family.married > husband.deathDate:
                        error_descrip = "Death of Husband ("+str(husband.deathDate)+") occurs before his marriage ("+str(family.married)+")"
                        error_location = [husband.uid]
                        print("\nError       User Story                            Description                         "
                              "                             Location")
                        print(('-' * 150)) 
                        report_error('ERROR',error_type, error_descrip, error_location)
                        return_flag = False

    return return_flag


#------------------------------------ US 06 -----------------------------------------
'''
def US06(individual, families):
    x.field_names = ["ID", "Name", "Gender","Birthday", "Alive", "Death", "Child", "Spouse"]
    for line in individual:
        attrs = vars(line)
        x.add_row(attrs.values())
        #print(x)

    print("\nFamilies")
    for line in families:
        if(vars(line)['divorced'] != 'NA'):
            print(vars(line)['husbandID'])
            for linei in individual:
                if vars(line)['husbandID'] == vars(linei)['uid']:
                    



            print(vars(line)['wifeID'])
'''


#------------------------------------ US 07 -----------------------------------------
    
def US07(individuals):
    #print(arg[2]+" "+arg[1]+" "+arg[0])
    return_flag = True
    error_type = "US04"
    for individual in individuals:
        
        birthDate=individual.birthday
        arg=birthDate
        #print(int(arg.strftime("%d")))
        x = datetime.now()
        #print(x.strftime("%Y"))
        
        a = int(x.strftime("%Y")) - int(arg.strftime("%Y"))
       
        arg1=int(arg.strftime("%m"))
        
        if (arg1==1):
            b=1
        elif(arg1==2):
            b=2
        elif(arg1==3):
            b=3
        elif(arg1==4):
            b=4
        elif(arg1==5):
            b=5
        elif(arg1==6):
            b=6
        elif(arg1==7):
            b=7
        elif(arg1==8):
            b=8
        elif(arg1==9):
            b=9
        elif(arg1==10):
            b=10
        elif(arg1==11):
            b=11
        elif(arg1==12):
            b=12
                                
        if (b>int(x.strftime("%m"))) and int(arg.strftime("%d"))>int(x.strftime("%d")):
            age = a                       
        else:
            age=a-1
    
        if age>150:
        

            error_descrip = "Age is more than 150"
            error_location = [individual.uid]
            
            print("\nError       User Story                            Description                         "
                          "                             Location")
            print(('-' * 150)) 
            report_error('ERROR',error_type, error_descrip, error_location)
            return_flag = False
 
    return return_flag


#-----------------------------  STORY VALIDATION  -------------------------------------
def story_validation(individuals, families):
   
    print('\n================================================ Validating User Stories ===================================================\n')
    
    returnFlag_US04=US04_marriage_before_divorce(families)
    returnFlag_US05=US05_marriage_before_death(individuals,families)
   
    returnFlag_US07=US07(individuals)
   
    
    
    
    if returnFlag_US04==True:
        print('\n\nUS04 >> No Bugs Encountered.')
    else:
        print('\n\nUS04 >> Errors Found!!\n')
   
    if returnFlag_US05==True:
      
        print('\nUS05 >> No Bugs Encountered.')
    else:
        print('\nUS05 >> Errors Found!!\n')
    
    if returnFlag_US07==True:
      
        print('\nUS07 >> No Bugs Encountered.')
    else:
        print('\nUS07 >> Errors Found!!\n')
    #print("\n* * * * * * * * * * * * * * * *  * * * * * * * * * *         ERRORS         * * * * * * * * * * * * * * * * * * * * * * * \n")
    
    
    
    


# ------------------------------- REOPRT ERRORS -------------------------------------
def report_error(rtype, error_type, description, locations):
        
            
        if isinstance(locations, list):
            locations = ','.join(locations)
    
        estr = '{:13.6s} {:15.15s}  {:80.80s}    {:70.70s}' \
            .format(rtype, error_type, description, locations)
        print(estr)
        error_locations.extend(locations)
        

# ------------------------------  UNIT TEST ---------------------------------------
    
import unittest
import os
#from gedcomParser import gedcomParser

cur_path = os.path.dirname(__file__)

passFile = "pass/SSW-555-Agile-Project-01_UserStories.ged"
failFile = "fail/SSW-555-Agile-Project-01_UserStories.ged"

    
class test_UserStories(unittest.TestCase):
    
    
    '''
    def test1_birth_before_death(self):
        individuals, _ = gedcomParser(passFile)
        self.assertTrue(birth_before_death(individuals))

    def test2_birth_before_death(self):
        individuals, _ = gedcomParser(passFile)
        self.assertEqual(birth_before_death(individuals),True)

    def test3_birth_before_death(self):
        individuals, _ = gedcomParser(passFile)
        self.assertIsNot(birth_before_death(individuals),False)

    def test4_birth_before_death(self):
        individuals, _ = gedcomParser(failFile)
        self.assertIsNotNone(birth_before_death(individuals))

    def test5_birth_before_death(self):
        individuals, _ = gedcomParser(passFile)
        self.assertIs(birth_before_death(individuals),True)
    '''  
    
    
     # ---------------------------- TESTING US_04 : CASE 1 -------------------------------
    def test_US04(self):
        print("\n============================================  Performing Unit test on User Stories ==========================================\n")
        print('TESTING US_04...')
        individuals, families = gedcomParser(passFile)
        #self.assertTrue(US04_marriage_before_divorce(families))
        self.assertNotEqual(US04_marriage_before_divorce(families),True)
        '''
        for family in families:
            if family.married:
                husband = None
                for indiv in individuals:
                    if indiv.uid == family.husbandID:
                        husband = indiv
                if husband!= None and husband.alive != None:
                    if husband.alive==False:
                        self.assertNotEquals(husband.deathDate, family.married)
        '''

    # ---------------------------- TESTING US_04 : CASE 2 ---------------------------------
    '''
    def test_US04_2(self):
        print('TESTING US_04 : CASE 2..')
        individuals, families = gedcomParser(passFile)
        #self.assertTrue(US04_marriage_before_divorce(families))
        self.assertIs(US04_marriage_before_divorce(families),True)
        
        for family in families:
            if family.married:
                wife = None
                for indiv in individuals:
                    if indiv.uid == family.wifeID:
                        wife = indiv
                if wife!=None and wife.alive!=None:
                    if wife.alive==False:
                        self.assertNotEquals(wife.deathDate, family.married)
    '''
                        
    # --------------------------- TESTING US_05 -------------------------------------------
    def test_US05(self):
        print('TESTING US_05...')
        individuals, families = gedcomParser(passFile)
        #self.assertFalse(US05_marriage_before_death(individuals, families))
        #self.assertContains(response, 'pagination', html=True)
        self.assertNotEqual(US05_marriage_before_death(individuals,families),True)
        

#----------------------- MAIN  METHOD ---------------------------------------
        
        
if __name__ == '__main__': 
    #countErrors=0
    individuals, families=gedcomParser(FILENAME)
    story_validation(individuals, families)
    
    unittest.main()         