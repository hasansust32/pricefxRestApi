import sys

# Saving the reference of the standard output
original_stdout = sys.stdout

with open('01.UpdateCustomerMigration.txt', 'a') as f:
    sys.stdout = f

    import requests
    def upsertData(payload):
      if "customerId" in payload:
        type_code = "C"
        base_url = "fbu-qa.pricefx.eu"
        partition = "iplex-dev"
        url = "https://" + base_url + "/pricefx/" + partition + "/integrate/" + type_code

        payload = {
          "data": {

            "typedId": payload["typedId"],
            "customerId": payload["customerId"]

          }
        }

        headers = {"Content-Type": "application/json"}
        print(f"Object update request payload {payload}")
        response = requests.post(url, json=payload, headers=headers, auth=('iplex-dev/sm.hasan', 'start123'))

        # print response statu
        data = response.json()
        print(data)

    def Migration():
        import csv

        with open("DataSet/Customer Mapping.csv", 'r') as file:
            csvreader = csv.reader(file)
            Migration = {

            }

            for row in csvreader:
                Migration[row[0]] = row[1]

            return (Migration)




    def updateCustomerId(idList):
      for id in idList:
        myID = id.split(".")[0]



        translationMap = Migration()


        type_code = "C"
        base_url = "fbu-qa.pricefx.eu"
        partition = "iplex-dev"
        url = "https://" + base_url + "/pricefx/" + partition + "/fetch/" + type_code + "/" + myID

        print(f"Fetching object {myID}")

        response = requests.post(url, auth=('iplex-dev/sm.hasan', 'start123'))

        AllCustomers = response.json()["response"]["data"][0]
        print(f"Fetched object {AllCustomers}")

        if "customerId" in AllCustomers:
          currentCustomerId = AllCustomers["customerId"]

        if currentCustomerId in translationMap:
          AllCustomers["customerId"] = translationMap[currentCustomerId]

        print("Updated object " + str(AllCustomers))
        upsertData(AllCustomers)


    type_code = "C"
    print("starting data migration for Type Code " + type_code)
    base_url = "fbu-qa.pricefx.eu"
    partition = "iplex-dev"
    url = "https://" + base_url + "/pricefx/" + partition + "/fetch/" + type_code

    payload = {
      "endRow": 1500,
      "operationType": "fetch",
      "startRow": 0,
      "textMatchStyle": "exact"
    }

    headers = {"Content-Type": "application/json"}
    print(f"fetching all {type_code} from partition {partition}")
    response = requests.post(url, json=payload, headers=headers, auth=('iplex-dev/sm.hasan', 'start123'))
    # // try catch exceptaion handeling
    CustomerRecords = response.json()["response"]["data"]
    CustomerIDs = []
    for obj in CustomerRecords:
      CustomerIDs.append(obj["typedId"])

    print("Fetched typedIds" + str(CustomerIDs))
    updateCustomerId(CustomerIDs)


    # print('Hello, Python!')
    # print('This message will be written to a file.')
    # # Reset the standard output
    sys.stdout = original_stdout


