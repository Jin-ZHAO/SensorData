import grovepi
import time
import collections
import grove6axis
import math

# get a timestamp so we know when it happened
timestamp = time.clock()

print ('time,yaw,yaw_accel,motion,ultra')

while True:
 grove6axis.init6Axis()
 ori = grove6axis.getOrientation()
 ori_list = list(ori)
 # x = ori_list[0] * 180.0 / math.pi
 y = ori_list[1] * 180.0 / math.pi
 # z = ori_list[2] * 180.0 / math.pi
 # returns orientation as yaw,pitch,roll
 # ori_list = list(ori)
 # pitch = ori_list[2] * 180.0 / math.pi
 a = grove6axis.getAccel()
 a_list  =list(a)
 # x_a = accel_list[0]
 y_a = accel_list[1]
 # z_a = accel_list[2]

 motion = grovepi.digitalRead(4)
 # read from Ultrasonic sensor on input D3
 ultra = grovepi.ultrasonicRead(3)
 # Filter1 De-trending / high pass filter:
 # it removes long term bias and drift & show short term variations

 #output the data
 print (time,y,y_a,motion,ultra)
 # returns orientation as yaw,pitch,roll
 # print (grove6axis.getMag())  # get magnetometer values
 # Read roughly 10 times a second
 # - n.b. analog read takes time to do also
 # set the time for 1s to display data
 time.sleep(0.1)