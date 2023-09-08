import requests
import json

response = requests.get("http://api.carbonintensity.org.uk/intensity/date/2023-01-11")

if response.status_code != 200:
    raise Exception(
        "Cannot reach (HTTP {}): {}".format(response.status_code, response.text)
    )
else:
    print(json.dumps(response.json(), indent=2))
