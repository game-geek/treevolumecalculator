import pygame

class Mouse_event2:


    def __init__(self, program):
        self.program = program

        self.letters = [(pygame.K_a, "a"), (pygame.K_b, "b"), (pygame.K_c, "c"), (pygame.K_d, "d"), (pygame.K_e, "e"), (pygame.K_f, "f"), (pygame.K_g, "g"), (pygame.K_h, "h"),
                   (pygame.K_i, "i"), (pygame.K_j, "j"), (pygame.K_k, "k"), (pygame.K_l, "l"), (pygame.K_m, "m"), (pygame.K_n, "n"), (pygame.K_o, "o"), (pygame.K_p, "p"),
                   (pygame.K_q, "q"), (pygame.K_r, "r"), (pygame.K_s, "s"), (pygame.K_t, "t"), (pygame.K_u, "u"), (pygame.K_v, "v"), (pygame.K_w, "w"), (pygame.K_x, "x"),
                   (pygame.K_y, "y"), (pygame.K_z, "z"), (pygame.K_SPACE, (" "))]

        self.numbers = [(pygame.K_1, "1"), (pygame.K_2, "2"), (pygame.K_3, "3"), (pygame.K_4, "4"), (pygame.K_5, "5"), (pygame.K_6, "6"), (pygame.K_7, "7"), (pygame.K_8, "8"),
                   (pygame.K_9, "9"), (pygame.K_0, "0"), (pygame.K_SEMICOLON, ".")]
        self.keys = [(pygame.K_BACKSPACE, "back_space"), (13, "enter")]


    def mouse_down(self):
        #set the pressed variable at true, because the mouse is being pressed
        self.program.right_click_pressed[1] = True
        self.program.was_pressed = False
        #self.program.was_pressed = False


    def mouse_up(self):
        if self.program.right_click_pressed[1] == True:  #check if the mouse was pressed before
            self.program.right_click_pressed[1] = False #set the pressed variable at false
            self.program.was_pressed = True  #presise that mouse was pressed before
        else:
            pass# if the mouse wasn't pressed before

            
    def check(self, event):

        if self.program.case == 0:
            if self.program.homepage.begin1 and self.program.homepage.open_button_rect.collidepoint(event):
                self.program.homepage.open(1)
            elif not self.program.homepage.begin1 and self.program.homepage.change_button_rect.collidepoint(event):
                self.program.homepage.open(1)
            elif self.program.homepage.begin2 and self.program.homepage.open_button2_rect.collidepoint(event):
                self.program.homepage.open(2)
            elif not self.program.homepage.begin2 and self.program.homepage.change_button2_rect.collidepoint(event):
                self.program.homepage.open(2)

            elif self.program.homepage.calculate_button_rect.collidepoint(event):
                self.program.case += 1
                self.program.homepage.image_sorter()
                self.program.hover.add_name(
                    "settings_button",
                    self.program.settings.button.get_width(),
                    self.program.settings.button.get_height(),
                    (self.program.settings.button_rect.x, self.program.settings.button_rect.y)
                )
                self.program.hover.reset()


################################################################################
        elif self.program.case == 1:
            if self.program.settings.button_rect.collidepoint(event):
                self.program.settings.set = True
            elif self.program.settings.set:########run the settings code
                self.settings(event)
            else:
                self.mouse_down()

###############################################################################
        elif self.program.case == 2:
            if self.program.settings.button_rect.collidepoint(event):
                self.program.settings.set = True
            elif self.program.settings.set:########run the settings code
                self.settings(event)


