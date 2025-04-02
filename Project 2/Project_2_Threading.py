from threading import Thread, Lock
from queue import Queue, Empty
import time

n = 0
THREAD_POOL_SIZE = 10

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def worker(work_queue): # Taken from Mr. Power's lecture notes.
    while not work_queue.empty():
        try:
            item = work_queue.get(block=False)
        except Empty:
            break
        else:
            # fetch_rate(base, rates,False, True)
            is_prime(item)
            work_queue.task_done()

def threaded_pool(): # Taken from Mr. Power's lecture notes.           
    work_queue = Queue()
    
    for n in range(0,11000000): 
        work_queue.put(n)
        threads = [
            Thread(target=worker, args = (work_queue,)) for _ in range(THREAD_POOL_SIZE)
        ]

    for thread in threads:
        thread.start()

    work_queue.join()

    while threads:    #used to delay the time output lines
        threads.pop().join()


end_time = time.time + (3*60) # sets up 3-minute working window

while time.time() < end_time:
    threaded_pool()

