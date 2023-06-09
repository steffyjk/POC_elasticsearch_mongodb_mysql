import pymongo

# make mongo client
client = pymongo.MongoClient("mongodb://localhost:27017/")

# database declaration
db = client['test']

# check for particular collection inside the database
collection = db['movies']

# make one field unique for the entire collection
collection.create_index("title", unique=True)

# insert one data
# insert_data = {
#     "title": "Dellema",
#     "year": 2025,
#     "dehg": 5678
# }

# try:
#     result = collection.insert_one(insert_data)
# except Exception as e:
#     print(e)

# print all data from the collection
documents = collection.find([], {"title": 0})
for document in documents:
    print(document)

# update
# filter = {'title': 'Dellema'}
# update = {'$set': {'title': 'Dellema2'}}
# result = collection.update_one(filter, update)
# print('Modified document count:', result.modified_count)

# delete
# collection.delete_one({"title":"Dellema"})
