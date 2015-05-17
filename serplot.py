import serial
import numpy as np
from matplotlib import pyplot as plt

ser = serial.Serial('COM17', 9600)

j=-1
plt.ion()
length=500
axes1=plt.axes()
plt.ylim([-3,3])
plt.yticks(np.arange(0,1023,30))
plt.ylabel('Accelerometer values')
plt.grid()
axdata = [j] * length

line1, = plt.plot(axdata)



while True:
    axs=ser.readline()
    ax1=float(axs)
    axdata.append(ax1)
    del axdata[0]
    line1.set_xdata(np.arange(len(axdata)))
    line1.set_ydata(axdata)
    plt.draw()

    
    
