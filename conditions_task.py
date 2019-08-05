#Get user input - two numbers and an operator
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operator = input("Choose the operation (+, -, /, *): ")

#if loop to check if numbers given by user are actually digits or not.
if num1.isdigit() and num2.isdigit() == True:
	num1 = int(num1)
	num2 = int(num2)

#if loop to print the output based on input. If operator is not valid it prints out an error.
	if operator == "+":
		print ("The answer is: %d" %(num1 + num2))
	elif operator == "-":
		print ("The answer is: %d" %(num1 - num2))
	elif operator == "*":
		print ("The answer is: %d" %(num1 * num2))
	elif operator == "/":
		if num1 % num2 > 0:
			print ("The answer is: %d with a remainder of %d" %(num1 / num2, num1 % num2))
		else:
			print ("The answer is: %d" %(num1 / num2))
	else:
		print ("Sorry, you input an invalid operator.")

#else statement for the first if statement.
else:
	print ("Sorry, you input an invalid number.")
	