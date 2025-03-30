from multiprocessing import Process, Pipe, Lock, Value, Manager
import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    processes = []
    NUM_OF_PROCESSES = 10
    num_to_factor = 10000000 #very large number to (hopefully get to by the end of 3 minutes)
    range_per_process = num_to_factor // NUM_OF_PROCESSES

    parent_conns, child_conns = zip(*[Pipe() for _ in range(NUM_OF_PROCESSES)])

    #locking mechanism taken from ChatGPT
    largest_prime = Value('i', 0)  
    lock = Lock()  
 
    end_time = time.time() + (3*60) # setting the end time to 3 minutes after starting
    print(f"End Time: {end_time}")

    while time.time() < end_time:
        print(i)
        p = Process(target=is_prime, args=(i,largest_prime, lock)) #args section from ChatGPT
        processes.append(p)        
        p.start()

        
        i = i + 1

    for p in processes: 
        p.join()

    print(f"Largest Prime: {largest_prime.value}")

    #The code runs, but it overwhelms the processor with all the processes it creates
