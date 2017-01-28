#Need to install requests package for python
#sudo easy_install requests
#Need sys to pipe print statements to temp file to manipulate strings
import requests
import sys
 
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
 
# Decode the JSON response into a dictionary and use the data. Also moves text to a temp file
sys.stdout = open('temp.txt','w')
print('Status:',response.status_code,'\n')
print('Headers:',response.headers,'\n')
print('Response:',response.json(),'\n')
print('Cookies', response.cookies,)
sys.stdout.close()

# Extract create time
time_created = 

# Extract incident No.
#incident_No = 

# Extract short description
#description =

# Extract caller information
#caller_info = 

# Extract responded date/time
#responded_date = 

# Extract resolved date/time
#resolved_date = 
