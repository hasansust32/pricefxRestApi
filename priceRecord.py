
import requests

type_code = "PR"
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
print(f"fetching all {type_code} from partition {partition}")
response = requests.post(url, json=payload, headers=headers, auth=('iplex-dev/sm.hasan', 'start123'))
# // try catch exceptaion handeling
priceRecords = response.json()["response"]["data"]
print(priceRecords)