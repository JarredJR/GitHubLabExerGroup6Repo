from pymongo import MongoClient
import pprint
import re

client = MongoClient("mongodb://localhost:27017/")

db = client["chinook"]
customers_collection = db["customers"]

print("All documents in 'customers' collection:\n")
for all_doc in customers_collection.find():
    print(all_doc)

print("\nOnly LastName and FirstName:\n")
for rec in customers_collection.find({}, {"_id": 0, "LastName": 1, "FirstName": 1}):
    print(rec)

print("\nCustomers with LastName starting with 'G':\n")
rgx = re.compile('^G.*?$', re.IGNORECASE) 
cursor = customers_collection.find({"LastName": rgx})

num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()

print("# of documents found: " + str(num_docs))

client.close()
