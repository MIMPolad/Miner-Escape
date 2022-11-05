import random
print("Type 1 for Easy Mode: ")
print("Type 2 for Hard Mode: ")
print("Type 3 for Quit: ")
Selection = input()
while (Selection != '1' or Selection != '2' or Selection != '3'):
  Selection = input()
  if Selection ==  "1" #EASY MODE
#VARIABLES
map = []
#p_start = (16,0) Starting point, later utilized with start_location
#first index is number of torches second number represents number of dynamite
p_item = [ 1, 0, 0]
start_location = (16, 0)
step = 1
escape = False
checkpoint = (16, 0) #checkpoint that changes at certain points
checkpoint_curr_steps = 0
#step_count = 1 step counter, used step instead
num_turns = 400
pROW = 16
pCOL = 0
torch_active = False
torch_time = 0
curr_point = (pROW, pCOL)
previous_step = (0,0)
death = False
#BEGIN CODE
#RIGHT IS NORTH (player moves one right)
#UP IS WEST (player moves one up)
#DOWN IS EAST (plaer moves one down)
        while(escape != True and death != True):


#If you hit a checkpoint save it 
          if Checkpoints(curr_point):
            checkpoint = curr_point
            checkpoint_curr_steps = step_count


#If you reach the win room at the end of the mine
          if Win(curr_point) == True:
            print("Congratulations!")
            print("You have succesfully escape the mine.")
            escape = True


#If the room you enter is loot room        
          elif Loot_Room(curr_point):
            loot = rand_init(0,10)
            if loot <= 4:
              print("You found a torch")
              p_item[0] + 1
            elif loot > 4 and loot < 9:
              print("You found a dynamite")
              p_item[1] + 1
            elif loot == 9:
              p_item[2] + 1
              print("You found a pickaxe")
            else
              print("You found nothing")
            #map[curr_point] = 0 I think we should update the move and map coords at the end of the while loop
            if p_item[1] or p_item[2]:
              if p_item[1]:
                print("Would you like to retrace steps to use the dynamite on the entrance? ")
                print("Option 1: YES")
                print("Option 2: NO")
                choice2 = input()
                if choice == 1:                                                                                               #If you choose to go back to the beginning
                  steps = steps * 2                                                                                           #Retrace steps (double them)
                  curr_point = start_location                                                                                 #Go back to start location
                  if p_item[0]:
                    print("You use a torch to light the dynamite, it clears the debris and you escape!")
                    escape = True
                  else:
                    dynamite_boom_chance = rand(0,3)                                                                          #25 chance for the dynamite to work without torch when thrown
                    if dynamite_boom_chance == 3:
                      print("You throw the dynamite at the wall and it miraculously explodes, you escape!")
                      escape = True
                    else:                                                                                                     #If the dynamite didn't light when you threw it at the wall
                      print("The dynamite wasn't lit and was destroyed in your attempt to escape.")
                      p_item[1] -= 1
                      print("Would you like to return to where you were and continue or restart finding your way through again?")
                      print("Option 1: Go back to where you left off.")
                      print("Option 2: Restart finding way from beginning.")
                      choice3 = input()
                      if choice3 == 1:
                        curr_point = previous_step
                      elif choice3 == 2:
                        curr_point = start_location                                                                                      #Reset the map as if they haven't traveled anywhere
                        for i in range(20):
                          for j in range(38):
                            if map[i][j] == 0:
                              map[i][j] = 1
                        map[curr_point] = 0

                elif choice2 = 2:
                  curr_point = previous_step                                                                                  #go back to previous room
              else:                                                                                                           #You got a pickaxe
                print("Would you like to retrace your steps to use pickaxe on the entrance?")
                print("Option 1: YES")
                print("Option 2: NO")
                choice2 = input()
                if choice2 == 1:
                  if((num_turns - step) >= 50):                                                                                 #If they have longer than 50 turns left they can pickaxe out
                    print("You dig through the debris with your trusty pick and escape!")
                    escape = True
                  else:
                    print("You run out of oxygen trying to pickaxe the mine entrance.")
                    death = True
                elif choice2 == 2:
                    #Is there supposed to be some code here to just continue from where they are?

            
