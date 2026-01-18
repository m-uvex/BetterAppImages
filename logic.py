import time
import os

watched_dir = os.path.expanduser('~/Downloads')
scan_interval = 1

while True:
    print('scanning')
    for filename in os.listdir(watched_dir):
        if filename.endswith('.AppImage'):
            filepath = os.path.join(watched_dir, filename)
            # LOGIC HERE
            print('File found: ', filename)

    time.sleep(scan_interval)
