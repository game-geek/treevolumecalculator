import pygame
from tkinter import *
from tkinter import filedialog
from info import Info

class HomePage:


    def __init__(self, program, screen):
        self.screen = screen
        self.program = program
        self.welcome_image = pygame.image.load("images/main_page.png")
        self.welcome_image = pygame.transform.scale(self.welcome_image, (640, 640))

        self.open_button = pygame.image.load("images/open.jpg")
        self.open_button = pygame.transform.scale(self.open_button, (213, 69))
        self.open_button_rect = self.open_button.get_rect()
        self.open_button_rect.x = 50
        self.open_button_rect.y = 400

        self.calculate_button = pygame.image.load("images/calculate.jpg")
        self.calculate_button = pygame.transform.scale(self.calculate_button, (213, 69))
        self.calculate_button_rect = self.calculate_button.get_rect()
        self.calculate_button_rect.x = 313
        self.calculate_button_rect.y = 400

        self.done_button = pygame.image.load("images/done_button_new.png")
        self.done_button = pygame.transform.scale(self.done_button, (100, 100))
        self.done_button_rect = self.done_button.get_rect()
        self.done_button_rect.x = 540
        self.done_button_rect.y = 0

        #self.image = "E:\Python\python_for_school_1.22\Tree_volume_calculator\tree.jpg"
        #self.tree_image = pygame.image.load(self.image)
        #self.tree_image = pygame.transform.scale(self.tree_image, (640, 640))

        self.show_error1 = True

        self.message_box = pygame.image.load("images/message_box.png")
        self.message_box = pygame.transform.scale(self.message_box, (round(self.message_box.get_width()/3), round(self.message_box.get_height()/3)))
        self.message_box_rect = self.message_box.get_rect()
        self.message_box_rect.x = 0
        self.message_box_rect.y = 0

        self.scale_box = pygame.image.load("images/input.png")
        #self.scale_box = pygame.transform.scale()
        self.scale_box_rect = self.scale_box.get_rect()
        self.scale_box_rect.x = self.message_box_rect.x+self.message_box.get_width()
        self.scale_box_rect.y = 0

        self.cursor = pygame.image.load("images/cross3.png")
        self.cursor_rect = self.cursor.get_rect()

        self.position_list = []
        self.keys = {}
        self.phrase1 = ""
        self.phrase2 = ""
        self.part = "phrase1"

        #self.transparent_green = pygame.image.load("E:\Python\python_for_school_1.22\Tree_volume_calculator\transparent.png")
        #self.transparent_green = pygame.transform.scale(self.transparent_green, (self.screen.get_width(), self.screen.get_height()))
        #self.transparent_green_rect = self.transparent_green.get_rect()
#
        #self.final_message_box = pygame.image.load("E:\Python\python_for_school_1.22\Tree_volume_calculator\message_box4.png")
        #self.final_message_box = pygame.transform.scale(self.final_message_box, (round(self.final_message_box.get_width() / 1.75), round(self.final_message_box.get_height() / 1.75)))
        #self.final_message_box_rect = self.final_message_box.get_rect()
        #self.final_message_box_rect.x = (self.screen.get_width() - self.final_message_box.get_width())/2
        #self.final_message_box_rect.y = (self.screen.get_height() - self.final_message_box.get_height())/2.5
