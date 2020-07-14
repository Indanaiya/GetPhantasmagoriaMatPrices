import json
import requests

universalis_url = "https://universalis.app/api/"
values = "values.json"
datacenter = "Chaos"

def getItemsFromUniversalis(items=None):
    with open(values) as f:
        valuesData = json.load(f)
        if not items:
            items = valuesData
    prices = {}
    for i in items:
        with requests.request("GET", universalis_url + datacenter + "/" + valuesData[i]['id']) as response:
            responseJson = response.json()
            price = responseJson['listings'][0]['pricePerUnit']
            price_per_tomestone = float(price) / float(valuesData[i]['tomestone_price'])
            prices[i] = {'price': price, 'price_per_tomestone': price_per_tomestone}
    sorted_prices = sorted(prices.items(), key=lambda x: x[1]['price_per_tomestone'], reverse=True)

    for k, v in sorted_prices:
        print(str(v['price_per_tomestone']) + " - " + str(k) + "(" + str(v['price']) + ")")

        
if __name__ == "__main__":
    getItemsFromUniversalis()