import os

import pymysql
import pika
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()


def fetch_data_from_mysql():
    """
        Method: fetch data from database & return that
        --> preferred database is MYSQL
        --> additionally used pymysql [ for connection of mysql db ]
    :return: list of rows of particular table data
    """

    # Establish a connection to the MySQL database
    cnx = pymysql.connect(
        host=os.environ.get("host"),
        user=os.environ.get("user"),
        password=os.environ.get("password"),
        database=os.environ.get("database")
    )

    # Create a cursor object to execute SQL queries
    cursor = cnx.cursor()

    # Define the SQL query to fetch all rows from the table
    query = "SELECT * FROM customers"

    # Execute the query
    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()
    data = rows
    # Close the cursor and connection
    cursor.close()
    cnx.close()

    return data


def send_data_to_rabbitmq(mysql_data):
    """
    This function going to take mysql data and send it to the rabbitmq
    :param mysql_data: DATA from mysql data
    :return: status weather data sent successfully or some error
    """

    try:
        # Establish a connection to RabbitMQ server
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ.get("rabbitmq_host")))
        channel = connection.channel()

        # Declare a queue
        queue_name = os.environ.get("rabbitmq_queue_name")
        channel.queue_declare(queue=queue_name)

        # Publish a message to the queue
        row_message = mysql_data
        message_str = str(row_message)  # Convert list to a string
        message = message_str.encode('utf-8')
        channel.basic_publish(exchange='', routing_key=queue_name, body=message)

        # Close the connection
        connection.close()
        return {
            "status": "send data"
        }
    except Exception as e:
        return {
            "status": e
        }


def fetch_data_from_rabbitmq():
    """
        This fucntion going to fetch data from rabbitMQ
        send it to Elasticsearch & save data there.
    :return: Nothing
    """
    # Establish a connection to Elasticsearch
    es = Elasticsearch(hosts=[os.environ.get("es_host")], )

    # Callback function to handle received messages
    def callback(ch, method, properties, body):
        # Process the received message
        print("Received message:", body.decode('utf-8'))
        # Process the received message
        message = body.decode('utf-8')
        print("Received message:", message)

        # Save the message to Elasticsearch
        try:
            es.index(index=os.environ.get("es_index_name"), body={'message': message})
            print("Message saved to Elasticsearch.")
            return None
        except Exception as e:
            print("---> error in es storing", e)

        # Acknowledge the message
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Establish a connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ.get("rabbitmq_host")))
    channel = connection.channel()

    # Declare a queue
    queue_name = os.environ.get("rabbitmq_queue_name")
    channel.queue_declare(queue=queue_name)

    # Start consuming messages from the queue
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    # Print a message to indicate the consumer has started
    print("Consumer started. Waiting for messages...")

    # Start the event loop for consuming messages
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        # Stop consuming messages when Ctrl+C is pressed
        channel.stop_consuming()

        # Close the connection
        connection.close()


def es_fetch_data():
    """
        This function going to fetch data from Elasticsearch
        for provided particular elasticsearch index
    :return: returns the particular fetched documents data
    """
    # Create an Elasticsearch client
    es = Elasticsearch(hosts=[os.environ.get("es_host")], )

    # Specify the index name
    index_name = os.environ.get("es_index_name")

    # Define the search query to fetch all documents
    query = {
        "query": {
            "match_all": {}
        }
    }
    delete_query = {
        "query": {
            "match_all": {}
        }
    }
    # Delete all documents matching the query
    response = es.delete_by_query(index=index_name, body=delete_query)
    # Perform the search request
    response = es.search(index=index_name, body=query, size=10000)

    # Extract the documents from the response
    documents = response['hits']['hits']
    end_data = [document['_source'] for document in documents]
    # Alternatively, if you just want the data without the metadata, you can use:
    data = [document['_source'] for document in documents]
    print(data)
    return end_data


if __name__ == "__main__":
    mysql_data = fetch_data_from_mysql()
    print(mysql_data)
    # Define the column names
    column_names = ['id', 'name', 'email', 'phone']

    # Convert the data into a list of dictionaries
    result1 = [dict(zip(column_names, row)) for row in mysql_data]

    result = send_data_to_rabbitmq(mysql_data=result1)
    print(result)
    if result['status'] == 'send data':
        fetch_data_from_rabbitmq()

    # fetch all data from ES index
    final_es_data = es_fetch_data()
    print(final_es_data)
