import pygame,sys
from print_template import *
from button import Button
from game_ended import game_over_lose
from game_ended import game_over_win
#from easy_mode import easy_mode
#from hard_mode import hard_mode

def Difficulty(SCREEN,get_font,main_menu):
    while True:
        DIFF_MOUSE_POS = pygame.mouse.get_pos() #track mouse position on this screen

        SCREEN.fill("black") #remove all rendered graphics by replacing it with a black screen

        #render select difficulty text
        printLine(SCREEN,"Select Difficulty", "White", 45, 640, 100, get_font)
        

        #render easy button
        DIFF_EASY = Button(image=None, pos=(640, 260), 
                            text_input="EASY", font=get_font(75), base_color="White", hovering_color="Green")
        DIFF_EASY.changeColor(DIFF_MOUSE_POS)
        DIFF_EASY.update(SCREEN)

        #render hard button
        DIFF_HARD = Button(image=None, pos=(640, 360), 
                            text_input="HARD", font=get_font(75), base_color="White", hovering_color="Green")
        DIFF_HARD.changeColor(DIFF_MOUSE_POS)
        DIFF_HARD.update(SCREEN)

        #render back button
        DIFF_BACK = Button(image=None, pos=(640, 560), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        DIFF_BACK.changeColor(DIFF_MOUSE_POS)
        DIFF_BACK.update(SCREEN)

        #check for events
        for event in pygame.event.get():
            #if x is pressed, close the console
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                #if back is pressed, go to main menu
                if DIFF_BACK.checkForInput(DIFF_MOUSE_POS):
                    main_menu()
                #if easy is pressed, begin easy mode function
                if DIFF_EASY.checkForInput(DIFF_MOUSE_POS):
                    easy_mode(SCREEN,get_font,main_menu)
                #if hard button is pressed, begin hard mode function (we don't have a hard mode, so they both do easy)
                if DIFF_HARD.checkForInput(DIFF_MOUSE_POS):
                    game_over_lose(SCREEN,get_font,main_menu)

        #render everything
        pygame.display.update()
