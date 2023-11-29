from multiprocessing import Process, Pipe
from os import getpid
from client import send

def eventCounter(pid, counter):
    counter += 1
    return counter

def processP(pipe12):
    pid = getpid()
    counter = 0
    send("Some more new stuff")
    counter = eventCounter(pid, counter)

def processQ():
    pid = getpid()
    counter = 0
    # Call the send function
    send("Some new stuff")
    counter = eventCounter(pid, counter)


P = Process(target=processP)
Q = Process(target=processQ)

P.start()
Q.start()

P.join()
Q.join()
