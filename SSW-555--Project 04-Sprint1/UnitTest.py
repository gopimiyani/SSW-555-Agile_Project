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
failFile = "SSW-555-Agile-Project-01_UserStories_Err.ged"


class test_UserStories(unittest.TestCase):
# ------------------------------- TESTING US_02 -------------------------------------
    def test_US02(self):
        print("\n======================Performing Unit test on User Stories ================\n")
        print('TESTING US_02...')
        individuals, families = GedcomParser.gedcomParser(passFile)
        self.assertEqual(UserStories.US02_birth_before_marriage(individuals,families), True)
        individuals, families = GedcomParser.gedcomParser(failFile)
        self.assertEqual(UserStories.US02_birth_before_marriage(individuals,families), False)

# ------------------------------- TESTING US_03 -------------------------------------

    def test_US03(self):
        print('TESTING US_03...')
        individuals, families = GedcomParser.gedcomParser(passFile)
        self.assertEqual(UserStories.US03_birth_before_death(individuals), True)
        individuals, families = GedcomParser.gedcomParser(failFile)
        self.assertEqual(UserStories.US03_birth_before_death(individuals), False)
     # ------------------------------- TESTING US_04 -------------------------------------
    def test_US04(self):
        print('TESTING US_04...')
        individuals, families = GedcomParser.gedcomParser(failFile)
        #self.assertTrue(US04_marriage_before_divorce(families))
        self.assertNotEqual(UserStories.US04_marriage_before_divorce(families), True)

    # --------------------------- TESTING US_05 -------------------------------------------

    def test_US05(self):
        print('TESTING US_05...')
        individuals, families = GedcomParser.gedcomParser(passFile)
        #self.assertFalse(US05_marriage_before_death(individuals, families))
        #self.assertContains(response, 'pagination', html=True)
        self.assertNotEqual(UserStories.US05_marriage_before_death(
            individuals, families), True)
 # --------------------------- TESTING US_05 -------------------------------------------

    def test_US06(self):
        print('TESTING US_06...')
        individuals, families = GedcomParser.gedcomParser(passFile)
        self.assertTrue(UserStories.US06_Divorce_before_death(individuals, families))
        individuals, families = GedcomParser.gedcomParser(failFile)
        self.assertFalse(UserStories.US06_Divorce_before_death(individuals, families))

    def test_US07(self):
        print('TESTING US_07...')
        individuals, families = GedcomParser.gedcomParser(passFile)
        self.assertTrue(UserStories.US07(individuals))
        individuals, families = GedcomParser.gedcomParser(failFile)
        self.assertFalse(UserStories.US07(individuals))
    


##############################       UNIT TEST  END      #########################################
