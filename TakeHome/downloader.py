import requests
import xmltodict
import json
import random
import threading
from queue import Queue, Empty
import time
#import parser # importing my own files
from increment_date import Date, today_str # importing my own files

rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]
base = random.choice(ratesForBase)

# initializing the way days will be counted
date = Date() # intitalizing starting values in Date 2011-05-04
date_str = date.return_date() # chaging starting values to a string

# storing rate values in a dictionary
exc_dict = {}

def get_data(date_str, base):
    """Retreives data from floatrates.com"""
    # URL of thetData data
    url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={date_str}&base_currency_code={base}&format_type=xml"
    
    # Fetch the XML data
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses

    # Parse the XML data to a Python dictionary
    data_dict = xmltodict.parse(response.text)

    # Convert the dictionary to a JSON string
    json_data =  json.dumps(data_dict, indent=4)

    # Write the JSON data to a file to save raw data
    with open(f"{date_str}_exchange_rates_{base}.json", "w") as raw_data:
        raw_data.write(json_data)


    # write specific information to a new dictionary
    with open(f"{date_str}_exchange_rates_{base}.json") as file:
        json_dict = json.load(file)

    # save the abbreviation of the target currency and the conversion rate to the new dict
    for info in json_dict["channel"]["item"]:
        key = info["targetCurrency"]
        value = info["exchangeRate"] 
        
        exc_dict[key] = value

    
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

while date_str <= today_str:
    threaded_pool()
    date.increment_date() # increments the yr/mo/day values in the class Date

    # Write the new dictionary to a JSON file
    with open(f"{base}_exchange_rates.json", "w") as rate_dict:
        rate_dict.write(exc_dict)