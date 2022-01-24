import pygame

class Info:


    def __init__(self, program, screen):
        self.program = program
        self.screen = screen
        self.font = pygame.font.SysFont("Liberation Serif", 20)
        self.font_big = pygame.font.SysFont("Liberation Serif", 40)


    def box_top(self, messages: tuple):
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.screen.get_width(), 100))
        pygame.draw.rect(self.screen, (36, 185, 30), (6, 6, self.screen.get_width() - 12, 88))
        y = 10
        for i in messages:
            self.screen.blit(self.font.render(i, True, (0, 0, 0)), (10, y))
            y += 20

    def box_bottom(self, messages: tuple):

        pygame.draw.rect(self.screen, (0, 0, 0), (0, self.screen.get_height()-100, self.screen.get_width(), 100))
        pygame.draw.rect(self.screen, (36, 185, 30), (6, self.screen.get_height()-94, self.screen.get_width() - 12, 88))
        y = self.screen.get_height()-80

        for i in messages:
            self.screen.blit(self.font.render(i, True, (0, 0, 0)), (10, y))
            y += 20




    def custom_message(self, messages: tuple, start_point: tuple = (10, 10), color: tuple = (0, 0, 0)):
        y = start_point[1]
        for i in messages:
            self.screen.blit(self.font.render(i, True, color), (start_point[0], y))
            y += 20


    def custom_message_version2(self, messages: tuple, start_point: tuple = (10, 10), color: tuple = (0, 0, 0)):
         y = start_point[1]
         for i in messages:
             self.screen.blit(self.font_big.render(i, True, color), (start_point[0], y))
             y += 20







