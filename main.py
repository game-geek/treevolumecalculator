import pygame
from pygame.locals import *
from program import Program
from mouse_event import Mouse_event
from mouse_event2 import Mouse_event2
from generate import Generate
import time

#start Pygame
pygame.init()
generate = Generate()
generate.Generate_pixels("data/pixels")
generate.Generate_pixels("data/pixels2")
generate.Clear("data/save", "csv")
see = True
stop = False
#name the app   
pygame.display.set_caption("TreeVolumeCalculator")

#set the screen size
screen = pygame.display.set_mode((640, 640))
pygame.display.set_icon(pygame.image.load("images/forest.png"))
preview = pygame.image.load("images/load_screen.jpg")
preview = pygame.transform.scale(preview, (screen.get_width(), screen.get_height()))
screen.blit(preview, (0,0))
pygame.display.flip()
time.sleep(0.1)

#image = input("please put the image directory \n ")



right_click_button = False



#screen = pygame.display.set_mode((1000, 500))


program_run = Program(screen)
#mouse_event = Mouse_event(program_run, screen)
mx, my = pygame.mouse.get_pos()


#Color_trunk = Color_Trunk(screen)



def generate(type):
    global mouse_event
    if type == 1:
        mouse_event = Mouse_event(program_run, screen)
        program_run.image_type = 1
        program_run.set_type()
        program_run.hover.add_name(
            "calculate_button",
            program_run.homepage.calculate_button.get_width(), program_run.homepage.calculate_button.get_height(),
            (program_run.homepage.calculate_button_rect.x, program_run.homepage.calculate_button_rect.y)
        )
        program_run.hover.add_name(
            "open_button",
            program_run.homepage.open_button.get_width(),program_run.homepage.open_button.get_height(),
            (program_run.homepage.open_button_rect.x, program_run.homepage.open_button_rect.y)

        )
        program_run.hover.reset()
    elif type == 2:
        mouse_event = Mouse_event2(program_run)
        program_run.image_type = 2
        program_run.set_type()

        program_run.hover.add_name(
            "calculate_button",
            program_run.homepage.calculate_button.get_width(), program_run.homepage.calculate_button.get_height(),
            (program_run.homepage.calculate_button_rect.x, program_run.homepage.calculate_button_rect.y)
        )
        program_run.hover.add_name(
            "open_button",
            program_run.homepage.open_button.get_width(), program_run.homepage.open_button.get_height(),
            (program_run.homepage.open_button_rect.x, program_run.homepage.open_button_rect.y),
            "images/open_test_black2.png"

        )
        program_run.hover.add_name(
            "open_button2",
            program_run.homepage.open_button2.get_width(), program_run.homepage.open_button2.get_height(),
            (program_run.homepage.open_button2_rect.x, program_run.homepage.open_button2_rect.y),
            "images/open_test_black2.png"

        )
        program_run.hover.add_name(
            "change_button",
            program_run.homepage.change_button.get_width(), program_run.homepage.change_button.get_height(),
            (program_run.homepage.change_button_rect.x, program_run.homepage.change_button_rect.y),
            "images/change_test_black2.png"

        )
        program_run.hover.add_name(
            "change_button2",
            program_run.homepage.change_button2.get_width(), program_run.homepage.change_button2.get_height(),
            (program_run.homepage.change_button2_rect.x, program_run.homepage.change_button2_rect.y),
            "images/change_test_black.png"

        )
        program_run.hover.reset()
    program_run.begin  = False
    program_run.begin_initial = False
    






running = True


while running:



    #if program_run.case == 2:
    #    screen = pygame.display.set_mode((640*2, 640*2))
    #print(program_run.homepage.tree_image.get_height())
    mx, my = pygame.mouse.get_pos()
    #print(mx, my)

    program_run.run(mx, my)








   # pygame.draw.rect(screen, (self.pen_color), [mx, my, 100, 5])



    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # pour verifier que l'évênement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if program_run.begin_initial:
                    if program_run.start1_button_rect.collidepoint(event.pos):
                        generate(1)
                    elif program_run.start2_button_rect.collidepoint(event.pos):
                        generate(2)
                else:
                    mouse_event.check(event.pos)



        elif event.type == MOUSEBUTTONUP:
            if not program_run.begin_initial:
                mouse_event.mouse_up()




        elif event.type == KEYDOWN and program_run.enable_text_input:
            mouse_event.key_board(event.key)






    # mettre à jour l'écran
    pygame.display.flip()






