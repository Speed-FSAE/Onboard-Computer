# for i in range(j+1):
#     print(i)
#     time.sleep(0.01)
#     if(i == j):
#         for i in range(j):
#             print(j-i)

# RPMs simulate from 0-10,000 and back
maxRPM = 10000
over = 0
class updateRPM:
    def __init__(self):
        self.currRPM = 0
    
    def __call__(self):
        global maxRPM, over
        temp = self.currRPM
        if(temp >= 10000):
            over = 1
        if(over == 1 and temp > 0):
            self.currRPM -= 1
            return self.currRPM
        if(over == 1 and temp == 0):
            over = 0
        if(over == 0):
            self.currRPM += 1
            return self.currRPM

# class prevRPM:
#     def __init__(self):
#         self.currRPM = 0

#     def __call__(self):
#         self.currRPM -= 1
#         return self.currRPM