#If the room you enter is death room
          elif Kill_Room(curr_point):
            death = True




#If the step led to dead end
          elif Dead_End(curr_point):
            print("You've come to a dead end, you retrace your steps back to the checkpoint.")
            curr_point = checkpoint
            step_count = step_count + (step_count - checkpoint_curr_steps)

#IF #EAST, WEST, NORTH, SOUTH
          elif(map[pROW + 1, pCOL] == ' ' and map[pROW - 1, pCOL] == ' ' and map[pROW, pCOL - 1] == ' ' and map[pROW, pCOL + 1] == ' '): #EAST, WEST, NORTH, SOUTH
            previous_step = (pROW, pCOL)
            if p_item[0] >= 1:
              print("You have 5 Options: ")
              print("Option 1: EAST")
              print("Option 2: WEST")
              print("Option 3: NORTH")
              print("Option 4: SOUTH")
              print("Option 5: Use Torch")
              choice = input()
              while(choice != '1' or choice != '2' or choice != '3' or choice != '4' or choice != '5'):
                print("Invalid Selection")
                choice = input()
              if choice == '1':
                pROW = pROW - 1
              elif choice == '2':
                pROW = pROW + 1
              elif choice == '3':
                pCOL = pCOL + 1
              elif choice == '4':
                pCOL = pCOL - 1
              elif choice == '5':
                torch_active = True
                p_item[0] - 1
                torch_time = 7
            else:
              print("You have 4 Options: ")
              print("Option 1: EAST")
              print("Option 2: WEST")
              print("Option 3: NORTH")
              print("Option 4: SOUTH")
              choice = input()
              while(choice != '1' or choice != '2' or choice != '3' or choice != '4' or choice != '5'):
                print("Invalid Selection")
                choice = input()
              if choice == '1':
                pROW = pROW - 1
              elif choice == '2':
                pROW = pROW + 1
              elif choice == '3':
                pCOL = pCOL + 1
              elif choice == '4':
                pCOL = pCOL - 1


#IF EAST, WEST, SOUTH
          elif(map[pROW + 1, pCOL] == ' ' and map[pROW - 1, pCOL] == ' ' and map[pROW , pCOL - 1] == ' '): #EAST, WEST, SOUTH
            previous_step = (pROW, pCOL)
            if p_item[0] >= 1:
              print("You have 4 Options: ")
              print("Option 1: EAST")
              print("Option 2: WEST")
              print("Option 3: SOUTH")
              print("Option 4: Use Torch")
              choice = input()
              while(choice != '1' or choice != '2' or choice != '3' or choice != '4'):
                print("Invalid Selection")
                choice = input()
              if choice == '1':
                pROW = pROW - 1
              elif choice == '2':
                pROW = pROW + 1
              elif choice == '3':
                pCOL = pCOL - 1
              elif choice == '4':
                torch_active = True
                p_item[0] - 1
                torch_time = 7
            else:
              print("You have 3 Options: ")
              print("Option 1: EAST")
              print("Option 2: WEST")
              print("Option 3: SOUTH")
              choice = input()
              while(choice != '1' or choice != '2' or choice != '3'):
                print("Invalid Selection")
                choice = input()
              if choice == '1':
                pROW = pROW - 1
              elif choice == '2':
                pROW = pROW + 1
              elif choice == '3':
                pCOL = pCOL - 1

