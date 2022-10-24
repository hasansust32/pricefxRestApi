import csv
import json

import requests

base_url = "fbu-qa.pricefx.eu"
partition = "iplex-dev"


def getproduct(typed_id):
    url1 = "https://" + base_url + "/pricefx/" + partition + "/quotemanager.fetchproducts"

    url2 = "https://" + base_url + "/pricefx/" + partition + "/quotemanager.fetch/" + typed_id

    response2 = requests.get(url2, auth=('iplex-dev/sm.hasan', 'start123'))

    data = response2.json()['response']['data'][0]

    skus = []



    lineItem = data["lineItems"]
    for product in lineItem:
        if "sku" in product:
            skus.append(product["sku"])

    productsku = " | ".join(skus) if len(skus) != 0 else ""
    return productsku



    # print(data)
    # return data
    #
    # # print(x["lineItems"])
    #
    #
    #
    #
    # payload2 = {
    #     "operationType": "fetch",
    #     "startRow": 0,
    #     "textMatchStyle": "exact",
    #     "oldValues": None,
    #     "distinctResults": False,
    #     "data": {
    #         "quote": data[0],
    #
    #         "filterCriteria": {
    #             "_constructor": "AdvancedCriteria",
    #             "operator": "and",
    #             "criteria": [
    #                 {
    #                     "fieldName": "",
    #                     "operator": "",
    #                     "value": ""
    #                 }
    #             ]
    #         }
    #     },
    #     "endRow": 2,
    #     "sortBy": [
    #         "sku"
    #     ]
    # }
    #
    # headers = {"Content-Type": "application/json"}
    #
    # response = requests.post(url1, json=payload2, headers=headers, auth=('iplex-dev/sm.hasan', 'start123'))
    #
    #
    # data = response.json()['response']['data']
    # # print(data)
    # skulist = []
    # for lineItems in x:
    #     skulist.append(lineItems["sku"] if "sku" in lineItems else "")
    #
    # productsku = " | ".join(skulist)
    # print("done")
    # return productsku
    #
    #
    #


# getproduct("24.Q")





import requests

base_url = "fbu-qa.pricefx.eu"
partition = "iplex-dev"

url = "https://" + base_url + "/pricefx/" + partition + "/quotemanager.fetchlist"

payload = {
    "endRow": 500,
    "oldValues": None,
    "operationType": "fetch",
    "startRow": 301,
    "textMatchStyle": "exact",
    "data": {
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
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers, auth=('iplex-dev/sm.hasan', 'start123'))
myjson = response.json()["response"]["data"]

ourdata = []
csvheader = ['UNIQUE-NAME', 'CUSTOMER-ID', 'PRODUCT-ID']


for x in myjson:
    cusId = x["customerId"] if "customerId" in x else ""
    unqname = x["uniqueName"] if "uniqueName" in x else ""
    productId = ""
    if unqname:
        productId = getproduct(unqname.split("-")[1] + ".Q")


    # productId = getProduct(unqname.split('P-')[1])

    listing = [unqname, cusId, productId]
    ourdata.append(listing)

with open('05.quote_report.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourdata)

# print(myjson)
