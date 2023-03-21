### Calculations ###
from Calculations.Acceleration_Correction import *
from Calculations.Velocity_and_Position import *
from Calculations.Position_of_Bump_Spring_Roll_Rocker_Heave_Spring import *
from Calculations.Angle_of_Roll_Bar_Arm_from_Horizontal import *
from Calculations.Roll_Bar_Displacement import *
from Calculations.Heave_Spring_ExtensionCompression import *
from Calculations.Bump_Spring_Compression import *
### General ###
from distutils.command.config import config
from random import randrange
import re
from tkinter import *
from turtle import screensize
import json
import time
import threading

### Calculations ###
def my_threaded_func():
    exec(open("getCalcs.py").read())

thread = threading.Thread(target=my_threaded_func)
thread.start()
print ("Spun off getCalcs thread")

### GUI ###
# global Settings
globalBG = "white"

# globalUpdateTiming Used with root.after() to update screen after logic functions (Units in ms)
globalUpdateTiming = 100

# init
root = Tk()
root.configure(background=globalBG)
root.title("Driver Display")

#Set Screen size#######
screenX = root.winfo_screenwidth()
screenY = root.winfo_screenheight()
root.geometry("{}x{}".format(screenX, screenY))
root.attributes('-fullscreen', True)
screenAvg = (screenX+screenY)/2
##########################

# Titles
titleLabel = Label(root, text="Driver Display V1", bg=globalBG, fg="black",
                    font=("Ariel", 12)).place(x=(screenX*0.91), y=(screenY*0.975))

# revsimulator
rpms = 0
gear = 0

def revUp():
    global rpms
    rpms += randrange(850, 1000)
    revCounter.config(text=str(rpms))
    gearNumber()
    return rpms
def revDown():
    global rpms
    rpms -= randrange(850, 1000)
    revCounter.config(text=str(rpms))
    gearNumber()
    return rpms

# Down button
revUpButton = Button(root, text="Throttle", command=revUp)
revUpButton.place(x=(screenX*0.6), y=(screenY*0.1))

# Up button
revDownButton = Button(root, text="Throttle Release", command=revDown)
revDownButton.place(x=(screenX*0.64), y=(screenY*0.1))

revCounter = Label(root, text=str(rpms), bg=globalBG, fg="red", font=("Ariel", 22))
revCounter.place(x=(screenX*0.4825), y=(screenY*0.1))

# SHIFT LIGHTS
######## Only change these values, leave everything else and it will maintain ratios
shiftLightW = screenX*0.5
shiftLightH = screenY*0.075
shiftLightX = screenX*0.25
shiftLightY = screenY*0.01
########
canvas = Canvas(root, width=(shiftLightW),
                height=(shiftLightH), bg="black")
canvas.place(x=(shiftLightX), y=(shiftLightY))

revRectangle1 = canvas.create_rectangle(
    shiftLightW*0.004, shiftLightH*0.04, shiftLightW*0.1016, shiftLightH*0.998, fill="white")
revRectangle2 = canvas.create_rectangle(
    shiftLightW*0.1016, shiftLightH*0.04, shiftLightW*0.2012, shiftLightH*0.998, fill="white")
revRectangle3 = canvas.create_rectangle(
    shiftLightW*0.2012, shiftLightH*0.04, shiftLightW*0.3008, shiftLightH*0.998, fill="white")
revRectangle4 = canvas.create_rectangle(
    shiftLightW*0.3008, shiftLightH*0.04, shiftLightW*0.4004, shiftLightH*0.998, fill="white")
revRectangle5 = canvas.create_rectangle(
    shiftLightW*0.4004, shiftLightH*0.04, shiftLightW*0.5, shiftLightH*0.998, fill="white")
revRectangle6 = canvas.create_rectangle(
    shiftLightW*0.5, shiftLightH*0.04, shiftLightW*0.5996, shiftLightH*0.998, fill="white")
revRectangle7 = canvas.create_rectangle(
    shiftLightW*0.5996, shiftLightH*0.04, shiftLightW*0.6992, shiftLightH*0.998, fill="white")
