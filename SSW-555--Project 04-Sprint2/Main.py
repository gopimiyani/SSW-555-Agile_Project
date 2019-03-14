#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:48:53 2019

@author: gopi
"""

import GedcomParser
import StoryValidation
import UnitTest


##############################       MAIN METHOD START    ########################################

#FILENAME = 'SSW-555-Agile-Project-01_UserStories.ged'
FILENAME='My-Family_EditedByGopi_Errors.ged'
if __name__ == '__main__':
   
    individuals, families = GedcomParser.gedcomParser(FILENAME)
    StoryValidation.story_validation(individuals, families)
    UnitTest.unittest.main()


##############################       MAIN METHOD END    #########################################

