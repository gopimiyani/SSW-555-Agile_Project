#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:53:49 2019
@author: Krutarth
         Deep
         Gopi
         Dhaval
"""


from datetime import datetime
from UDFunctions import getAge ,getChilds,getBirthdate,dates_within,getFamily, getIndividiual
from datetime import date,timedelta


##############################       FUNCTIONS  START      #######################################

#print(dates_within(datetime.strptime('2018-05-04',"%Y-%m-%d"), datetime.strptime('2011-05-04',"%Y-%m-%d"), 0, 15, 'years'))    
##############################       FUNCTIONS  START      #######################################
"""
    # Sprint 1
    Story ID	Story-Name	                            Owner
        US01	Dates before current date	           Dhaval
        US02	Birth before marriage	               Krutarth
        US03	Birth before death	                   Krutarth
        US04	Marriage before divorce	               Gopi
        US05	Marriage before death	               Gopi
        US06	Divorce before death	                   Deep
        US07	Less then 150 years old	               Deep
        US08	Birth before marriage of parents	       Dhaval


        #Sprint 2
        US09	Birth before death of parents	      Krutarth
        US10	Marriage after 14	                  Dhaval
        US11	No bigamy	                          Dhaval
        US12	Parents not too old	                  Gopi
        US13	Siblings spacing	                      Gopi
        US14	Multiple births <= 5	                  Deep
        US15	Fewer than 15 siblings	              Deep
        US31	List living single	                  Krutarth

        #Sprint 3
        US16	Male last names	                       Krutarth
        US18	Siblings should not marry              Krutarth
        US19	First cousins should not marry	       Gopi
        US20	Aunts and uncles	                       Gopi
        US21	Correct gender for role	               Deep
        US22	Unique IDs	                           Deep
        US23	Unique name and birth date	           Dhaval
        US24	Unique families by spouses	           Dhaval

        # Sprint 4
        US24	Unique families by spouses	             Dhaval
        US36	List recent deaths	                     Dhaval
        US25	Unique first names in families	         Gopi
        US35	List recent births	                     Gopi
        US38	List upcoming birthdays	                 Krutarth
        US39	List upcoming anniversaries	             Krutarth
        US30	List living married	                     Deep
        US33	List orphans	                             Deep

