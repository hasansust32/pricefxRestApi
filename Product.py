import requests

type_code = "P"
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
response = requests.post(url, json=payload, headers=headers, auth=('demo_ark_solutions/sm.hasan', 'smhasan123!'))
data = response.json()
print(data)



# type_code = "P"
# print("starting data migration for " + type_code)
# base_url = "demo-eu.demo1.pricefx.com"
# partition = "demo_ark_solutions"
# url = "https://" + base_url + "/pricefx/" + partition + "/fetch/" + type_code
#
# payload = {
#     "endRow": 300,
#     "operationType": "fetch",
#     "startRow": 0,
#     "textMatchStyle": "exact"
# }
#
# headers = {"Content-Type": "application/json"}
# print(f"fetching all {type_code} from partition {partition}")
# response = requests.post(url, json=payload, headers=headers, auth=('demo_ark_solutions/sm.hasan', 'smhasan123!'))
# # // try catch exceptaion handeling
# Products = response.json()["response"]["data"]
# ProductIDs = []
# for obj in Products:
#     ProductIDs.append(obj["typedId"])
#
# print("Fetched typedIds" + str(ProductIDs))


