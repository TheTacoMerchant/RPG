import pygame, sys, csv, os
from Settings import Settings
import Button
from pathlib import Path
from text_file_reader import read_from_file


    


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
    write_array = []
    just_text = load_stage('test')

    portrait = pygame.Surface((170, 170))
    map = pygame.Surface((250, 250))
    square = pygame.Surface((50, 50))
    pygame.display.set_caption("RPG")
    done = False
    button1 = Button.Button("Button1", "None", (280, 620), pygame.Surface((230, 30)))
    button2 = Button.Button("Button2", "None", (280, 680), pygame.Surface((230, 30)))
    button3 = Button.Button("Button3", "None", (280, 740), pygame.Surface((230, 30)))
    button4 = Button.Button("Button4", "None", (570, 620), pygame.Surface((230, 30)))
    button5 = Button.Button("Button5", "None", (570, 680), pygame.Surface((230, 30)))
    button6 = Button.Button("Button6", "None", (570, 740), pygame.Surface((230, 30)))

    buttons = [button1, button2, button3, button4, button5, button6]

    screen.fill(setting.bg_color)
    screen.blit(portrait, (40, 40))

    for i in range(0, 6):
        screen.blit(square, (40, 260 + i*90))

    pygame.draw.line(screen, (0,0,0), (250, 0), (250, 800), 10)
    pygame.draw.line(screen, (0,0,0), (850, 0), (850, 800), 10)
    pygame.draw.line(screen, (0,0,0), (250, 580), (850, 580), 10)
    
    for j in range(0, 10):
        pygame.draw.line(screen, (0,0,0), (900, 350+j*40), (1150, 350+j*40), 8)

    pygame.draw.line(screen, (0,0,0), (900, 350), (900, 710), 8)
    pygame.draw.line(screen, (0,0,0), (1150, 350), (1150, 710), 8)


    ########################################################################################

    #main gameplay loop, redraw changable elements
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        
        screen.blit(map, (900, 50))
        screen.blit(text_screen, (256,0))

        for button in buttons:
            screen.blit(button.surface, button.position)
            caption = font.render(button.caption, True, (0, 128, 0))
            screen.blit(caption, button.position)

        write_array = just_text
        while len(write_array) < 20:
            write_array.append(normal_font.render("", True, (0,128,0)))
        
        for line in range(1, 21):
            
            try:
                screen.blit(write_array[-line], (256, 580-(line)*29))
            except:
                screen.blit(normal_font.render("", True, (0,128,0)), (256, 580-(line)*29))

        
        pygame.display.flip()

########################################################################################
    #loads stages, splits opening text into friendly line lengths.
def load_stage(name):

    return_arr = []
    normal_font = pygame.font.SysFont("calibri", 27)
    stages_dir = Path("stages")
    file_path = stages_dir / (name + ".txt")
    raw_arr = read_from_file(file_path)
    opening = raw_arr['opening']
    opening_arr = opening.split()
    working_str =  opening_arr.pop(0)
    
    
    while opening_arr:
        while normal_font.size(working_str)[0] < 590 and opening_arr:
            old_str = working_str
            working_str = working_str + " " + opening_arr[0]
            if normal_font.size(working_str)[0] < 590:
                opening_arr.pop(0)
            
        
        if not opening_arr:
            old_str = working_str

        return_arr.append(normal_font.render(old_str, True, (0,128,0)))
        
        if opening_arr:
            working_str = opening_arr[0]
            opening_arr.pop(0)
    
    return return_arr


########################################################################################

    

run_game()