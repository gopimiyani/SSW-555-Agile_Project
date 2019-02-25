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

# ------------------- US05 All MARRIAGE DATES MUST BE BEFORE DEATH DATE ---------------
def marriage_before_death(individuals,families):

     # For each individual check if marriage occurs before death
    return_flag = True
    error_type = "US05"
    for family in families:
        if family.married:
            # Search through individuals to get husband and wife
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
                        #print('\n*************')
                        #print(family.married)
                        #print(wife.deathDate)
                        # Found a case spouse marries before birthday
                        error_descrip = "Death of wife (" + str(wife.deathDate) + ") occurs before her marriage (" +str(family.married)+")"
                        error_location = [wife.uid]
                        report_error('ERROR',error_type, error_descrip, error_location)
                        return_flag = False
            if husband!=None:
                if husband.alive == False:
                    if  family.married > husband.deathDate:
                        error_descrip = "Death of Husband ("+str(husband.deathDate)+") occurs before his marriage ("+str(family.married)+")"
                        error_location = [husband.uid]
                        report_error('ERROR',error_type, error_descrip, error_location)
                        return_flag = False

    return return_flag


# ------------------- US04 All MARRIAGE DATES MUST BE BEFORE DIVORCE DATE ---------------

def marriage_before_divorce(families):
   
    return_flag = True
    error_type = "US04"
    for family in families:
        if family.married!='NA' and family.divorced!='NA':
          
            
            if family.married > family.divorced:
                #print('\n\n*************')
                #print(family.married)
                #print(family.divorced)
                error_descrip = "Divorce (" + str(family.divorced) + ") occurs before marriage (" +str(family.married)+")" 
                error_location = [family.uid, family.husbandID, family.wifeID]
                report_error('ERROR',error_type, error_descrip, error_location)
                return_flag = False
    return return_flag



#-----------------------------  STORY VALIDATION  -------------------------------------
def story_validation(individuals, families):
   
    #print('Testing Done Successfully!\n')
    print("\n\t\t\t**************************   ERRORS   *********************************\n")
    print("\nError       User Story                            Description                         "
          "                             Location")
    print(('-' * 150))
    returnFlag_US05=marriage_before_death(individuals,families)
    returnFlag_US04=marriage_before_divorce(families)
    if returnFlag_US05==True:
      
        print('\n\nUS05 >> Tests Passed !\nNo Bugs Encountered....\n')
    else:
        print('\n\nUS05 >> Errors Found!!\n')
    if returnFlag_US04==True:
        print('\nUS04 >> Tests Passed !\nNo Bugs Encountered....\n')
    else:
        print('\nUS04 >> Errors Found!!\n')
    #else:
        #print('Some bugs are found...')


# ------------------------------- REOPRT ERRORS -------------------------------------
def report_error(rtype, error_type, description, locations):
  
    if isinstance(locations, list):
        locations = ','.join(locations)

    estr = '{:13.6s} {:15.15s}  {:80.80s}    {:70.70s}' \
        .format(rtype, error_type, description, locations)
    print(estr)
    error_locations.extend(locations)


#----------------------- MAIN  METHOD ---------------------------------------
        
        
if __name__ == '__main__': 
    
    individuals, families=gedcomParser(FILENAME)
    story_validation(individuals, families)
    