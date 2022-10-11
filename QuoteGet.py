

import requests

typed_id = "P"
base_url = "demo-eu.demo1.pricefx.com"
partition = "demo_ark_solutions"
url = "https://" + base_url + "/pricefx/" + partition + "/quotemanager.fetch/" + typed_id

response = requests.post(url, auth=('demo_ark_solutions/sm.hasan', 'smhasan123!'))

data = response.json()
print(data)