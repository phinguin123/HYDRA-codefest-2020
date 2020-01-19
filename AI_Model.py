import urllib3, requests, json
import pandas as pd

# Paste your Watson Machine Learning service apikey here
# Use the rest of the code sample as written
apikey = "pq-Tq-JJLys6T9sHoV45PBOFFibJbmO3XwZg0FIgyHbJ"

#url = 'traffic_level.csv'
#df = pd.read_csv(url, sep=',')

# Get an IAM token from IBM Cloud
url     = "https://iam.bluemix.net/oidc/token"
headers = { "Content-Type" : "application/x-www-form-urlencoded" }
data    = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
print("data:",data)
IBM_cloud_IAM_uid = "bx"
IBM_cloud_IAM_pwd = "bx"
response  = requests.post( url, headers=headers, data=data, auth=( IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd ) )
iam_token = response.json()["access_token"]
ml_instance_id = "962d4e59-b1b1-4868-bef0-15a6b1cf1b70"

# NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation	
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": ["time", "number of cars"], "values": [[10,8]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v4/deployments/bab186a3-d4e4-4879-9f49-c92b4c19a611/predictions', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))