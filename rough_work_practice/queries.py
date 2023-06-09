from elasticsearch import Elasticsearch
from datetime import datetime

# Create an Elasticsearch client
es = Elasticsearch(
    hosts=["http://localhost:9200"],

)

# Specify the index name
index_name = "classroom_index"

# Index the document
# doc = {
#     'name': 'stellajk',
#     'roll_no': 2,
#     'timestamp': datetime.now(),
# }
#
# # Index the document in Elasticsearch
# es.index(index=index_name, document=doc, id=1)

# Define the search query
# query = {
#     "query": {
#         "bool": {
#             "should": [
#                 {"match": {"name": "stellajk"}},
#                 {"match": {"roll_no": "1"}},
#             ]
#         }
#     }
# }

# Execute the search query
# try:
#     response = es.search(index=index_name, body=query)
#
#     # Retrieve the matching documents
#     matches = response["hits"]["hits"]
#
#     # Print the document list
#     for match in matches:
#         print("---")
#         print(match["_source"])
# except Exception as e:
#     print(e)


# Define the search query
# Define the search query
# query = {
#     "query": {
#         "bool": {
#             "must_not": [
#                 {"term": {"name": "steffyjk"}},
#                 # {"range": {"roll_no": {"gte": 0}}
#                 #  }
#                 # Add more query clauses as needed
#             ]
#         }
#     }
# }

# # Define the search query
# query = {
#     "query": {
#         "bool": {
#             "must_not": [
#                 {"term": {"name": "steffyjk"}}
#             ],
#             "should": [
#                 {"term": {"name": "sdf"}},
#                 {"term": {"roll_no": 2}}
#             ],
#             "minimum_should_match": 1
#         }
#     }
# }

# term query
# # Define the search query
# query = {
#     "query": {
#         "term": {
#             "name": "steffyjk"
#         }
#     }
# }
#
# # check the prefix
# # Define the search query
# query = {
#     "query": {
#         "prefix": {
#             "name": "ste"
#         }
#     }
# }
# check the prefix
# Define the search query
query = {
    "query": {
        "wildcard": {
            "name": "*ll*"
        }
    }
}
# Execute the search query
response = es.search(index=index_name, body=query, size=10000)  # Adjust the 'size' parameter as needed

# Retrieve the matching documents
hits = response["hits"]["hits"]

# Check if any documents were found
if len(hits) == 0:
    print("No documents found.")
else:
    # Print the documents
    for hit in hits:
        print(hit["_source"])
