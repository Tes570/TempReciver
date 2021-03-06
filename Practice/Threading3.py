import threading
import time
#from Queue import Queue

# ‘results’ is list of received data; ‘GPIO.inputs’ is list of inputs being checked
results = [{} for x in GPIO.inputs] 
def input(GPIO.input, result, index):
	try:
		result[index] = GPIO.input
	except:
		print(“Error: unable to start thread”)
		result[index] = {}
	return True

# creates list of threads
threads = [ ]

for i in range(len(GPIO.inputs)):
	process = Thread(target=input, args=[GPIO.inputs[i], result, i] )
	process.start()
	threads.append(process)

for process in threads:
	process.join()

# q = Queue(maxsize=0)
# num_threads = min(50, len(GPIO.inputs))
# results = [{} for x in GPIO.inputs] 
# for i in range(len(GPIO.inputs)):
#	q.put( (i, GPIO.inputs[i]) )
#
# def inputs(q, result):
# 	while not q.empty():
#		work = q.get()
#		try:
#			result[work[0]] = work[1]
#		except:
#			print(“Error: unable to start thread”)
#			result[work[0]] = {}		
#		q.task_done()
#	return True
#
# for i in range(num_threads):
#	worker = Thread(target=inputs, args=(q, results) )
#	worker.setDaemon(True)	allows main program to terminate when main thread ends
#	worker.start()
# q.join()
