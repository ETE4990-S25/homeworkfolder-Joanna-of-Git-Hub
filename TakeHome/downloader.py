import requests
import xmltodict
import json
import random
import threading
import parser, increment_date # importing my own files

rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]

# i_year = 2011
# i_month = 5
# i_day = 4

base = random.choice(ratesForBase)

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

while date != today_string:
    date = 1



json_data = get_data()

# Print the JSON data
##print(json_data)

# # Optionally, write the JSON data to a file
# with open(f"{date}_exchange_rates_{base}.json", "w") as json_file:
#     json_file.write(json_data)
