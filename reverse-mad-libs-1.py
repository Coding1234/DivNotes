# function to display high level and loop till level is finished
def displayHigh():
	# display high mat lab paragraph
	highLab = '''The list data type in python has several methods.
	The ---1--- method adds a single item to the end of the list,
	The ---2--- method removes an element from the list,
	The ---3--- method inserts an item at a given index in the list.
	The ---4--- method reverses the elements in a list (in place).'''
	#store the answers of the highLab. This is used to compare user raw_input with the correct answer
	highLabAnswers = {
			'1':'append',
			'2':'remove',
			'3':'insert',
			'4':'reverse'
	}
	print "Welcome to the High Level. You are braver than I thought."
	print "Replace the numbers 1 thru 4 with the correct word to win this level" 
	print "Type all answers in lower case"
	print highLab
	# store value of "true" when correct answer is provided for any given numbered blank
	option1 = "false"
	option2 = "false"
	option3 = "false"
	option4 = "false"

	# loop till all 4 numbered slots are provided correctly
	while option1<> "true" or option2<> "true" or option3 <> "true" or option4 <> "true":
		#loop till option1 is correctly entered
		while option1 == "false":
			#get user raw_input for blank 1
			getOption1 = raw_input("Provide word to replace ---1--- \n")
			# Get user raw_input for blank 1
			if getOption1 == highLabAnswers['1']:
				print "Great! you got that right"
				print getOption1
				# replace blank 1 with the correct value
				labOption1 = highLab.replace("---1---", highLabAnswers['1'])
				print labOption1
				# set option1 to true so that the program moves to option2
				option1 = "true"
			else:
				# if the user raw_input is not correct this will allow the user to try again
				print "Try again"

		# loop till option 2 is correctly entered
		while option2 == "false":
			getOption2 = raw_input("Provide word to replace ---2--- \n")
			if getOption2 == highLabAnswers['2']:
				print "Great! you got that right"
				print getOption2
				labOption2 = labOption1.replace("---2---", highLabAnswers['2'])
				print labOption2
				option2 = "true"
			else:
				print "Try again"
		
		# loop till option 3 is correctly entered
		while option3 == "false":
			getOption3 = raw_input("Provide word to replace ---3--- \n")
			if getOption3 == highLabAnswers['3']:
				print "Great! you got that right"
				print getOption3
				labOption3 =  labOption2.replace("---3---", highLabAnswers['3'])
				print labOption3
				option3 = "true"
			else:
				print "Try again"
		
		# loop till option 4 is correctly entered
		while option4 == "false":
			getOption4 = raw_input("Provide word to replace ---4--- \n")
			if getOption4 == highLabAnswers['4']:
				print "Great! you got that right"
				print getOption4
				labOption4 = labOption3.replace("---4---", highLabAnswers['4'])
				print labOption4
				option4 = "true"
			else:
				print "Try again"
	
	print "yes!!!!Congrats you did it!!!"
	# upon level completion provide option to restart game or quit
	goOn = raw_input("type 'again' to start over OR 'quit' to exit the game \n")
	if goOn == "quit":
		quit()
	elif goOn == "again":
		#if user wants to play again call getLevel to gain user raw_input
		getLevel()

# medium level
def displayMedium():
	#display medium mat lab paragraph
	medLab = '''The ---1--- comes to a line of code containing a "function call".
	The ---1--- enters the ---2---(starts at the first line in the function code).
	All instructions inside of the ---2--- are executed from ---3--- to bottom.
	The program leaves the function and goes back to where it started from.
	Any data computed and ---4--- by the function is used in place of the function in the original line of code.'''
	#store the answers of the highLab. This is used to compare user raw_input with the correct answer
	medLabAnswers = {
			'1':'program',
			'2':'function',
			'3':'top',
			'4':'returned'
	}
	print "Welcome to the Medium Level. You are cooler than I thought."
	print "Replace the numbers 1 thru 4 with the correct word to win this level" 
	print "Type all answers in lower case"
	print medLab
	# store value of "true" when correct answer is provided for any given numbered blank
	option1 = "false"
	option2 = "false"
	option3 = "false"
	option4 = "false"

	# loop till all 4 numbered slots are provided correctly
	while option1<> "true" or option2<> "true" or option3 <> "true" or option4 <> "true":
		#loop till option1 is correctly entered
		while option1 == "false":
			#get user raw_input for blank 1
			getOption1 = raw_input("Provide word to replace ---1--- \n")
			# Get user raw_input for blank 1
			if getOption1 == medLabAnswers['1']:
				print "Great! you got that right"
				print getOption1
				# replace blank 1 with the correct value
				labOption1 = medLab.replace("---1---", medLabAnswers['1'])
				print labOption1
				# set option1 to true so that the program moves to option2
				option1 = "true"
			else:
				# if the user raw_input is not correct this will allow the user to try again
				print "Try again"

		# loop till option 2 is correctly entered
		while option2 == "false":
			getOption2 = raw_input("Provide word to replace ---2--- \n")
			if getOption2 == medLabAnswers['2']:
				print "Great! you got that right"
				print getOption2
				labOption2 = labOption1.replace("---2---", medLabAnswers['2'])
				print labOption2
				option2 = "true"
			else:
				print "Try again"
		
		# loop till option 3 is correctly entered
		while option3 == "false":
			getOption3 = raw_input("Provide word to replace ---3--- \n")
			if getOption3 == medLabAnswers['3']:
				print "Great! you got that right"
				print getOption3
				labOption3 =  labOption2.replace("---3---", medLabAnswers['3'])
				print labOption3
				option3 = "true"
			else:
				print "Try again"
		
		# loop till option 4 is correctly entered
		while option4 == "false":
			getOption4 = raw_input("Provide word to replace ---4--- \n")
			if getOption4 == medLabAnswers['4']:
				print "Great! you got that right"
				print getOption4
				labOption4 = labOption3.replace("---4---", medLabAnswers['4'])
				print labOption4
				option4 = "true"
			else:
				print "Try again"
	
	print "yes!!!!Congrats you did it!!!"
	# upon level completion provide option to restart game or quit
	goOn = raw_input("type 'again' to start over OR 'quit' to exit the game \n")
	if goOn == "quit":
		quit()
	elif goOn == "again":
		#if user wants to play again call getLevel to gain user raw_input
		getLevel()

