

import csv
import sys
import pika
import time
from multiprocessing import Pool



def callback(ch, method, properties, body):
    print(" [x] %r received %r" % (multiprocessing.current_process().name, body))
    time.sleep(body.count('.'))
    with open('test.csv', 'w', newline='') as file:
        csv.writer(file)
        writer.writerow(multiprocessing.current_process().name, body)
    # print " [x] Done"
    ch.basic_ack(delivery_tag=method.delivery_tag)

def new_task():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='message_hello', durable = True)
    with open('file.csv', newline='') as f:
        reader = csv.reader(f)
        messages = list(reader)
    for every_message in messages:
        for word in every_message:
            #time.sleep(1)
            channel.basic_publish(exchange='', routing_key='message_hello', body= str(word), properties=pika.BasicProperties(delivery_mode=2,))

        print("[x] Sent %r" %word)
    connection.close()

def worker():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
    channel = connection.channel()
    channel.queue_declare(queue='message_hello', durable = True)
    print(' [*] Waiting for messages. To exit press CTRL+C')


    def callback(ch, method, properties, body):
        print(" [x] %r received %r" % (multiprocessing.current_process().name, body))
        time.sleep(body.count('.'))
        with open('test.csv', 'w', newline='') as file:
            csv.writer(file)
            writer.writerow(multiprocessing.current_process().name, body)
        # print " [x] Done"
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='message_hello', on_message_callback=callback)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        pass

def pool_handler():
    workers = 4
    p = Pool(workers)
    for i in range(0, workers):
        print(i)
        p.apply_async(worker())






