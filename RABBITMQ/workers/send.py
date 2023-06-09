import pika
import sys

# connect to local host
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

# create channel
channel = connection.channel()

# declaring a queue
channel.queue_declare(queue='task_queue', durable=True)

message=''.join(sys.argv[1:]) or 'hello world!'
channel.basic_publish(exchange="",
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2
                      )
                      )

print(f"message sent! {message}")

connection.close()