# get low level
def displayLow():
	
	#display medium mat lab paragraph
	lowLab = '''There are two types of loops in ---1---. The ---2--- and the ---3--- loop. 
	The ---2--- loop is useful to iterate over the contents of a list
	The ---3--- loop is useful to repeat a sequence of steps till a given condition is true or ---4---'''
	#store the answers of the highLab. This is used to compare user raw_input with the correct answer
	lowLabAnswers = {
			'1':'python',
			'2':'for',
			'3':'while',
			'4':'false'
	}
	print "Welcome to the Low Level. Enjoy!!"
	print "Replace the numbers 1 thru 4 with the correct word to win this level" 
	print "Type all answers in lower case"
	print lowLab
	# store value of "true" when correct answer is provided for any given numbered blank
	option1 = "false"
	option2 = "false"
	option3 = "false"
	option4 = "false"

	# loop till all 4 numbered slots are provided correctly
	while option1<> "true" or option2<> "true" or option3 <> "true" or option4 <> "true":
		#loop till option1 is correctly entered
		while option1 == "false":
			#get user raw_input for blank 1
			getOption1 = raw_input("Provide word to replace ---1--- \n")
			# Get user raw_input for blank 1
			if getOption1 == lowLabAnswers['1']:
				print "Great! you got that right"
				print getOption1
				# replace blank 1 with the correct value
				labOption1 = lowLab.replace("---1---", lowLabAnswers['1'])
				print labOption1
				# set option1 to true so that the program moves to option2
				option1 = "true"
			else:
				# if the user raw_input is not correct this will allow the user to try again
				print "Try again"

		# loop till option 2 is correctly entered
		while option2 == "false":
			getOption2 = raw_input("Provide word to replace ---2--- \n")
			if getOption2 == lowLabAnswers['2']:
				print "Great! you got that right"
				print getOption2
				labOption2 = labOption1.replace("---2---", lowLabAnswers['2'])
				print labOption2
				option2 = "true"
			else:
				print "Try again"
		
		# loop till option 3 is correctly entered
		while option3 == "false":
			getOption3 = raw_input("Provide word to replace ---3--- \n")
			if getOption3 == lowLabAnswers['3']:
				print "Great! you got that right"
				print getOption3
				labOption3 =  labOption2.replace("---3---", lowLabAnswers['3'])
				print labOption3
				option3 = "true"
			else:
				print "Try again"
		
		# loop till option 4 is correctly entered
		while option4 == "false":
			getOption4 = raw_input("Provide word to replace ---4--- \n")
			if getOption4 == lowLabAnswers['4']:
				print "Great! you got that right"
				print getOption4
				labOption4 = labOption3.replace("---4---", lowLabAnswers['4'])
				print labOption4
				option4 = "true"
			else:
				print "Try again"
	
	print "wowza!!!!Ready to take it up a notch?"
	# upon level completion provide option to restart game or quit
	goOn = raw_input("type 'again' to start over OR 'quit' to exit the game \n")
	if goOn == "quit":
		quit()
	elif goOn == "again":
		#if user wants to play again call getLevel to gain user raw_input
		getLevel()

# function to get user to choose the level they want to play
def getLevel():
	# get user raw_input and store it in variable
	level = raw_input("Enter a diffculty level. Options are 'High', 'Medium', 'Low' \n" )
	callLevel(level)
	return level

# understand user raw_input received via getLevel()
def callLevel(level):
	if level == 'High' or level == 'high' or level == 'HIGH':
		displayHigh()
	elif level == 'Medium' or level == 'medium' or level == 'MEDIUM':
		displayMedium()
	elif level == 'Low' or level == 'low' or level == 'LOW':
		displayLow()
	else:
		# do not accept any entries other than high, medium or low
		print "You must type 'high', 'medium' OR 'low'. Other values are not accepted"
		getLevel()

# Lets Play!!!!!!
getLevel()
