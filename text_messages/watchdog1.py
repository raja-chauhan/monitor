import sys
import time
import logging
import os
# creating an instance of the watchdog.observers.Observer from watchdogs class.
from watchdog.observers import Observer
# implementing a subclass of watchdog.events.FileSystemEventHandler which is LoggingEventHandler in our case
from watchdog.events import LoggingEventHandler


def handleevent():
    print('function called')


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = (r"login_log.txt")
    event_handler = LoggingEventHandler()
    # event_handler = handleevent()
    observer = Observer()
    # Scheduling monitoring of a path with the observer instance and event handler. There is 'recursive=True' because only with it enabled, watchdog.observers.Observer can monitor sub-directories
    observer.schedule(event_handler, path, recursive=True)
    observer.start()  # for starting the observer thread
    try:
        while True:
            # os.system('last > login_log.txt')
            # print("changes")
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
