import time
from datetime import datetime

def display_clock():
    print("Current Time:", datetime.now().strftime("%H:%M:%S"))

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    input("Press Enter to stop the stopwatch...")
    end_time = time.time()
    stop_watch = end_time - start_time
 
    print("stop watch time: ",stop_watch)
while True:
    print("\n************ Stopwatch + Clock ************")
    display_clock()
    stopwatch()
    
    choice = input("if you want to continue enter 1, else 0: ")
    if choice != '1':
        break