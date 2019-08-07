
itemList = {}
# function to check if user input done or not
def check (isDone):
	if isDone.lower() == "done":
		return True
	else:
		return False

#function to add items to the dictionary with item name as key, and the value is a list with price and quantity respectively.
def add_items():
	userVar = ""
	while check(userVar) != True:
		userVar = input("Input item or \'done\' to finish: ")
		if check(userVar) == False:
			price = float(input("Price: "))
			qty = int(input("Quantity: "))
			price *= qty
			itemList[userVar] = [price, qty]

# print function to loop through the items and calculate total then print out the receipt.
def print_receipt():
	total = 0
	print ("-------------------\nreceipt\n-------------------\n")
	for key in itemList:
		print ("%d %s %.3f KD" %(itemList[key][1], key, itemList[key][0] ))
		total += itemList[key][0]
	print("-------------------\nTotal: %.3f KD" %(total))

#Get input from user till they type 'done'
add_items()

print_receipt()
