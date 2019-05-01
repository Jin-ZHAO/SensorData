import os
import grovepi
import time
import collections

ultra_low = 0
light_low = 0


ultra_high = 0
light_high = 0

ultra_last = 0
light_last = 0

constant = 0.1
# output a CSV header to the file
print ("Time,Ultra,Light,Ultra_Hight,Light_Hight,Ultra_Low,Light_Low")

while True:
#read from a ultrasonic sensor on input 3
	 ultrasonic_sensor = grovepi.ultrasonicRead(3)

#read from an light sensor on input 2
	 light_sensor= grovepi.analogRead(0)
	 
# get a timestamp so we know when it happened
	 timestamp = time.clock()
	 
# get low pass data
	 ultra_low = ultra_low * (1.0-constant) + ultrasonic_sensor * constant
	 light_low = light_low * (1.0-constant) + light_sensor * constant

# y(k) = a * (y(k-1)+ x(k)-x(k-1))
	 ultra_high = constant * (ultra_high + ultrasonic_sensor - ultra_last) 
	 light_high = constant * (light_high + light_sensor - light_last) 
	 ultra_last = ultrasonic_sensor
	 light_last = light_sensor
	 
	 
#output all sensor values as comma separated values
	 print("%f,%d,%a,%d,%a,%d,%a"%(timestamp,ultrasonic_sensor,light_sensor,ultra_high,light_high,ultra_low,light_low))
# Read roughly 1 times a second
# - n.b. analog read takes time to do also
	 time.sleep(1)