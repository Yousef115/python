
itemDict = {}
itemList = []
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
			itemDict["name"] = userVar
			itemDict["price"] = float(input("Price: "))
			itemDict["quantity"] = int(input("Quantity: "))
			itemDict["price"] *= itemDict["quantity"]
			itemList.append (itemDict.copy())
			# print (itemDict)
			# print ("item list content: ")
			# print (itemList)


# print function to loop through the items and calculate total then print out the receipt.
def print_receipt():
	total = 0
	print ("-------------------\nreceipt\n-------------------\n")
	for x in itemList:
		print ("%d %s %.3f KD" %(x["quantity"], x["name"], x["price"] ))
		total += x["price"]
	print("-------------------\nTotal: %.3f KD" %(total))

# #Get input from user till they type 'done'
add_items()

print_receipt()
