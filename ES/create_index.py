import os

from elasticsearch import Elasticsearch

# Create an Elasticsearch client object
# Create an Elasticsearch client
es = Elasticsearch(
    hosts=[os.environ.get("es_host")],

)


# Define the index settings and mappings
index_name = 'data_index'
index_settings = {
    'settings': {
        'number_of_shards': 1,
        'number_of_replicas': 0
    },
    'mappings': {
        'properties': {
            'field1': {'type': 'text'},
            'field2': {'type': 'keyword'}
        }
    }
}

# Create the index
es.indices.create(index=index_name, body=index_settings)

# Check if the index was created successfully
if es.indices.exists(index=index_name):
    print(f"Index '{index_name}' created successfully.")
else:
    print(f"Failed to create index '{index_name}'.")
