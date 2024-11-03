from gzip import READ
from turtle import circle
import pygame
import random
import sys

pygame.init()
width=700
height=700
  
RED=[255,0,0]
BLUE=[0,0,255]
GREEN=[0,255,0]
BLACK=[0,0,0]
circles=[
[600, 500, 'red'], [500, 100, 'blue'], [300,100, 'green'],[600,100,'green']]

gapes=[]
gape1=[50,60]
gape2=[100,300]
gape3=[550,200]

screen = pygame.display.set_mode((width, height))
speed=1
def create_circle():
      for magnet in circles:
            color = RED if magnet[2] == 'red' else BLUE if magnet[2] == 'blue' else GREEN
            pygame.draw.circle(screen, color, (magnet[0], magnet[1]), 35)
def create_gape():
    pygame.draw.rect(screen,BLACK,(gape1[0],gape1[1],90,90),5)
    pygame.draw.rect(screen,BLACK,(gape2[0],gape2[1],90,90),5)
    pygame.draw.rect(screen,BLACK,(gape3[0],gape3[1],90,90),5)
 
def move_circles(index,cx,cy):
    x,y,colores=circles[index]
    circles[index]=((cx+x)*speed,(cy+y)*speed,colores) 
    
    

def move_circlesred():
      if  circles[1][1]==circles[2][1] :
           move_circles(2,-0.1,0)
      elif circles[1][1]==circles[2][1]:
             move_circles(2,-0.1,0)     

def move_circlesblue():
      if circles[0][0]==circles[3][0]:
         move_circles(3, 0, 0.1)    
      elif  circles[1][0]==circles[2][0]:
            move_circles(2,0,0.1)

while True:
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
   
    keys = pygame.key.get_pressed()
    
          
    if keys[pygame.K_RIGHT]:
            move_circles(1, 0.1, 0) 
           
    if keys[pygame.K_DOWN]:
                move_circles(1, 0, 0.1)
         
    if keys[pygame.K_UP]:
            move_circles(0, 0, -0.1)
            move_circlesblue()
          
  
    if keys[pygame.K_LEFT]:
            move_circles(1,-0.1,0)
            move_circlesred()

    screen.fill((255,255 ,0 ))
    create_circle()
    create_gape()
    pygame.display.flip()
