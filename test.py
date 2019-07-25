import logging
import traceback
LOG = logging.getLogger("zen.ThreadHunter")

class ThreadFactory(threading.Thread):
    def start(self):
        LOG.info(
            "ThreadFactory.start(): {name: %s, id: %s}\n\nStack:\n%s",
            getattr(self, "name", None),
            id(self),
            "".join(traceback.format_stack()))

        super(ThreadFactory, self).start()
cp 

 class ThreadPool:
     This class (hopefully) generalizes the functionality of a pool of threads
     workers = 0
     name = None
 
     threadFactory = ThreadFactory
     currentThread = staticmethod(threading.currentThread)
     _pool = staticmethod(_pool)