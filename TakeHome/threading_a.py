# attempt without thread pooling
import threading
from increment_date import Date # importing my own files
from downloader import get_data, base
import time
import json

date = Date()
date_str = date.return_date()

today = Date(year=2011,month=5,day=20)
today_str = today.return_date()

threads = []
lock = threading.Lock()

info = []
json_dict = None

while date_str <= today_str:
    for i in range(5):
        with lock:
            thread = threading.Thread(target=get_data,args=(date_str,base))
            threads.append(thread)
            thread.start()

            date.increment_date()
            date_str = date.return_date()

    #print(f"During: {threading.active_count()}")

    for thread in threads:
        thread.join()


#print(f"After: {threading.active_count()}")   