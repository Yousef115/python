from datetime import date
#from datetime import datetime

today = date.today()

def check_birthdate (year, month, day):
	
	bday = date(year, month, day)
	if today < bday:
		return False
	else:
		return True

def calculate_age (year, month, day):
	bday = date(year, month, day)
	print ("You are %d years, %d months, and %d days old" %( (today.year - bday.year), (today.month - bday.month), (today.day - bday.day) ))

year = int(input("Enter year of birth "))
month = int(input("Enter month of birth "))
day = int(input("Enter day of birth "))

if check_birthdate(year, month, day) == True:
	calculate_age(year, month, day)
else:
	print ("You have entered an invalid date of birth.")