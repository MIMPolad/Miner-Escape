import pygame,sys
from button import Button


def credits(SCREEN,get_font2,main_menu):
    while True:

        #track mouse position
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        #fill the background white
        SCREEN.fill("white")

        #create all credits text variables
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
        CREDITS_TEXT7 = get_font2(30).render("Jack Holland (Redwood) - Development, Quality control Consultant"
        , True, "Green")
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 30))
        CREDITS_RECT2 = CREDITS_TEXT2.get_rect(center=(640, 90))
        CREDITS_RECT3 = CREDITS_TEXT3.get_rect(center=(640, 130))
        CREDITS_RECT4 = CREDITS_TEXT4.get_rect(center=(640, 250))
        CREDITS_RECT5 = CREDITS_TEXT5.get_rect(center=(640, 300))
        CREDITS_RECT6 = CREDITS_TEXT6.get_rect(center=(640, 350))
        CREDITS_RECT7 = CREDITS_TEXT7.get_rect(center=(640, 400))
        
        #render all credit text
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)
        SCREEN.blit(CREDITS_TEXT2, CREDITS_RECT2)
        SCREEN.blit(CREDITS_TEXT3, CREDITS_RECT3)
        SCREEN.blit(CREDITS_TEXT4, CREDITS_RECT4)
        SCREEN.blit(CREDITS_TEXT5, CREDITS_RECT5)
        SCREEN.blit(CREDITS_TEXT6, CREDITS_RECT6)
        SCREEN.blit(CREDITS_TEXT7, CREDITS_RECT7)

        #create back button
        CREDITS_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font2(75), base_color="Black", hovering_color="Green")
        CREDITS_BACK.changeColor(CREDITS_MOUSE_POS)
        CREDITS_BACK.update(SCREEN)

        #check for events
        for event in pygame.event.get():
            #if x is clicked, close game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if back is pressed, go back to main menu
                if CREDITS_BACK.checkForInput(CREDITS_MOUSE_POS):
                    main_menu()

        #render all
        pygame.display.update()