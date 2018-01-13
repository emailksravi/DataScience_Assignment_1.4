"""
Problem Statement :
Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r^3
"""

import math

# Function to calculate volume of sphere - given input diameter
# round off to 3 decimal places
def calc_sphere_volume(diameter):
    volume = round(4 / 3 * math.pi * (diameter/2) ** 3, 3 )
    return volume

# init diameter
diameter = 12

# print final volume of sphere for given diameter
print ("Volume of sphere for diameter ", diameter , "cms : ", calc_sphere_volume(diameter), " cubic centimetre")

