import pygame
from pygame.locals import *


class Text:

    def __init__(self, program, screen, path, colorkey = (0,0,0)):
        self.colorkey = colorkey
        self.program = program
        self.screen = screen

        self.spacing = 1
        self.character_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                                'z', '.', '-', ',', ':', '+', '\'', '!', '?', '0', '1', '2', '3', '4', '5', '6', '7',
                                '8', '9', '(', ')', '/', '_', '=', '\\', '[', ']', '*', '"', '<', '>', ';']
        font_img = pygame.image.load(path).convert()

        font_img.set_colorkey(self.colorkey)


        current_char_width = 0
        self.characters = {}
        character_count = 0
        for x in range(font_img.get_width()):
            c = font_img.get_at((x, 0))
            if c[0] == 127:
                char_img = self.clip(font_img, x - current_char_width, 0, current_char_width, font_img.get_height())
                self.characters[self.character_order[character_count]] = char_img.copy()
                character_count += 1
                current_char_width = 0
            else:
                current_char_width += 1
        self.space_width = self.characters['A'].get_width()


    def clip(self,image, x, y, x_size, y_size):
        handle_surf = self.screen.copy()
        clipR = pygame.Rect(x, y, x_size, y_size)
        handle_surf.set_clip(clipR)
        image = image.subsurface(handle_surf.get_clip())
        return image.copy()


    def render(self, text, location):
        self.location = [location[0], location[1]]
        x_offset = 0
        for char in text:
            if char == "&":
                x_offset = 0
                self.location[1] += 16

            elif char != ' ':
                self.screen.blit(self.characters[char], (self.location[0] + x_offset, self.location[1]))#, special_flags=2
                x_offset += self.characters[char].get_width() + self.spacing
            else:
                x_offset += self.space_width + self.spacing



