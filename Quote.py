

import requests

typed_id = "24.Q"
base_url = "fbu-qa.pricefx.eu"
partition = "iplex-dev"

url = "https://" + base_url + "/pricefx/" + partition + "/quotemanager.fetchproducts"


url2 = "https://" + base_url + "/pricefx/" + partition + "/quotemanager.fetch/" + typed_id

response2 = requests.get(url2, auth=('iplex-dev/sm.hasan', 'start123'))
data = response2.json()['response']['data']
# print(data)



payload = {
  "operationType": "fetch",
  "startRow": 0,
  "textMatchStyle": "exact",
  "oldValues": None,
  "distinctResults": False,
  "data": {
    "quote": data[0],

    "filterCriteria": {
      "_constructor": "AdvancedCriteria",
      "operator": "and",
      "criteria": [
        {
          "fieldName": "",
          "operator": "",
          "value": ""
        }
      ]
    }
  },
  "endRow": 600,
  "sortBy": [
    "sku"
  ]
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers, auth=('iplex-dev/sm.hasan', 'start123'))

data = response.json()['response']['data']
print(data)


