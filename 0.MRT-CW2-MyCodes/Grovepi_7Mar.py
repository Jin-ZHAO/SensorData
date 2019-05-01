import grovepi
import grove6axis
import time
while True:
 #read from 6-Axis Accelerometer&Compass sensor on input I1
 grove6axis.init6Axis()  # start it up
 i1 = grove6axis.getOrientation() # returns orientation as yaw,pitch,roll
 i2 = grove6axis.getAccel() # get acceleration values
 i3 = grove6axis.getMag() # get magnetometer values
 print('Orientation',i1)
 print('Accel',i2)
 print('Mag',i3)

 #read from Tilt sensor on input D4
 #d4= grovepi.digitalRead(4)

 #read from Ultrasonic sensor on input D3
 d3= grovepi.ultrasonicRead(3)
 #output the data
 print("Ultrasonic_Distance:",d3)
 # Read roughly 10 times a second
 #  - n.b. analog read takes time to do also
 #  set the time for 1s to display data
 time.sleep(2)