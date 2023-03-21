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
accelCorrection = Acceleration_Correction_Class.accel_correction(30, 60, 90, 1, 1, 1)

# Velocity and Position -> velocity_vector(Ai, Aj, Ak), position_vector(Ai, Aj, Ak, Vi, Vj, Vk)
velocity = Velocity_and_Position_Class.velocity_vector(1, 1, 0)
position = Velocity_and_Position_Class.position_vector(1, 1, 0, 1, 1, 0)

# Position of Bump Spring, Roll Rocker, Heave Spring -> RollBarPos(Rr, phi, theta, C)
bumpSpringRollRocker = Position_of_Bump_Spring_Roll_Rocker_Heave_Spring_Class.RollBarPos(Rr, phi, 1, C)

# Angle of Roll Bar Arm from Horizontal -> RBA_Angle(C, L, R_RBA, x, y, z)
horizontalRBA = Angle_of_Roll_Bar_Arm_from_Horizontal_Class.RBA_Angle(C, L, R_RBA, 0, 0, 1)

# Roll Bar Displacement -> RollBarDelta(Theta_R_RBAL, Theta_R_RBAR)
rollBarDisp = Roll_Bar_Displacement_Class.RollBarDelta(0, 1)

# Heave Spring Extension/Compression -> HeaveSpringDelta(L_HS, xL, xR, yL, yR)
heaveSpringComp = Heave_Spring_ExtensionCompression_Class.HeaveSpringDelta(L_HS, 1, 1, 1, 1)

# Bump Spring Compression -> BumpSpringDelta(L_BS, xREF, yREF, x, y)
bumpSpringComp = Bump_Spring_Compression_Class.BumpSpringDelta(L_BS, xREF, yREF, 1, 0.2)


### Print
print("accelCorrection: ", accelCorrection)
print("velocity: ", velocity)
print("position: ", position)
print("bumpSpringRollRocker: ", bumpSpringRollRocker)
print("horizontalRBA: ", horizontalRBA)
print("rollBarDisp: ", rollBarDisp)
print("heaveSpringComp: ", heaveSpringComp)
print("bumpSpringComp: ", bumpSpringComp)