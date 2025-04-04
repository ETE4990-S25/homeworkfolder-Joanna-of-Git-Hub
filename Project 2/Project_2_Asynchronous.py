import time
import asyncio 
import nest_asyncio # from Mr. Power's notes: this will fix the iPython unable to perform Asynchronous tasks
nest_asyncio.apply()
import Project_2_Threading

async def factorial(n):
    if n == 0:
        return 1
    else: 
        return factorial(n - 1)

# taken from Mr. Power's notes
r = range(13500000)
num = 0
factorial_result = Project_2_Threading.fibonnaci_number

async def main():
    if time.time() < asy_end: 
        await asyncio.gather(*(factorial(num) for num in r))
        if num > factorial_result:
            factorial_result = num
    else: 
        print(f"Factorial Result: {factorial_result}") 

asy_start = time.time()
asy_time_range = float(60 * 3)
asy_end = asy_start + asy_time_range # ending time for the function

asyncio.run(main())
