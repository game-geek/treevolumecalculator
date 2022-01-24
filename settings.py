import pygame

class Settings:

    def __init__(self, program, screen):
        self.program = program
        self.screen = screen
        self.button = pygame.image.load("images/settings.png")
        self.button_rect = self.button.get_rect()
        self.button_rect.x = 10
        self.button_rect.y = 400
        self.set = False
        self.info_bar_state = True #True for up and False for down
        self.start = True



    def main_page(self, mx, my):
        if self.start:
            self.init()

        self.screen.fill((102, 102, 102))
        pygame.draw.rect(self.screen, (49, 47, 47), (10, 10, self.screen.get_width()-20, self.screen.get_height()/4))
        self.program.homepage.info.custom_message_version2(("SETTINGS", None), (self.screen.get_width()/2-100, 40))

        # draw the correspondent button
        pygame.draw.rect(self.screen, (71, 199, 12), (20, round(self.screen.get_height() / 2.5), 250, 80))

        if not self.info_bar_state:
            self.program.homepage.info.custom_message(("Set the info bar", "      on top"), (70, round(self.screen.get_height() / 2.5)+15))
        else:
            self.program.homepage.info.custom_message(("Set the info bar", "on the bottom"), (70, round(self.screen.get_height() / 2.5)+15))



    def init(self):
        self.button1_rect = [None, None]
        self.button1_rect[0] = 20
        self.button1_rect[1] = round(self.screen.get_height()/2.5)
        self.button1 = pygame.draw.rect(self.screen, (71, 199, 12), (self.button1_rect[0], self.button1_rect[1], 250, 80))

        self.start = False


    def register(self, case):
        if self.program.image_type == 2:
            if case == "button1":
                if self.info_bar_state:
                    self.info_bar_state = False
                    self.set = False

                    # for the show scale
                    for o in self.program.homepage.images:
                        for i in o.position_list:
                            i[1] -= 100
                    #for the precise scale
                    for o in self.program.homepage.images:
                        for i in o.leaf_lines:
                            i[2] -= 100
                            i[3] -= 100
                            for u in i[4]:
                                u[1] -= 100
                        try:
                            lenn = len(o.leaf_lines)
                            self.program.position1y = o.leaf_lines[lenn-1][3]
                        except IndexError:
                            pass

                else:
                    self.info_bar_state = True
                    self.set = False

                    # for the show scale
                    for o in self.program.homepage.images:
                        for i in o.position_list:
                            i[1] += 100
                    # for the precise scale
                    for o in self.program.homepage.images:
                        for i in o.leaf_lines:
                            i[2] += 100
                            i[3] += 100
                            for u in i[4]:
                                try:
                                    u[1] += 100
                                except TypeError:
                                    pass
                        try:
                            lenn = len(o.leaf_lines)
                            self.program.position1y = o.leaf_lines[lenn - 1][3]
                        except IndexError:
                            pass
        else:############################################################################
            if case == "button1":
                if self.info_bar_state:
                    for i in self.program.draw_line.leaf_lines:
                        i[2] -= 100
                        i[3] -= 100
                        for o in i:
                            try:
                                o[1] -= 100
                            except TypeError:
                                pass
                    self.info_bar_state = False
                    self.set = False



                else:
                    for i in self.program.draw_line.leaf_lines:
                        i[2] += 100
                        i[3] += 100
                        for o in i:
                            try:
                                o[1] += 100
                            except TypeError:
                                pass
#
                    self.info_bar_state = True
                    self.set = False

        self.start = True



        