#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################       UNIT TEST  START      #########################################

#from gedcomParser import gedcomParser
import os
import unittest
import GedcomParser
import UserStories
cur_path = os.path.dirname(__file__)


class test_UserStories(unittest.TestCase):
    print("\n=============================================== Performing Unit test on User Stories ==============================================\n")
# ------------------------------- TESTING US_01 -------------------------------------
    def test_US01(self):
     
        print('TESTING US_01...\n')
        individuals, families = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US01_dates_before_currentDate(individuals,families), False)
  
# ------------------------------- TESTING US_02 -------------------------------------
    def test_US02(self):
       
        print('\nTesting US_02...\n')
        #individuals, families = GedcomParser.gedcomParser(passFile)
        #self.assertEqual(UserStories.US02_birth_before_marriage(individuals,families), True)
        individuals, families = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US02_birth_before_marriage(individuals,families), False)

# ------------------------------- TESTING US_03 -------------------------------------

    def test_US03(self):
        print('\nTesting US_03...\n')
        #individuals = GedcomParser.gedcomParser(passFile)
        #self.assertEqual(UserStories.US03_birth_before_death(individuals), True)
        individuals, families  = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US03_birth_before_death(individuals), False)
     # ------------------------------- TESTING US_04 -------------------------------------
    def test_US04(self):
        print('\nTesting US_04...\n')
        individuals, families  = GedcomParser.gedcomParser()
        #self.assertTrue(US04_marriage_before_divorce(families))
        self.assertNotEqual(UserStories.US04_marriage_before_divorce(families), True)

    # --------------------------- TESTING US_05 -------------------------------------------

    def test_US05(self):
        print('\nTesting US_05...\n')
        individuals, families = GedcomParser.gedcomParser()
        #self.assertFalse(US05_marriage_before_death(individuals, families))
        #self.assertContains(response, 'pagination', html=True)
        self.assertNotEqual(UserStories.US05_marriage_before_death(individuals, families), True)
 # --------------------------- TESTING US_06 -------------------------------------------

    def test_US06(self):
        print('\nTesting US_06...\n')
        #individuals, families = GedcomParser.gedcomParser(passFile)
        #self.assertTrue(UserStories.US06_Divorce_before_death(individuals, families))
        individuals, families = GedcomParser.gedcomParser()
        self.assertFalse(UserStories.US06_Divorce_before_death(individuals, families))
        
# --------------------------- TESTING US_07 -------------------------------------------
    def test_US07(self):
        print('\nTesting US_07...\n')
        #individuals = GedcomParser.gedcomParser(passFile)
        #self.assertTrue(UserStories.US07(individuals))
        individuals, families  = GedcomParser.gedcomParser()
        self.assertFalse(UserStories.US07(individuals))

# --------------------------- TESTING US_08 -------------------------------------------
        
    def test_US08(self):
        print('\nTESTING US_08...\n')
        individuals, families = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US08_childbirth_after_marriage(individuals,families), False)
        
# ------------------------------- TESTING US_09 -------------------------------------

    def test_US09(self):
        print('\nTESTING US_09...\n')
        #individuals, families = GedcomParser.gedcomParser(passFile)
        #self.assertEqual(UserStories.US09_birth_before_death_of_parents(individuals,families), True)
        individuals, families = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US09_birth_before_death_of_parents(individuals,families), False)
        
# --------------------------- TESTING US_10 ------------------------------------------
    def test_US10(self):
        print('\nTESTINGTESTING US_10...\n')
        individuals, families = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US10_marriage_age_14(individuals,families), False)    
# --------------------------- TESTING US_11 -------------------------------------------
    
    def test_US11(self):
       
        print('\nTESTING US_11...\n')
        individuals, families = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US11_no_bigamy(individuals,families), True)    
        
# --------------------------- TESTING US_12 -------------------------------------------NEW AFTER REFACTORING
        
    def test_US12_NEW(self):
        print('\nTesting US_12...\n')
        #individuals, families = GedcomParser.gedcomParser(passFile)
        #self.assertTrue(UserStories.US12_parents_not_too_old(individuals,families))
        individuals, families = GedcomParser.gedcomParser()
        self.assertFalse(UserStories.US12_parents_not_too_old(individuals,families))

# --------------------------- TESTING US_13 -------------------------------------------NEW AFTER REFACTORING
        
    def test_US13_NEW(self):
        print('\nTesting US_13...\n')
        #individuals, families = GedcomParser.gedcomParser(passFile)
        #self.assertTrue(UserStories.US13_siblings_spacing(individuals,families))
        individuals, families = GedcomParser.gedcomParser()
        self.assertFalse(UserStories.US13_siblings_spacing(individuals,families))
        
