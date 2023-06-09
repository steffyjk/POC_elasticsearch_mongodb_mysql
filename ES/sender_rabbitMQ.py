import pika

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

message = 'Hello, RabbitMQ!'
channel.basic_publish(exchange='', routing_key=queue_name, body=message)
connection.close()
