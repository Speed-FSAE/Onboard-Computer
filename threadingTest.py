# # import the threading module
# import threading

# class calcsThread(threading.Thread):
#     # exec("getCalcs.py")
#     print('test1')

# class guiThread(threading.Thread):
#     # exec("main.py")
#     while True:
#         print('test2')


# thread1 = calcsThread()
# thread1.daemon = True
# thread2 = guiThread()
# thread2.daemon = True

# try:
#     # thread1.start()
#     thread2.start()
# except:
#     print("Error: unable to start thread")



# from multiprocessing import Process

# def calcsThread():
#     # with open("getCalcs.py") as f:
#         # exec(f.read())
#     exec(open("getCalcs.py").read())

# def guiThread():
#     # with open("main.py") as f:
#     #     exec(f.read())
#     exec(open("main.py").read())

# if __name__=='__main__':
#     p1 = Process(target = calcsThread())
#     p1.start()
#     p2 = Process(target = guiThread())
#     p2.start()

## Works
# with open("getCalcs.py") as f:
#     exec(f.read())
# exec(open("getCalcs.py").read())

# with open("main.py") as f:
    # exec(f.read())
# exec(open("main.py").read())



import time
import threading

def my_threaded_func():
    exec(open("getCalcs.py").read())

thread = threading.Thread(target=my_threaded_func)
thread.start()
print ("Spun off thread")