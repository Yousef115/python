skills = ["Python", "C++", "Web Development", "Googling" ]
cvSkills = []
cv = {
"name" : input("What is your name? "),
"age" : int(input("How old are you? ")),
"experience" : input ("How many years of experience do you have? "),
"skills" : cvSkills,
}

print ("1- %s\n2- %s\n3- %s\n4- %s\n " %(skills[0],skills[1],skills[2],skills[3]))

skill1 = (int(input("Choose a skill from above: ")) )
skill2 = (int(input("Choose another skill from above: ")) )

cvSkills.append(skills[skill1-1])
cvSkills.append(skills[skill2-1])


def qualified (applicant):
	score = 0
	if applicant["age"] > 20 and applicant["age"] < 35:
		score = score + 5
	if cvSkills.count("Googling") == 1:
		score = score + 5
	if score == 10:
		return True
	else:
		return False

	
if qualified (cv) == True:
	print ("You have been accepted " + cv["name"])
else:
	print ("You do not meet the criteria for this job.")