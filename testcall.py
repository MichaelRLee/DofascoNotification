#Need to install requests package for python
 #sudo easy_install requests
import requests
 
# Set the request parameters
url = 'https://dev14710.service-now.com/api/now/table/incident?sysparm_limit=1'
user = 'admin3'
pwd = 'admin3'
 
# Set proper headers
headers = {"Accept":"application/json"}
 
# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )
 
# Check for HTTP codes other than 200
if response.status_code != 200: 
   print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
   exit()
 
# Decode the JSON response into a dictionary and use the data
print('Status:',response.status_code,'Headers:',response.headers,'Response:',response.json())
print('Cookies', response.cookies)
