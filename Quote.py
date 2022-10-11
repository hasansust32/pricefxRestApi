import requests

base_url = "demo-eu.demo1.pricefx.com"
partition = "demo_ark_solutions"

url = "https://" + base_url + "/pricefx/" + partition + "/quotemanager.fetchlist"

payload = {
  "endRow": 300,
  "oldValues": None,
  "operationType": "fetch",
  "startRow": 0,
  "textMatchStyle": "exact",
  "data": {
    "_constructor": "AdvancedCriteria",
    "operator": "and",
    "criteria": [
      {
        "fieldName": "quoteStatus",
        "operator": "equals",
        "value": "DEAL"
      }
    ]
  }
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers, auth=('demo_ark_solutions/sm.hasan', 'smhasan123!'))

data = response.json()["response"]["data"]
print(data)