


import sys

# Saving the reference of the standard output
original_stdout = sys.stdout

with open('02.Reverse_Product_Migration.txt', 'a') as f:
    sys.stdout = f

    import requests
    def upsertData(datapayload):
        if "sku" in datapayload:
            type_code = "P"
            base_url = "fbu-qa.pricefx.eu"
            partition = "iplex-dev"
            url = "https://" + base_url + "/pricefx/" + partition + "/integrate/" + type_code

            payload = {
                "data": {
                    "typedId": datapayload["typedId"],
                    "sku": datapayload["sku"]

                }
            }

            headers = {"Content-Type": "application/json"}
            print(f"Object update request payload {payload}")
            response = requests.post(url, json=payload, headers=headers,
                                     auth=('iplex-dev/sm.hasan', 'start123'))
            # print response statu
            data = response.json()
            print(data)




    def migration():
        import csv

        with open("DataSet/ReverseProductMapping2.csv", 'r') as file:
            csvreader = csv.reader(file)
            Migration = {

            }

            for row in csvreader:
                Migration[row[0]] = row[1]

            return (Migration)


    def updateSKU(idList):
        translationMap = migration()


        for id in idList:
            myID = id.split(".")[0]


            type_code = "P"
            base_url = "fbu-qa.pricefx.eu"
            partition = "iplex-dev"
            url = "https://" + base_url + "/pricefx/" + partition + "/fetch/" + type_code + "/" + myID

            print(f"Fetching object {myID}")

            response = requests.post(url, auth=('iplex-dev/sm.hasan', 'start123'))

            ProductData = response.json()["response"]["data"][0]
            print(f"Fetched object {ProductData}")

            if "sku" in ProductData:
                currentSku = ProductData["sku"]

            if currentSku in translationMap:
                ProductData["sku"] = translationMap[currentSku]

            print("Updated object " + str(ProductData))

            upsertData(ProductData)







    type_code = "P"
    print(f"#--------------------------------------------------------------------------------------------------------------------------------------------------"
          f"--------------------------------------------------------------------------------------------------------------------------------------------------------------------"
          f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    print("starting data migration for Type Code " + type_code)
    base_url = "fbu-qa.pricefx.eu"
    partition = "iplex-dev"
    url = "https://" + base_url + "/pricefx/" + partition + "/fetch/" + type_code

    payload = {
      "endRow": 5000,
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

    sys.stdout = original_stdout






















    #
    # import sys
    #
    # # Saving the reference of the standard output
    # original_stdout = sys.stdout
    #
    # with open('02_Test_Product_Migration.txt', 'a') as f:
    #     sys.stdout = f
    #
    #     import requests
    #     def upsertData(payload):
    #       if "sku" in payload:
    #         type_code = "P"
    #         base_url = "fbu-qa.pricefx.eu"
    #         partition = "iplex-dev"
    #         url = "https://" + base_url + "/pricefx/" + partition + "/integrate/" + type_code
    #
    #         payload = {
    #           "data": {
    #             "typedId": payload["typedId"],
    #               "sku": payload["sku"]
    #
    #
    #           }
    #         }
    #
    #         headers = {"Content-Type": "application/json"}
    #         print(f"Object update request payload {payload}")
    #         response = requests.post(url, json=payload, headers=headers,
    #                                  auth=('iplex-dev/sm.hasan', 'start123'))
    #         # print response statu
    #         data = response.json()
    #         print(data)
    #
    #
    #     def Migration():
    #         import csv
    #
    #         with open("DataSet/UpdatedProductMapping.csv", 'r') as file:
    #             csvreader = csv.reader(file)
    #             Migration = {
    #
    #             }
    #
    #             for row in csvreader:
    #                 Migration[row[0]] = row[1]
    #
    #             return (Migration)
    #
    #
    #         # print(Migration())
    #
    #
    #     def updateSKU(idList):
    #       for id in idList:
    #         myID = id.split(".")[0]
    #
    #
    #         translationMap = Migration()
    #
    #
    #         type_code = "P"
    #         base_url = "fbu-qa.pricefx.eu"
    #         partition = "iplex-dev"
    #         url = "https://" + base_url + "/pricefx/" + partition + "/fetch/" + type_code + "/" + myID
    #
    #         print(f"Fetching object {myID}")
    #
    #         response = requests.post(url,  auth=('iplex-dev/sm.hasan', 'start123'))
    #
    #         dataProduct = response.json()["response"]["data"][0]
    #         print(f"Fetched object {dataProduct}")
    #
    #         if "sku" in dataProduct:
    #           currentSku = dataProduct["sku"]
    #
    #         if currentSku in translationMap:
    #           dataProduct["sku"] = translationMap[currentSku]
    #
    #         print("Updated object " + str(dataProduct))
    #         upsertData(dataProduct)
    #
    #
    #     type_code = "P"
    #     print("starting data migration for Type Code " + type_code)
    #     base_url = "fbu-qa.pricefx.eu"
    #     partition = "iplex-dev"
    #     url = "https://" + base_url + "/pricefx/" + partition + "/fetch/" + type_code
    #
    #     payload = {
    #       "endRow": 20,
    #       "operationType": "fetch",
    #       "startRow": 0,
    #       "textMatchStyle": "exact"
    #     }
    #
    #     headers = {"Content-Type": "application/json"}
    #     print(f"fetching all {type_code} from partition {partition}")
    #     response = requests.post(url, json=payload, headers=headers, auth=('iplex-dev/sm.hasan', 'start123'))
    #     # // try catch exceptaion handeling
    #     Products = response.json()["response"]["data"]
    #     ProductIDs = []
    #     for obj in Products:
    #       ProductIDs.append(obj["typedId"])
    #
    #     print("Fetched typedIds" + str(ProductIDs))
    #     updateSKU(ProductIDs)
    #
    #
    #     # print('Hello, Python!')
    #     # print('This message will be written to a file.')
    #     # # Reset the standard output
    #     sys.stdout = original_stdout
