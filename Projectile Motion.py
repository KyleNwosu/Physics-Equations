from math import *
from numpy import *
from pylab import *

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
   y=x*tan(angle)-(1/2)*(gravity*x**2)/(velocity**2*(cos(angle))**2 )
   figure(1,dpi=300)
   plot(x,y,'r-',linewidth=3)
   xlabel("Distance")
   ylabel("Height")
   ylim(0, max_height+0.05)
   savefig("ProjectileMotion.png")
   show()

def raisedProjectileMotion(height, velocity, angle):
   gravity = 9.81
   angle = radians(angle)
   time = sqrt(2 * height / gravity)
   distance = velocity * time * cos(angle)
   max_height = height + (velocity ** 2 * sin(angle) ** 2) / (2 * gravity)
   print("Time of flight: ", time, " seconds","\nDistance: ", distance, " meters","\nMaximum height: ", max_height, " meters")