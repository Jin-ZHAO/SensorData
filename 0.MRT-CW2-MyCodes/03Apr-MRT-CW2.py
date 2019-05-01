import grovepi
import time
import grove6axis
import collections

ultra_low = 0
ultra_high = 0
ultra_last = 0
constant = 0.1
# get a timestamp so we know when it happened
timestamp = time.time()

print ('time,yaw,pitch,roll,motion,ultra,ultra_low,ultra_high,ultra_median')
while True:
 #read from 6-Axis Accelerometer&Compass sensor on input I1
 grove6axis.init6Axis()  # start it up
 ori_feet = grove6axis.getOrientation()  # returns orientation as yaw,pitch,roll
 ori_list = list(ori_feet)
 yaw = ori_list[1] * 180.0 / math.pi
 pitch = ori_list[2] * 180.0 / math.pi
 roll =  ori_list[3] * 180.0 / math.pi
 # accel = grove6axis.getAccel() # get acceleration values

 # read from a digital sensor / PIR on input D4
 motion = grovepi.digitalRead(4)
 # read from Ultrasonic sensor on input D3
 ultra = grovepi.ultrasonicRead(3)  # back door
 # Filter1 De-trending / high pass filter:
 # it removes long term bias and drift & show short term variations
 ultra_high = constant * (ultra_high + ultra - ultra_last)
 ultra_last = ultra
 # Filter2 Smoothing / low pass filter:
 # it removes random noise & shows longer term variations
 ultra_low = ultra_low * (1.0 - constant) + ultra * constant
 # Filter3 Median / Non linear filter
 historyBuffer.append(ultra)
 orderedHistory = sorted(historyBuffer)
 ultra_median = orderedHistory[int(len(orderedHistory) / 2)]
 #output the data
 print ("%.4f,%.4d,%.4d,%.4d,%.4d,%.4d,%.4d,%.4d"%(time,yaw,pitch,roll,accel,motion,ultra,ultra_low,ultra_high,ultra_median))
 # returns orientation as yaw,pitch,roll
 # print (grove6axis.getMag())  # get magnetometer values
 # Read roughly 10 times a second
 # - n.b. analog read takes time to do also
 # set the time for 1s to display data
 time.sleep(0.1)