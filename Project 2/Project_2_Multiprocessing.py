from multiprocessing import Process, Pipe, Lock, Value, Manager, Queue, Pool
import time

def is_prime(n, end):
    while n != end:
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

NUM_OF_PROCESSES = 4
lock = Lock()
largest_prime = Value('i',0)
# pool = Pool(processes=largest_prime.value)

# if __name__ == "__main__":
#     num = [1,2,3,4,5,6,7,8,9,10,11,12]

#     pool.map(is_prime,num)
#     pool.close()
#     pool.join()

#The code runs, but it overwhelms the processor with all the processes it creates
if __name__ == "__main__":
    processes = []
    processes.append(
        Process(target=is_prime, args=(largest_prime,))
    )

 

    end_time = time.time() + 10 #(3*60) # setting the end time to 3 minutes after starting
    #print(f"End Time: {end_time}")

    i = 0

    while time.time() < end_time and i < NUM_OF_PROCESSES:
        print(i)
        #p = Process(target=is_prime, args=(i * range_per_process + 1, (i + 1) * range_per_process + 1))
        p = [Process(target=is_prime, args=()) for i in range(NUM_OF_PROCESSES)]
        #processes.append(p)        
        for processes in p:
            processes.start()
        for processes in p: 
            processes.join()
        #i = i + 1


    
    
    print(f"Largest Prime: {largest_prime.value}")