revRectangle8 = canvas.create_rectangle(
    shiftLightW*0.6992, shiftLightH*0.04, shiftLightW*0.7988, shiftLightH*0.998, fill="white")
revRectangle9 = canvas.create_rectangle(
    shiftLightW*0.7988, shiftLightH*0.04, shiftLightW*0.8984, shiftLightH*0.998, fill="white")
revRectangle10 = canvas.create_rectangle(
    shiftLightW*0.8984, shiftLightH*0.04, shiftLightW, shiftLightH*0.998, fill="white")

# Shift light colors
def updateRPMS():
    if 0 < rpms <= 1000:
        canvas.itemconfig(revRectangle1, fill="blue")
        canvas.itemconfig(revRectangle2, fill="white")
        canvas.itemconfig(revRectangle3, fill="white")
        canvas.itemconfig(revRectangle4, fill="white")
        canvas.itemconfig(revRectangle5, fill="white")
        canvas.itemconfig(revRectangle6, fill="white")
        canvas.itemconfig(revRectangle7, fill="white")
        canvas.itemconfig(revRectangle8, fill="white")
        canvas.itemconfig(revRectangle9, fill="white")
        canvas.itemconfig(revRectangle10, fill="white")
    if 1000 < rpms <= 2000:
        canvas.itemconfig(revRectangle1, fill='blue')
        canvas.itemconfig(revRectangle2, fill="blue")
        canvas.itemconfig(revRectangle3, fill="white")
        canvas.itemconfig(revRectangle4, fill="white")
        canvas.itemconfig(revRectangle5, fill="white")
        canvas.itemconfig(revRectangle6, fill="white")
        canvas.itemconfig(revRectangle7, fill="white")
        canvas.itemconfig(revRectangle8, fill="white")
        canvas.itemconfig(revRectangle9, fill="white")
        canvas.itemconfig(revRectangle10, fill="white")
    if 2000 < rpms <= 3000:
        canvas.itemconfig(revRectangle1, fill="blue")
        canvas.itemconfig(revRectangle2, fill="blue")
        canvas.itemconfig(revRectangle3, fill="green")
        canvas.itemconfig(revRectangle4, fill="white")
        canvas.itemconfig(revRectangle5, fill="white")
        canvas.itemconfig(revRectangle6, fill="white")
        canvas.itemconfig(revRectangle7, fill="white")
        canvas.itemconfig(revRectangle8, fill="white")
        canvas.itemconfig(revRectangle9, fill="white")
        canvas.itemconfig(revRectangle10, fill="white")
    if 3000 < rpms <= 4000:
        canvas.itemconfig(revRectangle1, fill="blue")
        canvas.itemconfig(revRectangle2, fill="blue")
        canvas.itemconfig(revRectangle3, fill="green")
        canvas.itemconfig(revRectangle4, fill="green")
        canvas.itemconfig(revRectangle5, fill="white")
        canvas.itemconfig(revRectangle6, fill="white")
        canvas.itemconfig(revRectangle7, fill="white")
        canvas.itemconfig(revRectangle8, fill="white")
        canvas.itemconfig(revRectangle9, fill="white")
        canvas.itemconfig(revRectangle10, fill="white")
    if 4000 < rpms <= 5000:
        canvas.itemconfig(revRectangle1, fill="blue")
        canvas.itemconfig(revRectangle2, fill="blue")
        canvas.itemconfig(revRectangle3, fill="green")
        canvas.itemconfig(revRectangle4, fill="green")
        canvas.itemconfig(revRectangle5, fill="green")
        canvas.itemconfig(revRectangle6, fill="white")
        canvas.itemconfig(revRectangle7, fill="white")
        canvas.itemconfig(revRectangle8, fill="white")
        canvas.itemconfig(revRectangle9, fill="white")
        canvas.itemconfig(revRectangle10, fill="white")
    if 5000 < rpms <= 6000:
        canvas.itemconfig(revRectangle1, fill="blue")
        canvas.itemconfig(revRectangle2, fill="blue")
        canvas.itemconfig(revRectangle3, fill="green")
        canvas.itemconfig(revRectangle4, fill="green")
        canvas.itemconfig(revRectangle5, fill="green")
        canvas.itemconfig(revRectangle6, fill="green")
        canvas.itemconfig(revRectangle7, fill="white")
        canvas.itemconfig(revRectangle8, fill="white")
        canvas.itemconfig(revRectangle9, fill="white")
        canvas.itemconfig(revRectangle10, fill="white")
    if 6000 < rpms <= 7000:
        canvas.itemconfig(revRectangle1, fill="blue")
        canvas.itemconfig(revRectangle2, fill="blue")
        canvas.itemconfig(revRectangle3, fill="green")
        canvas.itemconfig(revRectangle4, fill="green")
        canvas.itemconfig(revRectangle5, fill="green")
        canvas.itemconfig(revRectangle6, fill="green")
        canvas.itemconfig(revRectangle7, fill="green")
        canvas.itemconfig(revRectangle8, fill="white")
        canvas.itemconfig(revRectangle9, fill="white")
        canvas.itemconfig(revRectangle10, fill="white")
    if 7000 < rpms <= 8000:
        canvas.itemconfig(revRectangle1, fill="blue")
        canvas.itemconfig(revRectangle2, fill="blue")
        canvas.itemconfig(revRectangle3, fill="green")
        canvas.itemconfig(revRectangle4, fill="green")
        canvas.itemconfig(revRectangle5, fill="green")
        canvas.itemconfig(revRectangle6, fill="green")
        canvas.itemconfig(revRectangle7, fill="green")
        canvas.itemconfig(revRectangle8, fill="yellow")
        canvas.itemconfig(revRectangle9, fill="white")
        canvas.itemconfig(revRectangle10, fill="white")
    if 8000 < rpms <= 9000:
        canvas.itemconfig(revRectangle1, fill="blue")
        canvas.itemconfig(revRectangle2, fill="blue")
        canvas.itemconfig(revRectangle3, fill="green")
        canvas.itemconfig(revRectangle4, fill="green")
        canvas.itemconfig(revRectangle5, fill="green")
        canvas.itemconfig(revRectangle6, fill="green")
        canvas.itemconfig(revRectangle7, fill="green")
        canvas.itemconfig(revRectangle8, fill="yellow")
        canvas.itemconfig(revRectangle9, fill="red")
        canvas.itemconfig(revRectangle10, fill="white")
    if rpms <= 10000 and rpms > 9000:
        canvas.itemconfig(revRectangle1, fill="blue")
        canvas.itemconfig(revRectangle2, fill="blue")
        canvas.itemconfig(revRectangle3, fill="green")
        canvas.itemconfig(revRectangle4, fill="green")
        canvas.itemconfig(revRectangle5, fill="green")
        canvas.itemconfig(revRectangle6, fill="green")
        canvas.itemconfig(revRectangle7, fill="green")
        canvas.itemconfig(revRectangle8, fill="yellow")
        canvas.itemconfig(revRectangle9, fill="red")
        canvas.itemconfig(revRectangle10, fill="red")
    root.after(globalUpdateTiming, updateRPMS)


# Gear number
gearIndicator = Label(root, bg=globalBG, text=str(gear),
                      fg="black", font=("Arial", int(screenAvg*0.25)))
gearIndicator.place(x=(screenX*0.42), y=(screenY*0.25))


def gearNumber():
    global gear, rpms
    if gear < 6:
        if 9500 < rpms and gear >= 0:  # UPSHIFT
            gear += 1
            rpms = 0
            return gear, rpms
        if rpms < 700 and gear < 6:  # DOWNSHIFT
            gear -= 1
            rpms = 8000
            return gear, rpms
        if gear < 1 and 4000 < rpms < 6000:  # LAUNCH FROM NEUTRAL
            gear += 1
            rpms = 0
            return gear, rpms
    gearIndicator.configure(text=str(gear))

updateRPMS()


root.mainloop()  # create event loop to update GUI