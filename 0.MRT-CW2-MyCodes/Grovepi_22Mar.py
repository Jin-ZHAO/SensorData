import grovepi
import time
while True:
 #read from 6-Axis Accelerometer&Compass sensor on input
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