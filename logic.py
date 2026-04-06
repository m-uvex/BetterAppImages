#!/usr/bin/env python3
import time
import os
import subprocess

# --- Config ---
watched_dir = os.path.expanduser('~/Downloads')      # folder to scan
destination = os.path.expanduser('~/.local/bin/appimages')  # where AppImages get moved
desktop_path = os.path.expanduser('~/.local/share/applications')  # where .desktop files go
icon_path = os.path.expanduser('/usr/share/icons')

scanning = True
found_files = []
bar = [
    "Scanning for files [=     ]",
    "Scanning for files [ =    ]",
    "Scanning for files [  =   ]",
    "Scanning for files [   =  ]",
    "Scanning for files [    = ]",
    "Scanning for files [     =]",
    "Scanning for files [    = ]",
    "Scanning for files [   =  ]",
    "Scanning for files [  =   ]",
    "Scanning for files [ =    ]",
]
i = 0

try:
    os.system('clear')

    while scanning:
        print(bar[i % len(bar)], end="\r")
        time.sleep(0.2)
        i += 1

        if i % 5 == 0:
            # scan watched_dir for AppImages, avoid duplicates
            for filename in os.listdir(watched_dir):
                if filename.endswith('.AppImage'):
                    if filename not in found_files:
                        found_files.append(filename)
            found_files.sort()

            if found_files:
                scanning = False
                os.system('clear')

                if len(found_files) == 1:
                    print(f'> Found 1 AppImage: {found_files[0]}')
                    target = input('\nInstall it? (r to rescan, ^C to exit) [y/n]\n> ').strip().lower()
                    if target in ['', 'y', 'yes']:
                        target = '1'
                else:
                    print('> Found', len(found_files), 'AppImages.')
                    for i, filename in enumerate(found_files, 1):
                        print(f'{i}  →  {filename}')
                    target = input('\nFile to install? (r to rescan, ^C to exit)\n> ').strip().lower()

                # Rescan
                if target == 'r':
                    found_files = []
                    scanning = True
                    i = 0
                    os.system('clear')
                
                # Install logic
                elif target == '' or target.isdigit():

                    os.system('clear')

                    if target == '': target = '1'
                    index = int(target) - 1
                    target_file = found_files[index]
                    target_file_path = f'{watched_dir}/{target_file}'
                    if not os.path.exists(destination): os.makedirs(destination)
                    
                    print('Moving file...  ', end='\r')
                    os.rename(target_file_path, f'{destination}/{target_file}')
                    print('Setting permissions...', end='\r')
                    os.chmod(f'{destination}/{target_file}', 0o755)
                    print(f'✓ Done: ', f'{destination}/{target_file}')


except KeyboardInterrupt:
    print('\nExiting...')