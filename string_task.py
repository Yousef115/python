time = input("Please input a time using digits only: ")
noun = input("Please input an item: ")
name = input("Please input a name: ")
wacky = input("Please input a wacky sentence: ")
action = input ("Please input an action: ")

name = name.lower().title()
wacky = wacky.upper()


print ("\n\nIt was %d o'clock when I heard a knock at the door. \nI opened the door and there was a %s with a note saying \"From %s \". \nJust as I closed the door I heard a scream \"%s\". \nI froze in place and all I could do was %s." % (int(time), noun, name, wacky, action))