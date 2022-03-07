import requests
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=test&language=english&route=p&numbers=7021358802"
headers = {
    'authorization': "uUKHPVEWb72gRafi4pG1kTyXBNS6dDslJIn3vLMhACoqQ8YZzjAYzvfKVR06ZP5sbtErBJTOLhQGkU2F",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)