
import pygame

class Hover:


    def __init__(self, program, screen):
        self.screen = screen
        self.program = program
        self.black_border = 5
        self.black_box = {
        }
        self.initial = []


    def show(self, event):
        if self.program.image_type == 1:
            if not self.program.begin:
                if self.program.case == 0:
                    if self.program.homepage.open_button_rect.collidepoint(event):
                        self.blit("open_button")

                    elif self.program.homepage.calculate_button_rect.collidepoint(event):
                        self.blit("calculate_button")
                elif self.program.case == 1:
                    if self.program.settings.button_rect.collidepoint(event):
                        self.blit("settings_button")
                elif self.program.case == 2:
                    if self.program.settings.button_rect.collidepoint(event):
                        self.blit("settings_button")
                elif self.program.case == 3:
                    if self.program.homepage.done_button_rect.collidepoint(event):
                        self.blit("done_button")
                    elif self.program.homepage.backwards_button_rect.collidepoint(event):
                        self.blit("backwards_button")
                    elif self.program.settings.button_rect.collidepoint(event):
                        self.blit("settings_button")

                elif self.program.case == 4:
                    # print("passed")
                    if self.program.homepage.right_button_rect.collidepoint(event):
                        self.blit("right_button")
                elif self.program.case == 5:
                    if self.program.homepage.save_button_rect.collidepoint(event):
                        self.blit("save_button")
            elif self.program.start1_button_rect.collidepoint(event):
                self.blit("start1_button")

            elif self.program.start2_button_rect.collidepoint(event):
                self.blit("start2_button")
        else:############################################################################################################
            if self.program.case == 0:
                if self.program.homepage.begin1 and self.program.homepage.open_button_rect.collidepoint(event):
                    self.blit("open_button")
                elif not self.program.homepage.begin1 and self.program.homepage.change_button_rect.collidepoint(event):
                    self.blit("change_button")
                elif self.program.homepage.begin2 and self.program.homepage.open_button2_rect.collidepoint(event):
                    self.blit("open_button2")
                elif not self.program.homepage.begin2 and self.program.homepage.change_button2_rect.collidepoint(event):
                    self.blit("change_button2")

                elif self.program.homepage.calculate_button_rect.collidepoint(event):
                    self.blit("calculate_button")

            elif self.program.case == 1:
                if self.program.settings.button_rect.collidepoint(event):
                    self.blit("settings_button")

            elif self.program.case == 2:
                if self.program.settings.button_rect.collidepoint(event):
                    self.blit("settings_button")

            elif self.program.case == 3:
                if self.program.homepage.currently[0] == 1:
                    if self.program.homepage.images[0].done_button_rect.collidepoint(event):
                        self.blit("done_button")
                    elif self.program.homepage.images[0].backwards_button_rect.collidepoint(event):
                        self.blit("backwards_button")
                    elif self.program.settings.button_rect.collidepoint(event):
                        self.blit("settings_button")
                elif self.program.homepage.currently[0] == 2:
                    if self.program.homepage.images[1].done_button_rect.collidepoint(event):
                        self.blit("done_button")
                    elif self.program.homepage.images[1].backwards_button_rect.collidepoint(event):
                        self.blit("backwards_button")
                    elif self.program.settings.button_rect.collidepoint(event):
                        self.blit("settings_button")


            elif self.program.case == 4:
                if self.program.homepage.right_button_rect.collidepoint(event):
                    self.blit("right_button")

            elif self.program.case == 5:
                if self.program.homepage.save_button_rect.collidepoint(event):
                    self.blit("save_button")





    def add_name(self, name, x, y, location, image="images/black_box.png", border=True):
        self.initial.append((name, (x, y), location, image, border))


    def remove_name(self, name):
        for i in self.initial:
            if i[0] == name:
                self.initial.remove(i)

    def remove_all(self):
        self.initial = []

    def reset(self):
        self.black_box = {}
        for i in self.initial:
            if i[3]:
                self.black_box[i[0]] = pygame.image.load(i[3])
                self.black_box[i[0]] = pygame.transform.scale((self.black_box.get(i[0])), (i[1][0] + self.black_border*2, i[1][1] + self.black_border*2))
            else:
                self.black_box[i[0]] = pygame.image.load(i[3])
                self.black_box[i[0]] = pygame.transform.scale((self.black_box.get(i[0])), (i[1][0], i[1][1]))


    def blit(self, name):
        for i in self.initial:
            if i[0] == name:
                if i[4]:
                    self.screen.blit(self.black_box[name], (i[2][0] - self.black_border, i[2][1] - self.black_border))
                else:
                    self.screen.blit(self.black_box[name], (i[2][0], i[2][1]))

