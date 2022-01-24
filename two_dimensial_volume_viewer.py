import pygame

class VolumeViewer:

    def __init__(self, program, screen):
        self.screen = screen
        self.program = program
        self.data = self.program.draw_line.txt_gestion.Read("data/pixels.txt")


    def View(self, wanted_points):
        for row in wanted_points:
            #top
            pygame.draw.line(self.screen, (23, 32, 42), (row[0], row[2]), (row[1], row[2]), 5)
            #right
            pygame.draw.line(self.screen, (23, 32, 42), (row[1], row[2]), (row[1], row[3]), 5)
            #bottom
            pygame.draw.line(self.screen, (23, 32, 42), (row[1], row[3]), (row[0], row[3]), 5)
            #left
            pygame.draw.line(self.screen, (23, 32, 42), (row[0], row[3]), (row[0], row[2]), 5)





        #for all pixels
        #pix = pygame.PixelArray(self.screen)
        #count1 = 1
        #count2 = 1
        #for row in self.data:
        #    for number in row:
        #        if number == "1":
        #            pix[count2][count1] = (24, 66, 145)
        #        count2 += 1
        #    count1 += 1
        #    count2 = 1

        #for points in wanted_points:
        #    for point in points:
#
        #        #print(point[0],point[1])
#
        #        pix[point[0]][point[2]] = (24, 66, 145)
        #        pix[point[1]][point[2]] = (24, 66, 145)