#IF WEST, NORTH, SOUTH
          elif(map[pROW + 1, pCOL] == ' ' and map[pROW, pCOL - 1] == ' ' and map[pROW, pCOL + 1] == ' '):
            previous_step = (pROW, pCOL)
            if p_item[0] >= 1:
              print("You have 4 Options: ")
              print("Option 1: WEST")
              print("Option 2: NORTH")
              print("Option 3: SOUTH")
              print("Option 4: Use Torch")
              choice = input()
              while(choice != '1' or choice != '2' or choice != '3' or choice != '4'):
                print("Invalid Selection")
                choice = input()
              if choice == '1':
                pROW = pROW - 1
              elif choice == '2':
                pCOL = pCOL + 1
              elif choice == '3':
                pCOL = pCOL - 1
              elif choice == '4':
                torch_active = True
                p_item[0] - 1
                torch_time = 7
            else:
              print("You have 3 Options: ")
              print("Option 1: WEST")
              print("Option 2: NORTH")
              print("Option 3: SOUTH")
              choice = input()
              while(choice != '1' or choice != '2' or choice != '3'):
                print("Invalid Selection")
                choice = input()
              if choice == '1':
                pROW = pROW + 1
              elif choice == '2':
                pCOL = pCOL + 1
              elif choice == '3':
                pCOL = pCOL - 1
#IF EAST, NORTH, SOUTH
          elif(map[pROW + 1, pCOL] == ' ' and map[pROW, pCOL - 1] == ' ' and map[pROW, pCOL + 1] == ' '):
            previous_step = (pROW, pCOL)
            if p_item[0] >= 1:
              print("You have 4 Options: ")
              print("Option 1: EAST")
              print("Option 2: NORTH")
              print("Option 3: SOUTH")
              print("Option 4: Use Torch")
              choice = input()
              while(choice != '1' or choice != '2' or choice != '3' or choice != '4'):
                print("Invalid Selection")
                choice = input()
              if choice == '1':
                pROW = pROW - 1
              elif choice == '2':
                pCOL = pCOL + 1
              elif choice == '3':
                pCOL = pCOL - 1
              elif choice == '4':
                torch_active = True
                p_item[0] - 1
                torch_time = 7
            else:
              print("You have 3 Options: ")
              print("Option 1: EAST")
              print("Option 2: NORTH")
              print("Option 3: SOUTH")
              choice = input()
              while(choice != '1' or choice != '2' or choice != '3'):
                print("Invalid Selection")
                choice = input()
              if choice == '1':
                pROW = pROW + 1
              elif choice == '2':
                pCOL = pCOL + 1
              elif choice == '3':
                pCOL = pCOL - 1
#If EAST, WEST, and NORTH
          elif(map[pROW + 1, pCOL] == ' ' and map[pROW - 1, pCOL] == ' ' and map[pROW, pCOL + 1] == ' '): 
            previous_step = (pROW, pCOL)
            if p_item[0] >= 1: 
                print("You have 4 options: ")
                print("Option 1: Go WEST")
                print("Option 2: Go EAST")
                print("Option 3: Go NORTH") 
                print("Option 4: Light Torch")
                choice = input()
                while(choice != '1' or choice != '2' or choice != '3' or choice != '4'):
                  choice = input()
                  if choice == 1:                                            #Go Up one which is WEST
                    map[curr_point] = 0
                    pROW = pROW - 1
                    
                  elif choice == 2:                                          #Go Down one which is EAST
                    map[curr_point] = 0
                    pROW = pROW + 1

                  elif choice == 3:
                    map[curr_point] = 0
                    pCOL = pCOL + 1

                  elif choice == 4:
                    torch_active = True                                     #set the torch to active
                    p_item[0] - 1                                           #lose a torch
                    torch_time = 7                                          #start timer for torch (can edit time it lasts)


            elif p_item[0] == 0: #If no torches
                print("You have 3 options: ")
                print("Option 1: Go WEST")
                print("Option 2: Go EAST")
                print("Option 3: Go NORTH")
                choice = input()
                while(choice != '1' or choice != '2' or choice != '3'):
                  choice = input()
                  if choice == 1: #go WEST
                    pROW = pROW + 1
                    
                  elif choice == 2:#go EAST
                    pROW = pROW - 1

                  elif choice == 3:#go NORTH
                    pCOL = pCOL + 1

