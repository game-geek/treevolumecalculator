import pygame

class Trunk_line(pygame.sprite.Sprite):

    def __init__(self, Ax, Bx, Ay, By, points):
        super().__init__()
        self.pen_color = 23, 32, 42
        self.line_thickness = 4
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By

        self.points = points
        print(self.points)
