import time
import copy
import requests
from pymongo import MongoClient
import json

key = ''
areaCode =3
# url = f"https://100lifeplan.fss.or.kr/openapi/api/psCorpList.json?key={key}&year={year}&quarter={quarter}&areaCode={areaCode}"


## 2019-4Q data set
year = 2019
quarter = 4

url = f"https://100lifeplan.fss.or.kr/openapi/api/psProdList.json?key={key}&year={year}&quarter={quarter}"

data = ''
data_list =[]

response = requests.get(url)
time.sleep(1)

if response.status_code ==200:
    data = response.json()
    data_list = copy.deepcopy(data)


## MongoDB 2019-4Q

HOST = 'cluster0.o1n9upq.mongodb.net'
USER = 'Codestates_Jihye'
PASSWORD = '1234'
DATABASE_NAME = "Financial_Supervisory_Service_Pension"
COLLECTION_NAME = "2019_4Q"
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]
collection.insert_one(data_list)
# collection.insert_one(response.json())
# parsed_data = json.loads(response.text)
# collection.insert_one(list(parsed_data['list']))





## 2022-3Q data set
year = 2022
quarter = 3

url = f"https://100lifeplan.fss.or.kr/openapi/api/psProdList.json?key={key}&year={year}&quarter={quarter}"

data = ''
data_list =[]

response = requests.get(url)
time.sleep(1)

if response.status_code ==200:
    data = response.json()
    data_list = copy.deepcopy(data)

## MongoDB 2022-3Q

COLLECTION_NAME = "2022_3Q"

client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]
# collection.insert_many(data_list)
collection.insert_one(response.json())
# parsed_data = json.loads(response.text)
# collection.insert_one(parsed_data['list'])

