from threading import Thread, Lock
import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

lock = Lock()
thread = Thread(target=is_prime)
thread.start()

