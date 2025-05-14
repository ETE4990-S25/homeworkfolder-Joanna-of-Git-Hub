import requests
import xmltodict
import json
import random
import threading
import time
import parser # importing my own files
from increment_date import Date, today_str

rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]
base = random.choice(ratesForBase)

date = Date() # intitalizing starting values in Date 2011-05-04
date_str = date.return_date() # chaging starting values to a string

exc_dict = {}

def get_data(date, base):
    # URL of thetData data
    url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={date}&base_currency_code={base}&format_type=xml"
    ##print(url)
    
    # Fetch the XML data
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses

    # Parse the XML data to a Python dictionary
    data_dict = xmltodict.parse(response.text)

    # Convert the dictionary to a JSON string
    json_dict =  json.dumps(data_dict, indent=4)


    # get the abbreviation of the target currency and the conversion rate
    exc_dict[json_dict["channel"]["item"]["targetCurrency"]] = json_dict["channel"]["item"]["exchangeRate"]

def threaded(debug=False):
    threads = []
    for base in bases:
        thread = threading.Thread(target=fetch_rate, args=(base, rates, debug, debug))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()   








#thread = threading.Thread(target=get_data)
# thread.start()

# def worker(task_id):
#     print(f"Thread-{task_id} starting")
#     time.sleep(random.randint(1,4)) # run for a random time to illistrate threads can end at different times
#     print(f"Thread-{task_id} finished")

# Creating threads
threads = []
for i in range(5):
    thread = threading.Thread(target=get_data, args=(date_str,base))
    threads.append(thread)
    thread.start()

# #this will run
# for i in range(5):
#     print("Main thread continues to run...")
#     time.sleep(1)

# Joining threads tells the code to wait 
for thread in threads:
    thread.join()

#will run after 
print("All threads have completed.")












if date_str != today_str:
    
    # join the threads for threading
    a = 1    
else: 
    # continue??

    date.increment_date() # increments the yr/mo/day values in the class Date



# Print the JSON data
##print(json_data)

# # Optionally, write the JSON data to a file
# with open(f"{date}_exchange_rates_{base}.json", "w") as json_file:
#     json_file.write(json_data)
