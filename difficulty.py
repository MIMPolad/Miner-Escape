import pygame,sys
from button import Button
from game_ended import game_over_lose
from game_ended import game_over_win
#from easy_mode import easy_mode
#from hard_mode import hard_mode

def Difficulty(SCREEN,get_font,main_menu):
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
                    game_over_lose(SCREEN,get_font,main_menu)
                if DIFF_HARD.checkForInput(DIFF_MOUSE_POS):
                    game_over_win(SCREEN,get_font,main_menu)

        pygame.display.update()
