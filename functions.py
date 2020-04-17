import pygame, os
from pathlib import Path
from text_file_reader import read_from_file
from Stage import Stage
from Button import Button

def create_static(screen, setting):

    ###################################################################################
    #initialize pygame and "static" elements
    
    
    font = pygame.font.SysFont("comicsansms", 25)
    normal_font = pygame.font.SysFont("calibri", 27)
    write_array = []
    

    portrait = pygame.Surface((170, 170))
    
    square = pygame.Surface((50, 50))
    pygame.display.set_caption("RPG")
    
   

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

########################################################################################
    #loads stages, splits opening text into friendly line lengths.
def load_stage(name):

    normal_font = pygame.font.SysFont("calibri", 27)
    stages_dir = Path("stages")
    file_path = stages_dir / (name + ".txt")
    raw_arr = read_from_file(file_path)
    opening = raw_arr['opening']
    
    opening_arr = parse_str(opening)

    buttons = init_buttons(raw_arr)

    
    

    return Stage(opening_arr, buttons)


########################################################################################
def parse_str(string):

    return_arr = []
    string_arr = string.split()
    normal_font = pygame.font.SysFont("calibri", 27)
    
    while string_arr:
        working_str = string_arr.pop(0)

        while normal_font.size(working_str)[0] < 590 and string_arr:
            old_str = working_str
            working_str = working_str + " " + string_arr[0]

            if string_arr[0] == '{}':
                string_arr.pop(0)
                break

            if normal_font.size(working_str)[0] < 590:
                string_arr.pop(0)
            
        
        if not string_arr:
            old_str = working_str

        return_arr.append(normal_font.render(old_str, True, (0,128,0)))
    return return_arr

def init_buttons(array):

    button_positions = {
        0: (280, 620),
        1: (280, 680),
        2: (280, 740),
        3: (570, 620),
        4: (570, 680),
        5: (570, 740)
    }
    button_dim = (230, 30)
    buttons = ['button1', 'button2', 'button3', 'button4', 'button5', 'button6']
    new_buttons = []

    for button in range(0,6):
        try:
            buttonget = array[buttons[button]]
            
            if buttonget.find('c=') != -1:
                start_ind = buttonget.find('c=')
                end_ind = buttonget.find('c,')
                
                caption = buttonget[start_ind+2:end_ind]
                
            else:
                caption = buttons[button]
                
            if buttonget.find('l=') != -1:
                link = buttonget[buttonget.find('l=')+2: buttonget.find('l,')]
                
            else:
                link = None
                
            new_buttons.append(Button(caption, link, pygame.Rect(button_positions[button], button_dim), button_positions[button]))
        
        except:
            new_buttons.append(Button("", None, pygame.Rect(button_positions[button], button_dim), button_positions[button]))
    
    return new_buttons

def manage_text(screen, text):
    normal_font = pygame.font.SysFont("calibri", 27)
    write_array = text
    while len(write_array) < 20:
        write_array.append(normal_font.render("", True, (0,128,0)))
        
    for line in range(1, 21):
            
        try:
            screen.blit(write_array[-line], (256, 580-(line)*29))
        except:
            screen.blit(normal_font.render("", True, (0,128,0)), (256, 580-(line)*29))

        