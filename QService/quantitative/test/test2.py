#coding=utf-8
import Queue
import threading
import time

queue = Queue.Queue()


class ThreadNum(threading.Thread):
    """没打印一个数字等待1秒，并发打印10个数字需要多少秒？"""

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # 消费者端，从队列中获取num
            num = self.queue.get()
            print"i'm num %s" % (num)
            time.sleep(1)
            # 在完成这项工作之后，使用 queue.task_done() 函数向任务已经完成的队列发送一个信号
            self.queue.task_done()


start = time.time()


def main():
    # 产生一个 threads pool, 并把消息传递给thread函数进行处理，这里开启10个并发
    for i in range(10):
        t = ThreadNum(queue)
        t.setDaemon(True)
        t.start()

    # 往队列中填错数据
    for num in range(10):
        queue.put(num)
    # wait on the queue until everything has been processed
    queue.join()


main()
print"Elapsed Time: %s" % (time.time() - start)