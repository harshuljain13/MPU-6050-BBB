import serial
import numpy as np
from matplotlib import pyplot as plt

ser = serial.Serial('COM12', 9600)

#j=0
#k=0
#l=0
u=0
v=0
w=0

plt.ion()
length=200
axes1=plt.axes()
plt.ylim([-100,100])
plt.yticks(np.arange(-100,100, 10.0))
plt.ylabel('Gyroscope filtered values')
plt.grid()
#gyroxdata = [j] * length
#gyroydata = [k] * length
#gyrozdata = [l] * length
compl_gyroxdata=[u] * length
compl_gyroydata=[v] * length
compl_gyrozdata=[w] * length
#line1, = plt.plot(gyroxdata,color='blue')
#line2, = plt.plot(gyroydata,color='green')
#line3, = plt.plot(gyrozdata,color='red')
line4, = plt.plot(compl_gyroxdata,color='cyan')
line5, = plt.plot(compl_gyroydata,color='purple')
line6, = plt.plot(compl_gyrozdata,color='black')


while True:
 #   gyroxs=ser.read(8)
  #  gyroys=ser.read(8)
   # gyrozs=ser.read(8)
    compxs=ser.read(8)
    compys=ser.read(8)
    compzs=ser.read(8)
    #ax1=float(gyroxs)
    #ay1=float(gyroys)
    #az1=float(gyrozs)
    compx=float(compxs)
    compy=float(compys)
    compz=float(compzs)

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
    #gyroxdata.append(ax1)
    #gyroydata.append(ay1)
    #gyrozdata.append(az1)
    compl_gyroxdata.append(compx)
    compl_gyroydata.append(compy)
    compl_gyrozdata.append(compz)
    #del gyroxdata[0]
    #del gyroydata[0]
    #del gyrozdata[0]
    del compl_gyroxdata[0]
    del compl_gyroydata[0]
    del compl_gyrozdata[0]
    #line1.set_xdata(np.arange(len(gyroxdata)))
    #line1.set_ydata(gyroxdata)
    #line2.set_xdata(np.arange(len(gyroydata)))
    #line2.set_ydata(gyroydata)
    #line3.set_xdata(np.arange(len(gyrozdata)))
    #line3.set_ydata(gyrozdata)
    line4.set_xdata(np.arange(len(compl_gyroxdata)))
    line4.set_ydata(compl_gyroxdata)
    line5.set_xdata(np.arange(len(compl_gyroydata)))
    line5.set_ydata(compl_gyroydata)
    line6.set_xdata(np.arange(len(compl_gyrozdata)))
    line6.set_ydata(compl_gyrozdata)
    
    plt.draw()

    
    