# --------------------------- TESTING US_14 -------------------------------------------
    def test_US14(self):
        print('\nTESTING US_14...v')
        #individuals, families = GedcomParser.gedcomParser(passFile)
        #self.assertTrue(UserStories.US14_Multiple_births(individuals, families))
        individuals, families = GedcomParser.gedcomParser()
        self.assertFalse(UserStories.US14_Multiple_births(individuals, families))

# --------------------------- TESTING US_15 -------------------------------------------
    def test_US15(self):
        print('\nTESTING US_15...\n')
        #families = GedcomParser.gedcomParser(passFile)
        #self.assertTrue(UserStories.US15_Fewer_than_15_siblings(families))
        individuals, families  = GedcomParser.gedcomParser()
        self.assertFalse(UserStories.US15_Fewer_than_15_siblings(families))
                
# ------------------------------- TESTING US_31 -------------------------------------
    def test_US31(self):
        
        print('\nTESTING US_31...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US31_List_living_single(individuals),False)     

# ------------------------------- TESTING US_16 -------------------------------------
    def test_US16(self): 
        print('\nTESTING US_16...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US16_Male_last_names_should_be_same(individuals,families),False)


# ------------------------------- TESTING US_18 -------------------------------------
    def test_US18(self):
        print('\nTESTING US_18...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US18_no_sibling_should_marry_eachother(individuals, families),False)


# ------------------------------- TESTING US_19 -------------------------------------
    def test_US19(self):
        print('\nTESTING US_19...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US19_first_cousins(individuals,families),False)
        
# ------------------------------- TESTING US_20 -------------------------------------
    def test_US20(self):
        print('\nTESTING US_19...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US20_aunts_and_uncles(individuals,families),False)

# ------------------------------- TESTING US_21 -------------------------------------
    def test_US21(self):
        print('\nTESTING US_21...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US21_Correct_gender_for_role(individuals, families),False)

# ------------------------------- TESTING US_20 -------------------------------------
    def test_US22(self):
       
        print('\nTESTING US_22...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US22_Unique_IDs(individuals, families),False)


# ------------------------------- TESTING US_23 -------------------------------------
    def test_US23(self):
       
        print('\nTESTING US_23...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US23_Unique_name_birth_date(individuals,families),False)
        
# ------------------------------- TESTING US_24 -------------------------------------
    def test_US24(self):
       
        print('\nTESTING US_24...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US24_Unique_families_by_spouses(families),False)
        
# ------------------------------- TESTING US_25 -------------------------------------
    def test_US25(self):
       
        print('\nTESTING US_25...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US25_Unique_firstnames_families(individuals,families),False)
        self.assertIsNotNone(UserStories.US25_Unique_firstnames_families(individuals,families))
# ------------------------------- TESTING US_35 -------------------------------------
    def test_US35(self):
       
        print('\nTESTING US_35...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertFalse(UserStories.US35_list_recent_births(individuals))
        self.assertIsNot(UserStories.US35_list_recent_births(individuals),True)
# ------------------------------- TESTING US_38 -------------------------------------
    def test_US38(self):
       
        print('\nTESTING US_38...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertFalse(UserStories.US38_List_upcoming_birthdays(individuals))

# ------------------------------- TESTING US_39 -------------------------------------
    def test_US39(self):
       
        print('\nTESTING US_39...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertEqual(UserStories.US39_List_upcoming_marriage_anniversary(individuals,families), False)
# ------------------------------- TESTING US_27 -------------------------------------
    def test_US27(self):
       
        print('\nTESTING US_27...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertIsNot(UserStories.US27_List_individual_current_ages(individuals,families),None)
        self.assertEqual(UserStories.US27_List_individual_current_ages(individuals,families), False)
# ------------------------------- TESTING US_36 -------------------------------------
    def test_US36(self):
       
        print('\nTESTING US_36...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertFalse(UserStories.US36_List_recent_deaths(individuals,families))
        self.assertIsNotNone(UserStories.US36_List_recent_deaths(individuals,families))

# ------------------------------- TESTING US_31 -------------------------------------
    def test_US30(self):

        print('\nTESTING US 31...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertFalse(UserStories.US30_List_living_married(individuals, families))


# ------------------------------- TESTING US_33 -------------------------------------
    def test_US33(self):

        print('\nTESTING US 33...\n')
        individuals, families  = GedcomParser.gedcomParser()
        self.assertFalse(UserStories.US33_List_orphans(individuals, families))
        self.assertIsNot(UserStories.US33_List_orphans(individuals,families),True)
##############################       UNIT TEST  END      #########################################


##############################       MAIN METHOD START    ########################################

if __name__ == '__main__':
   
    individuals, families = GedcomParser.gedcomParser()
    unittest.main()


##############################       MAIN METHOD END    #########################################
