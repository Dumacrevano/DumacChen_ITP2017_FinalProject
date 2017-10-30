from pygame import *
import sys
import pygame

def menu_screen(Button,run_game):
    """make the screen for menu"""
    display.set_caption("Jet Mission")
    screen = pygame.display.set_mode((800, 600))
    #object button for quit and start
    start_button = Button("New Piskel.png")
    quit_button = Button("quit button.png")
    #image for the menu's backgound
    bg_image=pygame.image.load("asteroid_wall.jpg")
    bg_image=pygame.transform.scale(bg_image, (800, 600))


    pygame.init()

    while True:
        rect_start= draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))
        screen.blit(bg_image,(0,0))

        screen.blit(start_button.button,(250,200))
        screen.blit(quit_button.button,(250,300))

        ev=event.wait()

        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()):
                sys.exit()

        if ev.type == QUIT:
            sys.exit()

        display.update()

def pause_menu(Button,run_game):
    """pause_menu"""
    #make the screen display
    display.set_caption("Jet Mission")
    screen = pygame.display.set_mode((800, 600))

    # object button for quit and start
    start_button = Button("quit button.png")
    return_button = Button("pause button.png")

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall.jpg")
    bg_image = pygame.transform.scale(bg_image, (800, 600))


    pygame.init()
    paused=True #flag
    while paused:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))
        rect_return = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))
        screen.blit(bg_image, (0, 0))

        screen.blit(start_button.button, (250, 200))
        screen.blit(return_button.button, (250, 300))

        ev = event.wait()

        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):
                menu_screen(Button,run_game)
            if rect_return.collidepoint(mouse.get_pos()):
                paused = False #flag become  False

        if ev.type == QUIT:
            sys.exit()


        display.update()
