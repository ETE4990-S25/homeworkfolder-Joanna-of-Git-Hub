from multiprocessing import Process, Pipe, Lock, Value, Manager, Queue
import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n


#The code runs, but it overwhelms the processor with all the processes it creates
if __name__ == "__main__":
    #processes = []
    NUM_OF_PROCESSES = 4
    #num_to_factor = 10000000 #very large number to (hopefully get to by the end of 3 minutes)
    #range_per_process = num_to_factor // NUM_OF_PROCESSES

    # parent_conns, child_conns = zip(*[Pipe() for _ in range(NUM_OF_PROCESSES)])
    #result_queue = Queue()

    #locking mechanism taken from ChatGPT
    largest_prime = Value('i', 0)  
    lock = Lock()  

    end_time = time.time() + 10 #(3*60) # setting the end time to 3 minutes after starting
    #print(f"End Time: {end_time}")

    i = 0

    while time.time() < end_time and i < NUM_OF_PROCESSES:
        print(i)
        #p = Process(target=is_prime, args=(i * range_per_process + 1, (i + 1) * range_per_process + 1))
        p = [Process(target=is_prime, args=(largest_prime,)) for i in range(0,10)]
        #processes.append(p)        
        for processes in p:
            processes.start()
        
        i = i + 1


    # # structure taken from ChatGPT
    #     while not result_queue.empty():
    #         largest_found = 0
    #         for n in range(0, num_to_factor):
    #             if is_prime(n):
    #                 largest_found = max(largest_found, n)
    #         result_queue.put(largest_found)
            
    #         found_prime = result_queue.get()
    #         with lock:
    #             if found_prime > largest_prime.value:
    #                 largest_prime.value = found_prime

    for processes in p: 
        processes.join()
    
    print(f"Largest Prime: {largest_prime.value}")

