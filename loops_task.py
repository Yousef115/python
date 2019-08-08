#check if user typed done or not
def check (isDone):
	if isDone.lower() == "done":
		return True
	else:
		return False

#add items from user to the itemDict{} dictionary, then cloning it to the itemList[] list so it can be printed at the end.
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

# print function to loop through the items and calculate total then print out the receipt.
def print_receipt():
	total = 0
	print ("-------------------\nreceipt\n-------------------\n")
	for x in itemList:
		print ("%d %s %.3f KD" %(x["quantity"], x["name"], x["price"] ))
		total += x["price"]
	print("-------------------\nTotal: %.3f KD" %(total))

#Calling functions to add items then print the invoice, and declaring the dictionary and list objects. 
itemDict = {}
itemList = []

add_items()

print_receipt()