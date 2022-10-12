import sys

# Saving the reference of the standard output
original_stdout = sys.stdout

with open('02.UpdateProduct.txt', 'a') as f:
    sys.stdout = f

    import requests
    def upsertData(payload):
      if "sku" in payload:
        type_code = "P"
        base_url = "fbu-qa.pricefx.eu"
        partition = "iplex-dev"
        url = "https://" + base_url + "/pricefx/" + partition + "/integrate/" + type_code

        payload = {
          "data": {
            "typedId": payload["typedId"],
              "sku": payload["sku"]

            # "label": [payload["label"]],
            # "unitOfMeasure": payload["unitOfMeasure"],
            # "currency": payload["currency"],
            # "formulaName": payload["formulaName"],
            # "attribute1": payload["attribute1"],
            # "attribute2": payload["attribute2"],
            # "userGroupEdit": payload["userGroupEdit"],
            # "userGroupViewDetails": payload["userGroupViewDetails"]

          }
        }

        headers = {"Content-Type": "application/json"}
        print(f"Object update request payload {payload}")
        response = requests.post(url, json=payload, headers=headers,
                                 auth=('iplex-dev/sm.hasan', 'start123'))
        # print response statu
        data = response.json()
        print(data)


    def Migration():
        import csv

        with open("DataSet/ProductMappingData.csv", 'r') as file:
            csvreader = csv.reader(file)
            Migration = {

            }

            for row in csvreader:
                Migration[row[0]] = row[1]

            return (Migration)


        # print(Migration())


    def updateSKU(idList):
      for id in idList:
        myID = id.split(".")[0]


        translationMap = Migration()

        type_code = "P"
        base_url = "fbu-qa.pricefx.eu"
        partition = "iplex-dev"
        url = "https://" + base_url + "/pricefx/" + partition + "/fetch/" + type_code + "/" + myID

        print(f"Fetching object {myID}")

        response = requests.post(url,  auth=('iplex-dev/sm.hasan', 'start123'))

        productRecords = response.json()["response"]["data"][0]
        print(f"Fetched object {productRecords}")

        if "sku" in productRecords:
          currentSku = productRecords["sku"]

        if currentSku in translationMap:
          productRecords["sku"] = translationMap[currentSku]

        print("Updated object " + str(Products))
        upsertData(Products)


    type_code = "P"
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
    Products = response.json()["response"]["data"]
    ProductIDs = []
    for obj in Products:
      ProductIDs.append(obj["typedId"])

    print("Fetched typedIds" + str(ProductIDs))
    updateSKU(ProductIDs)


    # print('Hello, Python!')
    # print('This message will be written to a file.')
    # # Reset the standard output
    sys.stdout = original_stdout


