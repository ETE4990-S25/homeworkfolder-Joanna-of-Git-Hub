import asyncio 
import nest_asyncio # this will fix the iPython unable to perform Asynchronous tasks
nest_asyncio.apply()
# async def async_hello():
#     print("hello, world")
# async_hello()

async def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True