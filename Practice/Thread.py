#!/usr/bin/python

#import thread
import threading
import time

tes = "hey"
les = tes

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("{}: {}".format( tes, time.ctime(time.time()) ))

# Create two threads as follows
try:
   t1 = threading.Thread( target=print_time, args=("Thread-1", 2), daemon=True )
   t2 = threading.Thread( target=print_time, args=(les, 4), daemon=True )
except:
   print ("Error: unable to start thread")


t1.start()
#t2.start()

#t1.join()
#tes = "prin"
#t2.join()



time.sleep(3)
tes = "prin"