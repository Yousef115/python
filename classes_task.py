import datetime

class employee:
	def __init__(self, name, age, salary, empDate):
		self.name = name
		self.age = age
		self.salary = salary
		self.empDate = empDate

	def __str__(self):
		return ("Name: %s, Age: %d, Salary: %d, Working years: %d" 
				%(self.name,self.age,self.salary,self.get_working_years(self.empDate) ))

	def get_working_years(self, year):
		today = int(datetime.datetime.now().year)
		return (today - year)

class manager(employee):
	def __init__(self, name, age, salary, empDate, bonus_percentage):
		super().__init__(name, age, salary, empDate)
		self.bonus_percentage = bonus_percentage

	def __str__(self):
		return ("Name: %s, Age: %d, Salary: %d, Working years: %d, Bonus: %.3f\n"
				%(self.name,self.age,self.salary,self.get_working_years(self.empDate),
				(self.bonus_percentage*self.salary) ))

	def get_bonus(self):
		return bonus_percentage * salary

welcome = "Welcome to HR Pro 2019"
menu = """Choose an action to do:
	1. show employees
	2. show managers
	3. add an employee
	4. add a manager
	5. exit
"""
Joey = employee("Joey", 24, 500, 2018)
Yousef = manager("Joey", 44, 1000, 2009, 0.5)
employees_list = [Joey]
managers_list = [Yousef]


def print_employees():
	print ("-----------------\n")
	for x in employees_list:
		print (x)
	print ("-----------------\n")

def print_managers():
	print ("-----------------\n")
	for x in managers_list:
		print (x)
	print ("-----------------\n")

def add_employee():

	print ("-----------------\n")
	name = input("Name: ")
	age = int(input("Age: "))
	salary = int(input("Salary: "))
	empDate = int(input("Employment year: "))
	print ("Processing...")
	new_employee = employee(name, age, salary, empDate)
	employees_list.append(new_employee)
	print ("Employee added successfully.")
	print ("-----------------\n")

def add_manager():
	print ("-----------------\n")
	name = input("Name: ")
	age = int(input("Age: "))
	salary = int(input("Salary: "))
	empDate = int(input("Employment year: "))
	bonus_percentage = float(input("Bonus %: "))
	print ("Processing...")
	new_manager = employee(name, age, salary, empDate, bonus_percentage)
	managers.append(new_manager)
	print ("Manager added successfully.")
	print ("-----------------\n")

print (welcome)

userVar = 0
while userVar != 5:
	userVar = int(input(menu))
	if userVar == 1:
		print_employees()
	elif userVar == 2:
		print_managers()
	elif userVar == 3:
		add_employee()
	elif userVar == 4:
		add_manager()
	elif userVar > 5:
		print ("Please input a correct command. \n")

else:
	exit(1)