###############################################################################
        elif self.program.case == 3:
            if self.program.homepage.currently[0] == 1:#########################
                if self.program.homepage.images[0].done_button_rect.collidepoint(event):
                    self.program.draw_line.register_lines(self.program.homepage.images[0].leaf_lines, "data/pixels.txt")
                    self.program.homepage.images[0].points = self.program.volume2.calculate(10, self.program.homepage.images[0].min_height, self.program.homepage.images[0].max_height, file="data/pixels.txt")
                    self.program.case = 1  # move foward in solving the problem of calculating the volume of the tree
                    self.program.homepage.currently[0] = 2
                    self.program.homepage.images[1].resize_image()
                    self.program.started = False
                elif self.program.homepage.images[0].backwards_button_rect.collidepoint(event):
                    self.program.draw_line.txt_gestion.back("data/save.csv")
                elif self.program.settings.button_rect.collidepoint(event):
                    self.program.settings.set = True
                elif self.program.settings.set:  ########run the settings code
                    self.settings(event)
                else:
                    self.mouse_down()
            elif self.program.homepage.currently[0] == 2:#######################
                if self.program.homepage.images[1].done_button_rect.collidepoint(event):
                    self.program.draw_line.register_lines(self.program.homepage.images[1].leaf_lines, "data/pixels2.txt")
                    self.program.homepage.images[1].points = self.program.volume2.calculate(10, self.program.homepage.images[1].min_height, self.program.homepage.images[1].max_height, file="data/pixels2.txt")
                    self.program.case += 1  # move foward in solving the problem of calculating the volume of the tree
                    self.program.volume = self.program.volume2.fuse(self.program.homepage.images[0].points, self.program.homepage.images[1].points, self.program.homepage.images[0].position_list, self.program.homepage.images[1].position_list, (self.program.homepage.images[0].phrase1, self.program.homepage.images[0].phrase2), (self.program.homepage.images[1].phrase1, self.program.homepage.images[1].phrase2))########fuse!!
                    self.program.homepage.currently[0] = 0
                    self.program.homepage.tree_image2 = pygame.transform.scale(self.program.homepage.tree_image2,(self.program.screen.get_width(), self.program.screen.get_height()))
                    self.program.hover.add_name(
                        "right_button",
                        self.program.homepage.right_button.get_width(),
                        self.program.homepage.right_button.get_height(),
                        (self.program.homepage.right_button_rect.x, self.program.homepage.right_button_rect.y),
                        "images/right_new_black.png"
                    )
                    self.program.hover.reset()
                elif self.program.homepage.images[1].backwards_button_rect.collidepoint(event):
                    self.program.draw_line.txt_gestion.back("data/save2.csv")
                elif self.program.settings.button_rect.collidepoint(event):
                    self.program.settings.set = True
                elif self.program.settings.set:  ########run the settings code
                    self.settings(event)
                else:
                    self.mouse_down()


################################################################################
        elif self.program.case == 4:
            if self.program.homepage.right_button_rect.collidepoint(event):
                self.program.case += 1  # move foward in solving the problem of calculating the volume of the tree
                self.program.started = False
                self.program.hover.add_name(
                    "save_button",
                    self.program.homepage.save_button.get_width(),
                    self.program.homepage.save_button.get_height(),
                    (self.program.homepage.save_button_rect.x, self.program.homepage.save_button_rect.y)
                )
                self.program.hover.reset()

##################################################################################
        elif self.program.case == 5:
            if self.program.homepage.save_button_rect.collidepoint(event):
                self.program.reset()





    def settings(self, event):
        if self.program.settings.button1.collidepoint(event):
            self.program.settings.register("button1")






    def key_board(self, event):
        if self.program.homepage.currently[0] == 1:
            for i in self.numbers:
                if event == i[0]:
                    if self.program.homepage.images[0].part == "phrase1":
                        self.program.homepage.images[0].phrase1 += i[1]
                        # print(program_run.homepage.keys, program_run.homepage.phrase1)
                    elif self.program.homepage.images[0].part == "phrase2":
                        self.program.homepage.images[0].phrase2 += i[1]
                        # print(program_run.homepage.keys, program_run.homepage.phrase2)
            for i in self.keys:
                if event == i[0]:
                    self.program.homepage.images[0].keys[i[1]] = True

        else:
            for i in self.numbers:
                if event == i[0]:
                    if self.program.homepage.images[1].part == "phrase1":
                        self.program.homepage.images[1].phrase1 += i[1]
                        # print(program_run.homepage.keys, program_run.homepage.phrase1)
                    elif self.program.homepage.images[1].part == "phrase2":
                        self.program.homepage.images[1].phrase2 += i[1]
                        # print(program_run.homepage.keys, program_run.homepage.phrase2)

            for i in self.keys:
                if event == i[0]:
                        self.program.homepage.images[1].keys[i[1]] = True

