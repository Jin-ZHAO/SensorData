import grovepi
import time
while True:
 #read from 6-Axis Accelerometer&Compass sensor on input I1
 grove6axis.init6Axis()  # start it up
 print (grove6axis.getOrientation())  # returns orientation as yaw,pitch,roll
 print (grove6axis.getAccel())  # get acceleration values
 print (grove6axis.getMag())  # get magnetometer values

 #read from Ultrasonic sensor on input D4
 d4= grovepi.ultrasonicRead(4)  # back door
 #read from Ultrasonic sensor on input D3
 d3= grovepi.ultrasonicRead(3)  # front door

 #output the data
 print ("button:",d4,
        "Ultrasonic_Distance:",d3)
# Read roughly 10 times a second
# - n.b. analog read takes time to do also
# set the time for 1s to display data
 time.sleep(0.5)