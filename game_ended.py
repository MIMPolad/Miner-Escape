import pygame, sys
from button import Button

def game_over_win(SCREEN,get_font,main_menu):
 while True:
        #create image variables
        winImage = pygame.image.load("Assets/cave_exit.jpg")
        joeFull = pygame.image.load("Assets/JoeMinerFull.png")

        #track mouse position
        WIN_MOUSE_POS = pygame.mouse.get_pos()

        #fill background color yellow
        SCREEN.fill("#FFD700")

        #create win text
        WIN_TEXT = get_font(50).render("YOU'VE ESCAPED THE MINE!"
        , True, "Black")
        WIN_RECT = WIN_TEXT.get_rect(center=(640, 50))
        
        #render images and win text
        SCREEN.blit(winImage, (325, 100)) 
        SCREEN.blit(joeFull, (700, 400))
        SCREEN.blit(WIN_TEXT, WIN_RECT)

        #create back button
        LOSE_BACK = Button(image=None, pos=(640, 640), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        LOSE_BACK.changeColor(WIN_MOUSE_POS)
        LOSE_BACK.update(SCREEN)

        #check events
        for event in pygame.event.get():
            #if x clicked, exit console
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if back pressed, return to main menu
                if LOSE_BACK.checkForInput(WIN_MOUSE_POS):
                    main_menu()

        #render all
        pygame.display.update()

def game_over_lose(SCREEN,get_font,main_menu):
 while True:

        #Create lose image variable
        loseImage = pygame.image.load("Assets/death_image.jpg")

        #track mouse position
        LOSE_MOUSE_POS = pygame.mouse.get_pos()

        #fill background black
        SCREEN.fill("Black")

        #create lose texts
        LOSE_TEXT = get_font(50).render("GAME OVER!"
        , True, "White")
        LOSE_TEXT2 = get_font(50).render("YOU DIED"
        ,True, "#880808")
        
        #create lose text position
        LOSE_RECT = LOSE_TEXT.get_rect(center=(640, 100))
        LOSE_RECT2 = LOSE_TEXT2.get_rect(center=(640,200))

        #render image and text
        SCREEN.blit(loseImage, (500, 250))
        SCREEN.blit(LOSE_TEXT, LOSE_RECT)
        SCREEN.blit(LOSE_TEXT2,LOSE_RECT2)

        #create back button
        LOSE_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        LOSE_BACK.changeColor(LOSE_MOUSE_POS)
        LOSE_BACK.update(SCREEN)

        #check for events
        for event in pygame.event.get():
            #if x is clicked, exit console
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if back button is pressed, return to main menu
                if LOSE_BACK.checkForInput(LOSE_MOUSE_POS):
                    main_menu()

        #render all
        pygame.display.update()