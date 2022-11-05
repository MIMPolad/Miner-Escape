import random
print("Type 1 for Easy Mode: ")
print("Type 2 for Hard Mode: ")
print("Type 3 for Quit: ")
Selection = input()
do:
  match
    case "1" #EASY MODE
#VARIABLES
        map = []
        p_start = (16,0)
        #first index is number of torches second number represents number of dynamite
        p_item = [ 1,0 ]
        location = (16, 0)
        step = 1
        escape = False
        checkpoint = (16, 0) #checkpoint that changes at certain points
        checkpoint_curr_steps = 0
        step_count = 1
        num_turns = 400
        pROW = 16
        pCOL = 0
        torch_active = False
        torch_time = 0
        curr_point = (pROW, pCOL)
        previous_step = (0,0)
        death = False
#BEGIN CODE
#STRAIGHT IS NORTH (player moves one right)
#LEFT IS WEST (player moves one up)
#RIGHT IS EAST (plaer moves one down)
        while(escape != True or death != True):


#If you hit a checkpoint save it 
          if Checkpoints(curr_point) == True:
            checkpoint = curr_point
            checkpoint_curr_steps = step_count

#If the room you enter is loot room        
          if Loot_Room(curr_point) == True:
            loot = rand_init(0,3)
            if loot == 0:
              print("You found a torch")
              p_item[0] + 1
            elif loot == 1:
              print("You found a dynamite")
              p_item[1] + 1
            elif loot == 2:
              p_item[2] + 1
              print("You found a pickaxe")
            else
              print("You found nothing")
            curr_point = 0 #set the loot room to already visited
            curr_point = previous_step #go back to before the room
            
#If the room you enter is death room
          elif Kill_Room(curr_point) == True:
            death = True




#If the step led to dead end
          elif Dead_End(curr_point) == True:
            curr_point = checkpoint
            step_count = step_count + (step_count - checkpoint_curr_steps)


#If LEFT, RIGHT, and STRAIGHT
          elif((pROW + 1, pCOL) = ' ' and (pROW - 1, pCOL) = ' ' and (pROW, pCOL + 1) = ' '): 
            previous_step = (pROW, pCOL)
            if p_item[0] >= 1: 
                print("You have 4 options: ")
                print("Option 1: Go LEFT")
                print("Option 2: Go RIGHT")
                print("Option 3: Go STRAIGHT") 
                print("Option 4: Light Torch")
                choice = input()
                if choice == 1:
                  curr_point = 0
                  pROW = pROW + 1
                  
                elif choice == 2:
                  curr_point = 0
                  pROW = pROW - 1

                elif choice == 3:
                  curr_point = 0
                  pCOL = pCOL + 1

                elif choice == 4:
                  torch_active = True #set the torch to active
                  p_item[0] - 1 #lose a torch
                  torch_time = 7 #start timer for torch (can edit time it lasts)


            elif p_item[0] == 0: #If no torches
                print("You have 3 options: ")
                print("Option 1: Go LEFT")
                print("Option 2: Go RIGHT")
                print("Option 3: Go STRAIGHT")
                choice = input()
                if choice == 1: #go LEFT
                  pROW = pROW + 1
                  
                elif choice == 2:#go RIGHT
                  pROW = pROW - 1

                elif choice == 3:#go STRAIGHT
                  pCOL = pCOL + 1




#If LEFT AND RIGHT AVALIABLE
          elif ((pROW + 1, pCOL) = ' ' and (pROW - 1, pCOL) = ' '):
            if p_item[1] >= 1:
                print("You have 4 options: ")
                print("Option 1: Go LEFT")
                print("Option 2: Go RIGHT")
                print("Option 3: Light Torch")
            elif p_item[0] == 0: #If no torches
                print("You have 3 options: ")
                print("Option 1: Go LEFT")
                print("Option 2: Go RIGHT")
                print("Option 3: Go STRAIGHT")


#IF LEFT AND STRAIGHT
          elif ((prow - 1, pCOL) = ' ' and (pROW, pCOL + 1) = ' '):#If left and straight
            if p_item[1] >= 1:
                print("You have 4 options: ")
                print("Option 1: Go LEFT")
                print("Option 2: Go STRAIGHT")
                print("Option 3: Light Torch")
            elif p_item[0] == 0: #If no torches
                print("You have 2 options: ")
                print("Option 1: Go LEFT")
                print("Option 2: Go STRAIGHT")


# If RIGHT AND STRAIGHT
          elif ((pROW + 1, pCOL) = ' ' and (pROW, pCOL + 1) = ' '):
            if p_item[1] >= 1:
                print("You have 3 options: ")
                print("Option 1: Go RIGHT")
                print("Option 2: Go STRAIGHT")
                print("Option 3: Light Torch")
            elif p_item[0] == 0: #If no torches
                print("You have 3 options: ")
                print("Option 1: Go RIGHT")
                print("Option 2: Go STRAIGHT")


#IF ONLY STRAIGHT
          elif ((pROW, pCOL + 1) = ' '):
            if p_item[0] >= 1 :
              if (pROW, pCOL) == p_start and p_item[1] >= 1:
                print("You have 3 options: ")
                print("Option 1: Go STRAIGHT")
                print("Option 2: Light Torch")
                print("Option 3: Throw Dynamite at Entrance")
              else:
                print("You have 2 options: ")
                print("Option 1: Go STRAIGHT")
                print("Option 2: Light Torch")
            else: #If no torches or dynamite


#IF ONLY RIGHT
          elif ((pROW + 1, pCOL) = ' '): 
            if p_item[1] >= 1:
                print("You have 2 options: ")
                print("Option 1: Go RIGHT")
                print("Option 2: Light Torch")
            elif p_item[0] == 0: #If no torches
                print("You have 1 options: ")
                print("Option 1: Go RIGHT")



#IF ONLY LEFT            
          elif ((pROW - 1, pCOL) = ' '): 
            if p_item[1] >= 1:
                print("You have 2 options: ")
                print("Option 1: Go LEFT")
                print("Option 2: Light Torch")
            elif p_item[0] == 0: #If have torches but no dynamite
                print("You have 1 option: ")
                print("Option 1: Go LEFT")


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
    case "2"
    case "3"
      quit = true



while(quit = no)


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