#IF WEST and SOUTH
          elif(map[pROW - 1, pCOL] == ' ' and map[pROW, pCOL - 1] == ' '):
            previous_step = (pROW, pCOL)
            if p_item[1] >= 1:
                print("You have 3 options: ")
                print("Option 1: Go WEST")
                print("Option 2: Go SOUTH")
                print("Option 3: Light Torch")
                choice = input("You select: ")
                while(choice != '1' or choice != '2' or choice != '3'): #repeat until valid option is selected
                  choice = input("Invalid Selection new choice: ")
                if choice == '1': #go WEST
                  map[curr_point] = 0
                  pROW = pROW - 1
                elif choice == '2': #go SOUTH
                  map[curr_point] = 0
                  pCOL = pCOL - 1
                else:
                  torch_active = True                                     #set the torch to active
                  p_item[0] - 1                                           #lose a torch
                  torch_time = 7                                          #start timer for torch (can edit time it lasts)
            elif p_item[0] == 0: #If no torches
                print("You have 2 options: ")
                print("Option 1: Go EAST")
                print("Option 2: Go SOUTH")
                choice = input()
                while(choice != '1' or choice != '2'):
                  choice = input("Invalid Selection new choice: ")
                if choice == '1': #go WEST
                  map[curr_point] = 0
                  pROW = pROW + 1
                elif choice == '2': #go SOUTH
                  map[curr_point] = 0
                  pCOL = pCOL - 1
            
#IF EAST and SOUTH
          elif(map[pROW + 1, pCOL] == ' ' and map[pROW, pCOL - 1] == ' '):
            previous_step = (pROW, pCOL)
            if p_item[1] >= 1:
                print("You have 3 options: ")
                print("Option 1: Go EAST")
                print("Option 2: Go SOUTH")
                print("Option 3: Light Torch")
                choice = input("You select: ")
                while(choice != '1' or choice != '2' or choice != '3'): #repeat until valid option is selected
                  choice = input("Invalid Selection new choice: ")
                if choice == '1': #go EAST
                  map[curr_point] = 0
                  pROW = pROW + 1
                elif choice == '2': #go SOUTH
                  map[curr_point] = 0
                  pCOL = pCOL - 1
                else:
                  torch_active = True                                     #set the torch to active
                  p_item[0] - 1                                           #lose a torch
                  torch_time = 7                                          #start timer for torch (can edit time it lasts)
            elif p_item[0] == 0: #If no torches
                print("You have 2 options: ")
                print("Option 1: Go EAST")
                print("Option 2: Go SOUTH")
                choice = input()
                while(choice != '1' or choice != '2'):
                  choice = input()
                if choice == '1': #go EAST
                  map[curr_point] = 0
                  pROW = pROW + 1
                elif choice == '2': #go SOUTH
                  map[curr_point] = 0
                  pCOL = pCOL - 1
#IF NORTH and SOUTH
          elif(map[pROW, pCOL + 1] == ' ' and map[pROW, pCOL - 1] == ' '):
            previous_step = (pROW, pCOL)
            if p_item[1] >= 1:
                print("You have 3 options: ")
                print("Option 1: Go NORTH")
                print("Option 2: Go SOUTH")
                print("Option 3: Light Torch")
                choice = input("You select: ")
                while(choice != '1' or choice != '2' or choice != '3'): #repeat until valid option is selected
                  choice = input("Invalid Selection new choice: ")
                if choice == '1': #go NORTH
                  map[curr_point] = 0
                  pCOL = pCOL + 1
                elif choice == '2': #go SOUTH
                  map[curr_point] = 0
                  pCOL = pCOL - 1
                else:
                  torch_active = True                                     #set the torch to active
                  p_item[0] - 1                                           #lose a torch
                  torch_time = 7                                          #start timer for torch (can edit time it lasts)
            elif p_item[0] == 0: #If no torches
                print("You have 2 options: ")
                print("Option 1: Go NORTH")
                print("Option 2: Go SOUTH")
                choice = input()
                while(choice != '1' or choice != '2'):
                  choice = input()
                if choice == '1': #go NORTH
                  map[curr_point] = 0
                  pCOL = pCOL + 1
                elif choice == '2': #go SOUTH
                  map[curr_point] = 0
                  pCOL = pCOL - 1

