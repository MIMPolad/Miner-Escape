import pygame, sys
from button import Button

def game_over_win(SCREEN,get_font2,main_menu):
 while True:

        winImage = pygame.image.load("Assets/cave_exit.jpg")
        joeFull = pygame.image.load("Assets/JoeMinerFull.png")

        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#FFD700")

        CREDITS_TEXT = get_font2(50).render("YOU'VE ESCAPED THE MINE!"
        , True, "Black")
        
        
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 50))
        
        SCREEN.blit(winImage, (325, 100)) 
        SCREEN.blit(joeFull, (700, 400))
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 640), 
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

def game_over_lose(SCREEN,get_font2,main_menu):
 while True:
        loseImage = pygame.image.load("Assets/death_image.jpg")

        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        CREDITS_TEXT = get_font2(50).render("GAME OVER!"
        , True, "White")
        LOSE_TEXT2 = get_font2(50).render("YOU DIED"
        ,True, "#880808")
        
        
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 100))
        LOSE_RECT2 = LOSE_TEXT2.get_rect(center=(640,200))

        SCREEN.blit(loseImage, (500, 250))
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)
        SCREEN.blit(LOSE_TEXT2,LOSE_RECT2)

        OPTIONS_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font2(75), base_color="White", hovering_color="Green")

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