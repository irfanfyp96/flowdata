import time,sys
import urllib.request
import RPi.GPIO as GPIO
import time
import csv
import pigpio
import numpy as np

import http.client
import urllib

#Water flow sensor
FLOW_SENSOR1 = 14
FLOW_SENSOR2 = 15
FLOW_SENSOR3 = 18
FLOW_SENSOR4 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(FLOW_SENSOR2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(FLOW_SENSOR3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(FLOW_SENSOR4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Set up CSV file for data logging
csv_file_path = 'newdataloggerirfan_waterflow.csv'  # Replace with the actual path of your CSV file
csv_file = open(csv_file_path, mode='w')
csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csv_writer.writerow(['timestamp', 'Waterflowin1', 'Waterflowin2', 'Waterflowout1', 'Waterflowout2', 'Volume1', 'Volume2'])

# Initialize empty lists to store data
x1 = [] # FLOW SENSOR 3 time data in minutes
y1 = [] # FLOW SENSOR 3 flow rate data

x2 = [] # FLOW SENSOR 4 time data in minutes
y2 = [] # FLOW SENSOR 4 flow rate data

# Start recording data
start_time1 = time.time()
start_time2 = time.time()
stop_time1 = time.time()
stop_time2 = time.time()
flow_duration1 = stop_time1 - start_time1
flow_duration2 = stop_time2 - start_time2

#TRIED BUT FAILED def recording_duration1(end_time1, start_time1):
      recording_duration1 = end_time1 - start_time1
      if recording_duration1 == 0:
          return None
      elif recording_duration1 > 0:
          wait(lambda: recording_duration1(end_time1, start_time1), timeout_seconds = 300, waiting_for=recording_duration1)

#TRIED BUT FAILED def recording_duration2(end_time2, start_time2):
      recording_duration2 = end_time2 - start_time2
      if recording_duration2 == 0:
          return None
      elif recording_duration2 > 0:
          wait(lambda: recording_duration2(end_time2, start_time2), timeout_seconds = 300, waiting_for=recording_duration2)

class waterflow:
    global count, count2, count3, count4
    count = 0
    count2 = 0
    count3 = 0
    count4 = 0

    def countPulse(channel):
        global count
        if start_counter == 1:
            count = count+1
            
    GPIO.add_event_detect(FLOW_SENSOR1, GPIO.FALLING, callback=countPulse)

    def countPulse2(channel):
        global count2
        if start_counter2 == 1:
            count2 = count2+1
            
    GPIO.add_event_detect(FLOW_SENSOR2, GPIO.FALLING, callback=countPulse2)
    
    def countPulse3(channel):
        global count3, start_time1, stop_time1
        if start_counter3 == 1:
            count3 = count3+1
            start_time1 = time.time()
        else:
            stop_time1 = time.time()
            
    GPIO.add_event_detect(FLOW_SENSOR3, GPIO.FALLING, callback=countPulse3)
        
    def countPulse4(channel):
        global count4, start_time2, stop_time2
        if start_counter4 == 1:
            count4 = count4+1
            start_time2 = time.time()
        else:
            stop_time2 = time.time()
            
    GPIO.add_event_detect(FLOW_SENSOR4, GPIO.FALLING, callback=countPulse4)
        

while True:
    start_counter = 1
    time.sleep (1)
    start_counter = 0
    
    start_counter2 = 1
    time.sleep (1)
    start_counter2 = 0
    
    start_counter3 = 1
    time.sleep(1)
    start_counter3 = 0
    
    start_counter4 = 1
    time.sleep (1)
    start_counter4 = 0
    
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    Waterflowin1 = (count * 60 * 2.25 / 1000)
    Waterflowin2 = (count2 * 60 * 2.25 / 1000)
    Waterflowout1 = (count3 * 60 * 2.25 / 1000)
    Waterflowout2 = (count4 * 60 * 2.25 / 1000)

    current_outflow1 =  #not sure how to make the np.trapz(x,y) calculation to wait until flow duration is achieved
    current_outflow2 =

    #TRIED BUT FAILED Get the current outflow rate data
    current_outflow_rate1 = Waterflowout1
    current_outflow_rate2 = Waterflowout2
    
    #TRIED BUT FAILED Check if the outflow rate is zero
    if current_outflow_rate1 == 0:
        current_outflow_rate1 == Waterflowout1
    elif current_outflow_rate1 > 0:
        recording_duration1(end_time1, start_time1) 
    
    if current_outflow_rate2 == 0:
        current_outflow_rate2 == Waterflowout2
    elif current_outflow_rate2 > 0:
        recording_duration2(end_time2, start_time2) 

    # Add the data to the lists
    x1.append(flow_duration1)
    y1.append(current_outflow1)
    
    x2.append(flow_duration2)
    y2.append(current_outflow2)
    
    volume1 = np.trapz(x1,y1)
    volume2 = np.trapz(x2,y2)

    csv_writer.writerow([timestamp, Waterflowin1, Waterflowin2, Waterflowout1, Waterflowout2])
    csv_file.flush()
    print ("Timestamp:", timestamp)
    print ("Flow rate 1 is: %.3f Liter/min" %Waterflowin1)
    print ("Flow rate 2 is: %.3f Liter/min" %Waterflowin2)
    print ("Flow rate 3 is: %.3f Liter/min" %Waterflowout1)
    print ("Flow rate 4 is: %.3f Liter/min" %Waterflowout2)
    print ("Volume of Flowout1: %.3f Liter" %volume1)
    print ("Volume of Flowout2: %.3f Liter" %volume2)
    
    count = 0
    count2 = 0  
    count3 = 0   
    count4 = 0
    start_time1 = 0
    stop_time1 = 0
    start_time2 = 0
    stop_time2 = 0
    
    time.sleep(1)

print ("Recording duration1 %.3f seconds" %recording_duration1)
print ("Recording duration2 %.3f seconds" %recording_duration2)
