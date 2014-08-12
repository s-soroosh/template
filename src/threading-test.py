from Queue import Queue
from threading import Thread, Lock
from time import sleep
import logging


__author__ = 'soroosh'
import sys
import random


logging.basicConfig(level=logging.INFO)

params = sys.argv[1:]
print params
producer_count = params[0]
consumer_count = params[1]

q = Queue(maxsize=1000)
produced = 0


def produce_random_numbers(q, p):
    for i in range(1000):
        p = p + 1
        v = random.randint(0, 1000)
        logging.info('%s produced ' % v)
        q.put(v)


def consume_random_numbers(q):
    for i in range(1000):
        item = q.get()
        logging.info('%s consumed' % (item))


def monitor(q, p):
    for i in range(1):
        sleep(3)
        logging.info("Queue current size: %s max: %s" % (q.qsize(), q.maxsize))


producer_threads = [Thread(target=consume_random_numbers, args=(q,), name='thread-' + str(i)) for i in range(1, 2)]
map(lambda t: t.start(), producer_threads)
consumer_threads = [Thread(target=produce_random_numbers, args=(q, produced), name='thread-' + str(i)) for i in range(1, 2)]
map(lambda t: t.start(), consumer_threads)
monitor_thread = Thread(target=monitor, args=(q, produced), name='thread-monitor')
monitor_thread.start()

# map(lambda t: t.join(), consumer_threads)
# sleep(10)

l = Lock()




