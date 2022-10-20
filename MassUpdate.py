import requests

type_code = "P"

print("starting data migration for Type Code " + type_code)
base_url = "fbu-qa.pricefx.eu"
partition = "iplex-dev"

url = "https://" + base_url + "/pricefx/" + partition + "/massedit/" + type_code

payload = {
  "data": {
    "filterCriteria": {
      "_constructor": "AdvancedCriteria",
      "operator": "and",
      "criteria": [
        {
          "fieldName": "id",
          "operator": "inSet",
          "value": [
            "2147501189",
            "2147501188"
          ],
          "_constructor": "AdvancedCriteria"
        }
      ]
    },
    "massEditRecords": [
      {
        "fieldName": "currency",
        "massEditOperator": "=",
        "fieldValue": "USD",
        "precision": None
      }
    ]
  }
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers, auth=('iplex-dev/sm.hasan', 'start123'))

data = response.json()
print(data)