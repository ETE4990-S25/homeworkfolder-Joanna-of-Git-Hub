import time
import asyncio 
import nest_asyncio # from Mr. Power's notes: this will fix the iPython unable to perform Asynchronous tasks
nest_asyncio.apply()

async def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# taken from Mr. Power's notes
r = range(13500000)
num = 0
largest_prime = 0

async def main():
    if time.time() < asy_end: 
        await asyncio.gather(*(is_prime(num) for num in r))
        if num > largest_prime:
            largest_prime = num
    else: 
        print(f"Largest prime: {largest_prime}") 

asy_start = time.time()
asy_time_range = float(60 * 3)
asy_end = asy_start + asy_time_range # ending time for the function

asyncio.run(main())
