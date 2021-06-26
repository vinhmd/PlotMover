# PlotMover

## What is this?

Lets say you have one or more SSDs use as final destinations for copying phase (to speedup copying phase), and then you'll move plots to slower HDD or USB.

PlotMover will monitor the plotting's final destinations (TargerDirs) and move plot to HDD/USB (DestDirs) whenever it found new one.

## How to use?

1. Clone or download this project.

2. Edit the Python script `PlotMover.py`. Change `TargerDirs`, `DestDirs` as you want then save it.

   Note: Windows paths should go like this:  'C:\\\Users\\\admin\\\Desktop\\\Dest'

   You can also change `ScanInterval` if you want.

3. Open terminal.

4. Run command:

   ```
   cd PlotMover
   python3 ./PlotMover.py
   
   # On Windows it may go like this:
   python .\PlotMover.py
   ```

   

## How to Support?

XCH: xch1ddscgyr3fpjvxasw0dwqhhxtvxegt286mvwq7l0cekn0qt6pd4ds5m9xrw

ETH: 0x824686b5260cfae9df8a891d351ab10b4bace7a8

BTC: 3Hnvgs23PfSAszsCfLCcn94xKTERT4HFvW