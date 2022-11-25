import threading, queue, time
def producer(idnum, dataqueue):

def consumer(idnum, dataqueue): 

if __name__ == '__main__':
    for i in range(numconsumers):
        thread = threading.Thread(target=consumer, args=(i, dataQueue))
        thread.daemon = True # else cannot exit!
        thread.start()
    waitfor = []
    for i in range(numproducers):
        thread = threading.Thread(target=producer, args=(i, dataQueue))
        waitfor.append(thread)
        thread.start()
for thread in waitfor: thread.join() # or time.sleep() long enough here
print('Main thread exit.')