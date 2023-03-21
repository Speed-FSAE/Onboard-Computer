from math import *
from datetime import datetime
import time

# velocity vector vars
Vi0 = 1
Vj0 = 1
Vk0 = 0
tV0 = 0
tV1 = 0
Vi = 0
Vj = 0
Vk = 0

# position vector vars
Si0 = 1
Sj0 = 1
Sk0 = 0
tS0 = 0
tS1 = 0

class Velocity_and_Position_Class:
    def velocity_vector(Ai, Aj, Ak):
        global Vi0
        global Vj0
        global Vk0
        global tV0
        global tV1
        global Vi
        global Vj
        global Vk

        tV1 = time.time()
        tV = tV1 - tV0
        Vi = (Vi0+Ai*tV)
        Vj = (Vj0+Aj*tV)
        Vk = (Vk0+Ak*tV)
        Vi0 = Vi
        Vj0 = Vj
        Vk0 = Vk
        tV0 = time.time()
        return Vi, Vj, Vk

    def position_vector(Ai, Aj, Ak, Vi, Vj, Vk):
        global Si0
        global Sj0
        global Sk0
        global tS0
        global tS1

        tS1 = time.time()
        tS = tS1 - tS0
        Si = Si0+Vi0*tS+((Ai*(tS**2))/2)
        Sj = Sj0+Vj0*tS+((Aj*(tS**2))/2)
        Sk = Sk0+Vk0*tS+((Ak*(tS**2))/2)
        Si0 = Si
        Sj0 = Sj
        Sk0 = Sk
        tS0 = time.time()
        return Si, Sj, Sk