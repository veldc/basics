'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.

V=πr2h
A=2πrh+2πr2 = 2π(rh+r2)

'''
# import math
from math import pi, sqrt


radius = 3.14
height = 5
volume = (pi)*sqrt(radius)*height
surface = 2*pi*(radius*height+sqrt(radius))
print(volume)
print(surface)
