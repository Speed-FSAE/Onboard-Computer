from math import *
from datetime import datetime
import time

# constants
# L_BS = 0 # uncompressed length of the bump spring
# xREF = 0 # x-position of the bump spring mounting point
# yREF = 0 # y-position of the bump spring mounting point

# vars
BumpSpring_delta = 0 # Bump Spring Compression
x = 0 # x-position of the bump spring
y = 0 # y-position of the bump spring

class Bump_Spring_Compression_Class:
    def BumpSpringDelta(L_BS, xREF, yREF, x, y):
        global BumpSpring_delta
        BumpSpring_delta = sqrt(((xREF-x)**2)+((yREF-y)**2))
        return BumpSpring_delta