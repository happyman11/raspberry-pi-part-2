import serial
import time
import os
port = serial.Serial("/dev/serial0", baudrate=9600, timeout=1.0)
a = False
def value():
    global a
    x=10
    for i in range(x):
        rcv = port.readline().decode('utf-8').rstrip()
        
        if len(rcv)> 4:
            a=True
            break
    else:
        x=x+1
    while a:
        value = rcv.split(',')
        #print value
        ph= value[0]
        w= value[1]
        l= value[2]
        t= value[3]
        __,ph = ph.split(':')
        __,w = w.split(':')
        __,l = l.split(':')
        __,t = t.split(':')
        ph=float(ph)
        w=float(w)
        l=float(l)
        t=float(t)
        a=False
        return ph,w,l,t


def ph():
    x=10
    for i in range(x):
        rcv = port.readline().decode('utf-8').rstrip()
        
        if len(rcv)> 4:
            a=True
            break
    else:
        x=x+1
    while a:
        value = rcv.split(',')
        #print value
           
        ph= value[0]
        __,ph = ph.split(':')
        ph=float(ph)
        a=False
        return ph
    

def water():
    x=10
    for i in range(x):
        rcv = port.readline().decode('utf-8').rstrip()
        
        if len(rcv)> 4:
            a=True
            break
    else:
        x=x+1
    while a:
        value = rcv.split(',')
        #print value
           
        w= value[1]
        __,w = w.split(':')
        w=float(w)
        a=False
        return w


def ldr():
    x=10
    for i in range(x):
        rcv = port.readline().decode('utf-8').rstrip()
        
        if len(rcv)> 4:
            a=True
            break
    else:
        x=x+1
    while a:
        value = rcv.split(',')
        #print value         

        l= value[2]
        __,l = l.split(':')
        l=float(l)
        a=False
        return l


def temp():
    x=10
    for i in range(x):
        rcv = port.readline().decode('utf-8').rstrip()
        
        if len(rcv)> 4:
            a=True
            break
    else:
        x=x+1
    while a:
        value = rcv.split(',')
        #print value

        t= value[3]
        __,t = t.split(':')
        t=float(t)
        a=False
        return t
z=0
while True:
    print(value())
    print("Temperature: ",temp())
    print("Ph Level: ",ph())
    print("Level: ",water())
    print("Turbidity: ",ldr())
    print("---------------------------------------")
