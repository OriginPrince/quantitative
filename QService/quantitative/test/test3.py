#coding=utf-8
import threading
import time
import random
from Queue import Queue

queue = Queue(10)


class ProducerThread1(threading.Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print "Produced1", num
            time.sleep(random.random())

class ProducerThread2(threading.Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print "Produced2", num
            time.sleep(random.random())

class ConsumerThread(threading.Thread):
    def run(self):
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print "Consumed", num
            time.sleep(random.random())


ProducerThread1().start()
ProducerThread2().start()
ConsumerThread().start()