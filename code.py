import pygame
import random
import matplotlib.pyplot as plt

pygame.init()

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
green = (0,255,0)
Height = 512
Width = 1024
points = []


n = input("Enter Number of points:")
X = random.sample(range(1, Width-1), n)
Y = random.sample(range(1, Height-1), n)

i=0
while i<n:
	points.append([X[i],Y[i]])
	i = i + 1
print points

leftMost = []
rightMost = []

min = -1
max
for x in points:
	print x[1]
    



#algortihm
#create a  list newPolygon with points in proper order


points.append([0,0])
points.append([100,0])
points.append([50,200])

size = [Width,Height]
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

