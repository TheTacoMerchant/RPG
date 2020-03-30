import pygame, sys
from Settings import Settings
import Button

def run_game():

    pygame.init()
    setting = Settings()


    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    font = pygame.font.SysFont("comicsansms", 25)

    text = font.render("Hello World", True, (0, 128, 0))
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

    

    

    

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        
        screen.blit(map, (900, 50))

        for button in buttons:
            screen.blit(button.surface, button.position)
            caption = font.render(button.caption, True, (0, 128, 0))
            screen.blit(caption, button.position)
            
        
        

        pygame.display.flip()



    

run_game()