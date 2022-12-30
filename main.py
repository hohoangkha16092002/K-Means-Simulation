import pygame
import random
import math

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
royal_blue = (65,105,225)
crimson = (220,20,60)
gray = (112,128,144)

red_transparent = (255, 0, 0, 0.5)
blue_transparent = (0, 0, 255, 0.5)



def drawcircles(arr):
    for (x, y) in arr:
        pygame.draw.circle(display, black, (x, y), 4)


def drawRedBlueCircles(redarr, bluearr):
    for (x, y) in redarr:
        pygame.draw.circle(display, red, (x, y), 4)

    for (x, y) in bluearr:
        pygame.draw.circle(display, blue, (x, y), 4)


def drawCentroid(t1, t2):
    pygame.draw.circle(display, blue_transparent, t1, 8)
    pygame.draw.circle(display, red_transparent, t2, 8)


def selectCentroid(arr, bluearr, redarr):
    if count == 0:
        i1 = random.randrange(len(arr))
        t1 = arr[i1]
        i2 = random.randrange(len(arr))
        t2 = arr[i2]
        pygame.draw.circle(display, red, t1, 4)
        pygame.draw.circle(display, blue, t2, 4)
    else:
        sum_x_blue = 0
        sum_y_blue = 0
        sum_x_red = 0
        sum_y_red = 0
        for (x, y) in bluearr:
            sum_x_blue += x
            sum_y_blue += y
        for (x, y) in redarr:
            sum_x_red += x
            sum_y_red += y
        t1 = (sum_x_blue / len(bluearr), sum_y_blue / len(bluearr))
        t2 = (sum_x_red / (len(redarr)), sum_y_red / len(redarr))
    x1, y1 = t1
    x2, y2 = t2
    t1 = (int(x1), int(y1))
    t2 = (int(x2), int(y2))
    return t1, t2, int(x1), int(y1), int(x2), int(y2)


def assignPoints(t1, t2, arr):
    for (x, y) in arr:
        result = calculateShortestDistance(x, y, t1, t2)
        if result == 1:
            bluearr.append((x, y))
        else:
            redarr.append((x, y))


def calculateShortestDistance(x, y, t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    dist1 = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
    dist2 = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
    if dist1 < dist2:
        return 1
    return 0

#Clustering Simulation
pygame.init()
clock = pygame.time.Clock()
width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("K Means")
exit = False
arr = []
#----------------------------------
font = pygame.font.Font('freesansbold.ttf', 20)
cen1 = ''
cen2 = ''
#---------------------------------

global count, bluearr, redarr
count = 0
bluearr = []
redarr = []
display.fill((255, 255, 255))
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            arr.append((x, y))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                t1, t2, x1, y1, x2, y2 = selectCentroid(arr, bluearr, redarr)
                cen1 = str(x1) +' '+ str(y1)
                cen2 = str(x2) +' '+ str(y2)
                count += 1
    display.fill(white)
    drawcircles(arr)
    drawRedBlueCircles(redarr, bluearr)
    text1 = font.render(cen1, True, blue, gray)
    text2 = font.render(cen2, True, red, gray)
    textRect1 = text1.get_rect()
    textRect2 = text2.get_rect()
    textRect1.center = (680, 25)
    textRect2.center = (680, 50)
    if count > 0:
        drawCentroid(t1, t2)
        display.blit(text1, textRect1)
        display.blit(text2, textRect2)
        redarr = []
        bluearr = []
        assignPoints(t1, t2, arr)
    pygame.display.update()
    clock.tick(30)
pygame.display.quit()
pygame.quit()
quit()
