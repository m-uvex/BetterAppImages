import time
import os

scanning = True
watched_dir = os.path.expanduser('~/Downloads')
scan_interval = 3
max_tries = 3

files = []
tries = 0

if scanning:
    print('Scanning...\n')

while scanning:
    for filename in os.listdir(watched_dir):
        if filename.endswith('.AppImage'):
            filepath = os.path.join(watched_dir, filename)
            found_file = filename
            files.append(filename)
            files.sort()

    if files:
        scanning = False
        print('> Found', len(files), 'files.')
        for i, filename in enumerate(files, 1):
            print(f'{i}  -  {filename}')

        print('\nFiles to setup (eg: 1 2 3, 1-3 or all)')
        target = input()
        
    elif tries >= max_tries:
        if len(files) < 1:
            scanning = False
            tries = 0
            confirmation = input('No files found, rescan? [y/n] ')
            if confirmation.lower() in ["y", "yes", ""]:
                scanning = True
                print('\nScanning...\n')
            else: exit()

    elif tries < max_tries:
        tries += 1
        time.sleep(scan_interval)