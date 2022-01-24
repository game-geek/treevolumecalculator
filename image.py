import pygame
from info import Info
try:
    from win32api import GetSystemMetrics
except ModuleNotFoundError:
    pass

class Image:

    def __init__(self, program, screen, image):
        self.program = program
        self.screen = screen
        self.image = image
        self.min_height = 1000
        self.max_height = 1
        self.points = []

        self.message_box = pygame.image.load("images/message_box.png")
        self.message_box = pygame.transform.scale(self.message_box, (round(self.message_box.get_width() / 3), round(self.message_box.get_height() / 3)))
        self.message_box_rect = self.message_box.get_rect()
        self.message_box_rect.x = 0
        self.message_box_rect.y = 0
        self.begin1 = True
        self.begin2 = True

        self.scale_box = pygame.image.load("images/input.png")
        # self.scale_box = pygame.transform.scale()
        self.scale_box_rect = self.scale_box.get_rect()
        self.scale_box_rect.x = self.message_box_rect.x + self.message_box.get_width()
        self.scale_box_rect.y = 0

        self.cursor = pygame.image.load("images/cross3.png")
        self.cursor_rect = self.cursor.get_rect()

        self.position_list = []
        self.keys = {}
        self.phrase1 = ""
        self.phrase2 = ""
        self.part = "phrase1"

        self.backwards_button = pygame.image.load("images/back_new.png")
        self.backwards_button = pygame.transform.scale(self.backwards_button, (75, 50))
        self.backwards_button_rect = self.backwards_button.get_rect()
        self.backwards_button_rect.x = 20
        self.backwards_button_rect.y = 110

        self.done_button = pygame.image.load("images/new_done_button.png")
        self.done_button = pygame.transform.scale(self.done_button, (100, 100))
        self.done_button_rect = self.done_button.get_rect()
        self.done_button_rect.x = 20
        self.done_button_rect.y = 210

        self.font = pygame.font.SysFont("Liberation Serif", 20)

        self.bar = pygame.image.load("images/barrier.png")
        self.bar = pygame.transform.scale(self.bar, (self.screen.get_width(), 20))
        self.bar_rect = self.bar.get_rect()
        self.bar_rect.x = 0
        self.bar_rect.y = 100

        self.info = Info(self.program, self.screen)

        self.loop = 0
        self.max_loop = 300



        ##############
        self.leaf_lines = []

    def renew_images(self):
        self.bar = pygame.transform.scale(self.bar, (self.screen.get_width(), 20))

    def show_scale(self, mx, my):
        if self.program.settings.info_bar_state:
            self.info.box_top(("STEP 1", "Locate your scaling object on the screen"))
            self.screen.blit(self.image, (0, 100))

        else:
            self.info.box_bottom(("STEP 1", "Locate your scaling object on the screen"))
            self.screen.blit(self.image, (0, 0))


        self.program.hover.show((mx, my))
        self.screen.blit(self.program.settings.button, (self.program.settings.button_rect.x, self.program.settings.button_rect.y))

        if len(self.position_list) == 1:
            self.cursor_rect.x = mx - 25
            self.cursor_rect.y = self.position_list[0][1] - 25
        elif len(self.position_list) == 3:
            self.cursor_rect.x = self.position_list[2][0] - 25
            self.cursor_rect.y = my - 25
        else:
            self.cursor_rect.x = mx - 25
            self.cursor_rect.y = my - 25

        self.screen.blit(self.cursor, (self.cursor_rect.x, self.cursor_rect.y))
        count = 1
        for point in self.position_list:
            if count == 2:
                self.screen.blit(self.cursor, (self.position_list[1][0] - 25, self.position_list[0][1] - 25))
            elif count == 4:
                self.screen.blit(self.cursor, (self.position_list[2][0] - 25, self.position_list[3][1] - 25))
            else:
                self.screen.blit(self.cursor, (point[0] - 25, point[1] - 25))
            count += 1
        if len(self.position_list) == 4:
            self.program.case += 1

    def input_scale(self, mx, my):
        self.program.enable_text_input = True
        if self.keys.get("enter") and self.part == "phrase1":
            self.part = "phrase2"
            self.keys["enter"] = False
        elif self.keys.get("enter") and self.part == "phrase2":
            self.program.case += 1
            self.program.hover.remove_all()
            self.program.hover.add_name(
                "done_button",
                self.done_button.get_width(),
                self.done_button.get_height(),
                (self.done_button_rect.x, self.done_button_rect.y),
                "images/done_button_new_black.png"
            )
            self.program.hover.add_name(
                "backwards_button",
                self.backwards_button.get_width(),
                self.backwards_button.get_height(),
                (self.backwards_button_rect.x, self.backwards_button_rect.y),
                "images/back_new_black.png"
            )
            self.program.hover.add_name(
                "settings_button",
                self.program.settings.button.get_width(),
                self.program.settings.button.get_height(),
                (self.program.settings.button_rect.x, self.program.settings.button_rect.y)
            )
            self.program.hover.reset()
            self.keys["enter"] = False
        elif self.keys.get("back_space") and self.part == "phrase1":  # and not self.program.cooldown
            new_phrase = ""
            count = 1
            if self.phrase1 == "":
                self.keys["back_space"] = False
            else:
                for e in self.phrase1:
                    if count == len(self.phrase1):
                        self.keys["back_space"] = False
                        self.phrase1 = new_phrase
                        # self.program.cooldown = True
                        break
                    else:
                        new_phrase += e
                    count += 1

        elif self.keys.get("back_space") and self.part == "phrase2":  # and not self.program.cooldown
            new_phrase = ""
            count = 1
            if self.phrase2 == "":
                self.keys["back_space"] = False
            else:
                for e in self.phrase2:
                    if count == len(self.phrase2):
                        self.keys["back_space"] = False
                        self.phrase2 = new_phrase
                        # self.program.cooldown = True
                        break
                    else:
                        new_phrase += e
                    count += 1

        if self.program.settings.info_bar_state:
            self.info.box_top(("STEP 2", "Enter the scale in meters"))
            self.screen.blit(self.image, (0, 100))
            if self.part == "phrase1":
                if self.loop < self.max_loop / 2:
                    self.info.custom_message(("X : " + self.phrase1 + "|", None), (500, 10), (255, 0, 0))
                    self.info.custom_message(("Y : " + self.phrase2, None), (500, 30))
                    self.loop += 1
                else:
                    self.info.custom_message(("X : " + self.phrase1, None), (500, 10), (255, 0, 0))
                    self.info.custom_message(("Y : " + self.phrase2, None), (500, 30))
                    self.loop += 1
            elif self.part == "phrase2":
                if self.loop < self.max_loop / 2:
                    self.info.custom_message(("X : " + self.phrase1, None), (500, 10))
                    self.info.custom_message(("Y : " + self.phrase2 + "|", None), (500, 30), (255, 0, 0))
                    self.loop += 1
                else:
                    self.info.custom_message(("X : " + self.phrase1, None), (500, 10))
                    self.info.custom_message(("Y : " + self.phrase2, None), (500, 30), (255, 0, 0))
                    self.loop += 1



        else:
            self.info.box_bottom(("STEP 2", "Enter the scale in meters"))
            self.screen.blit(self.image, (0, 0))
            if self.part == "phrase1":
                if self.loop < self.max_loop / 2:
                    self.info.custom_message(("X : " + self.phrase1 + "|", None), (500, self.screen.get_height()-90), (255, 0, 0))
                    self.info.custom_message(("Y : " + self.phrase2, None), (500, self.screen.get_height()-70))
                    self.loop += 1
                else:
                    self.info.custom_message(("X : " + self.phrase1, None), (500, self.screen.get_height()-90), (255, 0, 0))
                    self.info.custom_message(("Y : " + self.phrase2, None), (500, self.screen.get_height()-70))
                    self.loop += 1
            elif self.part == "phrase2":
                if self.loop < self.max_loop / 2:
                    self.info.custom_message(("X : " + self.phrase1, None), (500, self.screen.get_height()-90))
                    self.info.custom_message(("Y : " + self.phrase2 + "|", None), (500, self.screen.get_height()-70), (255, 0, 0))
                    self.loop += 1
                else:
                    self.info.custom_message(("X : " + self.phrase1, None), (500, self.screen.get_height()-90))
                    self.info.custom_message(("Y : " + self.phrase2, None), (500, self.screen.get_height()-70), (255, 0, 0))
                    self.loop += 1





        if self.loop == self.max_loop:
                self.loop = 0

        self.program.hover.show((mx, my))
        self.screen.blit(self.program.settings.button, (self.program.settings.button_rect.x, self.program.settings.button_rect.y))


        count = 1
        if self.part == "phrase1":
            for point in self.position_list:
                if count == 1:
                    self.screen.blit(self.cursor, (point[0] - 25, point[1] - 25))
                elif count == 2:
                    self.screen.blit(self.cursor, (self.position_list[1][0] - 25, self.position_list[0][1] - 25))
                count += 1
        else:
            for point in self.position_list:
                if count == 3:
                    self.screen.blit(self.cursor, (point[0] - 25, point[1] - 25))
                elif count == 4:
                    self.screen.blit(self.cursor, (self.position_list[2][0] - 25, self.position_list[3][1] - 25))
                count += 1




    def precise_image(self, mx, my):
        if not self.program.right_click_pressed[1] and self.program.was_pressed:
            if self.program.started:
                self.program.position2x = mx
                self.program.position2y = my

                #add in database

                self.program.draw_line.register(self.program.position1x, self.program.position2x, self.program.position1y, self.program.position2y)
                self.program.position1x = self.program.position2x
                self.program.position1y = self.program.position2y
                self.program.was_pressed = False

            else:  # start the program (get the first coordinates)
                self.program.position1x = mx
                self.program.position1y = my
                # define the function as started
                self.program.started = True
                self.program.was_pressed = False


        if self.program.settings.info_bar_state:
            self.screen.blit(self.image, (0, 100))
            self.info.box_top(("STEP 3",
                               "By using your mouse,click around the image to let the computer know were the tree is.",
                               "When you have finished, press the top right button"
                               ))
        else:
            self.screen.blit(self.image, (0, 0))
            self.info.box_bottom(("STEP 3",
                               "By using your mouse,click around the image to let the computer know were the tree is.",
                               "When you have finished, press the top right button"
                               ))

        self.program.hover.show((mx, my))
        self.screen.blit(self.backwards_button, (self.backwards_button_rect.x, self.backwards_button_rect.y))
        self.screen.blit(self.done_button, (self.done_button_rect.x, self.done_button_rect.y),
                             special_flags=4)  # 3 &nd 4


        self.screen.blit(self.program.settings.button, (self.program.settings.button_rect.x, self.program.settings.button_rect.y))
        self.program.draw_line.update(self.leaf_lines)







    def resize_image(self):
        width = self.image.get_width()
        height = self.image.get_height()
        c_width = GetSystemMetrics(0)
        c_height = GetSystemMetrics(1)

        if width < c_width/1.2 or height < c_height/1.2-100:
            while width < c_width/1.2-400 or height < c_height/1.2-500:
                if width * 1.1 < c_width/1.7-200 or height < height * 1.1:
                    width *= 1.1
                    height *= 1.1
                else:
                    width *= 1.05
                    height *= 1.05

        elif width > c_width/1.2 or height > c_height/1.2-100:
            while width > c_width/1.2-400 or height > c_height/1.2-500:
                width /= 1.1
                height /= 1.1

        width = round(width)
        height = round(height)
        self.screen_x = width
        self.screen_y = height
        self.image = pygame.transform.scale(self.image, (width, height))
        pygame.display.set_mode((width, height+100))

        self.done_button_rect.x = self.screen.get_width()- 100
        self.done_button_rect.y = 0

        #here I load images
        self.right_button = pygame.image.load("images/right.png")
        self.right_button = pygame.transform.scale(self.right_button, (100, 100))
        self.right_button_rect = self.right_button.get_rect()
        self.right_button_rect.x = self.image.get_width()-self.right_button.get_width()
        self.right_button_rect.y = 0

        self.transparent_green = pygame.image.load("images/transparent.png")
        self.transparent_green = pygame.transform.scale(self.transparent_green,(self.screen.get_width(), self.screen.get_height()))
        self.transparent_green_rect = self.transparent_green.get_rect()

        self.final_message_box = pygame.image.load("images/message_box4.png")
        self.final_message_box = pygame.transform.scale(self.final_message_box, (round(self.final_message_box.get_width() / 1.75), round(self.final_message_box.get_height() / 1.75)))
        self.final_message_box_rect = self.final_message_box.get_rect()
        self.final_message_box_rect.x = (self.screen.get_width() - self.final_message_box.get_width()) / 2
        self.final_message_box_rect.y = (self.screen.get_height() - self.final_message_box.get_height()) / 2.5

        self.save_button = pygame.image.load("images/save.png")
        self.save_button = pygame.transform.scale(self.save_button, (round(self.save_button.get_width() / 2), round(self.save_button.get_height() / 2)))
        self.save_button_rect = self.save_button.get_rect()
        self.save_button_rect.x = round((self.screen.get_width() - self.save_button.get_width()) / 2)

        e = (self.final_message_box_rect.y + self.final_message_box.get_height() + self.save_button.get_height())
        self.save_button_rect.y = round(self.final_message_box_rect.y + self.final_message_box.get_height() + (self.screen.get_height() - e) / 2)



    def get_parameters(self, mx, my):
        if not self.program.right_click_pressed[1] and self.program.was_pressed:
            self.position_list.append([mx, my])
            self.program.was_pressed = False



