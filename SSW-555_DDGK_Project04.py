import sys
from datetime import date
from datetime import datetime

def verifyCurrentDate(year, month, day):
  
  givenDate=datetime.datetime(year, month, day)
  currentDate=datetime.today().date()
  
  if givenDate>currentDate:
    raise Exception('The given date should not exceed the current date!')
    
    #assuming that i/p's are in the format 4 MAR 1980
def verifyBirth(birthDateString, marriageDateString):
  
  birth_dd,birth_mmm,birth_yyyy=birthDateString.split()
  marriage_dd,marriage_mmm,marriage_yyyy=marriageDateString.split()
  
  birthDate=datetime.datetime(birth_yyyy, strptime(birth_mmm,'%b').tm_mon, birth_dd)
  marriageDate=datetime.datetime(marriage_yyyy, strptime(marriage_mmm,'%b').tm_mon, marriage_dd)
  
  if(birthDate<marriageDate)
  raise Exception('Birth date of child is older than marriage of parents!')
    
