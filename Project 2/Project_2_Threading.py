from threading import Thread, Lock
from queue import Queue, Empty
import time

n = 0

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
            is_prime(n)
            work_queue.task_done()

def threaded_pool(): # Taken from Mr. Power's lecture notes.           
    work_queue = Queue()

    for base in bases:
        work_queue.put(base)
        threads = [
            Thread(target=worker, args=(work_queue,)) 
            for _ in range(THREAD_POOL_SIZE)
        ]
    
    for thread in threads:
        thread.start()

    work_queue.join()

    while threads:    #used to delay the time output lines
        threads.pop().join



lock = Lock()
thread = Thread(target=is_prime)
thread.start()

