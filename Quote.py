
import sys

# Saving the reference of the standard output
original_stdout = sys.stdout

with open('01.Quote_Report.txt', 'a') as f:
    sys.stdout = f

    import requests

    base_url = "fbu-qa.pricefx.eu"
    partition = "iplex-dev"

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

    response = requests.post(url, json=payload, headers=headers, auth=('iplex-dev/sm.hasan', 'start123'))

    data = response.json()["response"]["data"]

    print(data)


