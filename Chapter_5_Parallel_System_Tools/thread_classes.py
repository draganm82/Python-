"""
thread class instances with state and run() for thread's action;
uses higher-level Java-like threading module object join method (not
mutexes or shared global vars) to know when threads are done in main
parent thread; see library manual for more details on threading;
"""
import threading

class Mythread(threading.Thread): #subclass Thread object
    def __init__(self,myiId,count, mutex):
        self.myId = myiId
        self.cout = count       # per-thread state information
        self.mutex = mutex      # shared objects, not globals
        threading.Thread.__init__(self)

    def run(self): # run provides thread logic
       for i in range(self.count): # still sync stdout access
           with self.mutex:
               print('[%s] => %s' % (self.myId, i))
stdoutmutex = threading.Lock()          # same as thread.allocate_lock()
threads =[]
for i in range(10):
    thread = Mythread(i, 100, stdoutmutex)  # make/start 10 threads
    thread.start()   # starts run method in a thread
    threads.append(thread)

for thread in threads:
    thread.join()
print ('Main thread exiting. ')
