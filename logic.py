#!/usr/bin/env python3
import time
import os
import subprocess

scanning = True
watched_dir = os.path.expanduser('~/Downloads')
destination = os.path.expanduser('~/.local/bin/appimages')
desktop_path = os.path.expanduser('~/.local/share/applications')
found_files = []

try:
    print('Scanning...')
    first_try = True
    while scanning:
        
        time.sleep(1)

        for filename in os.listdir(watched_dir):
            if filename.endswith('.AppImage'):
                if filename not in found_files:
                    found_files.append(filename)
        found_files.sort()

        if found_files:
            scanning = False
            print('> Found', len(found_files), 'files.')
            for i, filename in enumerate(found_files, 1):
                print(f'{i}  -  {filename}')

            target = input('\nFile to setup? (r to rescan, ^C to exit)\n> ').strip().lower()

            if target == 'r':
                found_files = []
                scanning = True
                first_try = True
            elif target == '' or target.isdigit():
                if target == '': target = '1'
                index = int(target) - 1
                target_file = found_files[index]
                target_file_path = f'{watched_dir}/{target_file}'
                if not os.path.exists(destination): os.makedirs(destination)
                os.rename(target_file_path, f'{destination}/{target_file}')
                target_file_path = f'{destination}/{target_file}'
                os.chmod(target_file_path, 0o755)
                print(f'✓ Done: {target_file_path}')
        else:
            if first_try:
                print('(^C to exit)\n')
                first_try = False

except KeyboardInterrupt:
    print('\nExiting...')