#If WEST AND EAST AVALIABLE
          elif map[pROW - 1, pCOL] = ' ' and map[pROW + 1, pCOL] = ' ':
            previous_step = (pROW, pCOL)
            if p_item[1] >= 1:
                print("You have 3 options: ")
                print("Option 1: Go WESTT")
                print("Option 2: Go EAST")
                print("Option 3: Light Torch")
                choice = input("You select: ")
                while(choice != '1' or choice != '2' or choice != '3'): #repeat until valid option is selected
                  choice = input("You select: ")
                  if choice == '1': #go WEST
                    map[curr_point] = 0
                    pROW = pROW - 1
                  elif choice == '2': #go EAST
                    map[curr_point] = 0
                    pROW = pROW + 1
                  else:
                    torch_active = True                                     #set the torch to active
                    p_item[0] - 1                                           #lose a torch
                    torch_time = 7                                          #start timer for torch (can edit time it lasts)
            elif p_item[0] == 0: #If no torches
                print("You have 2 options: ")
                print("Option 1: Go WEST")
                print("Option 2: Go EAST")
                choice = input()
                while(choice != '1' or choice != '2'):
                  choice = input()
                if choice == '1': #go WEST
                  map[curr_point] = 0
                  pROW = pROW - 1
                elif choice == '2': #go EAST
                  map[curr_point] = 0
                  pROW = pROW + 1


                


#IF WEST AND NORTH
          elif (map[prow - 1, pCOL] = ' ' and map[pROW, pCOL + 1] = ' '): #If WEST and NORTH
            previous_step = (pROW, pCOL)
            if p_item[1] >= 1:
                print("You have 3 options: ")
                print("Option 1: Go WEST")
                print("Option 2: Go NORTH")
                print("Option 3: Light Torch")
                choice = input("You select: ")
                while(choice != '1' or choice != '2' or choice != '3'): #repeat until valid option is selected
                  choice = input("Invalid Selection new choice: ")
                if choice == '1': #go WEST
                  map[curr_point] = 0
                  pROW = pROW - 1
                elif choice == '2': #go NORTH
                  map[curr_point] = 0
                  pCOL = pCOL + 1
                else:
                  torch_active = True                                     #set the torch to active
                  p_item[0] - 1                                           #lose a torch
                  torch_time = 7                                          #start timer for torch (can edit time it lasts)
            elif p_item[0] == 0: #If no torches
                print("You have 2 options: ")
                print("Option 1: Go WEST")
                print("Option 2: Go NORTH")
                choice = input()
                while(choice != '1' or choice != '2'):
                  choice = input("Invalid Selection new choice: ")
                if choice == '1': #go WEST
                  map[curr_point] = 0
                  pROW = pROW - 1
                elif choice == '2': #go NORTH
                  map[curr_point] = 0
                  pCOL = pCOL + 1


