from multiprocessing import Process, Pipe, Lock, Value, Manager, Queue, Pool
import time

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
