import pika

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)


def callback(body):
    print("Received message:", body.decode())


# Set the callback function to consume messages
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
connection.close()
