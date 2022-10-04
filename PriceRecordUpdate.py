import sys

# Saving the reference of the standard output
original_stdout = sys.stdout

with open('01.UpdatePriceRecord.txt', 'a') as f:
    sys.stdout = f

    import requests
    def upsertData(payload):
      if "sku" in payload:
        type_code = "PR"
        base_url = "demo-eu.demo1.pricefx.com"
        partition = "demo_ark_solutions"
        url = "https://" + base_url + "/pricefx/" + partition + "/integrate/" + type_code

        payload = {
          "data": {
            "sku": payload["sku"],
            "typedId": payload["typedId"],

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
                                 auth=('demo_ark_solutions/sm.hasan', 'smhasan123!'))
        # print response statu
        data = response.json()
        print(data)


    def updateSKU(idList):
      for id in idList:
        myID = id.split(".")[0]

        skuTranslationMap = {
          "A9N2103": "XYZ",
          "A9N17581": "XYA",
          "BR1200S-JP": "ABE",
          "BN1350M2": "XYB",
          "SUB001": "ABC",
          "SUB003": "ABD",
          "R9H13602": "ABF",
          "MEG5050-0000": "ABG",
          "C2": "ABH"
        }

        type_code = "PR"
        base_url = "demo-eu.demo1.pricefx.com"
        partition = "demo_ark_solutions"
        url = "https://" + base_url + "/pricefx/" + partition + "/fetch/" + type_code + "/" + myID

        print(f"Fetching object {myID}")

        response = requests.post(url, auth=('demo_ark_solutions/sm.hasan', 'smhasan123!'))

        priceRecords = response.json()["response"]["data"][0]
        print(f"Fetched object {priceRecords}")

        if "sku" in priceRecords:
          currentSku = priceRecords["sku"]

        if currentSku in skuTranslationMap:
          priceRecords["sku"] = skuTranslationMap[currentSku]

        print("Updated object " + str(priceRecords))
        upsertData(priceRecords)


    type_code = "PR"
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
    # // try catch exceptaion handeling
    priceRecords = response.json()["response"]["data"]
    priceRecordIDs = []
    for obj in priceRecords:
      priceRecordIDs.append(obj["typedId"])

    print("Fetched typedIds" + str(priceRecordIDs))
    updateSKU(priceRecordIDs)


    # print('Hello, Python!')
    # print('This message will be written to a file.')
    # # Reset the standard output
    sys.stdout = original_stdout

