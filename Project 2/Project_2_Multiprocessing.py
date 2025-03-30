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
    flag = True
 
    end_time = time.time() + (3*60) # setting the end time to 3 minutes after starting
    print(f"End Time: {end_time}")

    while time.time() < end_time:
        print(i)
        p = multiprocessing.Process(target=is_prime, args=(i,))
        processes.append(p)        
        p.start()
        
        # if time.time() >= end_time:
        #     flag = False
        #     p.join()
        #     print(f"Largest Prime: {processes[i]}")

        #     break
        
        i = i + 1

    for p in processes: 
        p.join()
