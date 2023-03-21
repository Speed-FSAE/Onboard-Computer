from math import *
from datetime import datetime
import time

# vars
RollBar_delta = 0 # Roll Bar Displacement

class Roll_Bar_Displacement_Class:
    def RollBarDelta(Theta_R_RBAL, Theta_R_RBAR):
        global RollBar_delta
        RollBar_delta = (Theta_R_RBAL-Theta_R_RBAR)
        return RollBar_delta