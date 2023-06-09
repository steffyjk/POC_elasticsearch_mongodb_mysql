import pika, sys, os


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback,
                          auto_ack=True)

    print(' [*] Waiting for message. To exit press ctrl+c')
    try:
        channel.start_consuming()
    except Exception as e:
        print("----------", e)


if __name__ == '__main__':

    main()
