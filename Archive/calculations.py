from math import *
from datetime import datetime
import time

########################################## Acceleration Correction \/
thetaR = 30 # IMU roll angle
thetaY = 60 # IMU yaw angle
thetaP = 90 # IMU pitch angle
AF = 1 # (A sub F) IMU forward acceleration
AS = 1 # (A sub S) IMU sideways acceleration
AT = 1 # (A sub T) IMU upward acceleration
Ai = 0 # (i) total acceleration vector
Aj = 0 # (j) total acceleration vector
Ak = 0 # (k) total acceleration vector

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
########################################## Acceleration Correction /\



########################################## Velocity and Position \/
# velocity vector
Vi0 = 1
Vj0 = 1
Vk0 = 0
tV0 = 0
tV1 = 0
Vi = 0
Vj = 0
Vk = 0
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
# position vector
Si0 = 1
Sj0 = 1
Sk0 = 0
tS0 = 0
tS1 = 0
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
########################################## Velocity and Position /\



########################################## Position of Bump Spring, Roll Rocker, Heave Spring \/
Rr = 0 # (R sub r) radius of the rocker
phi = 0 # reference angle of rocker
theta = 0 # angle of suspension change
C = 0 # constant X position of the roll bar arm

x = 0 # x-position of outer rocker connection
y = 0 # y-position of outer rocker connection
z = 0 # z-position of outer rocker connection

def RollBarPos(Rr, phi, theta, C):
    x = Rr*cos(phi+theta)
    y = Rr*sin(phi+theta)
    z = C
    return x, y, z
########################################## Position of Bump Spring, Roll Rocker, Heave Spring /\



########################################## Angle of Roll Bar Arm from Horizontal \/
L = 0 # length of the roll bar control rod
ThetaRBA = 0 # angle of Roll Bar Arm from Horizontal, to be calculated below
R_RBA = 0 # radius of the roll bar arm

# reference function, must be adapted to both right and left side (reference function will never be called)
def RBA_Angle(C, L, x, y, z):
    global ThetaRBA
    num = (((((L**2)-((C-x)**2)-(y**2)-(z**2)/2*R_RBA)-(R_RBA/2))/z)**2)-1
    denom = ((y**2)/(z**2))-1
    ThetaRBA = asin(sqrt(num/denom))
    return ThetaRBA

Theta_R_RBAL = 0 # left side, reference function will be copied and adapted to calculate this
Theta_R_RBAR = 0 # right side, reference function will be copied and adapted to calculate this
########################################## Angle of Roll Bar Arm from Horizontal /\



########################################## Roll Bar Displacement \/
RollBar_delta = 0 # Roll Bar Displacement

def RollBarDelta(Theta_R_RBAL, Theta_R_RBAR):
    global RollBar_delta
    RollBar_delta = (Theta_R_RBAL-Theta_R_RBAR)
    return RollBar_delta
########################################## Roll Bar Displacement /\



########################################## Heave Spring Extension,Compression \/
HeaveSpring_delta = 0 # Heave Spring Extension/Compression
L_HS = 0 # reference Heav Spring Length
xL = 0 # Left x-position of heave spring rocker
xR = 0 # Right x-position of heave spring rocker
yL = 0 # Left y-position of heave spring rocker
yR = 0 # Right y-position of heave spring rocker

def HeaveSpringDelta(L_HS, xL, xR, yL, yR):
    global HeaveSpring_delta
    HeaveSpring_delta = L_HS - sqrt(((xR-xL)**2)+((yR-yL)**2))
    return HeaveSpring_delta
########################################## Heave Spring Extension,Compression /\



########################################## Bump Spring Compression \/
BumpSpring_delta = 0 # Bump Spring Compression
L_BS = 0 # uncompressed length of the bump spring
xREF = 0 # x-position of the bump spring mounting point
yREF = 0 # y-position of the bump spring mounting point
x = 0 # x-position of the bump spring
y = 0 # y-position of the bump spring

def BumpSpringDelta(L_BS, xREF, yREF, x, y):
    global BumpSpring_delta
    BumpSpring_delta = sqrt(((xREF-x)**2)+((yREF-y)**2))
    return BumpSpring_delta
########################################## Bump Spring Compression /\