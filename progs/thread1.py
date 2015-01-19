#! /usr/bin/python
import time
from threading import Lock, Thread

lock = Lock()
class CreateListThread(Thread):
    def run(self):
        self.entries = []
        for i in range(10):
            time.sleep(1)
            self.entries.append(i)
        lock.acquire()
        print self.entries
        lock.release()

def use_create_list_thread():
    for i in range(3):
        t = CreateListThread()
        t.start()

use_create_list_thread()
