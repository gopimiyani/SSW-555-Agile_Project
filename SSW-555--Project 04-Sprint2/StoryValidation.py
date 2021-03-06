#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:32:15 2019

@author: gopi
"""
import UserStories

##############################       VALIDATING USER STORIES  START      #########################################

def story_validation(individuals, families):

    print('Validating User Stories..')
    print('\n========================================================= Reporting Errors ================================================================\n')

    returnFlag_US01 = UserStories.US01_dates_before_currentDate(individuals, families)
    returnFlag_US02 = UserStories.US02_birth_before_marriage(individuals,families)
    returnFlag_US03 = UserStories.US03_birth_before_death(individuals)
    returnFlag_US04 = UserStories.US04_marriage_before_divorce(families)
    returnFlag_US05 = UserStories.US05_marriage_before_death(individuals, families)
    returnFlag_US06 = UserStories.US06_Divorce_before_death(individuals, families)
    returnFlag_US07 = UserStories.US07(individuals)
    returnFlag_US08 = UserStories.US08_childbirth_after_marriage(individuals, families)
    returnFlag_US10 = UserStories.US10_marriage_age_14(individuals, families)
    returnFlag_US11 = UserStories.US11_no_bigamy(individuals, families)
    returnFlag_US12 = UserStories.US12_parents_not_too_old(individuals, families)
    returnFlag_US13 = UserStories.US13_siblings_spacing(individuals, families)
    returnFlag_US14 = UserStories.US14_Multiple_births(individuals, families)
    returnFlag_US15 = UserStories.US15_Fewer_than_15_siblings(families)
    
    
    print('\n======================================================= Errors in User Stories ============================================================\n')
    
   
    returnFlags={'US01':returnFlag_US01,'US02':returnFlag_US02,'US03':returnFlag_US03,'US04':returnFlag_US04,'US05':returnFlag_US05,
                 'US06':returnFlag_US06,'US07':returnFlag_US07,'US08':returnFlag_US08,'US10':returnFlag_US10,'US11':returnFlag_US11,'US12':returnFlag_US12,'US13':returnFlag_US13,'US14':returnFlag_US14,'US15':returnFlag_US15}
                 
    errorsUserStories=[]
    for key,value in returnFlags.items():
        if value==False:
            errorsUserStories.append(key)
    print('\nErrors found in below User Stories:\n')
    print(errorsUserStories)
    
   
   
    #print("\n* * * * * * * * * * * * * * * *  * * * * * * * * * *         ERRORS         * * * * * * * * * * * * * * * * * * * * * * * \n")


##############################       VALIDATING USER STORIES  END      #########################################
    
    
    

    
