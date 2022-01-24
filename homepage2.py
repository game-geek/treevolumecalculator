import pygame
from tkinter import *
from tkinter import filedialog
from image import Image
from info import Info

class HomePage2:


    def __init__(self, program, screen):
        self.screen = screen
        self.program = program
        self.welcome_image = pygame.image.load("images/main_page.png")
        self.welcome_image = pygame.transform.scale(self.welcome_image, (640, 640))



        self.save_button = pygame.image.load("images/save.png")
        self.save_button = pygame.transform.scale(self.save_button, (100, 100))
        self.save_button_rect = self.save_button.get_rect()
        self.save_button_rect.x = 10
        self.save_button_rect.y = 120

        self.right_button = pygame.image.load("images/right.png")
        self.right_button = pygame.transform.scale(self.right_button, (100, 100))
        self.right_button_rect = self.right_button.get_rect()
        self.right_button_rect.x = 10
        self.right_button_rect.y = 120


        self.open_button = pygame.image.load("images/open.jpg")
        self.open_button = pygame.transform.scale(self.open_button, (213, 69))
        self.open_button_rect = self.open_button.get_rect()
        self.open_button_rect.x = 50
        self.open_button_rect.y = 400

        self.calculate_button = pygame.image.load("images/calculate.jpg")
        self.calculate_button = pygame.transform.scale(self.calculate_button, (213, 69))
        self.calculate_button_rect = self.calculate_button.get_rect()
        self.calculate_button_rect.x = 313
        self.calculate_button_rect.y = 425

        self.done_button = pygame.image.load("images/new_done_button.png")
        self.done_button = pygame.transform.scale(self.done_button, (100, 100))
        self.done_button_rect = self.done_button.get_rect()
        self.done_button_rect.x = 540
        self.done_button_rect.y = 0

        #self.image = "E:\Python\python_for_school_1.22\Tree_volume_calculator\tree.jpg"
        #self.tree_image = pygame.image.load(self.image)
        #self.tree_image = pygame.transform.scale(self.tree_image, (640, 640))

        self.show_error1 = False
        self.show_error2 = False

        self.message_box = pygame.image.load("images/message_box.png")
        self.message_box = pygame.transform.scale(self.message_box, (round(self.message_box.get_width()/3), round(self.message_box.get_height()/3)))
        self.message_box_rect = self.message_box.get_rect()
        self.message_box_rect.x = 0
        self.message_box_rect.y = 0
        self.begin1 = True
        self.begin2 = True

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
        self.currently = [1]


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

        self.backwards_button = pygame.image.load("images/back.png")
        self.backwards_button = pygame.transform.scale(self.backwards_button, (100, 100))
        self.backwards_button_rect = self.backwards_button.get_rect()
        self.backwards_button_rect.x = 360
        self.backwards_button_rect.y = -8


        #open and change button

        self.open_button = pygame.image.load("images/open_test.png")
        self.open_button_rect = self.open_button.get_rect()
        self.open_button_rect.x = 170
        self.open_button_rect.y = 390

        self.open_button2 = pygame.image.load("images/open_test.png")
        self.open_button2_rect = self.open_button2.get_rect()
        self.open_button2_rect.x = 170
        self.open_button2_rect.y = 490


        self.change_button = pygame.image.load("images/change_test.png")
        self.change_button_rect = self.change_button.get_rect()
        self.change_button_rect.x = 170
        self.change_button_rect.y = 390

        self.change_button2 = pygame.image.load("images/change_test.png")
        self.change_button2_rect = self.change_button2.get_rect()
        self.change_button2_rect.x = 170
        self.change_button2_rect.y = 490

        self.image1 = "None"
        self.image2 = "None"

        self.counter = 0

        self.info = Info(self.program, self.screen)





    def home_page(self, mx, my):
        #screw up the background
        self.screen.blit(self.welcome_image, (0,0))
        self.program.hover.show((mx, my))

        #blit the essencial buttons


        if self.show_error1:
            self.program.error_text.render(self.image1, (30, 400))
        else:
            self.program.ok_text.render(self.image1, (30, 400))


        if self.show_error2:
            self.program.error_text.render(self.image2, (30, 500))
        else:
            self.program.ok_text.render(self.image2, (30, 500))

        if self.begin1:
            self.screen.blit(self.open_button, (self.open_button_rect.x, self.open_button_rect.y))
        else:
            self.screen.blit(self.change_button, (self.open_button_rect.x, self.open_button_rect.y))

        if self.begin2:
            self.screen.blit(self.open_button2, (self.open_button2_rect.x, self.open_button2_rect.y))
        else:
            self.screen.blit(self.change_button2, (self.open_button2_rect.x, self.open_button2_rect.y))

        self.screen.blit(self.calculate_button, (self.calculate_button_rect.x, self.calculate_button_rect.y))

    def calculate_1(self):
        self.screen.blit(self.welcome_image, (0, 0))
        self.screen.blit(self.open_button, (self.open_button_rect.x, self.open_button_rect.y))
        self.screen.blit(self.calculate_button, (self.calculate_button_rect.x, self.calculate_button_rect.y))
        if self.show_error1:
           self.program.error_text.render("Your file is not appropriate!", (50, 474))

    def image_sorter(self):
        self.images = []
        self.currently = []
        self.images.append(Image(self.program, self.screen, self.tree_image1))
        self.images.append(Image(self.program, self.screen, self.tree_image2))
        self.currently.append(1)
        self.images[0].resize_image()
        self.images[0].renew_images()

    def image_processor(self, mx, my):
        if self.currently[0] == 1:
            if self.program.case == 0:
                self.home_page(mx, my)
            elif self.program.case == 1:
                self.images[0].show_scale(mx, my)
                if not self.program.right_click_pressed[1] and self.program.was_pressed:
                    self.images[0].get_parameters(mx, my)

            elif self.program.case == 2:
                self.images[0].input_scale(mx, my)

            elif self.program.case == 3:
                self.images[0].precise_image(mx, my)


        elif self.currently[0] == 2:
            if self.program.case == 0:
                self.home_page(mx, my)
            elif self.program.case == 1:
                self.images[1].show_scale(mx, my)
                if not self.program.right_click_pressed[1] and self.program.was_pressed:
                    self.images[1].get_parameters(mx, my)

            elif self.program.case == 2:
                self.images[1].input_scale(mx, my)

            elif self.program.case == 3:
                self.images[1].precise_image(mx, my)
        else:
            if self.program.case == 4:
                self.calculate_step4(mx, my)
            elif self.program.case == 5:
                self.calculate_step5(mx, my)



    ###############################
    def calculate_step4(self, mx, my):
        self.screen.blit(self.tree_image2, (0,100))
        self.info.box_top(("PREVIEW",
                           "Check if no problems occured.",
                           "If none have occured please push the last button wich will reveal the volume of the tree!"
                           ))

        self.program.hover.show((mx, my))
        self.screen.blit(self.right_button, (self.right_button_rect.x, self.right_button_rect.y))

    def calculate_step5(self, mx, my):
        self.screen.blit(self.tree_image2, (0, 100))
        self.info.box_top((
            "Your finall volume is : "+str(self.program.volume) + " m3",
            "The approxamitive volume is : " + str(self.program.volume) + "m3"
        ))
        self.program.hover.show((mx, my))
        self.screen.blit(self.save_button, (self.save_button_rect.x, self.save_button_rect.y))

    def open(self, type):
        #print('start')
        root = Tk()

        root.config(bg='#4065A4')

        root.title("open...")

        root.filename = filedialog.askopenfilename(initialdir="D:\Python\python_for_school_1.19\Tree_volume_calculator", title='Select a file',filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))
        if type == 1:
            if root.filename != '':
                image = root.filename
                check_image = image.split(".")
                name = image.split("/")
                if check_image[-1] != "png" and check_image[-1] != "jpg":
                    self.show_error1 = True
                    self.program.homepage.begin1 = True
                else:
                    self.image1 = name[-1]
                    self.image = image
                    #################################################must rename self.tree_image   ####to####  self.tree_image1 ####
                    self.tree_image1 = pygame.image.load(self.image)
                    #self.tree_image = pygame.transform.scale(self.tree_image, (640, 640))
                    self.show_error1 = False
                    self.program.homepage.begin1 = False
        elif type == 2:
            if root.filename != '':
                image = root.filename
                check_image = image.split(".")
                name = image.split("/")
                #name = check_image[0].split("/")
                if check_image[-1] != "png" and check_image[-1] != "jpg":
                    self.show_error1 = True
                    self.program.homepage.begin2 = True
                else:
                    self.image2 = name[-1]
                    self.image = image
                    self.tree_image2 = pygame.image.load(self.image)
                    #self.tree_image = pygame.transform.scale(self.tree_image, (640, 640))
                    self.show_error1 = False
                    self.program.homepage.begin2 = False

        root.destroy()

        root.mainloop()
        #print('end')
















