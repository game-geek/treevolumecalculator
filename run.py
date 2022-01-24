import pygame
from cal2 import Cal
pygame.init()
screen = pygame.display.set_mode((1300, 700))
image = "tree.jpg"
#background = pygame.image.load(image)
#background = pygame.transform.scale(background, (1300, 700))
black = (0,0,0)
screen.fill(black)
cal1 = Cal()


a = 10
b = 20


running  = True


while running:


    pygame.display.flip()
    #screen.blit(background, (0, 0))
    cal1.imp(screen)



    for event in pygame.event.get():
        # pour verifier que l'évênement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()





