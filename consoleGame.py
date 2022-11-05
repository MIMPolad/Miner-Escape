import pygame,sys
from print_template import printLine
from game_ended import *

def easy_mode_console(SCREEN,get_font,main_menu):
    while True:
        SCREEN.fill("black") #remove all rendered graphics by replacing it with a black screen

        #render select difficulty text
        printLine(SCREEN,"Easy Mode Started, Check your Console!", "White", 45, 640, 100, get_font)
        printLine(SCREEN,"Good Luck!!!", "Green", 45, 640, 150, get_font)
        
        won = True#main()
        
        for event in pygame.event.get():
            #if x is pressed, close the console
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if won == True:
                game_over_win(SCREEN,get_font, main_menu)
            if won == False:
                game_over_lose(SCREEN,get_font, main_menu)


        pygame.display.update()