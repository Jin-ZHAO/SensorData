import grovepi
import time
import collections # for deque class
ultra_high = 0
ultra_low = 0
constant = 0.1

print ('time,yaw,pitch,roll,ultra,ultra_high,ultra_low')
while True:
 #read from 6-Axis Accelerometer&Compass sensor on input I1
 grove6axis.init6Axis()  # start it up
 ori_feet = grove6axis.getOrientation()  # returns orientation as yaw,pitch,roll
 ori_list = list(ori_feet)
 yaw = ori_list[1] * 180.0 / math.pi
 pitch = ori_list[2] * 180.0 / math.pi
 roll =  ori_list[3] * 180.0 / math.pi

 #read from Ultrasonic sensor on input D4
 motion = grovepi.digitalRead(3)
 #read from Ultrasonic sensor on input D3
 ultra = grovepi.ultrasonicRead(3)  # back door

 # high pass filter: it removes long term bias and drift & show short term variations
 ultra_high = constant * (ultra_high + ultrasonic_sensor - ultra_last)
 # low pass filter: it removes random noise & shows longer term variations
 ultra_low = ultra_low * (1.0 - constant) + ultrasonic_sensor * constant

 timestamp = time.clock()
 #output the data
 print ("%4.4f,%4.4f,%4.4f,%4.4f,%4.4f,%4.4f,%4.4f,%4.4f"%(timestamp,yaw,pitch,roll,motion,ultra,ultra_high,ultra_low))
 # returns orientation as yaw,pitch,roll
 # print (grove6axis.getMag())  # get magnetometer values
 # Read roughly 10 times a second
 # - n.b. analog read takes time to do also
 # set the time for 1s to display data
 time.sleep(0.1)