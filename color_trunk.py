import pygame
from trunk_line import Colored_Space
from module_draw_line import Draw_line

class Color_Trunk(pygame.sprite.Sprite):

    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.initial_time = 0
        self.time = 0
        self.actual = True
        self.draw_line = Draw_line(self.screen)
        self.space_colored = pygame.sprite.Group()
        self.on = False




    def calculate(self, mx, my):
        if self.right_click_pressed and not self.on:
            self.position1x = mx
            self.position1y = my
            self.on = True

        elif self.right_click_pressed and self.on:
            self.position2x = mx
            self.position2y = my
            self.on = False

            self.draw_line_screen(self.position1x, self.position2x, self.position1y, self.position2y)





    def draw_line_screen(self, Ax, Bx, Ay, By):

        self.draw_line.draw(Ax, Bx, Ay, By)



