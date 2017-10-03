import datetime

name = raw_input("What is your name? ")
age = int(raw_input("How old are you? "))
num = int(raw_input("Enter a number from 0 - 9: ")) # will print the final answer this number of times

while num < 0 or num > 20:	# loops until a valid number is entered
	num = int(raw_input("Invalid number. Please enter a number between 0 - 20: "))

year = datetime.datetime.now().year + 100 - age

while num > 0:
	print("Hi, " + name + "! You'll be 100 years old in " + str(year))
	num -= 1
