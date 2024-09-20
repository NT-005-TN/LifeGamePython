import copy

import pygame as pg
from random import randint
import ctypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
monitor_width = user32.GetSystemMetrics(0)
monitor_height = user32.GetSystemMetrics(1)

print(monitor_width, monitor_height)

size = 50
width_count, height_count = monitor_width//size - (monitor_width//size//8), monitor_height//size - (monitor_height//size//8)
resolution = width, height = size * width_count + 1, size * height_count + 1

screen = pg.display.set_mode(resolution)
#screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
FPS = 20

field = [[randint(0,1) for _ in range(width_count)] for _ in range(height_count)]
new_field = [[0 for _ in range(width_count)] for _ in range(height_count)]

def Paint(field, pos):
    x,y = pos
    count_neighboors = 0

    for y1 in range(y-1, y+2):
        for x1 in range(x-1, x+2):
            if field[y1][x1] == 1:
                count_neighboors += 1

    if field[y][x]:
        count_neighboors -= 1

        if count_neighboors in [2, 3]:
            return 1
        else:
            return 0
    else:
        if count_neighboors == 3:
            return 1
        else:
            return 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

    screen.fill(pg.Color('white'))

    [pg.draw.line(screen, (0, 0, 0), (x, 0), (x, height)) for x in range(0, width, size) ]
    [pg.draw.line(screen, (0, 0, 0), (0, y), (width, y)) for y in range(0, height, size) ]
    #Развернутый вариант снизу, сверху более короткий
    #for x in range(0, width, size):
    #    pg.draw.line(screen, (0, 0, 0), (x, 0), (x, height))

    for x in range(1, width_count - 1):
        for y in range(1, height_count - 1):
            if field[y][x] == 1:
                pg.draw.rect(screen, (0, 0, 0), (x * size + 2, y * size + 2, size - 2, size - 2))
            new_field[y][x] = Paint(field, (x,y))

    field = copy.deepcopy(new_field)

    clock.tick(FPS)
    pg.display.flip()


'''
Стена смерти
count = 0
for x in range(1, width_count-1):
    for y in range(1, height_count-1):
        field[y][x] = randint(0,1)

        if field[y][x] == 1:
            count += 1

        if count > height_count*width_count/8:
            break

    if count > height_count * width_count / 8:
        break

'''
