import pygame, sys, csv, os
from Settings import Settings
import Button
from pathlib import Path
from text_file_reader import read_from_file
from functions import create_static, load_stage, manage_text


    


def run_game():
    ###################################################################################
    #initialize pygame and "static" elements
    
    pygame.init()
    setting = Settings()

    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    text_screen = pygame.Surface((590, 570))
    text_screen.fill((230, 230, 230))

    font = pygame.font.SysFont("comicsansms", 25)
    normal_font = pygame.font.SysFont("calibri", 27)

    current_stage = load_stage('test')
    write_array = []
    just_text = current_stage.arr

    create_static(screen, setting)
    
    map = pygame.Surface((250, 250))
    
    done = False

    buttons = current_stage.button_arr

    ########################################################################################

    #main gameplay loop, redraw changable elements
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        current_stage = load_stage(button.link)
                        just_text = current_stage.arr
                        buttons = current_stage.button_arr
        
        screen.blit(map, (900, 50))
        screen.blit(text_screen, (256,0))

        for button in buttons:
            button.render(screen, font)

        manage_text(screen, just_text)

        
        pygame.display.flip()



    

run_game()