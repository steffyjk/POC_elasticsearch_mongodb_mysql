import pika, sys, os
import time


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    print(' [*] Waiting for message. To exit press ctrl+c')

    def callback(ch, method, properties, body):

        print(" [x] Received %r" % body.decode())
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    try:
        channel.start_consuming()
    except Exception as e:
        print("----------", e)


if __name__ == '__main__':
    main()
