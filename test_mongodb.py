from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://divymakwana23_db_user:admin123@cluster0.jvbjxwf.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

print("\nDatabases:")
print(client.list_database_names())

db = client["KANYEWEST"]
collection = db["NetworkData"]

print("\nCollections:")
print(db.list_collection_names())

print("\nFirst 5 documents:")
for document in collection.find().limit(5):
    print(document)

print("\nTotal documents:", collection.count_documents({}))