"""
##############################       IMPLEMENTING  USER STORIES  START      #######################################

#------------------------------------ US 01 START [Dhaval]--------------------------------
def US01_dates_before_currentDate(individuals,families):
    return_flag = True
    error_type = "US01"
    today=date.today()
    #print("yoyoyoyoyo")
    print("\nError     User Story                            Description                                    "
    "                             Location")
    print(('-' * 150)) 
                                   
    for family in families:   
        if family.married != 'NA':
           if family.married > today: 
                error_descrip = "Marriage date (" + str(family.married) + \
                    ") should not occur after today (" + str(today)+")" 
                error_location = [family.uid, family.husbandID, family.wifeID]
                report_error('ERROR',error_type, error_descrip, error_location)
                return_flag = False
                
        if family.divorced!="NA":
            if family.divorced>today: 
                    error_descrip = "Divorce date (" + str(family.divorced) + \
                        ") should not occur after today (" + str(today)+")" 
                    error_location = [family.uid, family.husbandID, family.wifeID]
                    report_error('ERROR',error_type, error_descrip, error_location)
                    return_flag = False                

    for individual in individuals:   
        if individual.birthday!='NA':
                
            if individual.birthday > today: 
                error_descrip = "Birthday date (" + str(individual.birthday) + \
                    ") should not occur after today (" + str(today)+")" 
                error_location = [individual.uid]
                report_error('ERROR',error_type, error_descrip, error_location)
                return_flag = False
                
        if individual.deathDate!='NA':
            if individual.deathDate > today: 
                    error_descrip = "Death date (" + str(individual.deathDate) + \
                        ") should not occur after today (" + str(today)+")" 
                    error_location = [individual.uid]
                    report_error('ERROR',error_type, error_descrip, error_location)
                    return_flag = False                
    return return_flag
#------------------------------------ US 01 END ------------------------------------------
#------------------------------------ US 02 START [Krutarth]------------------------------
## US02 All BIRTH DATES MUST BE BEFORE MARRIAGE 
def US02_birth_before_marriage(individuals,families):
    return_flag = True
    error_type = "US02"
    for family in families:
        if family.married != 'NA':
            husband = family.husbandID
            wife = family.wifeID
            for individual in individuals:                  
                if individual.uid == wife:
                   if individual.birthday!='NA' and family.married!='NA':
                        if individual.birthday > family.married:
                            error_descrip = "Birth of wife (" + str(individual.birthday) + ") occurs before her marriage (" +str(family.married)+")"
                            error_location = [wife]
                            report_error('ERROR',error_type, error_descrip, error_location)
                            return_flag = False
                if individual.uid == family.husbandID:
                    if individual.birthday!='NA' and family.married!='NA':
                        if individual.birthday > family.married:
                            error_descrip = "Birth of Husband ("+str(individual.birthday)+") occurs before his marriage ("+str(family.married)+")"
                            error_location = [husband]
                            report_error('ERROR',error_type, error_descrip, error_location)
                            return_flag = False
    return return_flag
#------------------------------------ US 02 END ------------------------------------------
#------------------------------------ US 03 START [Krutarth]------------------------------
## US03 All BIRTH DATES MUST BE BEFORE DEATH DATE
def US03_birth_before_death(individuals):
    return_flag = True
    error_type = "US03"
    for individual in individuals:   
        if individual.deathDate!='NA' and individual.birthday!='NA':
            if individual.birthday > individual.deathDate: 
                error_descrip = "Death (" + str(individual.deathDate) + ") occurs before Birthday (" +str(individual.birthday)+")" 
                error_location = [individual.uid]
                report_error('ERROR',error_type, error_descrip, error_location)
                return_flag = False
    return return_flag
#------------------------------------ US 03 END -----------------------------------------
#------------------------------------ US 04 START [Gopi]---------------------------------
## US04 All MARRIAGE DATES MUST BE BEFORE DIVORCE DATE
def US04_marriage_before_divorce(families):
    return_flag = True
    error_type = "US04"
    for family in families:
        if family.married != 'NA' and family.divorced != 'NA':
            if family.married > family.divorced:
                error_descrip = "Divorce (" + str(family.divorced) + \
                    ") occurs before marriage (" + str(family.married)+")"
                error_location = [family.uid, family.husbandID, family.wifeID]
                report_error('ERROR', error_type,
                             error_descrip, error_location)
                return_flag = False
    return return_flag
#------------------------------------ US 04 END ------------------------------------------
#------------------------------------ US 05 START [Gopi]-----------------------------------------
## US05 All MARRIAGE DATES MUST BE BEFORE DEATH DATE
def US05_marriage_before_death(individuals, families):
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
            if wife != None:
                if wife.alive == False:
                    if family.married!='NA' and wife.deathDate!='NA':
                        if family.married > wife.deathDate:
                            error_descrip = "Death of wife (" + str( wife.deathDate) + ") occurs before her marriage (" + str(family.married)+")"
                            error_location = [wife.uid]
                            report_error('ERROR', error_type,error_descrip, error_location)
                            return_flag = False
            if husband != None:
                if husband.alive == False:
                    if family.married!='NA' and husband.deathDate!='NA':
                        if family.married > husband.deathDate:
                            error_descrip = "Death of Husband ("+str(husband.deathDate)+") occurs before his marriage ("+str(family.married)+")"
                            error_location = [husband.uid] 
                            report_error('ERROR', error_type,error_descrip, error_location)
                            return_flag = False
    return return_flag
#------------------------------------ US 05 END -------------------------------------------
#------------------------------------ US 06 START [Deep]-----------------------------------------
def US06_Divorce_before_death(individual, families):
    return_flag = True
    error_type = "US06"
    for line in families:

        if(line.divorced != 'NA'):
            for linei in individual:
                if line.husbandID == linei.uid:
                    if linei.deathDate == 'NA':
                        return_flag = True

                    else:
                        divorce = str(line.divorced).split('-')
                        d_Date = str(linei.deathDate).split('-')

                        if(int(d_Date[0])-int(divorce[0])) > 0:
                            return_flag = True

                        elif d_Date[0] == divorce[0] and (d_Date[1]-divorce[1]) > 0:
                            return_flag = True

                        elif d_Date[0] == divorce[0] and d_Date[1] == divorce[1] and (d_Date[2]-divorce[2]) > 0:
                            return_flag = True

                        else:
                            error_descrip = "Divorce after death"
                            error_location = [linei.uid]
                            report_error('ERROR', error_type,
                                         error_descrip, error_location)
                            return_flag = False

                if line.wifeID == linei.uid:
                    if linei.deathDate == 'NA':
                        return_flag = True
                    else:
                        divorce = str(line.divorced).split('-')
                        d_Date = str(linei.deathDate).split('-')
                        if(int(d_Date[0])-int(divorce[0])) > 0:
                            return_flag = True
                        elif d_Date[0] == divorce[0] and (d_Date[1]-divorce[1]) > 0:
                            return_flag = True

                        elif d_Date[0] == divorce[0] and d_Date[1] == divorce[1] and (d_Date[2]-divorce[2]) > 0:
                            return_flag = True
                        else:
                            error_descrip = "Divorce after death"
                            error_location = [linei.uid]
                            report_error('ERROR', error_type,error_descrip, error_location)
                            return_flag = False
    return return_flag
#------------------------------------ US 06 END -------------------------------------------
#------------------------------------ US 07 START [Deep]-----------------------------------------
def US07(individuals):
    return_flag = True
    error_type = "US07"
    for individual in individuals:
        birthDate = individual.birthday
        arg = birthDate
        x = datetime.now()
        if arg!='NA':
            a = int(x.strftime("%Y")) - int(arg.strftime("%Y"))
            arg1 = int(arg.strftime("%m"))
            if (arg1 > int(x.strftime("%m"))) and int(arg.strftime("%d")) > int(x.strftime("%d")):
                age = a
            else:
                age = a-1
    
            if age > 150:
                error_descrip = "Age is more than 150"
                error_location = [individual.uid]
                report_error('ERROR', error_type, error_descrip, error_location)
                return_flag = False
    return return_flag

#------------------------------------ US 07 END -------------------------------------------
#------------------------------------ US 08 START [Dhaval]---------------------------------
def US08_childbirth_after_marriage(individuals,families):
    return_flag = True
    error_type = "US08"
    for family in families:
        if family.married != 'NA' and family.children:
            for individual in individuals:                  
                if individual.uid in family.children:
                   if individual.birthday!='NA':
                        if individual.birthday < family.married:
                            error_descrip = "Birth of child (" + str(individual.birthday) + ")"+str(individual.name)+ "cannot occur before marriage (" +str(family.married)+")"
                            error_location = [individual.uid,family.uid]
                            report_error('ERROR',error_type, error_descrip, error_location)
                            return_flag = False
    return return_flag
#------------------------------------ US 08 END ------------------------------------------
#------------------------------------ US 09 START [KRUTARTH]------------------------------
# US09 BIRTH BEFORE DEATH OF PARENTS
def US09_birth_before_death_of_parents(individuals, families):
   return_flag = True
   error_type = "US09"
   for family in families:
       husband = family.husbandID
       wife = family.wifeID
       children = family.children
       No_child = len(children)

       if No_child > 0:
           for child in children:
               for individual in individuals:
                   if husband == individual.uid:
                       dad_death = individual.deathDate
                   if wife == individual.uid:
                       mom_death = individual.deathDate
                   if child == individual.uid:
                       child_birthday = individual.birthday
               if dad_death != 'NA' and mom_death != 'NA' and child_birthday != 'NA':
                   if child_birthday > dad_death or child_birthday > mom_death:
                       error_descrip = "Death occurs before Birthday"
                       error_location = [individual.uid]
                       report_error('ERROR', error_type,
                                    error_descrip, error_location)
                       return_flag = False

               elif dad_death != 'NA' and mom_death == 'NA'and child_birthday != 'NA':
                   if child_birthday > dad_death:
                       error_descrip = "Death occurs before Birthday"
                       error_location = [individual.uid]
                       report_error('ERROR', error_type,
                                    error_descrip, error_location)
                       return_flag = False
               elif dad_death == 'NA' and mom_death != 'NA'and child_birthday != 'NA':
                   if child_birthday > mom_death:
                       error_descrip = "Death occurs before Birthday"
                       error_location = [individual.uid]
                       report_error('ERROR', error_type,
                                    error_descrip, error_location)
                       return_flag = False

   return return_flag
#------------------------------------ US 09 END -------------------------------------------
#------------------------------------ US 10 START [Dhaval]---------------------------------
def US10_marriage_age_14(individuals,families):
    return_flag = True
    error_type = "US10"
    for family in families:   
      if family.married != 'NA':
        for individual in individuals:
            if individual.uid==family.husbandID:
                return_flag =  not dates_within(getBirthdate(individual.uid),getFamily(individual.uid).married ,0,13,'years')
                if return_flag==True:
                    error_descrip = "Age during marriage less than 14 for husband! birth:"+str(getBirthdate(individual.uid))+" marriage:"+str(getFamily(individual.uid).married) 
                    error_location = [individual.uid]
                    report_error('ERROR',error_type, error_descrip, error_location)

        for individual in individuals:
            if individual.uid==family.wifeID:
                return_flag =  not dates_within(getBirthdate(individual.uid),getFamily(individual.uid).married ,0,13,'years')
                if return_flag==True:
                    error_descrip = "Age during marriage less than 14 for wife! birth"+str(getBirthdate(individual.uid))+" marriage:"+str(getFamily(individual.uid).married) 
                    error_location = [individual.uid]
                    report_error('ERROR',error_type, error_descrip, error_location)
                    return_flag = False
    return return_flag
#------------------------------------ US 10 END -------------------------------------------
#------------------------------------ US 11 START [Dhaval]---------------------------------
#Marriage should not occur during marriage to another spouse
def US11_no_bigamy(individuals,families):
    
    return_flag = True
    error_type = "US11"
    bigamy=[]
    check = []
    for family in families:
        if family.married:
            husband = None
            wife = None
            first_current_marriage = True
            first_marriage_start = family.married
            for indiv in individuals:
                if indiv.uid == family.husbandID:
                    husband = indiv
                if indiv.uid == family.wifeID:
                    wife = indiv
            if family.divorced!=None:
                first_current_marriage = False
                first_marriage_end=family.divorced


            else:
                if wife.alive == False and husband.alive == False:
                    if wife.deathDate < husband.deathDate:
                        first_marriage_end = wife.deathDate
                        first_current_marriage = False
                    else:
                        first_marriage_end = husband.deathDate
                        first_current_marriage = False
                else:
                    if wife.alive==False:
                        first_marriage_end=wife.deathDate
                        first_current_marriage = False
                    if husband.alive==False:
                        first_marriage_end=husband.deathDate
                        first_current_marriage = False

            # Search through individuals to get husband and wife
            for family2 in families:
                #find the spouse
                if family.married != family2.married:
                    if family2.married:
                        husband2 = None
                        wife2 = None
                        second_current_marriage = True
                        second_marriage_start = family2.married
                        for indiv1 in individuals:
                            if indiv1.uid == family2.husbandID:
                                husband2 = indiv1
                            if indiv1.uid == family2.wifeID:
                                wife2 = indiv1
                        if family2.divorced != None:
                            second_current_marriage = False
                            second_marriage_end = family2.divorced
                        else:
                            if wife2.alive==False and husband2.alive==False:
                                if wife2.deathDate<husband2.deathDate:
                                    second_marriage_end = wife2.deathDate
                                    second_current_marriage = False
                                else:
                                    second_marriage_end = husband2.deathDate
                                    second_current_marriage = False
                            else:
                                if wife2.alive == False:
                                    second_marriage_end = wife2.deathDate
                                    second_current_marriage = False
                                if husband2.alive == False:
                                    second_marriage_end = husband2.deathDate
                                    second_current_marriage = False
                        if husband.uid==husband2.uid or wife.uid==wife2.uid:

                            if first_current_marriage== True and second_current_marriage==True:
                                if husband.uid==husband2.uid:
                                    check.append((husband.uid))
                                    for element in check:
                                        if element not in bigamy:
                                            bigamy.append((husband.uid))
                                            error_descrip = "Bigamy Occurs in family"
                                            error_location = [family.uid ,family2.uid,husband.uid]
                                            report_error('ERROR',error_type, error_descrip, error_location)
                                            return_flag = False
                                if wife.uid==wife2.uid:
                                    check.append((wife.uid))
                                    for element in check:
                                        if element not in bigamy:
                                            bigamy.append((wife.uid))
                                            error_descrip = "Bigamy Occurs in family"
                                            error_location = [family.uid ,family2.uid, wife.uid]
                                            report_error('ERROR',error_type, error_descrip, error_location)
                                            return_flag = False
                            else:
                                if first_marriage_start!='NA' and second_marriage_start!='NA':
                                    if first_marriage_start > second_marriage_start:
                                        s_m_s = first_marriage_start
                                        f_m_s = second_marriage_start
                                        second_marriage_start=s_m_s
                                        first_marriage_start=f_m_s
                                        f_m_e=second_marriage_end
                                        second_marriage_end=first_marriage_end
                                        first_marriage_end=f_m_e

                                if first_marriage_end != None  and second_marriage_end!=None:
                                    if first_marriage_end!='NA' and second_marriage_start!='NA':
                                        if first_marriage_end > second_marriage_start :
                                            if husband.uid == husband2.uid:
                                                check.append((husband.uid))
                                                for element in check:
                                                    if element not in bigamy:
                                                        bigamy.append(( husband.uid))
                                                        error_descrip = "Bigamy Occurs in family"
                                                        error_location = [family.uid ,family2.uid ,husband.uid]
                                                        report_error(error_type, error_descrip, error_location)
                                                        return_flag = False
                                            if wife.uid == wife2.uid:
                                                check.append((wife.uid))
                                                for element in check:
                                                    if element not in bigamy:
                                                        bigamy.append(( wife.uid))
                                                        error_descrip = "Bigamy Occurs in families and the bigamist is "
                                                        error_location = [family.uid ,family2.uid, wife.uid]
                                                        report_error('ERROR',error_type, error_descrip, error_location)
                                                        return_flag = False

    return return_flag
   
#------------------------------------ US 11 END -------------------------------------------
    
#------------------------------------ US 12 START [GOPI]----------------------------------

## US12	Parents not too old	---Mother should be less than 60 years older than her children and father should be less than 80 years older than his children

def US12_parents_not_too_old(individuals, families):
    return_flag = True
    error_type = "US12"
    for family in families:
        birthday_husband=getBirthdate(family.husbandID)
        birthday_wife=getBirthdate(family.wifeID)
        childs=(family.children)
        birthday_childs={}
      
        for child in childs:
            birthday=getBirthdate(child)
            birthday_childs[child]=birthday
        
        for childID,childBirthday in birthday_childs.items():
                return_flag =  not dates_within(birthday_husband,childBirthday ,0,79,'years')
                if return_flag==False:
                    error_descrip = "Husband (Id,Age: " + family.husbandID + ', ' + str(getAge(family.husbandID)) + ") is >80 years than his children(Id,Age: " + childID + ', ' + str(getAge(childID)) + ')'
                    error_location = [family.husbandID]
                    report_error('ERROR',error_type, error_descrip, error_location)
                    return return_flag
                return_flag = not dates_within(birthday_wife,childBirthday,0,59,'years')
                if return_flag==False:
                    error_descrip = "Wife (Id,Age: "+ family.wifeID + ', '  + str(getAge(family.wifeID)) + ") is >60 years than her children (Id,Age: " + childID + ', ' + str(getAge(childID)) + ')'
                    error_location = [family.wifeID]
                    report_error('ERROR',error_type, error_descrip, error_location)
                    return return_flag
    return return_flag
#----------------------------------- US 12 END -------------------------------------------
#------------------------------------ US 13 START [GOPI]-----------------------------------
def US13_siblings_spacing(individuals, families):
    return_flag = True
    error_type = "US13"
    for family in families:
        childs=family.children
        birthdayOfChilds={}
        for individual in individuals:
            for child in childs:
                if child==individual.uid:
                    birthdayOfChilds[individual.uid]=getBirthdate(child)
        childslen=len(birthdayOfChilds)
        for i in range(0,childslen):
            for j in range (i+1,childslen):
                return_flag = dates_within(birthdayOfChilds[childs[i]],birthdayOfChilds[childs[j]],2,243,'days')
                if return_flag==False:
                    error_descrip = "Child (ID: " +str(childs[i])+", B'day: " +str(birthdayOfChilds[childs[i]]) + ") violates sibling spacing with (ID: " +str(childs[j]) +", B'day: " +str(birthdayOfChilds[childs[j]]) + ")"
                    error_location = [childs[i]]
                    report_error('ERROR',error_type, error_descrip, error_location)
                    return return_flag
    return return_flag

#------------------------------------ US 13 END ------------------------------------------
#------------------------------------ US 14 START [DEEP]----------------------------------
def US14_Multiple_births(individuals, families):
   return_flag = True
   error_type = "US14"
   for family in families:
       birthdays = []
       children = family.children
       Number_of_children = len(children)
       if Number_of_children > 5:
           for child in children:
               for individual in individuals:
                   if (child == individual.uid):
                       birthdays.append(individual.birthday)
           for birthC in birthdays:
               count = 1
               for birth1 in birthdays:
                   if birthC == birth1:
                       count = count + 1
               if count >= 5:
                   error_descrip = "Multiple births"
                   error_location = [family.uid]
                   report_error('ERROR', error_type,error_descrip, error_location)
                   return_flag = False
   return return_flag
#------------------------------------ US 14 END ------------------------------------------   
#------------------------------------ US 15 START [DEEP]----------------------------------
def US15_Fewer_than_15_siblings(families):
   return_flag = True
   error_type = "US15"
   for family in families:
       child = family.children
       Number_of_children = len(child)
       if Number_of_children > 15:
           error_descrip = "More than 15 siblings"
           error_location = [family.uid]
           report_error('ERROR', error_type, error_descrip, error_location)
           return_flag = False

   return return_flag
#------------------------------------ US 15 END -------------------------------------------
#------------------------------------ US 31 START [KRUTARTH]-------------------------------
# US31 List all living people over 30 who have never been married in a GEDCOM file
def US31_List_living_single(individuals):
    return_flag = True
    error_type = "US31"
    people=[]
    currentDate=datetime.now()
    for individual in individuals:
        birthDate = individual.birthday
        spouse = individual.fams
        name = individual.name[0]
        if birthDate!='NA':
            lifeSpan = int(currentDate.strftime("%Y")) - int(birthDate.strftime("%Y"))
            age = int(birthDate.strftime("%m"))
            if (age > int(currentDate.strftime("%m"))) and int(birthDate.strftime("%d")) > int(currentDate.strftime("%d")):
                age = lifeSpan
            else:
                age = lifeSpan-1
            if lifeSpan > 30:
               #if I put any condition in spouse(if conition) then it is showing that errors found
                if spouse:
                    pass
                else:
                   people.append(name)
    if people!=[]:
        error_descrip = "List of people who are un married is: " + str(people)
     
        report_list('LIST', error_type, error_descrip)
        return_flag = False   
    return return_flag 
   
#------------------------------------ US 31 END [KRUTARTH]-------------------------------
#------------------------------------ US 16 START [KRUTARTH] -------------------------------------------
#US16 All Male members of a family should have the same last name (surname)
def US16_Male_last_names_should_be_same(individuals,families):
    
    return_flag = True
    error_type = "US16"
    for families in families:
        if families.married:
            lastname = families.husbandName[1]
            for individual in individuals:
                id = individual.uid
                gender=individual.gender
                name=individual.name
                if id in families.children:
                    if gender == "M":
                        if lastname not in name:
                            error_descrip = "Lastname not the same as father " 
                            error_location = [individual.uid]
                            report_error('ERROR',error_type, error_descrip, error_location)
                            return_flag = False

    return return_flag
#------------------------------------ US 16 END [KRUTARTH]-------------------------------
    
#------------------------------------ US 18 START [KRUTARTH] -------------------------------------------
#US18 - Siblings should not marry one another

def US18_no_sibling_should_marry_eachother(individuals, families):
   return_flag = True
   error_type="US18"

   for family in families:
       siblingUid = family.children
       siblings = list(sameId for sameId in individuals if sameId.uid in siblingUid)

       for sibling in siblings:
           sib_fam = next((famId for famId in families if famId.husbandID == sibling.uid),None)

           if sib_fam and sib_fam.wifeID in siblingUid:
                return_flag = False
                error_descrip = "Sibling is married to another sibling" 
                error_location = [sibling.uid, sib_fam.wifeID]
                report_error('ERROR',error_type, error_descrip, error_location)
                                        

   return return_flag
#------------------------------------ US 18 END [KRUTARTH]------------------------------

#------------------------------------ US 19 START [GOPI]------------------------------- 
## US19	First cousins should not marry	First cousins should not marry one another    
def US19_first_cousins(individuals,families):
    
    return_flag = True
    error_type = "US19"
    family_childs={}
    family_uncles_aunts={}
    family_cousins={}
    for family in families:
        family_childs[family.uid]=family.children
    for family,childs in family_childs.items():
        for child in childs:
            for family1 in families:
                if child in family1.children:
                    family_uncles_aunts[family]=family1.children;
    for family,uncle_aunts in family_uncles_aunts.items():
        for f in families:
            if family==str(f.uid):
                
                family_cousins=f.children
    for family,childs in family_childs.items():
       
        for child in childs:
            for f in families:
                if child==str(f.husbandID) or child==str(f.wifeID):
                    husband=str(f.husbandID)
                    wife=str(f.wifeID)
                    if husband in family_cousins or wife in family_cousins:
                         return_flag = False
                         error_descrip =str(f.husbandName) +"married to his cousin " +str( f.wifeName )
                         error_location = [f.husbandID]
                         report_error('ERROR',error_type, error_descrip, error_location)
                         return return_flag
    return return_flag
    
#------------------------------------ US 19 END ------------------------------------------- 

#------------------------------------ US 20 START [GOPI]------------------------------- 
## US20	Aunts and uncles should not marry their nieces or nephews
def US20_aunts_and_uncles(individuals,families):
    return_flag = True
    error_type="US20"
    family_childs={}
    family_uncles_aunts={}
    for family in families:
        family_childs[family.uid]=family.children
    for family,childs in family_childs.items():
        for child in childs:
            for family1 in families:
                if child in family1.children:
                    family_uncles_aunts[family]=family1.children
    for family,childs in family_childs.items():
        for child in childs:
            for f in families:
                if child==str(f.husbandID) or child==str(f.wifeID):
                    husband=str(f.husbandID)
                    wife=str(f.wifeID)
                    if husband in family_uncles_aunts[family] or wife in family_uncles_aunts[family]:
                         return_flag = False
                         error_descrip =str(f.husbandName) +"married to his niece or nephew " +str( f.wifeName )
                         error_location = [f.husbandID]
                         report_error('ERROR',error_type, error_descrip, error_location)
                         return return_flag
    return return_flag
#------------------------------------ US 20 END ------------------------------------------- 
#------------------------------------ US 21 START [DEEP] -------------------------------------------
def US21_Correct_gender_for_role(individuals, families):
   return_flag = True
   error_type = "US21"
   for family in families:
       husbund=family.husbandID
       wife=family.wifeID

       for individual in individuals:
           if wife == individual.uid:
               genderWife=individual.gender

           elif husbund == individual.uid:
               genderHus = individual.gender

       if(genderWife == 'F' and genderHus == 'M'):
           pass
           #abc=1
         
       else:
           error_descrip = "Wrong gender for role"
           error_location = [family.uid]
           report_error('ERROR', error_type, error_descrip, error_location)
           return_flag = False

   return return_flag

#------------------------------------ US 21 END [DEEP]--------------------------------------
#------------------------------------ US 22 START -------------------------------------------
def US22_Unique_IDs(individuals, families):
   return_flag = True
   error_type = "US22"
   familyID = []
   for family in families:
       familyID.append(family.uid)

   for id in familyID:
       count = 0
       for id1 in familyID:
           if id == id1:
               count = count + 1

       if count > 1:
           error_descrip = "same id"
           error_location = id
           report_error('ERROR', error_type,error_descrip, error_location)
           return_flag = False


   individualID=[]
   for individual in individuals:
       individualID.append(individual.uid)


   for id in individualID:
       count = 0
       for id1 in individualID:
           if id == id1:
               count = count + 1

       if count > 1:
           error_descrip = "same id"
           error_location = id
           report_error('ERROR', error_type,error_descrip, error_location)
           return_flag = False
   return return_flag

#------------------------------------ US 22 END [DEEP]-------------------------------

#------------------------------------ US 23 START [DHAVAL]----------------------------------
def US23_Unique_name_birth_date(individuals,families):
   return_flag = True
   error_type = "US23"
   for individual in individuals:
       birthDate=individual.birthday
       name=individual.name
       for indi in individuals:
           if individual.uid!=indi.uid:
               if indi.name==name and indi.birthday==birthDate:
                   error_descrip = "Name and birth date same for different individuals"
                   error_location = [individual.uid,indi.uid]
                   report_error('ERROR', error_type, error_descrip, error_location)
                   return_flag = False

   return return_flag
#------------------------------------ US 23 END -------------------------------------------
#------------------------------------ US 24 START [DHAVAL]----------------------------------
def US24_Unique_families_by_spouses(families):
   return_flag = True
   error_type = "US24"
   for family in families:
       for fam in families:
           if family.uid!=fam.uid:
               if family.married!='NA' and fam.married!='NA':
                   if family.husbandName==fam.husbandName and family.wifeName==fam.wifeName and family.married==fam.married:
                       error_descrip = "Spouse's names and marriage dates same for different families"
                       error_location = [family.uid,fam.uid]
                       report_error('ERROR', error_type, error_descrip, error_location)
                       return_flag = False

   return return_flag
#------------------------------------ US 24 END -------------------------------------------
#------------------------------------ US 25 START [GOPI]----------------------------------
##US25	Unique first names in families	No more than one child with the same name and birth date should appear in a family

def US25_Unique_firstnames_families(individuals,families):
   return_flag = True
   error_type = "US25"
   for family in families:
       childs=family.children
       for child in childs:
           child_individual=getIndividiual(child)
           for individual in individuals:
               if individual.uid!=child_individual.uid:
                   if individual.birthday== child_individual.birthday and individual.name[0]==child_individual.name[0]:
                       error_descrip = "First names and birth dates same for different child in same family"
                       error_location = [individual.uid,child_individual.uid]
                       report_error('ERROR', error_type, error_descrip, error_location)
                       return_flag = False   
   return return_flag
       
#------------------------------------ US 25 END -------------------------------------------
#------------------------------------ US 35 START [GOPI]----------------------------------
##US35	List recent births	List all people in a GEDCOM file who were born in the last 30 days
def US35_list_recent_births(individuals):
    return_flag = True
    error_type = "US35"
    people_recent_birth=[]
    currentDate=datetime.now()
    dateBefore30Days=currentDate+timedelta(-30)
    for individual in individuals:
        if individual.birthday!= 'NA':     
            if individual.birthday <= currentDate.date() and individual.birthday >= dateBefore30Days.date():
                people_recent_birth.append(individual.name)
    if people_recent_birth!=[]:
        error_descrip = "List of people who born in the last 30 days :" +str(people_recent_birth)
       
        report_list('LIST', error_type, error_descrip)
        return_flag = False   
    return return_flag

#------------------------------------ US 35 END -------------------------------------------
#------------------------------------ US 38 START [KRUTARTH]-------------------------------
# US38 List all living people in a GEDCOM file whose birthdays occur in the next 30 da
def US38_List_upcoming_birthdays(individuals):    
    return_flag = True
    error_type = "US38"
    people=[]
    currentDate=datetime.now()
    for individual in individuals:
        if individual.birthday!= 'NA':     
            if individual.alive == True:
                birthdate = individual.birthday
                birthdate = datetime(currentDate.year,birthdate.month,birthdate.day)
                upcoming_birthday=(birthdate - currentDate).days        
            
                if upcoming_birthday<= 30 and upcoming_birthday >= 0:
                    people.append(individual.name[0])
    if people!=[]:
        error_descrip = "List of people who born in Coming 30 days:" +str(people)
     
        report_list('LIST', error_type, error_descrip)
        return_flag = False   
    return return_flag 
        
#------------------------------------ US 38 END [KRUTARTH]-------------------------------   
#------------------------------------ US 39 START [KRUTARTH]-------------------------------
# US39 List all living couples in a GEDCOM file whose marriage anniversaries occur in the next 30 days
def US39_List_upcoming_marriage_anniversary(individuals, families):    
    return_flag = True
    error_type = "US39"
    people=[]
    currentDate=datetime.today()
    for individual in individuals:
        if individual.alive == True:
            name = individual.name
            individualId = individual.uid
            for family in families:
                if family.married != 'NA':     
                    husband = family.husbandID
                    wife = family.wifeID
                    marriageDate = family.married 
                    Anniversary = datetime(currentDate.year,marriageDate.month,marriageDate.day)
                    upcomingAnniversary = (Anniversary - currentDate).days
                    if upcomingAnniversary<= 30 and upcomingAnniversary >= 0:
                        if individualId == wife:
                            people.append(name[0])
                        if individualId == husband:
                            people.append(name[0])
    if people!=[]:
        error_descrip = "List of people who has Anniversary in next 30 days: " + str(people)
        report_list('LIST', error_type, error_descrip)
        return_flag = False   
    return return_flag 
#------------------------------------ US 39 END [KRUTARTH]-------------------------------   
        
#------------------------------------ US 27 START [DHAVAL]-------------------------------
def US27_List_individual_current_ages(individuals, families):    
    return_flag=True
    error_type = "US27"
    list_individual=[]
    
    for individual in individuals:
        if individual.alive == True and individual.birthday!='NA':
            listItem='ID: '+str(individual.uid)+'\tName: '+str(individual.name)+'\tCurrent Age:'+str(getAge(individual.uid))+',\tGender:'+str(individual.gender)
            list_individual.append(str(listItem))
    if list_individual!=[]:
        string=""
        for item in list_individual:
            string=string+item+'\n'
        error_descrip = "Below is listing of Individuals with current age: \n\n" + string
        report_list('LIST', error_type, error_descrip)
        return_flag = False   
        return return_flag 
    return return_flag 
#------------------------------------ US 27 END [DHAVAL]-------------------------------           

#------------------------------------ US 36 START [DHAVAL]-------------------------------
def US36_List_recent_deaths(individuals, families):    
    return_flag=True
    error_type = "US36"
    people=[]
    for individual in individuals:
        if individual.alive == False:
            if dates_within(datetime.now().date(),individual.deathDate,0,30,'days'):
                people.append(individual.name)
    if people!=[]:
        error_descrip = "List of people died in last 30 days: " + str(people)
      
        report_list('LIST', error_type, error_descrip)
        return_flag = False   
    return return_flag

#------------------------------------ US 36 END [DHAVAL]------------------------------- 

#------------------------------------ US 30 START [DEEP]-------------------------------
##List all living married people in a GEDCOM file
def US30_List_living_married(individuals, families):
    living_married=[]
    return_flag = False
    error_type = "US30"
    for family in families:
        hus = family.husbandID
        wife = family.wifeID
        count = 0
        for individual in individuals:
            if hus == individual.uid or wife == individual.uid:
                if individual.alive == True:
                    count = count + 1        
        if count == 2 :
            living_married.append(family.husbandName[0])
            living_married.append(family.wifeName[0])
    if living_married!=[]:
            error_descrip = "List of Married_living: "+str(living_married)
          
            report_list('LIST', error_type,error_descrip)
            return_flag = False    
    return return_flag

#------------------------------------ US 30 END [DEEP]-------------------------------

#------------------------------------ US 33 START [DEEP]-------------------------------
## List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
def US33_List_orphans(individuals, families):
    return_flag = False
    error_type = "US33"
    currentDate = datetime.now()
    orphans=[]
    for family in families:
        hus = family.husbandID
        wife = family.wifeID
        children = family.children
        count = 0
        for individual in individuals:
            if hus == individual.uid or wife == individual.uid:
                if individual.alive == False:
                    count = count + 1

        if count == 2:
            for child in children:
                for individual in individuals:
                    if child == individual.uid:
                        birthdate = individual.birthday
                        birthdate = datetime(birthdate.year, birthdate.month, birthdate.day)
                        age = (currentDate-birthdate).days/365.25
                        if age < 18:
                            orphans.append(individual.name)
                            
    if orphans!=[]:
        error_descrip = 'List of Orphans: '+str(orphans)
        
        report_list('LIST ', error_type, error_descrip)
        return_flag = False                                                
    
    return return_flag
                            

                

          

#------------------------------------ US 33 END [DEEP]-------------------------------

##############################       IMPLEMENTING  USER STORIES  END      ########################################

##############################       REPORTING ERRORS  START      #########################################

error_locations = []

def report_error(rtype, error_type, description, locations):

        if isinstance(locations, list):
            locations = ','.join(locations)

        estr = '{:10.10s} {:10.5s}  {:105.105s}    {:40.40s}' \
            .format(rtype, error_type, description, locations)
        print(estr)
        error_locations.extend(locations)
        
        
def report_list(rtype, error_type, description):

        print('\n'+rtype+'\t   '+error_type+'\t\t'+description)
       

##############################       REPORTING ERRORS  END      #########################################


