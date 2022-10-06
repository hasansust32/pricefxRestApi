
import requests

type_code = "MLTV2"
print("starting data migration for Type Code " + type_code)
base_url = "demo-eu.demo1.pricefx.com"
partition = "demo_ark_solutions"
url = "https://" + base_url + "/pricefx/" + partition + "/fetch/" + type_code

payload = {
  "endRow": 300,
  "operationType": "fetch",
  "startRow": 0,
  "textMatchStyle": "exact"
}

headers = {"Content-Type": "application/json"}
print(f"fetching all {type_code} from partition {partition}")
response = requests.post(url, json=payload, headers=headers, auth=('demo_ark_solutions/sm.hasan', 'smhasan123!'))
data = response.json()["response"]["data"]
print(data)

