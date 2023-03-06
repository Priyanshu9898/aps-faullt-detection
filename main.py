import pymongo

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/APS_DB")

# Database Name
dataBase = client["APS_DB"]

# Collection  Name
collection = dataBase['Products']

# Sample data
d = {'companyName': 'Priyanshu Malaviya',
     'product': 'Affordable AI development product',
     'courseOffered': 'Machine Learning with Deployment'}

# Insert above records in the collection
rec = collection.insert_one(d)

# Lets Verify all the record at once present in the record with all the fields
all_record = collection.find()

# Printing all records present in the collection
for idx, record in enumerate(all_record):
     print(f"{idx}: {record}")
