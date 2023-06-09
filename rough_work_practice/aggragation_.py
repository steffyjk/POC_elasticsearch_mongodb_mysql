import pymongo

# BASIC MONGODB --> DATABASE --> COLLECTION --> datas

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['books_db']
users = db.users
# for i in users.find({}):
#     print(i)

# DEFINING THE AGGREGATION PIPELINE
pipeline = [
    {'$match': {'name': 'steffy'}},
    {'$group': {'_id': 'name', 'count': {'$sum': 1}}},
    {'$sort': {'count': -1}},
    {'$limit': 10}
]

result = users.aggregate(pipeline)
for document in result:
    print(document)
