import grovepi
import os
import time
import collections

# this value indicates the total length or height of the unit,
# which were got from implementation, the initial steady number that Ultrasonic got.
unit_width = 51  # default
item_width = 7 # default
history_motion=collections.deque(maxlen=30) # will be used for median filter later
history_ultra=collections.deque(maxlen=30)

ultra_lastA = 0 # for ultra raw value
ultra_lastB = 0 # for ultra filter value
before_dA = 0
before_dB = 0
after_dA = 0
after_dB = 0


print ('times,motion,motion_mean,button,ultra,ultra_median,changeA, changeB,behaviorA, behaviorB,unit_status,n_items')

while True:
    ########################################################################################################
    # read time and raw data from sensors
    # PIR-D2, button-D3, Ultrasonic-D4
    times = time.clock()
    motion = grovepi.digitalRead(2)  # alternative 1
    button = grovepi.digitalRead(3) # alternative 2
    ultra = grovepi.ultrasonicRead(4) # raw distance

    ########################################################################################################
    # use filter
    history_motion.append(motion)
    motion_mean = sum(history_motion) / 30

    history_ultra.append(ultra)
    ordered_ultra = sorted(history_ultra)
    ultra_median = history_ultra[int(len(ordered_ultra) / 2)]

    ########################################################################################################
    # Judge the number of items
    n_items = round((unit_width - ultra) / item_width)

    # Judge the stock status
    if n_items < 0:
        unit_status = 2  # 'Abnormal'
    else:
        if n_items<=1:
            unit_status = 1  # 'Shortage'
        else:
            unit_status = 0 # 'Well-stocked'

    ########################################################################################################
    # Judge the Mode by Motion & Identify the change
    if motion_mean != 0: # 'Action-ing'
        before_dA = ultra_lastA
        before_dB = ultra_lastB
    else: # motion_mean == 0:
        unit_mode = 1 # 'Action-End'
        after_dA = ultra
        after_dB = ultra_median

    after_d = ultra_median
    changeA = after_dA - before_dA
    changeB = after_dB - before_dB

    # update and record this time as the last values
    ultra_lastA = ultra
    ultra_lastB = ultra_median


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
    # Step 7: output the data & Set the speed of data recording
    print ('%f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d'
           %(times,motion,motion_mean,button,ultra,ultra_median,
             changeA, changeB,
             behaviorA, behaviorB,
             unit_status,
			 n_items))

    time.sleep(0.1) 