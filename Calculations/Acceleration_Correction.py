from math import *
from datetime import datetime
import time

class Acceleration_Correction_Class:
    def accel_correction(thetaR, thetaY, thetaP, AF, AS, AT):
        # vectorized forward acceleration
        AFi = (AF*sin(thetaP))*cos(thetaY)
        AFj = (AF*sin(thetaP))*cos(thetaY)
        AFk = AF*cos(thetaY)
        # vectorized sideways acceleration
        ASi = (AS*sin(thetaR))*cos(thetaY+90)
        ASj = (AS*sin(thetaR))*cos(thetaY+90)
        ASk = AF*cos(thetaR)
        # A sub A
        AAi = (cos(thetaP)*sin(thetaY))+(cos(thetaR)*sin(thetaY+90))
        AAj = (sin(thetaP)*sin(thetaY))+(sin(thetaR)*sin(thetaY+90))
        AAk = cos(thetaP)+cos(thetaR)
        AAmag = sqrt((AAi)**2+(AAj)**2+(AAk)**2)
        # vectorized upward acceleration
        ATi = AT*(AAi/AAmag)
        ATj = AT*(AAj/AAmag)
        ATk = AT*(AAk/AAmag)
        # total acceleration vector
        global Ai
        global Aj
        global Ak
        Ai = AFi+ASi+ATi
        Aj = AFj+ASj+ATj
        Ak = AFk+ASk+ATk
        return Ai, Aj, Ak