#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:47:44 2019

@author: gopi
"""

##############################       UNIT TEST  START      #########################################

#from gedcomParser import gedcomParser
import os
import unittest
import GedcomParser
import UserStories
cur_path = os.path.dirname(__file__)

passFile = "SSW-555-Agile-Project-01_UserStories.ged"
#failFile = "SSW-555-Agile-Project-01_UserStories_Err.ged"
#failFile="My-Family_EditedByGopi_Errors.ged"
failFile= "Family-sprin2-error.ged"

class test_UserStories(unittest.TestCase):
    
# ------------------------------- TESTING US_01 -------------------------------------
    def test_US01(self):
        print("\n======================Performing Unit test on User Stories ================\n")
        print('TESTING US_01...')
        individuals, families = GedcomParser.gedcomParser(failFile)
        self.assertEqual(UserStories.US01_dates_before_currentDate(individuals,families), False)
    
# ------------------------------- TESTING US_02 -------------------------------------
    def test_US02(self):
        print("\n============================== Performing Unit test on User Stories ================================\n")
        print('\nTesting US_02...')
        individuals, families = GedcomParser.gedcomParser(passFile)
        self.assertEqual(UserStories.US02_birth_before_marriage(individuals,families), True)
        individuals, families = GedcomParser.gedcomParser(failFile)
        self.assertEqual(UserStories.US02_birth_before_marriage(individuals,families), False)

# ------------------------------- TESTING US_03 -------------------------------------

    def test_US03(self):
        print('\nTesting US_03...')
        individuals = GedcomParser.gedcomParser(passFile)
        self.assertEqual(UserStories.US03_birth_before_death(individuals), True)
        individuals = GedcomParser.gedcomParser(failFile)
        self.assertEqual(UserStories.US03_birth_before_death(individuals), False)
     # ------------------------------- TESTING US_04 -------------------------------------
    def test_US04(self):
        print('\nTesting US_04...')
        families = GedcomParser.gedcomParser(failFile)
        #self.assertTrue(US04_marriage_before_divorce(families))
        self.assertNotEqual(UserStories.US04_marriage_before_divorce(families), True)

    # --------------------------- TESTING US_05 -------------------------------------------

    def test_US05(self):
        print('\nTesting US_05...')
        individuals, families = GedcomParser.gedcomParser(passFile)
        #self.assertFalse(US05_marriage_before_death(individuals, families))
        #self.assertContains(response, 'pagination', html=True)
        self.assertNotEqual(UserStories.US05_marriage_before_death(
            individuals, families), True)
 # --------------------------- TESTING US_06 -------------------------------------------

    def test_US06(self):
        print('\nTesting US_06...')
        individuals, families = GedcomParser.gedcomParser(passFile)
        self.assertTrue(UserStories.US06_Divorce_before_death(individuals, families))
        individuals, families = GedcomParser.gedcomParser(failFile)
        self.assertFalse(UserStories.US06_Divorce_before_death(individuals, families))
        
# --------------------------- TESTING US_07 -------------------------------------------
    def test_US07(self):
        print('\nTesting US_07...')
        individuals = GedcomParser.gedcomParser(passFile)
        self.assertTrue(UserStories.US07(individuals))
        individuals = GedcomParser.gedcomParser(failFile)
        self.assertFalse(UserStories.US07(individuals))
    

# --------------------------- TESTING US_08 -------------------------------------------
        
    def test_US08(self):
        print("\n======================Performing Unit test on User Stories ================\n")
        print('TESTING US_08...')
        individuals, families = GedcomParser.gedcomParser(failFile)
        self.assertEqual(UserStories.US08_childbirth_after_marriage(individuals,families), False)
        
# ------------------------------- TESTING US_09 -------------------------------------

    def test_US09(self):
        print("\n======================Performing Unit test on User Stories ================\n")
        print('TESTING US_09...')
        individuals, families = GedcomParser.gedcomParser(passFile)
        self.assertEqual(UserStories.US09_birth_before_death_of_parents(individuals,families), True)
        individuals, families = GedcomParser.gedcomParser(failFile)
        self.assertEqual(UserStories.US09_birth_before_death_of_parents(individuals,families), False)
        
# --------------------------- TESTING US_10 ------------------------------------------
    def test_US10(self):
        print("\n======================Performing Unit test on User Stories ================\n")
        print('TESTING US_10...')
        individuals, families = GedcomParser.gedcomParser(failFile)
        self.assertEqual(UserStories.US10_marriage_age_14(individuals,families), True)    
# --------------------------- TESTING US_11 -------------------------------------------
    
    def test_US11(self):
        print("\n======================Performing Unit test on User Stories ================\n")
        print('TESTING US_11...')
        individuals, families = GedcomParser.gedcomParser(failFile)
        self.assertEqual(UserStories.US11_no_bigamy(individuals,families), True)    
        
# --------------------------- TESTING US_12 -------------------------------------------NEW AFTER REFACTORING
        
    def test_US12_NEW(self):
        print('\nTesting US_12...')
        individuals, families = GedcomParser.gedcomParser(passFile)
        self.assertTrue(UserStories.US12_parents_not_too_old(individuals,families))
        individuals, families = GedcomParser.gedcomParser(failFile)
        self.assertFalse(UserStories.US12_parents_not_too_old(individuals,families))

# --------------------------- TESTING US_13 -------------------------------------------NEW AFTER REFACTORING
        
    def test_US13_NEW(self):
        print('\nTesting US_13...')
        individuals, families = GedcomParser.gedcomParser(passFile)
        self.assertTrue(UserStories.US13_siblings_spacing(individuals,families))
        individuals, families = GedcomParser.gedcomParser(failFile)
        self.assertFalse(UserStories.US13_siblings_spacing(individuals,families))
        
# --------------------------- TESTING US_14 -------------------------------------------
    def test_US14(self):
        print('TESTING US_14...')
        individuals, families = GedcomParser.gedcomParser(passFile)
        self.assertTrue(UserStories.US14_Multiple_births(individuals, families))
        individuals, families = GedcomParser.gedcomParser(failFile)
        self.assertFalse(UserStories.US14_Multiple_births(individuals, families))

# --------------------------- TESTING US_15 -------------------------------------------
    def test_US15(self):
        print('TESTING US_15...')
        families = GedcomParser.gedcomParser(passFile)
        self.assertTrue(UserStories.US15_Fewer_than_15_siblings(families))
        families = GedcomParser.gedcomParser(failFile)
        self.assertFalse(UserStories.US15_Fewer_than_15_siblings(families))
                
# ------------------------------- TESTING US_31 -------------------------------------
    def test_US31(self):
        print("\n======================Performing Unit test on User Stories ================\n")
        print('TESTING US_31...')
        individuals = GedcomParser.gedcomParser(passFile)
        self.assertEqual(UserStories.US31_List_living_single(individuals), True)
        individuals = GedcomParser.gedcomParser(failFile)
        self.assertEqual(UserStories.US31_List_living_single(individuals), False)     
        


##############################       UNIT TEST  END      #########################################

##############################       MAIN METHOD START    ########################################

#FILENAME = 'SSW-555-Agile-Project-01_UserStories_Err.ged'
#FILENAME='My-Family_EditedByGopi_Errors.ged'
FILENAME='Family-sprin2-error.ged'
if __name__ == '__main__':
   
    individuals, families = GedcomParser.gedcomParser(FILENAME)
    unittest.main()


##############################       MAIN METHOD END    #########################################





