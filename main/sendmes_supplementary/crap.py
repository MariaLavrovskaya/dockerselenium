import csv
import sys
import pika
from multiprocessing import Pool
import sendmes
import multiprocessing


import time


def callback(ch, method, properties, body):
    print(" [x] Current process %r Received %r" % (multiprocessing.current_process(), body))
    with open('../file.csv', newline='') as f:
        reader = csv.reader(f)
        messages = list(reader)
        for every_message in messages:
            for word in every_message:
                with open('test6.csv', 'a') as file:
                    writer = csv.writer(file)
                    writer.writerow()
                    writer.writerow(multiprocessing.current_process().name, body)

    #time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def callback_1(links):
    for link in links:
        print(multiprocessing.current_process().name)
        with open('test6.csv', 'a') as file:
            writer=csv.writer(file)
            writer.writerow(link)




def consume():
    workers = 4
    pool =Pool(processes = workers)

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='message_hello', durable = True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_qos(prefetch_count=1)
    with pool as p:
        p.apply_async(channel.basic_consume(queue='message_hello', on_message_callback=callback))
    channel.start_consuming()





if __name__ == '__main__':
    links = []
    with open('../file.csv', newline='') as f:
        reader = csv.reader(f)
        messages = list(reader)
        for every_message in messages:
            for word in every_message:
                links.append(word)
    pool = Pool(4)
    pool.map(callback_1, links)
    pool.close()
    pool.join()





