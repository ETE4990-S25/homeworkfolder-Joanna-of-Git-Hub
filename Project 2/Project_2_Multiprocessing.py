from multiprocessing import Process, Pipe, Lock, Value, Manager, Queue, Pool
import time

def is_prime(start, end):
    for a in range(start,end):
        if a <= 1:
            return False
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        largest_prime.value = a

NUM_OF_PROCESSES = 4
lock = Lock()
largest_prime = Value('i',0)

if __name__ == "__main__":
    end_time = time.time() + 30 #180 # setting the end time to 3 minutes after starting
    print(f"End Time: {end_time}")
    
    start = 1

    if time.time() < end_time:
        
        end = start + 12
        start = end + 1

        processes = [Process(target=is_prime, args=(start,end)) for i in range(NUM_OF_PROCESSES)]
    
        for p in processes:
            p.start()
        for p in processes: 
            p.join()
 
    print(f"Largest Prime: {largest_prime.value}")



    # i = 0

    # while time.time() < end_time and i < NUM_OF_PROCESSES:
    #     print(i)
    #     #p = Process(target=is_prime, args=(i * range_per_process + 1, (i + 1) * range_per_process + 1))
    #     p = [Process(target=is_prime, args=()) for i in range(NUM_OF_PROCESSES)]
    #     #processes.append(p)        
    #     for processes in p:
    #         processes.start()
    #     for processes in p: 
    #         processes.join()
    #     #i = i + 1


    
    

