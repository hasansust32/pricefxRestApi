import requests

type_code = "C"
print("starting data migration for Type Code " + type_code)
base_url = "fbu-qa.pricefx.eu"
partition = "iplex-dev"
url = "https://" + base_url + "/pricefx/" + partition + "/fetch/" + type_code

payload = {
  "endRow": 300,
  "operationType": "fetch",
  "startRow": 0,
  "textMatchStyle": "exact"
}

headers = {"Content-Type": "application/json"}
response = requests.post(url, json=payload, headers=headers, auth=('iplex-dev/sm.hasan', 'start123'))
data = response.json()["response"]["data"]
print(data)

