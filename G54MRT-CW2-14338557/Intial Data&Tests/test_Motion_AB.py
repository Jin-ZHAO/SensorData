import grovepi
import os
import time
import collections

# this value indicates the total length or height of the unit,
# which were got from implementation, the initial steady number that Ultrasonic got.
unit_width = 50  # default
item_width = 7 # default
action = 0
mode_last = 0 # 'Locked'# default
status_lastA = 0 #'Normal' # default for raw data, which will be change after the first run
status_lastB = 0 # 'Normal' # default for filter data, which will be change after the first run
button_last = 0 # the started point
ultra_lastA = 0 # for ultra raw value
ultra_lastB = 0 # for ultra filter value
n_lastA = 0
n_lastB = 0
before_distanceA = 0
before_distanceB = 0
after_distanceA = 0
after_distanceB = 0

history_ultra=collections.deque(maxlen=11) # will be used for median filter later

print ('times, motion, button, ultra, ultra_median, before_distanceA, before_distanceB, after_distanceA, after_distanceB, changeA, changeB, unit_mode, abnormal, behaviorA, behaviorB, unit_statusA, unit_statusB,n_itemsA, n_itemsB')

while True:
    ########################################################################################################
    # Step 1: read time and raw data from sensors
    # PIR-D2, button-D3, Ultrasonic-D4
    times = time.clock()
    motion = grovepi.digitalRead(2)  # alternative 1
    button = grovepi.digitalRead(3) # alternative 2
    ultra = grovepi.ultrasonicRead(4) # raw distance

    ########################################################################################################
    # Step 2: use filter to pre-process raw data, which will be tested the effect later
    # Median Filter for Ultrasonic / Non linear filter
    # got the Median ( 1 from n ) to make it more steady and reliable
    # As we actually don't care about the changing process,
    # we only care about the change before and after putting/taking (end point - start point)
    history_ultra.append(ultra)
    ordered_ultra = sorted(history_ultra)
    ultra_median = history_ultra[int(len(ordered_ultra) / 2)]

    ########################################################################################################
    # Step 3: Judge the storage mode ( 0 Unlocked / 1 Locked ) & Record the data
	# Method : Motion
    before_distanceA = ultra_lastA
    before_distanceB = ultra_lastB
    after_distanceA = ultra
    after_distanceB = ultra_median
    changeA = after_distanceA - before_distanceA
    changeB = after_distanceB - before_distanceB

    # Judge the number of current inventory / items
    n_itemsA = round((unit_width - after_distanceA) / item_width)
    n_itemsB = round((unit_width - after_distanceB) / item_width)
    if motion == 1: # present: Open the door, start
        unit_mode = 1 # 'Unlocked'
    else: # motion == 0 : # present: Close the door, complete
        unit_mode = 0 #'Locked'

    # update and record this time as the last values
    ultra_lastA = ultra
    ultra_lastB = ultra_median

	########################################################################################################
    # Step 4: Identify the Abnormal Behaviours
    # Mode = Unlocked & Motion = 1
    if unit_mode == 1 :  #'Locked'
        if motion == 1 : #'There is a movement'
            abnormal = 1 #'YES, Alarm!'
        else:
            abnormal = 0 #'Everything is Fine!'
    else: # unit_mode == 1 , 'Locked'
        abnormal = 0 #'Everything is Fine!'

	
    ########################################################################################################
    # Step 5: Judge the behaviour (Put-In / Put-Out / No-Change)
    #  Recorded BehaviorA and BehaviorB for testing the accuracy caused by filter

    #####################
    # Use Raw Data of Ultrasonic
    if changeA > 0 :
        behaviorA = 1 #'Put-In'
    elif changeA < 0 :
        behaviorA = 2 #'Put-Out'
    else: # changeA = 0
        behaviorA = 0 #'No-Change'

    #####################
    # Use Filter Data of Ultrasonic (Median)
    if changeB > 0 :
        behaviorB = 1 #'Put-In'
    elif changeB < 0 :
        behaviorB = 2 #'Put-Out'
    else: # changeB = 0
        behaviorB = 0 #'No-Change'

    ########################################################################################################
    # Step 6: When mode is 'Locked', Judge the current status (Shortage or Normal)
    # use the threshold got from prototype implementation, 
	# which can be set as default when it becomes real situation.

    #####################
    # Use Raw Data of Ultrasonic
    if action == 1 :
        # the mode is 'Unlocked', we simply remain the last status and didn't judge it.
        unit_statusA = status_lastA
        unit_statusB = status_lastB
    else: # action == 0, the mode is 'Locked'
        #####################
        # Use Raw Data of Ultrasonic
        if ultra_lastA > 10:
            unit_statusA = 1 #'Shortage'
        else: # ultra_lastA <= 10
            unit_statusA = 0 # 'Normal'
        #####################
        # Use Filter Data of Ultrasonic (Median)
        if ultra_lastB > 10:
            unit_statusB = 1 # 'Shortage'
        else: # ultra_lastA <= 10
            unit_statusB = 0 # 'Normal'
	
    ########################################################################################################
    # Step 7: output the data & Set the speed of data recording
    print ('%f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d'
           %(times,motion,button,ultra,ultra_median,
             before_distanceA, before_distanceB,
             after_distanceA, after_distanceB,
             changeA, changeB,
             unit_mode, abnormal,
             behaviorA, behaviorB,
             unit_statusA, unit_statusB,
			 n_itemsA, n_itemsB))

    time.sleep(0.1) 