import time

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import subprocess as sp

logfile = "temp.log"

def read_log(logfile):
    with open(logfile, 'rb') as f:
        data = []
        while True:
            line = f.readline().decode('utf-8')
            temp = line.split('=')[1].split('\'')[0]
            time.sleep(0.1)
            print(temp)
            if line:
                data.append(temp)
                yield data

def read_raw():
    data = []
    while True:
        res = sp.getoutput('vcgencmd measure_temp')
        temp = res.split('=')[1].split('\'')[0]
        data.append(temp)
        time.sleep(1)
        yield data

def animate(values):
    line, = plt.plot(values, color='blue')
    return line, 

fig = plt.figure(figsize=(40,40))
plt.title("Sysbench benchmark - Temperature ")
plt.xlabel("Time in min")
plt.ylabel("Temperature in Celsius")
# plt.axis([1, 200, 0.0, 80.0])
# plt.axes()

# ani = FuncAnimation(fig, animate, frames=read(logfile), interval=1)
ani = FuncAnimation(fig, animate, frames=read_raw(), interval=1)
plt.show()
