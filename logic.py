import time
import os

scanning = True
watched_dir = os.path.expanduser('~/Downloads')
scan_interval = 5

while scanning:
    count = 0
    print('scanning')
    for filename in os.listdir(watched_dir):
        if filename.endswith('.AppImage'):
            filepath = os.path.join(watched_dir, filename)
            # LOGIC HERE
            print('File found: ', filename)
            count += 1

    if count > 0:
        print('> Found ', count, " files.")
        scanning = False
    else:
        time.sleep(scan_interval)
        print('No files found')
        print()
