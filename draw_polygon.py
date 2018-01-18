"""
this program takes number (n) as input from user, generates 'n' random points and constructs a sequence of points forming polygon and plots it on GUI
author : rahul25rocker@gmail.com
author : nasruddinali9246@gmail.com
dated : 18th January, 2018
"""

import pygame
from random import randint
import sys

pygame.init()

red = (255,0,0)
white = (255,255,255)
Height = 512
Width = 1024

#takes three points L,R,P i.e leftmost , rightmost and some point 'P' and tells whether point 'P' lies upper or lower to the line segment 'LR' using slope formula
def isUpper(L,R,P):
	if ((P[1]-L[1])*(R[0]-L[0]) - (P[0]-L[0])*(R[1]-L[1])) > 0:
		return 1
        else:
		return 0

n = input("Enter Number of points : ")
count = 0;                                  #counts unique point generated
map = set()                                 #checks whether the co-ordinate is generated already
points = []                                 #list of unique co-ordinates generated
while count < n:
	x = randint(0, Width-1)
	y = randint(0, Height-1)
        if ((x,y) in map) == False:
		map.add((x,y))
		points.append([x,y])
		count = count + 1
#print points

max = sys.maxint
min = -sys.maxint-1 
leftMost = [max,max]                         #leftmost coordinate
rightMost = [min,min]                        #rightmost coordinate

#algortihm
for ptr in points:
	if ptr[0] < leftMost[0]:
		leftMost = ptr
	if ptr[0] > rightMost[0]:
		rightMost = ptr

upper = []                                   #set of points upper to the line segment (leftmost,rightmost)
lower = []                                   #set of points lower to the line segment (leftmost,rightmost)
for ptr in points:
	if ptr != leftMost and ptr != rightMost:
		if isUpper(ptr,leftMost,rightMost):
			upper.append(ptr)
		else:
			lower.append(ptr)

upper.sort(key = lambda x : x[0])
upper.reverse()
lower.sort(key = lambda x : x[0])
lower.insert(0,leftMost)
upper.insert(0,rightMost)
points = lower + upper

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
    pygame.draw.polygon(screen, red, points, 1)
    pygame.display.flip()
    clock.tick(20)
