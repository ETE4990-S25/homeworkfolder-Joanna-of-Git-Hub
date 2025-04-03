import asyncio 
import nest_asyncio # this will fix the iPython unable to perform Asynchronous tasks
nest_asyncio.apply()
# async def async_hello():
#     print("hello, world")
# async_hello()

r = range(13500000)

async def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# taken from Mr. Power's notes
async def main():
    await asyncio.gather(*(is_prime(num) for num in r)) 

asy_start = time.time()
asyncio.run(main())
asy_total = time.time() - asy_start