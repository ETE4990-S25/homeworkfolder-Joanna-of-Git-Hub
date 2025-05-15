import threading
from queue import Queue, Empty
import time
import json
from increment_date import Date, today_str # importing my own files
from downloader import get_data, date_str, base, ratesForBase, exc_dict
    
def worker(work_queue): # taken from Mr. Power's notes
    while not work_queue.empty():
        try:
            item = work_queue.get(block=False)
        except Empty:
            break
        else:
            get_data(date_str,base)
            work_queue.task_done()

def threaded_pool(): # taken from Mr. Power's notes           
    work_queue = Queue()

    for base in ratesForBase:
        work_queue.put(base)
        threads = [
            threading.Thread(target=worker, args=(work_queue,)) 
            for _ in range(5)
        ]
    
    for thread in threads:
        thread.start()

    work_queue.join()

    while threads:    #used to delay the time output lines
        threads.pop().join