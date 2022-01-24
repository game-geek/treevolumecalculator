import pygame
# https://www.programiz.com/python-programming/methods/list





class Aire_leaf(pygame.sprite.Sprite):

    def __init__(self, module_draw_line,screen, program):
        super().__init__()
        self.program = program
        self.draw_line = module_draw_line
        self.a = 1
        self.pen_color = 23, 32, 42
        self.screen = screen

        self.aire_calculator("leaf")


        self.initial_value = 0



    def aire_calculator(self, type):
        print("hahah\n hahaha")
        self.start_value = 0
        self.end_value = 0
        self.end_value2 = 0
        self.x_value = 1
        self.x_max_value = 3
        self.total_points = []
        self.pixel_numbers = []
        self.lol = []
        self.lol2 = []
        self.seperate = 0
        self.pixels = 0
        if type == 'leaf':
            #print(self.draw_line.points)
            lol = self.draw_line.points[:]
            loll = []
            for e in lol:
                if e == 'seperate':
                    pass
                else:
                    loll.append(e[0])
            loll.sort()
            small = loll[0]
            big = loll[-1]

            #print("\n" + str(small))
            print(big)





            for o in range(small, big):
                for i in self.draw_line.points:
                    #print(i[0])
                    if i[0] == o:
                        self.total_points.append(i[1])
                        self.lol.append(i[0])
                        self.lol2.append(i[1])
                    elif i == "seperate":
                        #print('seperated!!!')
                        self.seperate += 1
                leen = len(self.total_points)
                if self.total_points[leen-1] > self.total_points[0]:
                    self.pixel_numbers.append(self.total_points[leen - 1]-self.total_points[0])
                else:
                    self.pixel_numbers.append(self.total_points[0] - self.total_points[leen - 1])

                self.total_points.clear()

            print(self.draw_line.points)
            print(self.lol)
            print(self.lol2)
            print(self.total_points)
            print(self.pixel_numbers)
            print(self.seperate)
            for i in self.pixel_numbers:
                self.pixels += i
            print(self.pixels)
            print("setups   :  " + str(self.program.setups))









