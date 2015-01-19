import time
from threading import Thread, Lock

l = Lock()
def myfunc(i):
    l.acquire()
    print "sleeping 5 sec from thread %d" % i
    time.sleep(5)
    print "finished sleeping from thread %d" % i
    l.release()

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()
