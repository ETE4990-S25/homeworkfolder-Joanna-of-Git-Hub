import time
import asyncio 
import nest_asyncio # from Mr. Power's notes: this will fix the iPython unable to perform Asynchronous tasks
nest_asyncio.apply()
import Project_2_Multiprocessing

async def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else: 
        return factorial(n - 1)

# taken from Mr. Power's notes
num = 0
n = Project_2_Multiprocessing.largest_prime.value
factorial_number = 0

async def main():
    if time.time() < asy_end: 
        await factorial_number = asyncio.gather(*(factorial(num) for num in n))
        # if num > factorial_result:
        #     factorial_result = num
        
    else: 
        print(f"Factorial Result: {factorial_number}") 

asyncio.run(main())