#
        #self.save_button = pygame.image.load("E:\Python\python_for_school_1.22\Tree_volume_calculator\save.png")
        #self.save_button = pygame.transform.scale(self.save_button,(round(self.save_button.get_width() / 2), round(self.save_button.get_height() / 2)))
        #self.save_button_rect = self.save_button.get_rect()
        #self.save_button_rect.x = round((self.screen.get_width()-self.save_button.get_width())/2)
        #e = (self.final_message_box_rect.y + self.final_message_box.get_height() + self.save_button.get_height())
        #self.save_button_rect.y = round(self.final_message_box_rect.y  + self.final_message_box.get_height() +(self.screen.get_height() - e)/2)

        self.backwards_button = pygame.image.load("images/back_new.png")
        self.backwards_button = pygame.transform.scale(self.backwards_button, (100, 100))
        self.backwards_button_rect = self.backwards_button.get_rect()
        self.backwards_button_rect.x = 0
        self.backwards_button_rect.y = 110

        self.info = Info(self.program, self.screen)

        self.loop = 0
        self.max_loop = 300





    def home_page(self, mx, my):
        #screw up the background
        self.screen.blit(self.welcome_image, (0,0))
        self.program.hover.show((mx, my))
        #blit the essencial buttons
        self.screen.blit(self.open_button, (self.open_button_rect.x, self.open_button_rect.y))
        self.screen.blit(self.calculate_button, (self.calculate_button_rect.x, self.calculate_button_rect.y))

        if self.show_error1:
            self.program.error_text.render("Your file is not appropriate!", (50, 474))

    def calculate_1(self):
        self.screen.blit(self.welcome_image, (0, 0))
        self.screen.blit(self.open_button, (self.open_button_rect.x, self.open_button_rect.y))
        self.screen.blit(self.calculate_button, (self.calculate_button_rect.x, self.calculate_button_rect.y))
        if self.show_error1:
           self.program.error_text.render("Your file is not appropriate!", (50, 474))




    def calculate_step1(self, mx, my):
        self.program.get_parameters(mx, my)
        self.program.was_pressed = False
        if self.program.settings.info_bar_state:
            self.screen.blit(self.tree_image, (0, 100))
            self.program.hover.show((mx, my))
            self.info.box_top(("STEP 1", "Locate Your Scaling object on the screen"))
        else:
            self.screen.blit(self.tree_image, (0, 0))
            self.program.hover.show((mx, my))
            self.info.box_bottom(("STEP 1", "Locate Your Scaling object on the screen"))

        self.screen.blit(self.program.settings.button, (self.program.settings.button_rect.x, self.program.settings.button_rect.y))

        if len(self.position_list) == 1:
            self.cursor_rect.x = mx - 25
            self.cursor_rect.y = self.position_list[0][1]-25
        elif len(self.position_list) == 3:
            self.cursor_rect.x = self.position_list[2][0]-25
            self.cursor_rect.y = my - 25
        else:
            self.cursor_rect.x = mx-25
            self.cursor_rect.y = my - 25


        self.screen.blit(self.cursor, (self.cursor_rect.x, self.cursor_rect.y))
        count = 1
        for point in self.position_list:
            if count == 2:
                self.screen.blit(self.cursor, (self.position_list[1][0]-25, self.position_list[0][1]-25))
            elif count == 4:
                self.screen.blit(self.cursor, (self.position_list[2][0] - 25, self.position_list[3][1] - 25))
            else:
                self.screen.blit(self.cursor, (point[0] - 25, point[1] - 25))
            count += 1


    def calculate_step2(self, mx,my):
        self.program.enable_text_input = True
        if self.keys.get("enter") and self.part == "phrase1":
            self.part = "phrase2"
            self.keys["enter"] = False
        elif self.keys.get("enter") and self.part == "phrase2":
            self.program.case += 1
            self.program.hover.add_name(
                "done_button",
                self.done_button.get_width(), self.done_button.get_height(),
                (self.done_button_rect.x, self.done_button_rect.y),
                "images/done_button_new_black.png"
            )
            self.program.hover.add_name(
                "backwards_button",
                self.program.homepage.backwards_button.get_width(), self.backwards_button.get_height(),
                (self.backwards_button_rect.x, self.backwards_button_rect.y),
                "images/back_new_black.png",
            )
            self.program.hover.reset()
            self.keys["enter"] = False
        elif self.keys.get("back_space") and self.part == "phrase1":# and not self.program.cooldown
            new_phrase = ""
            count = 1
            if self.phrase1 == "":
                self.keys["back_space"] = False
            else:
                for e in self.phrase1:
                    if count == len(self.phrase1):
                        self.keys["back_space"] = False
                        self.phrase1 = new_phrase
                        #self.program.cooldown = True
                        break
                    else:
                        new_phrase += e
                    count += 1

        elif self.keys.get("back_space") and self.part == "phrase2":# and not self.program.cooldown
            new_phrase = ""
            count = 1
            if self.phrase2 == "":
                self.keys["back_space"] = False
            else:
                for e in self.phrase2:
                    if count == len(self.phrase2):
                        self.keys["back_space"] = False
                        self.phrase2 = new_phrase
                        #self.program.cooldown = True
                        break
                    else:
                        new_phrase += e
                    count += 1
        if self.program.settings.info_bar_state:
            self.screen.blit(self.tree_image, (0, 100))
            self.program.hover.show((mx, my))
            self.info.box_top(("STEP 2", "Enter the scale in meters"))
        else:
            self.screen.blit(self.tree_image, (0, 0))
            self.program.hover.show((mx, my))
            self.info.box_bottom(("STEP 2", "Enter the scale in meters"))

        count = 1
        if self.part == "phrase1":
            for point in self.position_list:
                if count == 1:
                    self.screen.blit(self.cursor, (point[0] - 25, point[1] - 25))
                elif count == 2:
                    self.screen.blit(self.cursor, (self.position_list[1][0] - 25, self.position_list[0][1] - 25))
                count += 1
            if self.loop < self.max_loop / 2:
                self.info.custom_message(("X : " + self.phrase1 + "|", None), (500, 10), (255, 0, 0))
                self.info.custom_message(("Y : " + self.phrase2, None), (500, 30))
                self.loop += 1
            else:
                self.info.custom_message(("X : " + self.phrase1, None), (500, 10), (255, 0, 0))
                self.info.custom_message(("Y : " + self.phrase2, None), (500, 30))
                self.loop += 1


        elif self.part == "phrase2":
            for point in self.position_list:
                if count == 3:
                    self.screen.blit(self.cursor, (point[0] - 25, point[1] - 25))
                elif count == 4:
                    self.screen.blit(self.cursor, (self.position_list[2][0] - 25, self.position_list[3][1] - 25))
                count += 1

            if self.loop < self.max_loop / 2:
                self.info.custom_message(("X : " + self.phrase1, None), (500, 10))
                self.info.custom_message(("Y : " + self.phrase2 + "|", None), (500, 30), (255, 0, 0))
                self.loop += 1
            else:
                self.info.custom_message(("X : " + self.phrase1, None), (500, 10))
                self.info.custom_message(("Y : " + self.phrase2, None), (500, 30), (255, 0, 0))
                self.loop += 1

        if self.loop == self.max_loop:
                self.loop = 0

        self.screen.blit(self.program.settings.button, (self.program.settings.button_rect.x, self.program.settings.button_rect.y))

    def image_processor(self, mx, my):
        if self.program.case == 0:
            self.home_page(mx,my)
        elif self.program.case == 1:
            self.calculate_step1(mx, my)
        elif self.program.case == 2:
            self.calculate_step2(mx,my)
        elif self.program.case == 3:
            self.calculate_step3(mx,my)
        elif self.program.case == 4:
            self.calculate_step4(mx,my)
        elif self.program.case == 5:
            self.calculate_step5(mx,my)

    def calculate_step3(self, mx,my):

        if self.program.settings.info_bar_state:
            self.screen.blit(self.tree_image, (0, 100))
            self.info.box_top(("STEP 3", "By using your mouse, click around the image to let the computer know were the tree is.", "When you have finished, press the top right button"))
            self.program.hover.show((mx, my))
            self.screen.blit(self.done_button, (self.done_button_rect.x, self.done_button_rect.y))  # 3 &nd 4
        else:
            self.screen.blit(self.tree_image, (0, 0))
            self.info.box_bottom(("STEP 3",
                               "By using your mouse, click around the image to let the computer know were the tree is.",
                               "When you have finished, press the top right button"))
            self.program.hover.show((mx, my))
            self.screen.blit(self.done_button, (self.done_button_rect.x, self.done_button_rect.y))  # 3 &nd 4

        self.screen.blit(self.backwards_button, (self.backwards_button_rect.x, self.backwards_button_rect.y))
        self.program.draw_line.update(self.program.draw_line.leaf_lines)

        self.screen.blit(self.program.settings.button, (self.program.settings.button_rect.x, self.program.settings.button_rect.y))

    def calculate_step4(self,mx,my):
        if self.program.settings.info_bar_state:
            self.screen.blit(self.tree_image, (0, 100))
            self.info.box_top(("PREVIEW     Check if no problems occured.", "If none have occured please push the last button wich will reveal the volume of the tree!"))
            self.program.hover.show((mx, my))
            self.screen.blit(self.right_button, (self.right_button_rect.x, self.right_button_rect.y))
            self.program.viewer.View(self.program.leaf_volume.total_points_volume)
        else:
            self.screen.blit(self.tree_image, (0, 0))
            self.info.box_top(("PREVIEW     Check if no problems occured.",
                               "If none have occured please push the last button wich will reveal the volume of the tree!"))
            self.program.hover.show((mx, my))
            self.screen.blit(self.right_button, (self.right_button_rect.x, self.right_button_rect.y))
            self.program.viewer.View(self.program.leaf_volume.total_points_volume)


    def calculate_step5(self, mx,my):
        if self.program.settings.info_bar_state:
            self.screen.blit(self.tree_image, (0, 100))
            self.info.box_top(("Your finall volume is : "+str(self.program.leaf_volume.Ptotal_volume)+"m3",
                               "The approxamitive volume is : " + str(self.program.leaf_volume.Ptotal_volume_round) + "m3"))
            self.program.hover.show((mx, my))
            self.screen.blit(self.save_button, (self.save_button_rect.x, self.save_button_rect.y))
        else:
            self.screen.blit(self.tree_image, (0, 0))
            self.info.box_bottom(("Your finall volume is : " + str(self.program.leaf_volume.Ptotal_volume) + "m3",
                               "The approxamitive volume is : " + str(self.program.leaf_volume.Ptotal_volume_round) + "m3"))
            self.program.hover.show((mx, my))
            self.screen.blit(self.save_button, (self.save_button_rect.x, self.save_button_rect.y))


    def open(self):
        #print('start')
        root = Tk()

        root.config(bg='#4065A4')

        root.title("open...")

        root.filename = filedialog.askopenfilename(initialdir="D:\Python\python_for_school_1.19\Tree_volume_calculator", title='Select a file',filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))

        if root.filename != '':
            image = root.filename
            check_image = image.split(".")
            if check_image[-1] != "png" and check_image[-1] != "jpg":
                self.show_error1 = True
            else:
                self.image = image
                self.tree_image = pygame.image.load(self.image)
                #self.tree_image = pygame.transform.scale(self.tree_image, (640, 640))
                self.show_error1 = False

        root.destroy()

        root.mainloop()
        #print('end')

    def resize_image(self):
        width = self.tree_image.get_width()
        height = self.tree_image.get_height()
        if width > pygame.display.Info().current_w or height > pygame.display.Info().current_h:
            while width > pygame.display.Info().current_w or height > pygame.display.Info().current_h:
                w = width/10
                width = round(w*9)
                h = height/10
                height = round(h*9)
                #print("rezised !")
        elif width < pygame.display.Info().current_w or height < pygame.display.Info().current_h:
            while width < pygame.display.Info().current_w*1.3 and height < pygame.display.Info().current_h*1.3:
                    w = width / 10
                    width = round(w * 11)
                    h = height / 10
                    height = round(h * 11)
                    #print("rezised 2!")

        self.screen_x = width
        self.screen_y = height
        self.tree_image = pygame.transform.scale(self.tree_image, (width, height))
        pygame.display.set_mode((width, height))

        self.done_button_rect.x = self.screen.get_width()- 100
        self.done_button_rect.y = 0

        #here I load images
        self.right_button = pygame.image.load("images/right_new.png")
        self.right_button = pygame.transform.scale(self.right_button, (100, 100))
        self.right_button_rect = self.right_button.get_rect()
        self.right_button_rect.x = self.tree_image.get_width()-self.right_button.get_width()
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
        self.save_button = pygame.transform.scale(self.save_button, (250, 100))
        self.save_button_rect = self.save_button.get_rect()
        self.save_button_rect.x = 20
        self.save_button_rect.y = 150













