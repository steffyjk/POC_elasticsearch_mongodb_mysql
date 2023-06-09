from elasticsearch import Elasticsearch

# Create an Elasticsearch client
client = Elasticsearch(
    hosts=["http://localhost:9200"],

)

from datetime import datetime

# indexing a document [ create ]
doc = {
    'author': 'steffyjk',
    'text': 'data content...',
    'timestamp': datetime.now(),
}
# resp = client.index(index="document_index", id=1, document=doc)
# print(resp['result'])  # --> it will return CREATED means index created [ UPDATED if already exists ]

# GETTING Document
# try:
#     resp = client.get(index="document_index", id=1)
#     print(resp['_source'])  # --> it will return the dictionary data that we have added as document -> doc
# except Exception as e:  # in case of No found error
#     print(e)

# client.indices.refresh(index="document_index")  # refresh the index

# SEARCHING for a document
# resp = client.search(index="document_index", query={"match_all": {}})
# print("Got %d Hits:" % resp['hits']['total']['value'])
# for hit in resp['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

# UPDATE the document
doc = {
    'author': 'stella',
    'text': 'Interesting modified content...',
    'timestamp': datetime.now(),
}
# try:
#     resp = client.update(index="document_index", id=1, document=doc)
#     print(resp['result'])  # --> result as updated
# except Exception as e:
#     print(e)


# delete the document
# client.delete(index="document_index", id=1)  # --> delete the particular document


# LIST out all indexes
#
# indices = client.cat.indices(format="json")
#
# # Print the list of indices
# # lis=[]
# for index in indices:
#     print(index['index'])


# fetch all documents

