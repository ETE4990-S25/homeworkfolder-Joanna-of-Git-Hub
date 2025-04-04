from threading import Thread, Lock
from queue import Queue, Empty
import time

n = 0
THREAD_POOL_SIZE = 10
largest_prime = 0 
lock = Lock()

def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonnaci(n - 1) + fibonnaci(n - 2)

def worker(work_queue): # Taken from Mr. Power's lecture notes.
    global largest_prime
    while not work_queue.empty():
        try:
            item = work_queue.get(block=False)
        except Empty:
            break
        else:
            # taken lock structure from ChatGPT
            if fibonnaci(item):
                with lock: 
                    if item > largest_prime:
                        largest_prime = item
            work_queue.task_done()

def threaded_pool(): # Taken from Mr. Power's lecture notes.           
    global largest_prime
    work_queue = Queue()
    
    for n in range(0,11000000): # changed the n to create the largest number the thing will (hopefully get to)
        work_queue.put(n)
        threads = [
            Thread(target=worker, args = (work_queue,)) for _ in range(THREAD_POOL_SIZE)
        ]

    for thread in threads:
        thread.start()

    work_queue.join()

    while threads:    #used to delay the time output lines
        threads.pop().join()


now = time.time()
time_range = float(60 * 3) 
end_time = now + time_range # sets up 3-minute working window

while time.time() < end_time:
    threaded_pool()

print(f"Largest prime found: {largest_prime}")
