import watchdog.events
import watchdog.observers
import time
import requests
import os
from pathlib import Path


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.txt'],
                                                             ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        print("Watchdog received created event - % s." % event.src_path)
        # Event is created, you can process it now

    def on_modified(self, event):
        print("Watchdog received modified event - % s." % event.src_path)
        # Event is modified, you can process it now

        # login log file path --> /var/log/auth.log
        f = open("loginlog.txt", "r")
        # print(f.readline()) 
        data = f.readline()
        print('data -->',data)


        message = data[0:]
        n = 1


        url = "https://www.fast2sms.com/dev/bulk"

        payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers=7021358802"
        headers = {
            'authorization': "uUKHPVEWb72gRafi4pG1kTyXBNS6dDslJIn3vLMhACoqQ8YZzjAYzvfKVR06ZP5sbtErBJTOLhQGkU2F",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
        }
        if n == 1:

            response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)


if __name__ == "__main__":
    src_path = r"/var/log/auth.log"
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
