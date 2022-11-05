import pygame,random, sys
from game_ended import *
from print_template import *

def Win(curr_point):
  if curr_point == (8,29):
    return True
  else:
    return False

def Checkpoints(curr_point):
  if curr_point == (0,17) or curr_point == (4,33) or curr_point == (6,20) or curr_point == (13,24) or curr_point == (3,28):
    return True
  else:
    return False

def Loot_Room(curr_point):
  if curr_point == (3,12) or curr_point == (3,36) or curr_point == (12,9) or curr_point == (13,13) or curr_point == (14,17) or curr_point == (14,31) or curr_point == (20,7):
    return True
  else:
    return False

def easy_mode(SCREEN,get_font,main_menu):
    while True:
        GAME_MOUSE_POS = pygame.mouse.get_pos()
        #VARIABLES
        map = []
        p_start = (16,0)
        #first index is number of torches second number represents number of dynamite
        p_item = [ 1,0 ]
        start_location = (16, 0)
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

        #If you hit a checkpoint save it 
        if Checkpoints(curr_point) == True:
            checkpoint = curr_point
            checkpoint_curr_steps = step_count
        
        #If you reach the win room at the end of the mine
        if Win(curr_point) == True:
            escape = True

        elif Loot_Room(curr_point) == True:
            loot = rand_init(0,3)
            if loot == 0:
                p_item[0] + 1
                printLine(SCREEN,"You found a torch!", "White", 20, 100, 100, get_font)
            elif loot == 1:
                p_item[1] + 1
                printLine(SCREEN,"You found a dynamite!", "White", 20, 100, 100, get_font)
            elif loot == 2:
                p_item[2] + 1
                printLine(SCREEN,"You found a pickaxe!", "White", 20, 100, 100, get_font)
            else:
                printLine(SCREEN,"You found nothing...", "White", 20, 100, 100, get_font)
            map[curr_point] = 0
            if loot == 1 or loot == 2:
                if loot == 1:
                    printLine(SCREEN,"would you like to retrace steps?", "White", 20, 100, 100, get_font) #NEED A BUTTON
                    YES_BUTTON1 = Button(image=None, pos=(640, 560), 
                            text_input="YES", font=get_font(75), base_color="White", hovering_color="Green")
                    YES_BUTTON1.changeColor(GAME_MOUSE_POS)
                    YES_BUTTON1.update(SCREEN)
        
        
        if death == True:
            game_over_lose(SCREEN,get_font,main_menu)
        if escape == True:
            game_over_win(SCREEN,get_font,main_menu)

        for event in pygame.event.get():
            #if x is clicked, exit console
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if back button is pressed, return to main menu
                if YES_BUTTON1.checkForInput(GAME_MOUSE_POS):
                    steps = steps * 2                                                                                           #Retrace steps (double them)
                    curr_point = start_location                                                                                 #Go back to start location
                    if torch_active:
                        printLine(SCREEN,"You lit the dynamite and escaped!!!", "White", 20, 100, 100, get_font)
                        escape = True
            

        #render everything
        pygame.display.update()



