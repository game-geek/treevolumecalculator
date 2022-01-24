import pygame
from leaf_line import Leaf_line
from trunk_line import Trunk_line
from txt_gestion import TxtGestion

class Draw_line(pygame.sprite.Sprite):

    def __init__(self, program, surface):
        super().__init__()
        self.program = program
        self.screen = surface
        self.leaf_lines = []
        self.trunk_lines = []
        self.pen_color = 23, 32, 42
        self.txt_gestion = TxtGestion(self.program)
        self.line_thickness = 5



    def register(self, Ax,  Bx, Ay, By):
        if self.program.image_type == 2:
            if self.program.homepage.currently[0] == 1:
                points = self.txt_gestion.calculate(Ax, Ay, Bx, By)
                self.program.homepage.images[0].leaf_lines.append([Ax, Bx, Ay, By, points])
            else:
                points = self.txt_gestion.calculate(Ax, Ay, Bx, By)
                self.program.homepage.images[1].leaf_lines.append([Ax, Bx, Ay, By, points])
        elif self.program.image_type == 1:
            points = self.txt_gestion.calculate(Ax, Ay, Bx, By)
            self.leaf_lines.append([Ax, Bx, Ay, By, points])




    def update(self, location):

      for line in location:
            pygame.draw.line(self.screen, self.pen_color, (line[0], line[2]), (line[1], line[3]), self.line_thickness)

    def register_lines(self,location, file="data/pixels.txt"):
        #print("passed!")
        total_points = []
        for i in location:
            total_points.append(i[4])

        self.txt_gestion.Write(total_points, "multiple", file)


























