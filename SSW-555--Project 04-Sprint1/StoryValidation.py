#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:32:15 2019

@author: gopi
"""
import UserStories
##############################       VALIDATING USER STORIES  START      #########################################
def story_validation(individuals, families):

    print('\n================================================ Validating User Stories ===================================================\n')

    returnFlag_US02 = UserStories.US02_birth_before_marriage(individuals,families)
    returnFlag_US03 = UserStories.US03_birth_before_death(individuals)
    returnFlag_US04 = UserStories.US04_marriage_before_divorce(families)
    returnFlag_US05 = UserStories.US05_marriage_before_death(individuals, families)
    returnFlag_US06 = UserStories.US06_Divorce_before_death(individuals, families)
    returnFlag_US07 = UserStories.US07(individuals)

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
error_locations = []

def report_error(rtype, error_type, description, locations):

        if isinstance(locations, list):
            locations = ','.join(locations)

        estr = '{:13.6s} {:15.15s}  {:80.80s}    {:70.70s}' \
            .format(rtype, error_type, description, locations)
        print(estr)
        error_locations.extend(locations)

##############################       REPORTING ERRORS  END      #########################################

    