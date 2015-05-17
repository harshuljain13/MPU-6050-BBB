import serial
import numpy as np
from matplotlib import pyplot as plt

ser = serial.Serial('COM12', 9600)

j=0
k=0
l=0
plt.ion()
length=150
axes1=plt.axes()
plt.ylim([-250,250])
plt.yticks(np.arange(-250,250, 40.0))
plt.ylabel('Gyroscope values')
plt.grid()
axdata = [j] * length
aydata = [k] * length
azdata = [l] * length

line1, = plt.plot(axdata,color='blue')
line2, = plt.plot(aydata,color='green')
line3, = plt.plot(azdata,color='red')


while True:
    axs=ser.read(8)
    ays=ser.read(8)
    azs=ser.read(8)
    ax1=float(axs)
    ay1=float(ays)
    az1=float(azs)

    #ax1=1
    #ay1=2
    #az1=3
    
    #j+=0.3
    #k+=0.3
    #l+=0.3
    #if (j>1):
     #   j=-1
    #if (k>1):
     #   k=-1
    #if (l>1):
     #   l=-1
    axdata.append(ax1)
    aydata.append(ay1)
    azdata.append(az1)
    del axdata[0]
    del aydata[0]
    del azdata[0]
    line1.set_xdata(np.arange(len(axdata)))
    line1.set_ydata(axdata)
    line2.set_xdata(np.arange(len(aydata)))
    line2.set_ydata(aydata)
    line3.set_xdata(np.arange(len(azdata)))
    line3.set_ydata(azdata)
    plt.draw()

    
    
