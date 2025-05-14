import requests
import xmltodict
import json
import random
import threading
import time
import parser

rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]

i_year = 2011
i_month = 5
i_day = 3
days_31 = [1,3,5,7,8,10,12]
days_30 = [4,6,9,11]

today_string = time.strftime("%Y-%m-%d",time.gmtime()) # figured this out using the Python datasheet

base = random.choice(ratesForBase)

def increment_date(year, month, day):
    """A function to increment the date and returns date in yr-mos-day format as a string."""
    # incrementing dates depending on the month
    if day == 31 and month == 12:
        year += 1
    elif day == 31 and month in days_31:
        month += 1
    elif day == 30 and month in days_30:
        month += 1
    elif day == 28 and month == 2 or day == 29 and month == 2:
        month += 1
    else:
        day += 1

    # turning date into a string. Adds a zero ahead of day/month number if needed.
    if day < 10 and month > 10:
        date = f"{year}-{month}-0{day}"
    elif day < 10 and month < 10:
        date = f"{year}-0{month}-0{day}"
    elif day > 10 and month < 10:
        date = f"{year}-0{month}-{day}"
    else:
        date = f"{year}-{month}-{day}"
    
    return date

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
    return json.dumps(data_dict, indent=4)





json_data = get_data()

# Print the JSON data
##print(json_data)

# # Optionally, write the JSON data to a file
# with open(f"{date}_exchange_rates_{base}.json", "w") as json_file:
#     json_file.write(json_data)
