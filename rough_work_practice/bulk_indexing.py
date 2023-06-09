from elasticsearch import Elasticsearch
from datetime import datetime

# Create an Elasticsearch client
es = Elasticsearch(
    hosts=["http://localhost:9200"],

)

# Specify the index name
# Define the index settings and mappings
index_name = 'classroom_index'
index_settings = {
    'settings': {
        'number_of_shards': 1,
        'number_of_replicas': 1
    },
    'mappings': {
        'properties': {
            'name': {'type': 'text'},
            'content': {'type': 'text'}
        }
    }
}

# Create the index
es.indices.create(index=index_name, body=index_settings)

# Index the documents

documents = [
    {'_index': "bulk_indexing", '_id': 8, 'name': 'Document 1', 'content': 'Lorem ipsum dolor sit amet.'},
    {'_index': "bulk_indexing", '_id': 9, 'name': 'Document 2', 'content': 'Consectetur adipiscing elit.'},
    {'_index': "bulk_indexing", '_id': 10, 'name': 'Document 3',
     'content': 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'},

]
from elasticsearch.helpers import bulk

# Use the bulk API to index the documents
response = bulk(client=es, actions=documents)

# Check the response for errors
if response[0] != len(documents):
    print('Some documents failed to index.')

# fetch all documents
search_query = {
    "query": {
        "match_all": {}
    }
}

# Search for all documents in the index
response = es.search(index="classroom_index", body=search_query, size=1000)

# Print the documents
for hit in response['hits']['hits']:
    print(hit['_source'])
