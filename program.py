import pygame
#from color_trunk import Color_Trunk
from module_draw_line import Draw_line
from aire import Aire_leaf
from Volume import Volume
from Volume2 import Volume2
from two_dimensial_volume_viewer import VolumeViewer
from homepage import HomePage
from homepage2 import HomePage2
from text import Text
import time
from generate import Generate
from hover import Hover
from settings import Settings

class Program:

    def __init__(self, surface):
        self.screen = surface
#       self.color_trunk = Color_Trunk(self.screen)
        self.draw_line = Draw_line(self, self.screen)
        self.right_click_pressed = {}
        self.right_click_pressed[1] = False
        #to get the click position
        self.was_pressed = False
        # to make the lines continuous
        self.switch = False

        self.end_leaf = False
        self.end_trunk = False
        self.case = 0   # 0: homepage , 1 : get parameters, 2 continue getting parameters,  3 :
        # leaf parameters , 4 : calculate and show preview results, 5 : final volume and page
        self.image_type = 1   #1 or 2
        self.calculate = True  # True   False
        self.end_partial = False
        self.setups = []
        self.checker = True
        self.pressing = False
        self.begin = True
        self.load()

        self.begin_initial = True

        self.started = False
        self.volume2 = Volume2(self)


        self.e = 1


        self.point1 = ()
        self.point2 = ()
        self.part1 = True
        self.part2 = True
        self.scale = []




        self.error_text = Text(self, self.screen, "images/large_font.png")
        self.ok_text = Text(self, self.screen, "images/large_font_green.png")
        self.informative_text = Text(self, self.screen, "images/large_font_black2.png", (0,100,0))

        self.enable_text_input = 0 #the same as False

        #create an instance of the hover class
        self.hover = Hover(self, self.screen)
        #set the hover types
        self.hover.add_name("start1_button", self.start1_button.get_width(), self.start1_button.get_height(), (self.start1_button_rect.x, self.start1_button_rect.y))
        self.hover.add_name("start2_button", self.start2_button.get_width(), self.start2_button.get_height(), (self.start2_button_rect.x, self.start2_button_rect.y))
        self.hover.reset()

        self.settings = Settings(self, self.screen)



    def run(self, mx, my):




        if self.settings.set:
            self.settings.main_page(mx, my)
        else:
            if self.begin:
                self.begin_settings(mx, my)
            else:
                self.homepage.image_processor(mx, my)


            if self.image_type == 1:
                if not self.right_click_pressed[1] and self.was_pressed and self.case == 3:
                    if self.started:
                        self.position2x = mx
                        self.position2y = my

                        #add in database
                        self.draw_line.register(self.position1x, self.position2x, self.position1y, self.position2y)
                        self.position1x = self.position2x
                        self.position1y = self.position2y
                        self.was_pressed = False

                    else:  # start the program (get the first coordinates)
                        self.position1x = mx
                        self.position1y = my
                        # define the function as started
                        self.started = True
                        self.was_pressed = False
                elif self.case == 1:
                    pass
                #self.get_parameters(mx, my)
                #self.was_pressed = False




    def begin_settings(self, mx, my):
        self.screen.blit(self.welcome_image, (0, 0))
        self.hover.show((mx, my))

        # blit the essencial buttons
        self.screen.blit(self.start1_button, (self.start1_button_rect.x, self.start1_button_rect.y))
        self.screen.blit(self.start2_button, (self.start2_button_rect.x, self.start2_button_rect.y))

    def load(self):
        self.start1_button = pygame.image.load("images/start_1.png")
        self.start1_button = pygame.transform.scale(self.start1_button, (500, 100))
        self.start1_button_rect = self.start1_button.get_rect()
        self.start1_button_rect.x = 70
        self.start1_button_rect.y = 350

        self.start2_button = pygame.image.load("images/start_2.png")
        self.start2_button = pygame.transform.scale(self.start2_button, (500, 100))
        self.start2_button_rect = self.start2_button.get_rect()
        self.start2_button_rect.x = 70
        self.start2_button_rect.y = 500

        self.welcome_image = pygame.image.load("images/main_page.png")
        self.welcome_image = pygame.transform.scale(self.welcome_image, (640, 640))



    def calculate_leaf_volume(self):
        #register all the traced lines
        self.draw_line.register_lines(self.draw_line.leaf_lines)
        print('lol')

        #calculate the disks
        self.leaf_volume = Volume(self)
        self.leaf_volume.Leaf_volume(10)
        self.leaf_volume.Precise_volume()
        self.viewer = VolumeViewer(self, self.screen)



    def get_parameters(self, mx, my):
        if self.right_click_pressed[1] == False and self.was_pressed and self.part1 :
            self.point1 = (mx, my)
            self.part1 = False
            self.part2 = True
            self.homepage.position_list.append((mx,my))
        elif self.right_click_pressed[1] == False and self.was_pressed and self.part2:
            self.point2 = (mx, my)
            self.part2 = False
            self.part1 = True
            #print(self.point1, self.point2)
            self.scale.append((self.point1, self.point2))
            self.homepage.position_list.append((mx, my))
        if len(self.scale) == 2:
            self.case += 1
            self.part1 = False
            self.part2 = False

    def setup(self):

        self.setups.append((self.position1x, self.position2x))
        self.setups.append((self.position1y, self.position2y))
        self.checker = False

    def reset(self):
        #reset all parameters

        generate = Generate()
        generate.Generate_pixels("data/pixels")
        generate.Clear("data/save", "csv")
        generate.Generate_pixels("data/pixels2")
        generate.Clear("data/save2", "csv")

        self.draw_line = Draw_line(self, self.screen)
        self.switch = False
        self.end_leaf = False
        self.end_trunk = False
        self.point1 = ()
        self.point2 = ()
        self.part1 = True
        self.part2 = True
        self.scale = []
        del self.homepage
        self.homepage = HomePage(self, self.screen)
        self.enable_text_input = 0
        self.hover = Hover(self, self.screen)

        self.hover.add_name(
            "start1_button",
            self.start1_button.get_width(),
            self.start1_button.get_height(),
            (self.start1_button_rect.x, self.start1_button_rect.y)
        )
        self.hover.add_name(
            "start2_button",
            self.start2_button.get_width(),
            self.start2_button.get_height(),
            (self.start2_button_rect.x, self.start2_button_rect.y)
        )
        self.hover.reset()

        try:
            del self.leaf_volume
        except AttributeError:
            pass

        self.image_type = 1
        self.leaf_volume = Volume(self)
        self.case = 0
        pygame.display.set_mode((640, 640))
        self.begin = True
        self.begin_initial = True


    def set_type(self):
        if self.image_type == 1:
            self.homepage = HomePage(self, self.screen)
        elif self.image_type == 2:
            self.homepage = HomePage2(self, self.screen)
