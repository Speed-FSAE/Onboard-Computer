from math import *
from datetime import datetime
import time

# Constants
# L = 0 # length of the roll bar control rod
# R_RBA = 0 # radius of the roll bar arm

# Globals
ThetaRBA = 0 # angle of Roll Bar Arm from Horizontal, to be calculated below

class Angle_of_Roll_Bar_Arm_from_Horizontal_Class:
    # reference function, must be adapted to both right and left side (reference function will never be called)
    def RBA_Angle(C, L, R_RBA, x, y, z):
        global ThetaRBA
        num = (((((L**2)-((C-x)**2)-(y**2)-(z**2)/2*R_RBA)-(R_RBA/2))/z)**2)-1
        denom = ((y**2)/(z**2))-1
        ThetaRBA = asin(sqrt(num/denom))
        return ThetaRBA

    Theta_R_RBAL = 0 # left side, reference function will be copied and adapted to calculate this
    Theta_R_RBAR = 0 # right side, reference function will be copied and adapted to calculate this