try:
    from win32api import GetSystemMetrics
except ModuleNotFoundError:
    pass
import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))



while True:

    pygame.display.update()
    print(pygame.display.Info().current_w, pygame.display.Info().current_h)
    print(GetSystemMetrics(0), GetSystemMetrics(1))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()