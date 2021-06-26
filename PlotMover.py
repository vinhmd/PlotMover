#! python
# -*- encoding: utf-8 -*-
#

from pathlib import Path
from time import sleep
from datetime import datetime
import shutil
import signal
import sys
import os

################################################## Global vars
StartTime = datetime.now()


################################################## Mover settings
ScanInterval = 60   # Scan interval in second
PlotSize = 108797952330 # MadMax plot's size in bytes

# Where to scan for plots
TargetDirs = [
    '/mnt/ssd1',
    '/mnt/ssd2'
]

# Where will plots be moved
DestDirs = [
    '/mnt/usb1',
    '/mnt/usb2'
]


################################################## Function to catch ctrl-c
# Handle ctr-c
def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C!')
    RunTime()
    exit()



################################################## Function Run timme
def RunTime():
    print('\nRun in', datetime.now() - StartTime)


################################################## Function Scan for new plots
def ScanNewPlot(ScanDirs):
    Plots = []
    for d in ScanDirs:
        d = Path(d)
        for f in os.listdir(d):
            if f.endswith('.plot'):
                Plots.append(Path.joinpath(d, f))
    return Plots


################################################## Function Calculate number of plots base on Dest free space
def CalPlot(Dest, PlotSize):
    DiskTatol, DiskUsed, DiskFree = shutil.disk_usage(Dest)
    return int(DiskFree/PlotSize)


################################################## Function Selct a dest for moving
def FindDest(Dests):
    while len(Dests):
        d = Path(Dests[0])
        try:
            PlotAvailable = CalPlot(d, PlotSize)
            if PlotAvailable > 1: 
                return d

            if PlotAvailable == 1:
                Dests.remove(d)
                return d

            Dests.remove(d)

        except FileNotFoundError:
            print(d, 'does not exist')
            Dests.remove(d)
    
    print('There is no suitable destination')
    RunTime()
    exit()


################################################## Main function
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    # Check TargetDirs
    i = 0
    while len(TargetDirs) > 0:
        d = TargetDirs[i]
        if not os.path.isdir(d):
            print(d, 'does not exist')
            TargetDirs.remove(d)
        else:
            i += 1
            if i == len(TargetDirs):
                break
    
    if not TargetDirs:
        print('No valid target to monitor')
        exit()

    # Check dest
    i = 0
    while len(DestDirs):
        d = DestDirs[i]
        try:
            PlotAvailable = CalPlot(d, PlotSize)
            if PlotAvailable: 
                print(f'{d}: {PlotAvailable} plots available')
                i += 1
            else:
                DestDirs.remove(d)

        except FileNotFoundError:
            print(d, 'does not exist')
            DestDirs.remove(d)
        
        if i == len(DestDirs):
            break
    
    # Scan and move plot
    while True:
        if not DestDirs:
            print('There is no suitable destination left')
            RunTime()
            exit()

        Plots = ScanNewPlot(TargetDirs)
        if Plots:
            print(f'{datetime.now()}: Found {len(Plots)} new plot(s)')
            for Plot in Plots:
                SeletectedDest = FindDest(DestDirs)
                NewPlot = Path.joinpath(SeletectedDest, Plot.name)
                print(f'{datetime.now()}: Moving {Plot} to {NewPlot}')
                shutil.move(Plot, NewPlot)
                print(f'{datetime.now()}: Finished moving')

            continue
        else:
            sleep(ScanInterval)

    RunTime()