# If EAST AND NORTH
          elif (map[pROW + 1, pCOL] = ' ' and map[pROW, pCOL + 1] = ' '):
            previous_step = (pROW, pCOL)
            if p_item[1] >= 1:
                print("You have 3 options: ")
                print("Option 1: Go EAST")
                print("Option 2: Go NORTH")
                print("Option 3: Light Torch")
                choice = input("You select: ")
                while(choice != '1' or choice != '2' or choice != '3'): #repeat until valid option is selected
                  choice = input("Invalid Selection new choice: ")
                if choice == '1': #go EAST
                  map[curr_point] = 0
                  pROW = pROW + 1
                elif choice == '2': #go NORTH
                  map[curr_point] = 0
                  pCOL = pCOL + 1
                else:
                  torch_active = True                                     #set the torch to active
                  p_item[0] - 1                                           #lose a torch
                  torch_time = 7                                          #start timer for torch (can edit time it lasts)
            elif p_item[0] == 0: #If no torches
                print("You have 2 options: ")
                print("Option 1: Go EAST")
                print("Option 2: Go NORTH")
                choice = input()
                while(choice != '1' or choice != '2'):
                  choice = input("Invalid Selection new choice: ")
                if choice == '1': #go EAST
                  map[curr_point] = 0
                  pROW = pROW + 1
                elif choice == '2': #go NORTH
                  map[curr_point] = 0
                  pCOL = pCOL + 1


#IF ONLY NORTH
          elif (map[pROW, pCOL + 1] == ' '):
            previous_step = (pROW, pCOL)
            if p_item[0] >= 1 :                                         #if for having torch
              if (pROW, pCOL) == p_start and p_item[1] >= 1:            #if for if you are on starting square with dynamite
                print("You have 3 options: ")
                print("Option 1: Go NORTH")
                print("Option 2: Light Torch")
                print("Option 3: Throw Dynamite at Entrance")
                choice = input()
                while(choice != '1' or choice != '2' or choice != '3'):
                  choice = input("Invalid Selection, new choice: ")
                if choice == '1':                                         #go NORTH
                  pCOL = pCOL + 1
                elif choice == '2':
                  torch_active = True                                     #set the torch to active
                  p_item[0] - 1                                           #lose a torch
                  torch_time = 7                                          #start timer for torch (can edit time it lasts)      
                elif choice == '3':                                       #Throw Dynamite
                  if torch_active == True:
                    print("You lit the dynamite and cleared the entrance escaping.")
                    escape = True
                  else:
                    dynamite_boom_chance = rand(0,3)
                    if dynamite_boom_chance == 3:
                      print("You threw the dynamite at the entrance and it exploded clearing the rubble")
                      escape = True
                    else:
                      print("The dynamite didn't explode and is now wasted.")
                      p_item[1] - 1                                       #lose dynamite

#if you have a torch and no dynamite
              else:
                print("You have 2 options: ")
                print("Option 1: Go NORTH")
                print("Option 2: Light Torch")
                choice = input()
                while(choice != '1' or choice != '2'):
                  choice = input("Invalid Selection, new choice: ")
                if choice == '1':
                  pCOL = pCOL + 1
                elif choice == '2':
                  torch_active = True                                     #set the torch to active
                  p_item[0] - 1                                           #lose a torch
                  torch_time = 7                                          #start timer for torch (can edit time it lasts)
#if you have no torch and north is only option
            else:                                                         
              print("You have 1 options: ")
              print("Option 1: Go NORTH")
              choice = input()
              while(choice != '1'):
                choice = input("Invalid Selection, new choice: ")
              if choice == '1':
                pCOL = pCOL + 1

            else: #If no torches or dynamite
#IF ONLY SOUTH
          elif(map[pROW, pCOL - 1] == ' '):
            previous_step = (pROW, pCOL) 
            if p_item[1] >= 1:
                print("You have 2 options: ")
                print("Option 1: Go SOUTH")
                print("Option 2: Light Torch")
                choice = input()
                while (choice != '1' or '2'):
                  choice = input("Invalid Selection new choice: ")
                if choice == '1':
                  pCOL = pCOL - 1
                elif choice == '2':
                  torch_active = True                                     #set the torch to active
                  p_item[0] - 1                                           #lose a torch
                  torch_time = 7                                          #start timer for torch (can edit time it lasts)  

            elif p_item[0] == 0: #If no torches
                print("You have 1 options: ")
                print("Option 1: Go SOUTH")
                choice = input()
                while(choice != '1'):
                  choice = input("Invalide Selection new choice: ")
                if choice == '1':
                  pCOL = pCOL - 1
                
            


