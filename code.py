import pygame
import random
import sys

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


max = sys.maxint
min = -sys.maxint-1 
leftMost = [max,max]
rightMost = [min,min]


for ptr in points:

	if ptr[0] < leftMost[0]:
		leftMost = ptr
	if ptr[0] > rightMost[0]:
		rightMost = ptr
"""
print leftMost
print rightMost
"""

def isUpper(L,R,P):
	if ((P[1]-L[1])*(R[0]-L[0]) - (P[0]-L[0])*(R[1]-L[1])) > 0:
		return 1
        else:
		return 0

upper = []
lower = []
for ptr in points:
	if ptr != leftMost and ptr != rightMost:s
		if isUpper(ptr,leftMost,rightMost):
			upper.append(ptr)
		else:
			lower.append(ptr)

print ("upper")
print upper

print ("lower")
print lower

		



    

#algortihm
#create a  list newPolygon with points in proper order

"""
points.append([0,0])
points.append([100,0])
points.append([50,200])
"""


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

