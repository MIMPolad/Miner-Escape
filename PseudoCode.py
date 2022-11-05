print("Type 1 for Easy Mode: ")
print("Type 2 for Hard Mode: ")
print("Type 3 for Quit: ")
Selection = input()
do
  match
    case "1"
      #VARIABLES
        array[]
        p_start = (16,0)
        #first index is number of torches second number represents number of dynamite
        p_item = [ 1,0 ]
        location = (16, 0)
        escape = false
        FLAG DICTIONARY
        step_count = 1
        num_turns = 400
        pROW = 16
        pCOL = 0
      #BEGIN CODE
        while(escape = false):
          step = 1


#IF LEFT, RIGHT, and STRAIGHT AVALIABLE
          if((pROW + 1, pCOL) = ' ' and (pROW - 1, pCOL) = ' ' and (pROW, pCOL + 1) = ' '): 
            if p_item[0] >= 1: 
                print("You have 4 options: ")
                print("Option 1: Go LEFT")
                print("Option 2: Go RIGHT")
                print("Option 3: Go STRAIGHT")
                print("Option 4: Light Torch")
            elif p_item[0] == 0: #If no torches
                print("You have 3 options: ")
                print("Option 1: Go LEFT")
                print("Option 2: Go RIGHT")
                print("Option 3: Go STRAIGHT")
            


#If LEFT AND RIGHT AVALIABLE
          elif ((pROW + 1, pCOL) = ' ' and (pROW - 1, pCOL) = ' '):
            if p_item[1] >= 1 and p_item[2] > 1:
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
            if p_item[1] >= 1 and p_item[2] > 1:
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
 #CASE 2 is for HARD MODE
    case "2"
 #CASE 3 is for QUITING
    case "3"
      quit = true



while(quit = no)
