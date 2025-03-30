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
    # processes = []
    # i = 0
    rangec = range(0,100001)
    
    #locking mechanism taken from ChatGPT
    largest_prime = multiprocessing.Value('i', 0)  
    lock = multiprocessing.Lock()  
 
    end_time = time.time() + (3*60) # setting the end time to 3 minutes after starting
    print(f"End Time: {end_time}")

    with multiprocessing.Pool(10) as p:
        while time.time() < end_time:
            p.map(is_prime, rangec) #args section from ChatGPT
            # processes.append(p)        

            
            # i = i + 1


    print(f"Largest Prime: {largest_prime.value}")
