import pygame
from pygame.draw import *
from random import *
import math

def igolki(screen, x_0, y_0, r=1):
    c = randint(0, 50)
    pygame.draw.polygon(screen, (c, c, c), [(x_0, y_0), (x_0 + randint(0, 4) * r, y_0 - randint(2, 8) * r), (x_0 + 2 * r, y_0 + randint(2, 5))])

def ezik(screen, x, y, a, b, r):
    pygame.draw.ellipse(screen, (64, 65, 62), (x, y, a, b))
    pygame.draw.ellipse(screen, (64, 65, 62), (x + 5 * a // 6, y + 2 * b // 7, a // 2, b // 2))
    # тело ежика
    for i in range(7 * r):
        x_0 = randint(x, x + 5 * a // 6)
        y_0 = randint(y, y + (2 * b // 3))
        igolki(screen, x_0, y_0, r)    # набор иголок
    pygame.draw.circle(screen, (randint(110, 250), randint(10, 100), randint(10, 100)), (x + a // 3, y - 15), 2 * r)  # яблоко
    pygame.draw.ellipse(screen, (186, 143, 143), (x + 2 * a // 3, y - 20, 3 * r, 7 * r))  # гриб
    pygame.draw.ellipse(screen, (255, 43, 43), (x + 2 * a // 3 - 2 * r, y - 20, 7 * r, 3 * r))
    for i in range(7 * r):
        x_0 = randint(x, x + (2 * a // 3))
        y_0 = randint(y, y + (b // 2))
        igolki(screen, x_0, y_0, r)    # набор иголок 2
    pygame.draw.circle(screen, (255, 255, 255), (x + (7 * a // 6) + 6, y + (b // 2) - 2), r)  # глаза
    pygame.draw.circle(screen, (0, 0, 0), (x + (7 * a // 6) + 7, y + (b // 2) - 2), r - 1)
    pygame.draw.circle(screen, (255, 255, 255), (x + (7 * a // 6) - 4, y + (b // 2)), r)
    pygame.draw.circle(screen, (0, 0, 0), (x + (7 * a // 6) - 3, y + (b // 2)), r - 1)
    pygame.draw.circle(screen, (0, 0, 0), (x + 4 * a // 3, y + (b // 2) + 4), r - 1)  # нос
    pygame.draw.circle(screen, (63,61, 58), (x + a // 6, y + b), r + 2)
    pygame.draw.circle(screen, (64, 65, 62), (x + 2 * a // 6, y + b),  r + 2)
    pygame.draw.circle(screen, (64, 65, 62), (x + 4 * a // 6, y + b), r + 2)
    pygame.draw.circle(screen, (64, 65, 62), (x + 5 * a // 6, y + b), r + 2)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))
screen.fill([44, 77, 50])
pygame.display.set_caption("My program")

# кусты
pygame.draw.rect(screen, (0, 0,0), ((0, 350), (500, 150)))
for i in range(100):
    pygame.draw.circle(screen, (randint(50, 109), randint(70, 120), randint(20, 50)),
                       (randint(0, 500), randint(350, 500)), randint(30, 60))

# пол
pygame.draw.rect(screen, (46, 35, 35), ((0, 500), (500, 200)))

# деревья
pygame.draw.rect(screen, (105, 60, 55), ((0, 0), (75, 650)))
pygame.draw.rect(screen, (125, 80, 75), ((0, 0), (25, 650)))
pygame.draw.rect(screen, (84, 60, 70), ((200, 0), (70, 550)))
pygame.draw.rect(screen, (135, 101, 124), ((200, 0), (20, 550)))
pygame.draw.rect(screen, (135, 82, 76), ((430, 0), (50, 700)))
pygame.draw.rect(screen, (157, 109, 93), ((430, 0), (15, 700)))

# листва
pygame.draw.rect(screen, (92, 105, 68), ((0, 0), (500, 150)))
for i in range(100):
    pygame.draw.circle(screen, (randint(90, 159), randint(110, 170), randint(60, 90)),
                       (randint(-100, 500), randint(-10, 200)), randint(5, 60))


ezik(screen, 150, 600, 100, 60, 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