#IF ONLY EAST
          elif (map[pROW + 1, pCOL] = ' '):
            previous_step = (pROW, pCOL) 
            if p_item[1] >= 1:
                print("You have 2 options: ")
                print("Option 1: Go EAST")
                print("Option 2: Light Torch")
                choice = input()
                while (choice != '1' or '2'):
                  choice = input("Invalid Selection new choice: ")
                if choice == '1':
                  pROW = pROW + 1
                elif choice == '2':
                  torch_active = True                                     #set the torch to active
                  p_item[0] - 1                                           #lose a torch
                  torch_time = 7                                          #start timer for torch (can edit time it lasts)  

            elif p_item[0] == 0: #If no torches
                print("You have 1 options: ")
                print("Option 1: Go EAST")
                choice = input()
                while(choice != '1'):
                  choice = input("Invalide Selection new choice: ")
                if choice == '1':
                  pROW = pROW + 1



#IF ONLY WEST            
          elif (map[pROW - 1, pCOL] = ' '):
            previous_step = (pROW, pCOL) 
            if p_item[1] >= 1:
                print("You have 2 options: ")
                print("Option 1: Go WEST")
                print("Option 2: Light Torch")
                choice = input()
                while (choice != '1' or '2'):
                  choice = input("Invalid Selection new choice: ")
                if choice == '1':
                  pROW = pROW - 1
                elif choice == '2':
                  torch_active = True                                     #set the torch to active
                  p_item[0] - 1                                           #lose a torch
                  torch_time = 7                                          #start timer for torch (can edit time it lasts)  

            elif p_item[0] == 0: #If no torches
                print("You have 1 options: ")
                print("Option 1: Go WEST")
                choice = input()
                while(choice != '1'):
                  choice = input("Invalide Selection new choice: ")
                if choice == '1':
                  pROW = pROW - 1

#IF ONLY SOUTH

#End of LOOP STUFF
          if torch_active = True:
            torch_time = torch_time - 1:
          if torch_time == 0:
            torch_active = False
            print("Torch has run out you feel more cold")
          step = step + 1
          if step == num_turns:
            print("You ran out of oxygen!!!!")
            death = True

def Kill_Room(curr_point):
  if curr_point == (0,3):
    print("You were devoured by cannibals!")
    return True 
  elif curr_point == (3,18):
    print("You were crushed by Boulders!")
    return True
  elif curr_point == (4,36): 
    print("You were attacked by poisonous spiders!")
    return True
  elif curr_point == (10,38):
    print("The floor caves in below you!")
    return True  
  elif curr_point == (12,7):
    print("You were impaled by a stalactite!")
    return True  
  elif curr_point == (17,36):
    print("The ceiling caves in, and water falls in drowning you!")
    return True
  elif curr_point == (20,16):
    print("You were ran over by a mine cart!!")
    return True
  else:
    return False
def Loot_Room(curr_point):
  if curr_point == (3,12) or curr_point == (3,36) or curr_point == (12,9) or curr_point == (13,13) or curr_point == (14,17) or curr_point == (14,31) or curr_point == (20,7):
    return True
  else:
    return False
def Dead_End(curr_point):
  if curr_point == (0,24) or curr_point == (0,33) or curr_point == (6,33) or curr_point == (11,17) or curr_point == (13,36) or curr_point == (20,24):
    print("You have reached a Deadend go back to last check point")
    return True
  else:
    return False
def Checkpoints(curr_point):
  if curr_point == (0,17) or curr_point == (4,33) or curr_point == (6,20) or curr_point == (13,24) or curr_point == (3,28):
    return True
  else:
    return False
def Win(curr_pint):
  if curr_point == (8,29):
    return True
  else:
    return False




