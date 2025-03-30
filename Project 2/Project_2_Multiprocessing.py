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
    i = 0

    start_time = time.time()
    end_time = start_time + (3*60) # setting the end time to 3 minutes after starting
    
    for i in range(0,):
        p = multiprocessing.Process(target=is_prime, args=(i,))
        processes.append(p)        
        p.start()
        
        if time.time() == end_time:
            p.join()
            print(f"Largest Prime: {i}")
