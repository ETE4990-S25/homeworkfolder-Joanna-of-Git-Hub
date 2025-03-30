import multiprocessing
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
    #manager = multiprocessing.Manager()
    shared_dict = manager.dict()
    i = 0
    
    #locking mechanism taken from ChatGPT
    largest_prime = multiprocessing.Value('i', 0)  
    lock = multiprocessing.Lock()  
 
    end_time = time.time() + (3*60) # setting the end time to 3 minutes after starting
    print(f"End Time: {end_time}")

    while time.time() < end_time:
        print(i)
        p = multiprocessing.Process(target=is_prime, args=(i,largest_prime, lock)) #args section from ChatGPT
        processes.append(p)        
        p.start()

        
        i = i + 1

    for p in processes: 
        p.join()

    print(f"Largest Prime: {largest_prime.value}")

    #The code runs, but it overwhelms the processor with all the processes it creates
