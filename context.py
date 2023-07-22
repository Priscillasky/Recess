#Context manager
#Multithreading and multiprocessing
#context manager - is an object that defines a temporary context for a block ofcode.
#Example:Demonstarte a context manager to open a file and returns a context ,manager instance.
def open_file(filename):
    #open file and return a context manager instance
    file = open(filename,"r")

    def __enter__():
        return file

    def __exit__(self,exc_value,exc_tb,exc_type):
        file.close()

        return __enter__, __exit__
    
with open_file('gum.txt') as f:
    contenys = f.read()
    
#Example 2-Demonstrate context manager using a time series
import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, trace):
        end_time = time.time()
        execution_time = end_time - self.start_time
        print(f"Time for this execution{execution_time}:{execution_time} seconds elapsed")
with Timer():
    #measure the execution time
    time.sleep(2)
    """

#MULTITHREADING AND MULTIPROCESSING
technique where multiple threads are created within a single process
i.e multiple threads are created in a single process
Example of multithreading
import threading
def task(name):
    print(f"running task {name}")

#create multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=task, args = (f"Thread{i}",))
    threads.append(t)
    t.start()

#Wait for all threads to finish
for t in threads:
    t.join() 


#Example on multiprocessing
import multiprocessing
 
def process_task(name):
    print(f'Processing task {name}')

#create a pool of processes
pool = multiprocessing.Pool(processes=5)

#submit multiple 
for i in range(5):
    pool.apply_async(process_task, args=(f"Process {i}",))


#close the pool and wait for all processes to finish
pool.close()
pool.join()
"""

#Multiprocessing + multithreading
import threading
import multiprocessing

def task(name):
    print(f"Running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name} to complete")

#create multiple threads
threads = []
for i in range(3):
    t = threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(t)
    t.start()


for t in threads:
    t.join()
