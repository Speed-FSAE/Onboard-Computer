### Calculations ###
from Calculations.Acceleration_Correction import *
from Calculations.Velocity_and_Position import *
from Calculations.Position_of_Bump_Spring_Roll_Rocker_Heave_Spring import *
from Calculations.Angle_of_Roll_Bar_Arm_from_Horizontal import *
from Calculations.Roll_Bar_Displacement import *
from Calculations.Heave_Spring_ExtensionCompression import *
from Calculations.Bump_Spring_Compression import *
### General ###
import json
import time
import threading


### Print
def Calcs():
    ### Calculations ###
    ### Config file
    with open("Configs/config.json", "r") as json_data_file:
        data = json.load(json_data_file)
    ## Constants
    # General
    C = data["Constants"]["General"]["C"]

    # Position_of_Bump_Spring_Roll_Rocker_Heave_Spring
    Rr = data["Constants"]["Position_of_Bump_Spring_Roll_Rocker_Heave_Spring"]["Rr"]
    phi = data["Constants"]["Position_of_Bump_Spring_Roll_Rocker_Heave_Spring"]["phi"]

    # Angle_of_Roll_Bar_Arm_from_Horizontal
    L = data["Constants"]["Angle_of_Roll_Bar_Arm_from_Horizontal"]["L"]
    R_RBA = data["Constants"]["Angle_of_Roll_Bar_Arm_from_Horizontal"]["R_RBA"]

    # Heave_Spring_ExtensionCompression
    L_HS = data["Constants"]["Heave_Spring_ExtensionCompression"]["L_HS"]

    # Bump_Spring_Compression
    L_BS = data["Constants"]["Bump_Spring_Compression"]["L_BS"]
    xREF = data["Constants"]["Bump_Spring_Compression"]["xREF"]
    yREF = data["Constants"]["Bump_Spring_Compression"]["yREF"]

    ## Variables
    # Acceleration Correction -> accel_correction(thetaR, thetaY, thetaP, AF, AS, AT)
    thetaY = 30
    thetaP = 60
    thetaR = 90
    AF = 1
    AS = 1
    AT = 1
    accelCorrection = Acceleration_Correction_Class.accel_correction(thetaR, thetaY, thetaP, AF, AS, AT)

    # Velocity and Position -> velocity_vector(Ai, Aj, Ak), position_vector(Ai, Aj, Ak, Vi, Vj, Vk)
    Ai = 1
    Aj = 1
    Ak = 0
    Vi = 1
    Vj = 1
    Vk = 0
    velocity = Velocity_and_Position_Class.velocity_vector(Ai, Aj, Ak)
    position = Velocity_and_Position_Class.position_vector(Ai, Aj, Ak, Vi, Vj, Vk)

    # Position of Bump Spring, Roll Rocker, Heave Spring -> RollBarPos(Rr, phi, theta, C)
    theta = 1
    bumpSpringRollRocker = Position_of_Bump_Spring_Roll_Rocker_Heave_Spring_Class.RollBarPos(Rr, phi, theta, C)

    # Angle of Roll Bar Arm from Horizontal -> RBA_Angle(C, L, R_RBA, x, y, z)
    x = 0
    y = 0
    z = 1
    horizontalRBA = Angle_of_Roll_Bar_Arm_from_Horizontal_Class.RBA_Angle(C, L, R_RBA, x, y, z)

    # Roll Bar Displacement -> RollBarDelta(Theta_R_RBAL, Theta_R_RBAR)
    Theta_R_RBAL = 0
    Theta_R_RBAR = 1
    rollBarDisp = Roll_Bar_Displacement_Class.RollBarDelta(Theta_R_RBAL, Theta_R_RBAR)

    # Heave Spring Extension/Compression -> HeaveSpringDelta(L_HS, xL, xR, yL, yR)
    xL = 1
    xR = 1
    yL = 1
    yR = 1
    heaveSpringComp = Heave_Spring_ExtensionCompression_Class.HeaveSpringDelta(L_HS, xL, xR, yL, yR)

    # Bump Spring Compression -> BumpSpringDelta(L_BS, xREF, yREF, x, y)
    x = 1
    y = 0.2
    bumpSpringComp = Bump_Spring_Compression_Class.BumpSpringDelta(L_BS, xREF, yREF, x, y)

    # print("accelCorrection: ", accelCorrection)
    # print("velocity: ", velocity)
    # print("position: ", position)
    # print("bumpSpringRollRocker: ", bumpSpringRollRocker)
    # print("horizontalRBA: ", horizontalRBA)
    # print("rollBarDisp: ", rollBarDisp)
    # print("heaveSpringComp: ", heaveSpringComp)
    # print("bumpSpringComp: ", bumpSpringComp)
    x = 20
    return accelCorrection, velocity, position, bumpSpringRollRocker, horizontalRBA, rollBarDisp, heaveSpringComp, bumpSpringComp

while True:
    print(Calcs())
    time.sleep(1) # 1s or 1hz
    # time.sleep(0.001) # 1ms or 1000hz