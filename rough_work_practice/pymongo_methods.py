import pymongo

# BASIC MONGODB --> DATABASE --> COLLECTION --> datas

client = pymongo.MongoClient("mongodb://localhost:27017/")

# CREATE NEW DATABASE
db = client['books_db']

# list all database of MONGODB
all_database_names = client.list_database_names()
# print(all_database_names)

# delete particular database
# client.drop_database("DATABASE_NAME")

# CREATE COLLECTION INSIDE DATABASE
# collection = db['book-collection']

# LETS INSERT DATA INSIDE COLLECTION
import datetime

# post = {
#     "author": "steffy",
#     "text": "My second blog post!",
#     "tags": ["flask", "python", "pymongo"],
#     "date": datetime.datetime.now(datetime.timezone.utc),
# }
# #
#
# posts = db.posts # this going to create posts collection inside our database
# post_id = posts.insert_one(post).inserted_id # this going to insert post into posts collection
# print(post_id)

# print(db.list_collection_names())

users = db.users
# insertion = users.insert_many(
#     [
#         {"name": "steffy",
#          "number": 1,
#          "field": "python"
#          },
#         {"name": "stella",
#          "number": 2,
#          "field": "python"
#          },
#     ]
# )
# print(insertion.inserted_ids)
# Empty the collection using delete_many()
# result = users.delete_many({})
# print("Deleted", result.deleted_count, "documents")

print(users.count_documents({}))

# UNIQUE key mandatory
result = db.users.create_index([('number', pymongo.ASCENDING)],
                               unique=True)

# try:
#     users.insert_one({
#         "name":"ginny",
#         "number":2,
#         "field":"python"
#     })
# except Exception as e:
#     print(e)

# PRINTING ALL USERS FROM USERS COLLECTION
for i in users.find([], {"_id": 0}):
    print(i['name'])
