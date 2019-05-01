import grovepi
import time
import collections
import grove6axis
import math

ultra_low = 0
ultra_high = 0
ultra_last = 0
constant = 0.1
# get a timestamp so we know when it happened
timestamp = time.clock()
historyBuffer=collections.deque(maxlen=21)

print ('time,yaw,motion,ultra,ultra_low,ultra_high,ultra_median')

while True:
 grove6axis.init6Axis()
 # returns orientation as yaw,pitch,roll
 # ori_list = list(ori)
 yaw = ori_list[3] * 180.0 / math.pi
 # pitch = ori_list[2] * 180.0 / math.pi
 # roll =  ori_list[3] * 180.0 / math.pi
 grove6axis.getAccel()

 motion = grovepi.digitalRead(4)
 # read from Ultrasonic sensor on input D3
 ultra = grovepi.ultrasonicRead(3)
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
 print (time,yaw,motion,ultra,ultra_low,ultra_high,ultra_median)
 # returns orientation as yaw,pitch,roll
 # print (grove6axis.getMag())  # get magnetometer values
 # Read roughly 10 times a second
 # - n.b. analog read takes time to do also
 # set the time for 1s to display data
 time.sleep(0.1)