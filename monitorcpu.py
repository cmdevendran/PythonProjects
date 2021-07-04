import os
from time import sleep, strftime, time
import matplotlib.pyplot as plt


plt.ion()
x = []
y = []

def write_temp(temp):
    with open("Linux_cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()

def getTemp():
    celcius = None
    temp = '/sys/devices/virtual/thermal/thermal_zone0/temp'
    if os.path.exists(temp):
        celcius = int(open(temp).read().strip()) / 1000
    return celcius
        
while True:
        cel = getTemp()
        write_temp(cel)
        graph(cel)
        sleep(2)
        plt.pause(1)
