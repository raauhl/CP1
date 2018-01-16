import pygame
import random
import matplotlib.pyplot as plt

pygame.init()

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
green = (0,255,0)

n = input("Enter Number of points:")
X = random.sample(range(1, 500), n)
Y = random.sample(range(1, 700), n)
points = []
i=0
while i<n:
	points.append([Y[i],X[i]])
	i = i + 1
print points

#algortihm
#create a  list newPolygon with points in proper order

"""
points.append([50,40])
points.append([100,150])
points.append([60,200])
"""

size = [1000,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("CODING PROJECT")

done = False

clock = pygame.time.Clock();

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
	    done = True

    screen.fill(white)
    pygame.draw.polygon(screen, green, points, 2)

    #for i in range(15):
    #    pygame.draw.line(screen, green, [i*10,100], [40,490],2)
    pygame.display.flip()


    clock.tick(20)

