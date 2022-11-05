import pygame
from button import Button
def printLine(SCREEN,text, color, size, xval, yval, get_font):
    PRINT_TEXT = get_font(size).render(text, True, color)
    PRINT_RECT = PRINT_TEXT.get_rect(center=(xval, yval))
    SCREEN.blit(PRINT_TEXT, PRINT_RECT)

def printButton(SCREEN,MOUSE_POS,get_font,text,size,xval,yval):
        PRNTBTN = Button(image=None, pos=(xval, yval), 
                            text_input= text, font=get_font(size), base_color="White", hovering_color="Green")
        PRNTBTN.changeColor(MOUSE_POS)
        PRNTBTN.update(SCREEN)