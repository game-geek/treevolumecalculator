import pygame

class Mouse_event:


    def __init__(self, program, screen):
        self.screen = screen
        self.program = program

        self.letters = [(pygame.K_a, "a"), (pygame.K_b, "b"), (pygame.K_c, "c"), (pygame.K_d, "d"), (pygame.K_e, "e"),
                        (pygame.K_f, "f"), (pygame.K_g, "g"), (pygame.K_h, "h"),
                        (pygame.K_i, "i"), (pygame.K_j, "j"), (pygame.K_k, "k"), (pygame.K_l, "l"), (pygame.K_m, "m"),
                        (pygame.K_n, "n"), (pygame.K_o, "o"), (pygame.K_p, "p"),
                        (pygame.K_q, "q"), (pygame.K_r, "r"), (pygame.K_s, "s"), (pygame.K_t, "t"), (pygame.K_u, "u"),
                        (pygame.K_v, "v"), (pygame.K_w, "w"), (pygame.K_x, "x"),
                        (pygame.K_y, "y"), (pygame.K_z, "z"), (pygame.K_SPACE, (" "))]

        self.numbers = [(pygame.K_1, "1"), (pygame.K_2, "2"), (pygame.K_3, "3"), (pygame.K_4, "4"), (pygame.K_5, "5"),
                        (pygame.K_6, "6"), (pygame.K_7, "7"), (pygame.K_8, "8"),
                        (pygame.K_9, "9"), (pygame.K_0, "0"), (pygame.K_SEMICOLON, ".")]
        self.keys = [(pygame.K_BACKSPACE, "back_space"), (13, "enter")]






        #self.initial = [
        #    ("start1_button", (self.program.start1_button_rect.x, self.program.start1_button_rect.y)),
        #    ("start2_button", (self.program.start2_button_rect.x, self.program.start2_button_rect.y)),
        #    ("open_button", (self.program.homepage.open_button_rect.x, self.program.homepage.open_button_rect.y)),
        #    ("calculate_button",(self.program.homepage.calculate_button_rect.x, self.program.homepage.calculate_button_rect.y)),
        #    ("done_button", (self.program.homepage.done_button_rect.x, self.program.homepage.done_button_rect.y)),
        #    ("backwards_button",(self.program.homepage.backwards_button_rect.x, self.program.homepage.backwards_button_rect.x)),
        #    ("right_button", (self.program.homepage.right_button_rect.x, self.program.homepage.right_button_rect.y)),
        #    ("save_button", (self.program.homepage.save_button_rect.x, self.program.homepage.save_button_rect.y))
        #]
        #for i in self.initial:
        #    self.black_box[i[0]] = pygame.image.load("black_box.png")
        #    self.black_box[i[0]] = pygame.transform.scale((self.black_box.get(i[0])), (
        #    i[1][0] + self.black_border, i[1][1] + self.black_border))
        #print('loolo')




    def mouse_down(self):
        #set the pressed variable at true, because the mouse is being pressed
        self.program.right_click_pressed[1] = True
        #self.program.was_pressed = False


    def mouse_up(self):
        if self.program.right_click_pressed[1] == True:  #check if the mouse was pressed before
            self.program.right_click_pressed[1] = False #set the pressed variable at false
            self.program.was_pressed = True  #presise that mouse was pressed before
        else:
            pass# if the mouse wasn't pressed before

    def finish(self, type=None):
        ##################################
        if type == "open":
            self.program.homepage.open()
        elif type == "calculate":
            self.program.case += 1
            self.program.homepage.resize_image()
            self.program.hover.add_name(
                "settings_button",
                self.program.settings.button.get_width(),
                self.program.settings.button.get_height(),
                (self.program.settings.button_rect.x, self.program.settings.button_rect.y)
            )
            self.program.hover.reset()
        ##################################
        elif self.program.case == 5:
            #here we zach the end of all calculations
            self.program.reset()
        elif self.program.case == 3 and type == "back":
            self.program.draw_line.txt_gestion.back()
            count = 1

        else:

            self.program.case += 1 # move foward in solving the problem of calculating the volume of the tree

            if self.program.case == 4:
                self.program.calculate_leaf_volume()
                self.program.started = False
                self.program.hover.add_name(
                    "right_button",
                    self.program.homepage.right_button.get_width(),
                    self.program.homepage.right_button.get_height(),
                    (self.program.homepage.right_button_rect.x, self.program.homepage.right_button_rect.y),
                    "images/right_new_black.png"
                )
                self.program.hover.reset()
            elif self.program.case == 5:
                self.program.hover.add_name(
                    "save_button",
                    self.program.homepage.save_button.get_width(),
                    self.program.homepage.save_button.get_height(),
                    (self.program.homepage.save_button_rect.x, self.program.homepage.save_button_rect.y),
                )
                self.program.hover.reset()
            elif self.program.case == 2:
                pass
            
            
    def check(self, event):
        if not self.program.begin:
            if self.program.case == 0:
                if self.program.homepage.open_button_rect.collidepoint(event):
                    self.finish("open")

                elif self.program.homepage.calculate_button_rect.collidepoint(event):
                    self.finish("calculate")
            elif self.program.case == 1:
                if self.program.settings.button_rect.collidepoint(event):
                    self.program.settings.set = True
                elif self.program.settings.set:  ########run the settings code
                    self.settings(event)
                else:
                    self.mouse_down()

            elif self.program.case == 2:
                if self.program.settings.button_rect.collidepoint(event):
                    self.program.settings.set = True
                elif self.program.settings.set:  ########run the settings code
                    self.settings(event)

            elif self.program.case == 3:
                if self.program.homepage.done_button_rect.collidepoint(event):
                    self.finish()
                elif self.program.homepage.backwards_button_rect.collidepoint(event):
                    self.finish("back")
                elif self.program.settings.button_rect.collidepoint(event):
                    self.program.settings.set = True
                elif self.program.settings.set:  ########run the settings code
                    self.settings(event)
                else:
                    self.mouse_down()
            elif self.program.case == 4:
                # print("passed")
                if self.program.homepage.right_button_rect.collidepoint(event):
                    self.finish()

                    # ("should work")
            elif self.program.case == 5:
                if self.program.homepage.save_button_rect.collidepoint(event):
                    self.finish()



    def settings(self, event):
        if self.program.settings.button1.collidepoint(event):
            self.program.settings.register("button1")






    def key_board(self, event):

        for i in self.numbers:
            if event == i[0]:
                if self.program.homepage.part == "phrase1":
                    self.program.homepage.phrase1 += i[1]
                    # print(program_run.homepage.keys, program_run.homepage.phrase1)
                elif self.program.homepage.part == "phrase2":
                    self.program.homepage.phrase2 += i[1]
                    # print(program_run.homepage.keys, program_run.homepage.phrase2)
        for i in self.keys:
            if event == i[0]:
                self.program.homepage.keys[i[1]] = True

