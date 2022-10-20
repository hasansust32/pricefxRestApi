import sys

# Saving the reference of the standard output
original_stdout = sys.stdout

with open('01.Final_PriceRecord_Update1.txt', 'a') as f:
    sys.stdout = f

    import requests
    def upsertData(payload):
        if "sku" in payload:
            type_code = "PR"
            base_url = "fbu-qa.pricefx.eu"
            partition = "iplex-dev"
            url = "https://" + base_url + "/pricefx/" + partition + "/integrate/" + type_code

            payload = {
                "data": {
                    "typedId": payload["typedId"],
                    "sku": payload["sku"],
                    "customerId": payload["customerId"]
                }
            }

            headers = {"Content-Type": "application/json"}
            print(f"Object update request payload {payload}")
            response = requests.post(url, json=payload, headers=headers,
                                     auth=('iplex-dev/sm.hasan', 'start123'))
            # print response statu
            data = response.json()
            print(data)




    def ProductMigration():
        import csv

        with open("DataSet/ProductMappingData.csv", 'r') as file1:
            csvreader = csv.reader(file1)
            Migration1 = {

            }

            for row in csvreader:
                Migration1[row[0]] = row[1]

            return (Migration1)

    def CustomerMigration():
        import csv

        with open("DataSet/CustomerMapForPR.csv", 'r') as file2:
            csvreader = csv.reader(file2)
            Migration2 = {

            }

            for row in csvreader:
                Migration2[row[0]] = row[1]

            return (Migration2)





    def updatePriceRecord(idList):
        ProductTranslationMap = ProductMigration()
        CustomerTranslationMap = CustomerMigration()

        for id in idList:
            myID = id.split(".")[0]

            type_code = "PR"
            base_url = "fbu-qa.pricefx.eu"
            partition = "iplex-dev"
            url = "https://" + base_url + "/pricefx/" + partition + "/fetch/" + type_code + "/" + myID

            print(f"Fetching object {myID}")

            response = requests.post(url, auth=('iplex-dev/sm.hasan', 'start123'))

            priceRecord = response.json()["response"]["data"][0]
            print(f"Fetched object {priceRecord}")

            if "sku" in priceRecord:
                currentSku = priceRecord["sku"]

            if currentSku in ProductTranslationMap:
                priceRecord["sku"] = ProductTranslationMap[currentSku]

            if "customerId" in priceRecord:
                currentCustomerId = priceRecord["customerId"]

            if currentCustomerId in CustomerTranslationMap:
                priceRecord["customerId"] = CustomerTranslationMap[currentCustomerId]

            print("Updated object " + str(priceRecord))

            upsertData(priceRecord)



    type_code = "PR"
    print(f"#-----------------------------------------------------------------------------------------------------------------------------------------------------")

    print("starting data migration for Type Code " + type_code)
    base_url = "fbu-qa.pricefx.eu"
    partition = "iplex-dev"
    url = "https://" + base_url + "/pricefx/" + partition + "/fetch/" + type_code

    payload = {
      "endRow": 5500,
      "operationType": "fetch",
      "startRow": 0,
      "textMatchStyle": "exact"
    }

    headers = {"Content-Type": "application/json"}
    print(f"fetching all {type_code} from partition {partition}")
    response = requests.post(url, json=payload, headers=headers, auth=('iplex-dev/sm.hasan', 'start123'))
    # // try catch exceptaion handeling
    priceRecords = response.json()["response"]["data"]
    priceRecordIDs = []

    for obj in priceRecords:
      priceRecordIDs.append(obj["typedId"])

    print("Fetched typedIds" + str(priceRecordIDs))
    updatePriceRecord(priceRecordIDs)

    CustomerIDs = []
    for obj in priceRecords:
      CustomerIDs.append(obj["typedId"])

    print("Fetched typedIds" + str(CustomerIDs))
    updatePriceRecord(CustomerIDs)



    sys.stdout = original_stdout


