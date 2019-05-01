import grovepi
import time
import grove6axis
import math


# get a timestamp so we know when it happened
timestamp = time.time()

print ('time,ori,accel')
while True:
 #read from 6-Axis Accelerometer&Compass sensor on input I1
 grove6axis.init6Axis()  # start it up
 print (grove6axis.getOrientation())  # returns orientation as yaw,pitch,roll print (grove6axis.getAccel()) # get acceleration values
 print (grove6axis.getMag())  # get magnetometer values
 grove6axis.getAccel()grove6axis.getAccel()
 # returns orientation as yaw,pitch,roll
 # ori_list = list(ori)
 yaw = ori_list[3] * 180.0 / math.pi
 # pitch = ori_list[2] * 180.0 / math.pi
 # roll =  ori_list[3] * 180.0 / math.pi
 time.sleep(0.5)