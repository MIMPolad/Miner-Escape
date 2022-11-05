import pygame, sys
import webbrowser
from button import Button
from game import *
from credits import credits
from difficulty import Difficulty

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Miner Odyssey")

BG = pygame.image.load("Assets/caveMenu.png")


def get_font(size): # Returns font 1 in the desired size
    return pygame.font.Font("Assets/font.ttf", size)
def get_font2(size): # returns font 2 in desired size
    return pygame.font.Font("Assets/creditsFont.ttf", size)


def hyperlink():
    #use webbrowser.open to open the website
  webbrowser.open("https://pickhacks.io/")

def main_menu():
    while True:
        SCREEN.fill("Black") #fill the screen black so that any extra graphics are removed and the screen is fresh
        SCREEN.blit(BG, (0, 0)) #add the cave background image at position 0,0


        MENU_MOUSE_POS = pygame.mouse.get_pos() #get the position of the mouse

        TITLE_TEXT = get_font(75).render("Miner Odyssey", True, "#b68f40") #make variable for the main title
        TITLE_RECT = TITLE_TEXT.get_rect(center=(640, 100)) #make variable for main title position

        HYPERLINK_TEXT = get_font(15).render("Click on Joe to see what PickHacks is up to!", True, "Green") #make varable for the text under joe
        HYPERLINK_RECT = HYPERLINK_TEXT.get_rect(center=(950,700)) #make variable for hyperlink position

        # make variables for all main menu buttons
        PLAY_BUTTON = Button(image=pygame.image.load("Assets/button.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        CREDITS_BUTTON = Button(image=pygame.image.load("Assets/button.png"), pos=(640, 400), 
                            text_input="CREDITS", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        QUIT_BUTTON = Button(image=pygame.image.load("Assets/button.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        HYPERLINK_BUTTON = Button(image = pygame.image.load("Assets/JoeMinerHead.png"),pos=(1150,600),
                            text_input = "", font = get_font(0), base_color = "#d7fcd4", hovering_color="Green")

        # render main title and hyperlink text
        SCREEN.blit(TITLE_TEXT, TITLE_RECT)
        SCREEN.blit(HYPERLINK_TEXT, HYPERLINK_RECT)

        # loop to check if mouse position is on any button, if yes, change color from base to hover value
        for button in [PLAY_BUTTON, CREDITS_BUTTON, QUIT_BUTTON, HYPERLINK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        #start to check for events
        for event in pygame.event.get():

            #if the topright x is clicked, exit game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #else, check to see if a button was clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if play button is pushed, go to difficulty function
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Difficulty(SCREEN,get_font,main_menu)
                #if credits button pushed, go to credit function
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits(SCREEN,get_font2,main_menu)
                #if quit button pushed, end program
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                #if joe miner pushed, run hyperlink function
                if HYPERLINK_BUTTON.checkForInput(MENU_MOUSE_POS):
                  hyperlink()

        #display all changes made this cycle
        pygame.display.update()

#when program is started, run main_menu function
main_menu()