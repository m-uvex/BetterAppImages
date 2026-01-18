import time
import os

scanning = True
watched_dir = os.path.expanduser('~/Downloads')
scan_interval = 5

print('Scanning...')
print()

while scanning:
    files = []
    for filename in os.listdir(watched_dir):
        if filename.endswith('.AppImage'):
            filepath = os.path.join(watched_dir, filename)
            found_file = filename
            files.append(filename)
            files.sort()

    if files:
        print('> Found', len(files), 'files.')
        for i, filename in enumerate(files, 1):
            print(f'{i}  -  {filename}')

        print()
        print('Files to setup (eg: 1 2 3, 1-3 or all)')
        target = input()
        scanning = False
    else:
        time.sleep(scan_interval)
        print('No files found')
        print()
