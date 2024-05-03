#!/usr/bin/env python3
'''
NoSQL
'''
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('your_mongodb_uri')
db = client['logs']
collection = db['nginx']

# Get total number of logs
total_logs = collection.count_documents({})
print(f"{total_logs} logs")

# Get count each method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\t{method}: {count}")

# Get count of documents with method=GET and path=/status
count_status = collection.count_documents({"method": "GET", "path": "/status"})
print(f"GET /status: {count_status}")
