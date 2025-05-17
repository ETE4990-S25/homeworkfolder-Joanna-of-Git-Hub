import requests
import xmltodict
import json
import random
from increment_date import Date, today_str # importing my own files

rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]
base = random.choice(ratesForBase)

# storing rate values in a list to make into csv
exc_list = [] # has indicies 0-39
i = 0

def get_data(a_date_str, a_base):
    """Retreives data from floatrates.com"""
    
    # URL of thetData data
    url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={a_date_str}&base_currency_code={a_base}&format_type=xml"
    
    # Fetch the XML data
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses

    # Parse the XML data to a Python dictionary
    data_dict = xmltodict.parse(response.text)

    # Convert the dictionary to a JSON string
    json_data =  json.dumps(data_dict, indent=4)

    # Write the JSON data to a file to save raw data
    with open(f"{a_date_str}_exchange_rates_{a_base}.json", "w") as raw_data:
        raw_data.write(json_data)

def write_data(a_date_str, a_base):
    # write specific information to a new dictionary
    with open(f"{a_date_str}_exchange_rates_{a_base}.json") as file:
        json_dict = json.load(file)

    index = i

    # save the abbreviation of the target currency and the conversion rate to the new dict
    for info in json_dict["channel"]["item"]:
        target = info["targetCurrency"]
        exchange = info["exchangeRate"] 
        
        if index < 40:
            exc_list.append(target)
            index += 1
        else:
            exc_list.append(exchange)