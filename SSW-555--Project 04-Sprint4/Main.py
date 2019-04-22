#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:48:53 2019

@author: gopi
"""

import GedcomParser
import StoryValidation



##############################       MAIN METHOD START    ########################################


if __name__ == '__main__':
   
    individuals, families = GedcomParser.gedcomParser()
    GedcomParser.printPrettyTable(individuals,families)
    StoryValidation.story_validation(individuals, families)
    


##############################       MAIN METHOD END    #########################################

 