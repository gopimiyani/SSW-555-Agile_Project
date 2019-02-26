#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Gopi Miyani
         Deep Chokshi
         Krutarth Trivedi
         Dhaval Dongre
"""

import sys
from datetime import date
from datetime import datetime

from prettytable import PrettyTable
FILENAME = 'SSW-555-Agile-Project-01_UserStories.ged'
#FILENAME='My-Family-27-Jan-2019-216.ged'

x = PrettyTable()
y = PrettyTable()

allValidTags = ['NAME', 'SEX', 'FAMS', ' FAMC', 'MARR', 'BIRT', 'WIFE', 'HUSB', 'CHIL', 'DEAT', 'DIV', 'DATE', 'HEAD','TRLR', 'NOTE','INDI', 'FAM']



class gedcomFileReadLine(object):

    def __init__(self, line):
        self.level = 'NA' 
        self.tag = 'NA' 
        self.arg = 'NA' 
        self.ref = 'NA' 

        listLine = line.split(' ',)
        # set level of the object
        self.level = int(listLine[0])

        # for setting tag and argument
        if self.level > 0:
            self.tag = listLine[1]
            self.arg = listLine[2:]

        if self.level == 0:
            if listLine[1] in allValidTags:
                self.tag = listLine[1]
                self.arg = None
            else:
                self.tag = listLine[2]
                self.ref = listLine[1]


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
      


# ---------------------- GEDCOM PARSER (PARSING GEDCOM FILE) ---------------------
def gedcomParser(filename):
   
    gedcomList = []
    individualList = []
    familyList = []
   
    lines = [line.rstrip('\n\r') for line in open(filename)]

 
    for line in lines:
        current_gedcom = gedcomFileReadLine(line)
        gedcomList.append(current_gedcom)

    for index, gedcomline in enumerate(gedcomList):
       
        #------------------------- INDIVDIUAL -------------------------------
        if gedcomline.tag == 'INDI':

            date_type = None
            individualObject = individualClass(gedcomline.ref)

            for gedline in gedcomList[index + 1:]:
                if gedline.level == 0:
                    break
                if gedline.tag == "NAME":
                    individualObject.name = gedline.arg
                if gedline.tag == "SEX":
                    individualObject.gender = gedline.arg[0]
                if gedline.tag == "BIRT":
                    date_type = "BIRT"
                if gedline.tag == "DEAT":
                    date_type = "DEAT"
                if gedline.tag == "FAMC":
                    individualObject.famc.append(gedline.arg[0])
                if gedline.tag == "FAMS":
                    individualObject.fams.append(gedline.arg[0])

              
                if gedline.tag == 'DATE':
                    if date_type == 'BIRT':
                        individualObject.birthday = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])
                        )
                        date_type = None

                        Y=US07(gedline.arg)

                        if Y == "true":
                            print ("valid age")
                        else:
                            print ("unvalid age")

                    elif date_type == 'DEAT':
                        individualObject.deathDate = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])
                        )
                        individualObject.alive = False
                        date_type = None

           
            individualList.append(individualObject)

        #------------------------- FAMILY ------------------------------
        if gedcomline.tag == 'FAM':

            date_type = None
            familyObject = familyClass(gedcomline.ref)
            for gedline in gedcomList[index + 1:]:
                if gedline.level == 0:
                    break
                if gedline.tag == "MARR":
                    date_type = "MARR"
                if gedline.tag == "DIV":
                    date_type = "DIV"
                if gedline.tag == "HUSB":
                    familyObject.husbandID = gedline.arg[0]
                    for individual in individualList:
                        if individual.uid == gedline.arg[0]:
                            familyObject.husbandName = individual.name
                if gedline.tag == "WIFE":
                    familyObject.wifeID = gedline.arg[0]
                    for individual in individualList:
                        if individual.uid == gedline.arg[0]:
                            familyObject.wifeName = individual.name
                if gedline.tag == "CHIL":
                    familyObject.children.append(gedline.arg[0])
              
                if gedline.tag == "DATE":
                    if date_type == "MARR":
                        familyObject.married = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0]))
                        date_type = None

                    elif date_type == "DIV":
                        familyObject.divorced = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0]))
                        date_type = None
                        
          
            
            familyList.append(familyObject)
            '''
            print('********** INDIVIDUAL LIST *********')
            print(individualList)
            print('*********** FAMILY LIST *************')
            print(familyList)
            '''
    return individualList, familyList




# ---------------------- PRINT INDIVIDUAL AND FAMILY LIST ------------------------
def printPrettyTable(individual, families):
    print("\nIndividuals")
   
    x.field_names = ["ID","Name","Gender","Birthday","Alive","Death","Child","Spouse"]
    for line in individual:
        attrs = vars(line)
        x.add_row(attrs.values())
    print(x)
    
    print("\nFamilies")
    y.field_names = ["ID","Married","Divorced","Husband ID","Husband Name","Wife ID","Wife Name","Children"]
    for line in families:
        attrs = vars(line)
        y.add_row(attrs.values())
    print(y)


# ----------------------------- User story 7 ------------------------------------
def US07(arg):
    #print(arg[2]+" "+arg[1]+" "+arg[0])
    x = datetime.now()
    a = int(x.strftime("%Y")) - int(arg[2])
    
    if (arg[1]=="JAN"):
        b=1
    elif(arg[1]=="FEB"):
        b=2
    elif(arg[1]=="MAR"):
        b=3
    elif(arg[1]=="APR"):
        b=4
    elif(arg[1]=="MAY"):
        b=5
    elif(arg[1]=="JUN"):
        b=6
    elif(arg[1]=="JUL"):
        b=7
    elif(arg[1]=="AUG"):
        b=8
    elif(arg[1]=="SEP"):
        b=9
    elif(arg[1]=="OCT"):
        b=10
    elif(arg[1]=="NOV"):
        b=11
    elif(arg[1]=="DEC"):
        b=12
                            
    if (b>int(x.strftime("%m"))) and arg[0]>x.strftime("%d"):
        age = a                       
    else:
        age=a-1

    if age<150:
        return "true"
    else:
        return "false"


# ----------------------------- MAIN METHOD -------------------------------------
def main():
    

    individual=[]
    families=[]
    individual, families = gedcomParser(FILENAME)
    printPrettyTable(individual, families)



if __name__ == '__main__':
    #sys.stdout = open("SSW-555_DDGK_Project3_Output.txt","w")
    main()
    #sys.__stdout__.close()
