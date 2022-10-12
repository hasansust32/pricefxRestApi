
import sys

# Saving the reference of the standard output
original_stdout = sys.stdout

with open('02.UpdateQuotefile.txt', 'a') as f:
    sys.stdout = f

    import requests
    def upsertData(payload):
      if "customerId" in payload:
          import requests

          base_url = "companynode.pricefx.eu"
          partition = "companypartition"
          url = "https://" + base_url + "/pricefx/" + partition + "/quotemanager.save"

          payload = {
              "data": {
                  "customerId": payload["customerId"],
                  "typedId": payload["typedId"]

              }
          }

          # payload = {
          #     "data": {
          #         "quote": {
          #             "version": 5,
          #             "typedId": "2147491342.Q",
          #             "uniqueName": "P-2147491340-REV-2",
          #             "label": "Quote01",
          #             "targetDate": "2021-11-01",
          #             "workflowStatus": "DRAFT",
          #             "headerText": "<p>Quote message.</p>",
          #             "inputs": [
          #                 {
          #                     "name": "Customer",
          #                     "label": "Customer",
          #                     "lookupTableId": None,
          #                     "url": "/fetch/C/",
          #                     "type": "CUSTOMER",
          #                     "value": "00003",
          #                     "valueHint": "Kate Smith",
          #                     "readOnly": None,
          #                     "filter": None,
          #                     "parameterGroup": None,
          #                     "required": None,
          #                     "labelTranslations": None,
          #                     "addUnknownValues": None,
          #                     "typedId": None,
          #                     "alwaysEditable": None,
          #                     "inputs": [],
          #                     "parameterConfig": {},
          #                     "formattingOptions": {},
          #                     "valueOptions": None
          #                 }
          #             ],
          #             "viewState": {
          #                 "gridViewState": None,
          #                 "openFolders": None,
          #                 "selectedNodes": [
          #                     "0pnOfOZ0RNyO8LA",
          #                     "n0MnhY2gThX7adD",
          #                     "IZpgAGs8pCAxG2p"
          #                 ]
          #             },
          #             "outputs": [],
          #             "lastUpdateByName": "root",
          #             "createdByName": "admin",
          #             "submittedByName": "admin",
          #             "calculationStatus": 0,
          #             "dirty": False,
          #             "refreshInputs": False,
          #             "nodeId": None,
          #             "userGroupEdit": None,
          #             "userGroupViewDetails": None,
          #             "serverMessages": None,
          #             "additionalInfo1": None,
          #             "additionalInfo2": None,
          #             "additionalInfo3": None,
          #             "additionalInfo4": None,
          #             "numberOfAttachments": 0,
          #             "creationWorkflowStatus": None,
          #             "creationWorkflowCurrentStep": None,
          #             "creationWorkflowStepCount": None,
          #             "creationWorkflowStepLabel": None,
          #             "signature": None,
          #             "lineItems": [
          #                 {
          #                     "version": 3,
          #                     "typedId": "2147515659.QLI",
          #                     "clicId": 2147491342,
          #                     "inputs": [],
          #                     "outputs": [
          #                         {
          #                             "resultName": "price",
          #                             "resultLabel": "Price",
          #                             "result": 666,
          #                             "excludeFromExport": False,
          #                             "warnings": None,
          #                             "alertMessage": None,
          #                             "alertType": None,
          #                             "displayOptions": 2,
          #                             "formatType": "INTEGER",
          #                             "suffix": None,
          #                             "resultType": "SIMPLE",
          #                             "cssProperties": None,
          #                             "userGroup": None,
          #                             "resultGroup": None,
          #                             "overrideValueOptions": None,
          #                             "overrideAllowEmpty": True,
          #                             "labelTranslations": None,
          #                             "overridable": False,
          #                             "overridden": False,
          #                             "resultDescription": None
          #                         }
          #                     ],
          #                     "dirty": False,
          #                     "lineId": "0pnOfOZ0RNyO8LA",
          #                     "parentId": None,
          #                     "calculationStatus": 0,
          #                     "editabilityStatus": 0,
          #                     "label": "Label One",
          #                     "sku": "11111",
          #                     "priceRecordId": None,
          #                     "folder": False,
          #                     "treeLabel": "Label One",
          #                     "createDate": "2021-11-02T09:12:58",
          #                     "createdBy": 2147490696,
          #                     "lastUpdateDate": "2021-11-02T09:12:58",
          #                     "lastUpdateBy": 1
          #                 },
          #                 {
          #                     "version": 3,
          #                     "typedId": "2147515660.QLI",
          #                     "clicId": 2147491342,
          #                     "inputs": [],
          #                     "outputs": [
          #                         {
          #                             "resultName": "price",
          #                             "resultLabel": "Price",
          #                             "result": 666,
          #                             "excludeFromExport": False,
          #                             "warnings": None,
          #                             "alertMessage": None,
          #                             "alertType": None,
          #                             "displayOptions": 2,
          #                             "formatType": "INTEGER",
          #                             "suffix": None,
          #                             "resultType": "SIMPLE",
          #                             "cssProperties": None,
          #                             "userGroup": None,
          #                             "resultGroup": None,
          #                             "overrideValueOptions": None,
          #                             "overrideAllowEmpty": True,
          #                             "labelTranslations": None,
          #                             "overridable": False,
          #                             "overridden": False,
          #                             "resultDescription": None
          #                         }
          #                     ],
          #                     "dirty": False,
          #                     "lineId": "n0MnhY2gThX7adD",
          #                     "parentId": None,
          #                     "calculationStatus": 0,
          #                     "editabilityStatus": 0,
          #                     "label": "Label Two",
          #                     "sku": "22222",
          #                     "priceRecordId": None,
          #                     "folder": False,
          #                     "treeLabel": "Label Two",
          #                     "createDate": "2021-11-02T09:12:58",
          #                     "createdBy": 2147490696,
          #                     "lastUpdateDate": "2021-11-02T09:12:58",
          #                     "lastUpdateBy": 1
          #                 },
          #                 {
          #                     "version": 3,
          #                     "typedId": "2147515661.QLI",
          #                     "clicId": 2147491342,
          #                     "inputs": [],
          #                     "outputs": [
          #                         {
          #                             "resultName": "price",
          #                             "resultLabel": "Price",
          #                             "result": 666,
          #                             "excludeFromExport": False,
          #                             "warnings": None,
          #                             "alertMessage": None,
          #                             "alertType": None,
          #                             "displayOptions": 2,
          #                             "formatType": "INTEGER",
          #                             "suffix": None,
          #                             "resultType": "SIMPLE",
          #                             "cssProperties": None,
          #                             "userGroup": None,
          #                             "resultGroup": None,
          #                             "overrideValueOptions": None,
          #                             "overrideAllowEmpty": True,
          #                             "labelTranslations": None,
          #                             "overridable": False,
          #                             "overridden": False,
          #                             "resultDescription": None
          #                         }
          #                     ],
          #                     "dirty": False,
          #                     "lineId": "IZpgAGs8pCAxG2p",
          #                     "parentId": None,
          #                     "calculationStatus": 0,
          #                     "editabilityStatus": 0,
          #                     "label": "Label Three",
          #                     "sku": "33333",
          #                     "priceRecordId": None,
          #                     "folder": False,
          #                     "treeLabel": "Label Three",
          #                     "createDate": "2021-11-02T09:12:58",
          #                     "createdBy": 2147490696,
          #                     "lastUpdateDate": "2021-11-02T09:12:58",
          #                     "lastUpdateBy": 1
          #                 }
          #             ],
          #             "expiryDate": "2021-11-01",
          #             "externalRef": None,
          #             "customerId": "00003",
          #             "customerName": None,
          #             "customerGroup": None,
          #             "quoteStatus": "DRAFT",
          #             "renderInfo": None,
          #             "serverMessagesExtended": None,
          #             "approvalRequiredEmailAttachmentsJson": None,
          #             "hasWorkflowHistory": False,
          #             "approvedByName": None,
          #             "deniedByName": None,
          #             "createDate": "2021-11-01T17:20:17",
          #             "createdBy": 2147490696,
          #             "lastUpdateDate": "2021-11-02T09:12:58",
          #             "lastUpdateBy": 1,
          #             "supersededBy": None,
          #             "prevRev": "P-2147491340",
          #             "rootUniqueName": "P-2147491340",
          #             "quoteType": None,
          #             "status": "DRAFT"
          #         }
          #     }
          # }

          headers = {"Content-Type": "application/json"}
          print(f"Object update request payload {payload}")

          response = requests.post(url, json=payload, headers=headers, auth=('demo_ark_solutions/sm.hasan', 'smhasan123!'))

          data = response.json()
          print(data)



    def updateQuote(idList):
      for id in idList:

        # myID = id.split(".")[0]

        QuoteTranslationMap = {
          "CID-0017": "Hasan-0017",
          "CID-0011": "Hasan-0011",
          "CID-0039": "Hasan-0039",
          "CID-0040": "Hasan-0040",
          "CID-0041": "Hasan-0041",
          "CID-0046": "Hasan-0046"

        }

        # type_code = "Q"

        base_url = "demo-eu.demo1.pricefx.com"
        partition = "demo_ark_solutions"
        url = "https://" + base_url + "/pricefx/" + partition + "/quotemanager.fetch/" + id

        response = requests.post(url, auth=('demo_ark_solutions/sm.hasan', 'smhasan123!'))

        data = response.json()
        print(data)


        QuoteRecords = response.json()["response"]["data"][0]
        print(f"Fetched object {QuoteRecords}")

        if "customerId" in QuoteRecords:
          currentQuote = QuoteRecords["customerId"]

        if currentQuote in QuoteTranslationMap:
          QuoteRecords["customerId"] = QuoteTranslationMap[currentQuote]

        print("Updated object " + str(Customers))
        upsertData(Customers)



    base_url = "demo-eu.demo1.pricefx.com"
    partition = "demo_ark_solutions"
    url = "https://" + base_url + "/pricefx/" + partition + "/quotemanager.fetchlist"

    payload = {
        "endRow": 300,
        "oldValues": None,
        "operationType": "fetch",
        "startRow": 0,
        "textMatchStyle": "exact",
        "data": {
            "_constructor": "AdvancedCriteria",
            "operator": "and",
            "criteria": [
                {
                    "fieldName": "quoteStatus",
                    "operator": "equals",
                    "value": "DEAL"
                }
            ]
        }
    }

    headers = {"Content-Type": "application/json"}
    # print(f"fetching all {type_code} from partition {partition}")


    response = requests.post(url, json=payload, headers=headers, auth=('demo_ark_solutions/sm.hasan', 'smhasan123!'))
    # // try catch exceptaion handeling

    Customers = response.json()["response"]["data"]
    customerIds = []
    for obj in Customers:
      customerIds.append(obj["typedId"])

    print("Fetched typedIds" + str(customerIds))
    updateQuote(customerIds)


    # print('Hello, Python!')
    # print('This message will be written to a file.')
    # # Reset the standard output
    sys.stdout = original_stdout


