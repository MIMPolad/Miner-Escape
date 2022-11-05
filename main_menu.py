import pygame, sys
import webbrowser
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Miner Odyssey")

BG = pygame.image.load("Assets/caveMenu.png")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def hyperlink():
  webbrowser.open("https://pickhacks.io/")

    
def credits():
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        CREDITS_TEXT = get_font(45).render("This game was coded by: "
        , True, "Black")
        CREDITS_TEXT2 = get_font(25).render("Kellen Mezines, Calen Carter, Jack Holland,"
        , True, "Black")
        CREDITS_TEXT3 = get_font(25).render("and Riley Fuller"
        , True, "Black")
        CREDITS_TEXT4 = get_font(15).render("Riley Fuller (Drip) - Level Design, Level Tester, Marketing Lead"
        , True, "Blue")
        CREDITS_TEXT5 = get_font(15).render("Calen Carter (Bluto) - Level Design, Level Tester"
        , True, "Red")
        CREDITS_TEXT6 = get_font(15).render("Kellen Mezines (Vibe)- UI/UX Design, Development"
        , True, "Purple")
        CREDITS_TEXT7 = get_font(15).render("Jack Holland (Redwood) - Development"
        , True, "Green")
        
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 30))
        CREDITS_RECT2 = CREDITS_TEXT2.get_rect(center=(640, 90))
        CREDITS_RECT3 = CREDITS_TEXT3.get_rect(center=(640, 120))
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
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

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
        SCREEN.fill("Black")
        SCREEN.blit(BG, (0, 0))


        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(75).render("Miner Odyssey", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        HYPERLINK_TEXT = get_font(15).render("Click on Joe to see what PickHacks is up to!", True, "Green")
        HYPERLINK_RECT = HYPERLINK_TEXT.get_rect(center=(950,700))

        PLAY_BUTTON = Button(image=pygame.image.load("Assets/button.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        CREDITS_BUTTON = Button(image=pygame.image.load("Assets/button.png"), pos=(640, 400), 
                            text_input="CREDITS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Assets/button.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        HYPERLINK_BUTTON = Button(image = pygame.image.load("Assets/JoeMinerHead.png"),pos=(1150,600),
                            text_input = "", font = get_font(0), base_color = "#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(HYPERLINK_TEXT, HYPERLINK_RECT)

        for button in [PLAY_BUTTON, CREDITS_BUTTON, QUIT_BUTTON, HYPERLINK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if HYPERLINK_BUTTON.checkForInput(MENU_MOUSE_POS):
                  hyperlink()

        pygame.display.update()

main_menu()