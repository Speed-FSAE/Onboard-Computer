from math import *
from datetime import datetime
import time

# constants
# L_HS = 0 # reference Heave Spring Length

# vars
HeaveSpring_delta = 0 # Heave Spring Extension/Compression
xL = 0 # Left x-position of heave spring rocker
xR = 0 # Right x-position of heave spring rocker
yL = 0 # Left y-position of heave spring rocker
yR = 0 # Right y-position of heave spring rocker

class Heave_Spring_ExtensionCompression_Class:
    def HeaveSpringDelta(L_HS, xL, xR, yL, yR):
        global HeaveSpring_delta
        HeaveSpring_delta = L_HS - sqrt(((xR-xL)**2)+((yR-yL)**2))
        return HeaveSpring_delta