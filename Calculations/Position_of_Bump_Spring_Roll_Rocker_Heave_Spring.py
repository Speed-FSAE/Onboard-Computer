from math import *
from datetime import datetime
import time

# constants
# Rr = 0 # (R sub r) radius of the rocker
# phi = 0 # reference angle of rocker
# C = 0 # constant X position of the roll bar arm

# globals
theta = 0 # angle of suspension change
x = 0 # x-position of outer rocker connection
y = 0 # y-position of outer rocker connection
z = 0 # z-position of outer rocker connection

class Position_of_Bump_Spring_Roll_Rocker_Heave_Spring_Class:

    def RollBarPos(Rr, phi, theta, C):
        x = Rr*cos(phi+theta)
        y = Rr*sin(phi+theta)
        z = C
        return x, y, z