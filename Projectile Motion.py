from math import *
from numpy import *

def horizontalProjectileMotion(height, velocity):
   gravity = 9.81
   time = sqrt(2 * height / gravity)
   distance = velocity * time
   print("Time of flight: ", time, " seconds","\nDistance: ", distance, " meters")

def angledProjectileMotion(velocity, angle):
   gravity = 9.81
   angle = radians(angle)
   distance = (velocity ** 2 * sin(2 * angle)) / gravity
   max_height = (velocity ** 2 * sin(angle) ** 2) / (2 * gravity)
   x = linspace(0, distance, 20)
  