import random
#no easy or hard mode
#
#
#
#

def main():
	"""
	vibe to implement start screen
	Implement main code, full game in while loop, and maybe iterative
	external while-loop for replayability. Lot's of work to do...
	"""
	#Drip working on filling map array
	p_item = [1, 0, 0] #Item array: torches, dynamite, pickaxe
	start_location = (16, 0) #Starting location for the mine
	step = 1 #The amount of steps (turns) the player has taken
	escape = False #lcv to check if miner found the exit
	checkpoint = start_location #Init cp is just the start pos
	checkpoint_curr_steps = 0 #This is the num of steps from previous cp
	num_turns = 400
	#These two vars are to iterate through the mine
	pROW = 16
	pCOL = 0
	torch_active = False #bool to see if the miner has a torch lit
	torch_time = 0 #Var to see how many turns the miner has with the current lit torch
	curr_point = start_location #miner's curr pos in mine, init to start point
	prevoius_step = start_location #last pos the miner was in, init to beginning
	death = False #bool discerning if the miner has met their end
	menu = True #bool for vibe to help with start menu/play cycle
	playing = False #bool to actually start the game
	#This is where vibe will implement the menu functionality

	lROOMS = [(3, 12), (3, 36), (12, 9), (13,13), (14, 17), (14, 31), (20, 7)]
	cPS = [(0, 17), (4, 33), (6, 20), (13, 24), (3, 28)]
	dENDS = [(0, 24), (0, 33), (6, 33), (11, 17), (13, 36), (20, 24)]

    victory = False #We return this to see if we print death or win screen

	while(!(escape) and !(death)):
		#move first, then check location
		#check if on edge of array
		#bounds for up-down val
		if(curr_point[0] == 0):
			#cant move up
			move_up = False
		elif(curr_point[0] == 20):
			#cant move down
			move_down = False
		if(curr_point[1] == 0):
			#cant move left
			move_left = False
		elif(curr_point[1] == 37):
			#cant move right
			move_right = False

		#make an array for menu printing move options
		moves = [0, 0, 0, 0]

		#now we decide to move
		if(move_up and 'get curr pos - 1 u/d coord == 1'):
			up_opt = True
		if(move_down and 'get curr pos +1 u/d coord == 1'):
			down_opt = True
		if(move_left and 'get curr pos -1 l/r coord == 1'):
			left_opt = True
		if(move_right and 'get curr pos +1 l/r coord == 1'):
			right_opt = True

		moves[0] = up_opt
		moves[1] = down_opt
		moves[2] = left_opt
		moves[3] = right_opt

		for x in range(3):
			if(moves[x]):
				#update the moves number to print out moves
				move_opt += 1
		
		choice = -1
		while(choice < 0 || > 5):
			if(move_opt == 4):
				print("You have 4 Options:")
				print("Option 1: EAST")
				print("Option 2: WEST")
				print("Option 3: NORTH")
				print("Option 4: SOUTH")
			elif(move_opt == 3):
				print("You have 3 Options")
				if(moves[0] and moves[1] and moves[2]):
					print("Option 1: EAST")
					print("Option 2: WEST")
					print("Option 3: NORTH")
				elif(moves[0] and moves[1] and moves[3]):
					print("Option 1: EAST")
					print("Option 2: WEST")
					print("Option 4: SOUTH")
				elif(moves[0] and moves[2] and moves[3]):
					print("Option 1: EAST")
					print("Option 3: NORTH")
					print("Option 4: SOUTH")
				elif(moves[1] and moves[2] and moves[3]):
					print("Option 2: WEST")
					print("Option 3: NORTH")
					print("Option 4: SOUTH")
			elif(move_opt == 2):
				print("You have 2 Options")
				if(moves[0] and moves [1]):
					print("Option 1: EAST")
					print("Option 2: WEST")
				elif(moves[0] and moves [2]):
					print("Option 1: EAST")
					print("Option 3: NORTH")
				elif(moves[0] and moves[3]):
					print("Option 1: EAST")
					print("Option 4: SOUTH")
				elif(moves[1] and moves[2]):
					print("Option 2: WEST")
					print("Option 3: NORTH")
				elif(moves[1] and moves[3]):
					print("Option 2: WEST")
					print("Option 4: SOUTH")
				elif(moves[2] and moves[3]):
					print("Option 3: NORTH")
					print("Option 4: SOUTH")
			elif(move_opt == 1):
				print("You have 1 Option:")
				if(moves[0]):
					print("Option 1: EAST")
				elif(moves[1]):
					print("Option 2: WEST")
				elif(moves[2]):
					print("Option 3: NORTH")
				elif(moves[3]):
					print("Option 4: SOUTH")
			else:
				#I don't believe we should be able to make it here, but if we do fuck
			
			"""
			if(p_item[0] > 0):
				print("Additional Option 5: light a torch")
			"""
			#choice = -1
			usrIn = False

			#This while loop checks the validity of their input choice, making sure we can move
			while(usrIn != True):
				choice = input(int())
				"""
				if(choice == 5):
					if(p_item[0] == 0):
						print("Please enter a different choice: ")
					else
						usrIn == True
				"""
				if(moves[choice] != True):
					print("Please enter a different choice: ")
				elif(moves[choice):
					usrIn == True
				else:
					#I don't think we should get here either but fuck
			print("Your choice was:", choice)
		#Move east (up)
		#previous_step = curr_point
		if(choice == 1):
			previous_step = curr_point
			pROW--
			curr_point = (pROW, pCOL)
		#move west (down)
		elif(choice == 2):
			previous_step = curr_point
			pROW++
			curr_point = (pROW, pCOL)
		#move north (right)
		elif(choice == 3):
			previous_step = curr_point
			pCOL++
			curr_point = (pROW, pCOL)
		#move south (left)
		elif(choice == 4):
			previous_step = curr_point
			pCOL--
			curr_point = (pROW, pCOL)
		"""
		#torch choice
		elif(choice == 5):
			#start torch
		"""
		else:
			#We should never reach here, but again fuck

		#Check if the new room is an item room, cp, or death room
		
		#let's check death first, then we can just be done with the thing
			
		if(Kill_Room(curr_point)):
			victory = False
			death = True
		
		#next will be a loot room
		
		elif(Loot_Room(curr_point)):
			#code to find loot
			loot = random.randint(0,10)
			if(loot <= 4):
				print("You find a torch.")
				p_item[0]++
			elif(loot > 4 and < 9):
				print("You found a stick of dynamite.")
				p_item[1]++
			elif(loot == 9):
				print("You found a pickaxe.")
				p_item[2]++
			else:
				print("You didn't find anything.")

			#if they find pick
			if(p_item[2]):
				print("With your pickaxe would you like to go back to the beginning and dig your way out?")
				print("Option 1: YES")
				print("Option 2: NO")
				choicePick = -1
				while(choicePick != 1 and choicePick != 2):
				    choicePick = input(int())
					if(choicePick != 1 and choicePick != 2):
						print("Please choose a valid option.")
				if(choicePick == 1):
					steps = steps * 2
					curr_point = start_location
					if(steps <= 300):
						print("You successfully dug your way out!")
						victory = True
						escape = True
					elif(steps > 300):
						print("While toiling away at the entrance, you slowly become weak. Never seeing the light again, you die of exhaustion.")
					    death = True
						victory = False
					else:
						#We should never reach this part of the code
				else:
					print("You continue with the pick in hand.")

			#if they have the dynamite and no torch
			if(p_item[1] and !(death) and !(p_item[0])):
				print("With your stick of dynamite, would you like to go back to the entrance and attempt to escape?")
				print("Option 1: YES")
				print("Option 2: NO")
				choiceDyn = -1
				while(choiceDyn != 1 and choiceDyn != 2):
					choiceDyn = input(int())
					if(choiceDyn != 1 and choiceDyn != 2):
						print("Please choose a valid option.")
				if(choiceDyn == 1):
					steps = steps * 2
					if(steps >= num_turns):
						print("On your way back to the entrance you pass out due to lack of oxygen.")
						death = True
					else:
						print("You've made your way to the entrance, but have no torch to light the dynamite.")
						print("Would you like to throw the dynamite in an attempt to escape?")
						print("Option 1: YES")
						print("Option 2: NO")
						choiceNoTorch = -1
						while(choiceNoTorch != 1 and choiceNoTorch != 2):
							choiceNoTorch = input(int())
							if(choiceNoTorch != 1 and choiceNoTorch != 2):
								print("Please choose a valid option.")
						if(choiceNoTorch == 1):
							#random escape chance stuff
							boom = random.randint(3)
							if(boom == 3):
								print("The dynamite went off when you threw it at the wall, you escape!")
								victory = True
								escape = True
							else:
								p_item[1]--
								print("The dynamite hit the wall but nothing happened, upon inspection, you see the stick broke and is useless.")
								#re-explore or go back to where they came from
								print("Would you like to got back to the last checkpoint, or try exploring again?")
								print("Option 1: CHECKPOINT")
								print("Option 2: EXPLORE")
								exChoice = -1
								while(exChoice != 1 and exChoice != 2):
									exChoice = input(int())
									if(exChoice != 1 and exChoice != 2):
										print("Please choose a valid option.")
								if(exChoice == 1):
									#
									curr_point = checkpoint
									steps = steps + (steps - checkpoint_current_steps)
								else:
									startmap()
						elif(choiceNoTorch == 2):
							#re-explore or go back to where you came from?
							print("Would you like to got back to the last checkpoint, or try exploring again?")
							print("Option 1: CHECKPOINT")
							print("Option 2: EXPLORE")
							exChoice = -1
							while(exChoice != 1 and exChoice != 2):
								exChoice = input(int())
								if(exChoice != 1 and exChoice != 2):
									print("Please choose a valid option.")
							if(exChoice == 1):
								#
								curr_point = checkpoint
								steps = steps + (steps - checkpoint_current_steps)
							else:
								startmap()

			#if they have a torch and dynamite
			if(p_item[1] and !(death) and p_item[0] and torch_lit):
				print("With your stick of dynamite, would you like to go back to the entrance and attempt to escape?")
				print("Option 1: YES")
				print("Option 2: NO")
				choiceDyn = -1
				while(choiceDyn != 1 and choiceDyn != 2):
					choiceDyn = input(int())
					if(choiceDyn != 1 and choiceDyn != 2):
						print("Please choose a valid option.")
				if(choiceDyn == 1):
					steps = steps * 2
					if(steps >= num_turns):
						print("On your way back to the entrance you pass out due to lack of oxygen.")
						death = True
					else:
						print("With your torch lit you make your way to the cave entrance and detonate the dynamite, you escape!")
						victory = True
						escape = True
				if(choiceDyn == 2):
					print("You continue on with the dynamite in your hand.")



		#next is to check if the room is a cp

		elif(Check_Point(curr_point)):
			#set current spot to a check point and update various counters
			checkpoint = curr_point
			checkpoint_curr_steps = steps
		
		#next check if the current pos is a dead end
		elif(Dead_End(curr_point)):
			#implement code for dead end
			print("You've come to a dead end, you retrace your steps back to the checkpoint.")
            curr_point = checkpoint
            step_count = step_count + (step_count - checkpoint_curr_steps)

		#next check if the secret exit is found
		elif(win(curr_point)):
			victory = True
			escape = True

		#in this case, the room is normal, and I suppose we continue on normally
		else:
			#dunno if we need any code really, might have to reinitialize other vars

		#increase turn iterator
		steps++
		if(steps == num_turns):
			print("You ran out of oxygen and died!")
			death = True
			victory = False

	#end of main, returns if we win or not
	return victory

"""
Here are gonna be the bool funcs we use to handle the main

"""
#Check to see if the room will kill you
#DBG MAKE SURE THE ROOMS ARE CORRECT POS
def Kill_Room(curr_point):
	if(curr_point == (0, 3)):
		print("You were devoured by cannibals!")
		return True
	elif(curr_point == (3, 18)):
		print("You were crushed by boulders!")
		return True
	elif(curr_point == (4, 36)):
		print("You were attacked by poisonous spiders!")
		return True
	elif(curr_point == (10, 38)):
		print("The floor breaks away before you, you fall to your death!")
		return True
	elif(curr_point == (12, 7)):
		print("You were impaled by a falling stalactite!")
		return True
	elif(curr_point == (17, 36)):
		print("The ceiling caves in above you, water fills the room, drowning you!")
		return True
	elif(curr_point == (20, 16)):
		print("You were ran over by a runaway mine cart!")
		return True
    else:
		return False

#Check to see if the room is a loot room
def Loot_Room(curr_point):
	for x in range(6):
		if(lROOMS[x] == curr_point):
			return True
	return False

def Check_Point(curr_point):
	for x in range(4):
		if(cPS[x] == curr_point):
			return True
	return False

def Dead_End(curr_point):
	for x in range(5):
		if(dENDS[x] == curr_point):
			return True
	return False

def Win(curr_point):
	if(curr_point == 8,29):
		return True
	else:
		return False


#should reinitialize map and cp vars, but leave steps the same
def startmap():


if __name__ == "__main__":
	main()
