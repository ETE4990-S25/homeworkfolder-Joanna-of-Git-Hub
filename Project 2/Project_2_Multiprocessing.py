from multiprocessing import Process, Pipe, Lock, Value, Manager, Queue, Pool
from threading import Thread, Lock
from queue import Queue, Empty
import asyncio 
import nest_asyncio # from Mr. Power's notes: this will fix the iPython unable to perform Asynchronous tasks
nest_asyncio.apply()
import time

### Project_2_Multiprocessing.py ###
NUM_OF_PROCESSES = 4
lock = Lock()
largest_prime = Value('i',0)

def is_prime(largest_prime, start, end):
    for a in range(start,end):
        if a <= 1:
            return False
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        largest_prime.value = a

if __name__ == "__main__":
    end_time = time.time() + 180 # setting the end time to 3 minutes after starting
    print(f"End Time: {end_time}")
    
    start = 1
    
    
    while time.time() < end_time:
        
        end = start + 60000

        processes = [Process(target=is_prime, args=(largest_prime,start,end)) for i in range(NUM_OF_PROCESSES)]
    
        for p in processes:
            p.start()
        for p in processes: 
            p.join()
        
        start = end
 
    print(f"Largest Prime: {largest_prime.value}")

### Project_2_Threading.py ###
n = largest_prime.value
THREAD_POOL_SIZE = 10
fibonnaci_number = 0 
lock = Lock()

def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonnaci(n - 1) + fibonnaci(n - 2)

def worker(work_queue): # Taken from Mr. Power's lecture notes.
    global fibonnaci_number
    while not work_queue.empty():
        try:
            item = work_queue.get(block=False)
        except Empty:
            break
        else:
            # taken lock structure from ChatGPT
            if fibonnaci(item):
                with lock: 
                    if item > fibonnaci_number:
                        fibonnaci_number = item
            work_queue.task_done()

def threaded_pool(): # Taken from Mr. Power's lecture notes.           
    global fibonnaci_number
    work_queue = Queue()
    
    for i in range(0,n): # changed the n to create the largest number the thing will (hopefully get to)
        work_queue.put(i)
        threads = [
            Thread(target=worker, args = (work_queue,)) for _ in range(THREAD_POOL_SIZE)
        ]

    for thread in threads:
        thread.start()

    work_queue.join()

    while threads:    #used to delay the time output lines
        threads.pop().join()



threaded_pool()

print(f"Fibonnaci number: {fibonnaci_number}")



### Project_3_Asynchronous.py ###
async def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else: 
        return factorial(n - 1)

# taken from Mr. Power's notes
num = 0
n = largest_prime.value
factorial_number = 0

async def main():
    if time.time() < asy_end: 
        await factorial_number = asyncio.gather(*(factorial(num) for num in n))
        # if num > factorial_result:
        #     factorial_result = num
        
    else: 
        print(f"Factorial Result: {factorial_number}") 

asyncio.run(main())
