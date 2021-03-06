#Need to install requests package for python
#sudo easy_install requests
#Need sys to pipe print statements to temp file to manipulate strings
import requests
import sys
import math
 
# Set the request parameters
incidents = 100
url = 'https://dev14710.service-now.com/api/now/table/incident?sysparm_limit='+str(incidents)
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
 
# Decode the JSON response into a dictionary and use the data. Also moves text to a temp file
#sys.stdout = open('temp.txt','w')
#print('Status:',response.status_code,'\n')
#print('Headers:',response.headers,'\n')
#print('Response:',response.json(),'\n')
#print('Cookies', response.cookies,)
#sys.stdout.close()

for i in range(incidents):
   # Extract create time
   time_created = 'Created on: ' + response.json()['result'][i]['sys_created_on']
   print(time_created)

   # Extract incident No.
   incident_No = 'Incident No.: ' + response.json()['result'][i]['number']
   print(incident_No)

   # Extract short description
   description = 'Description: ' + response.json()['result'][i]['short_description']
   print(description)

   # Extract caller information
   caller_info = 'Caller ID: ' + response.json()['result'][i]['caller_id']['value']
   print(caller_info)

   # Extract responded date/time
   responded_date = 'Responded by WhiteBoard at: ' + response.json()['result'][i]['opened_at']
   print(responded_date)

   # Extract resolved date/time
   resolved_date = 'Resolved at: ' + response.json()['result'][i]['resolved_at']
   print(resolved_date)

   crit = int(response.json()['result'][i]['priority']) + int(response.json()['result'][i]['impact'])
   crit = ((crit/8)*5)
   print (math.ceil(crit))
   print('\n')

