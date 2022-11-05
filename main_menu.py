import pygame, sys
import webbrowser
from button import Button
from game import *

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Miner Odyssey")

BG = pygame.image.load("Assets/caveMenu.png")


def get_font(size): # Returns font 1 in the desired size
    return pygame.font.Font("Assets/font.ttf", size)
def get_font2(size): # returns font 2 in desired size
    return pygame.font.Font("Assets/creditsFont.ttf", size)

def Difficulty():
    while True:
        DIFF_MOUSE_POS = pygame.mouse.get_pos() #track mouse position on this screen

        SCREEN.fill("black") #remove all rendered graphics by replacing it with a black screen

        DIFF_TEXT = get_font(45).render("Select Difficulty", True, "White")
        DIFF_RECT = DIFF_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(DIFF_TEXT, DIFF_RECT)

        DIFF_EASY = Button(image=None, pos=(640, 260), 
                            text_input="EASY", font=get_font(75), base_color="White", hovering_color="Green")
        DIFF_EASY.changeColor(DIFF_MOUSE_POS)
        DIFF_EASY.update(SCREEN)

        DIFF_HARD = Button(image=None, pos=(640, 360), 
                            text_input="HARD", font=get_font(75), base_color="White", hovering_color="Green")
        DIFF_HARD.changeColor(DIFF_MOUSE_POS)
        DIFF_HARD.update(SCREEN)

        DIFF_BACK = Button(image=None, pos=(640, 560), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        DIFF_BACK.changeColor(DIFF_MOUSE_POS)
        DIFF_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if DIFF_BACK.checkForInput(DIFF_MOUSE_POS):
                    main_menu()
                if DIFF_EASY.checkForInput(DIFF_MOUSE_POS):
                    easy_mode()
                if DIFF_HARD.checkForInput(DIFF_MOUSE_POS):
                    hard_mode()

        pygame.display.update()

def hyperlink():
  webbrowser.open("https://pickhacks.io/")

    
def credits():
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        CREDITS_TEXT = get_font2(80).render("This game was coded by: "
        , True, "Black")
        CREDITS_TEXT2 = get_font2(45).render("Kellen Mezines, Calen Carter, Jack Holland,"
        , True, "Black")
        CREDITS_TEXT3 = get_font2(45).render("and Riley Fuller"
        , True, "Black")
        CREDITS_TEXT4 = get_font2(30).render("Riley Fuller (Drip) - Level Design, Level Tester, Marketing Lead"
        , True, "Blue")
        CREDITS_TEXT5 = get_font2(30).render("Calen Carter (Bluto) - Level Design, Level Tester"
        , True, "Red")
        CREDITS_TEXT6 = get_font2(30).render("Kellen Mezines (Vibe)- UI/UX Design, Development"
        , True, "Purple")
        CREDITS_TEXT7 = get_font2(30).render("Jack Holland (Redwood) - Development"
        , True, "Green")
        
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 30))
        CREDITS_RECT2 = CREDITS_TEXT2.get_rect(center=(640, 90))
        CREDITS_RECT3 = CREDITS_TEXT3.get_rect(center=(640, 130))
        CREDITS_RECT4 = CREDITS_TEXT4.get_rect(center=(640, 250))
        CREDITS_RECT5 = CREDITS_TEXT5.get_rect(center=(640, 300))
        CREDITS_RECT6 = CREDITS_TEXT6.get_rect(center=(640, 350))
        CREDITS_RECT7 = CREDITS_TEXT7.get_rect(center=(640, 400))
        
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)
        SCREEN.blit(CREDITS_TEXT2, CREDITS_RECT2)
        SCREEN.blit(CREDITS_TEXT3, CREDITS_RECT3)
        SCREEN.blit(CREDITS_TEXT4, CREDITS_RECT4)
        SCREEN.blit(CREDITS_TEXT5, CREDITS_RECT5)
        SCREEN.blit(CREDITS_TEXT6, CREDITS_RECT6)
        SCREEN.blit(CREDITS_TEXT7, CREDITS_RECT7)

        OPTIONS_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font2(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(CREDITS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(CREDITS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

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
                    Difficulty()
                #if credits button pushed, go to credit function
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
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