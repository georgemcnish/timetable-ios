# Timetable
This is a timetable intended to be used as a iOS widget paired with [Pythonista 3](http://omz-software.com/pythonista/).
## Installation
1. Place the timetable.py and timetable.pyui in a **local** directory (do not place into iCloud synced folder).
2. Set the script as the today widget in the Pythonista settings.
## Usage
### Subject Population
The subjects are stored within a dictionary which is declared at the start of the code.
```python
timetable = {'MondayA': {'P1': '','P2': '','P3': '','P4': '','P5': ''},
             'TuesdayA': {'P1': '','P2': '','P3': '','P4': '','P5': ''},
             'WednesdayA': {'P1': '','P2': '','P3': '','P4': '','P5': ''},
             'ThursdayA': {'P1': '','P2': '','P3': '','P4': '','P5': ''},
             'FridayA': {'P1': '','P2': '','P3': '','P4': '','P5': ''},
             'MondayB': {'P1': '','P2': '','P3': '','P4': '','P5': ''},
             'TuesdayB': {'P1': '','P2': '','P3': '','P4': '','P5': ''},
             'WednesdayB': {'P1': '','P2': '','P3': '','P4': '','P5': ''},
             'ThursdayB': {'P1': '','P2': '','P3': '','P4': '','P5': ''},
             'FridayB': {'P1': '','P2': '','P3': '','P4': '','P5': ''},
             'SaturdayA': {'P1': '','P2': '','P3': '','P4': '','P5': ''},
             'SaturdayB': {'P1': '','P2': '','P3': '','P4': '','P5': ''},
             'SundayA': {'P1': '','P2': '','P3': '','P4': '','P5': ''},
             'SundayB': {'P1': '','P2': '','P3': '','P4': '','P5': ''}}
```
Currently, the timetable only supports 5 lessons each day and 2 alternating weeks. To populate this dictionary simply fill in the sub dictionaries of each day with the keys of `P1, P2, P3, P4 and P5`. An example day may look like:
```python
'MondayA': {'P1': 'Mathematics','P2': 'Philosophy','P3': 'Computing','P4': 'Study','P5': 'Ethics'}
```
### Alternating Weeks
The timetable supports 2 alternating weeks *Week A and B*. Each day stored in the timetable dictionary is followed by a week identifier e.g: `MondayA`. To alternate between weeks simply change the `week` variable declared at the start of the code. *Currently as of right now, there is no way to automatically alternate between each week due to limitations with iOS software data persistence*.
### Day Timings
The timetable supports 2 types of timings of the day: normal day timings and an alternative day timing. The timings in the code are stored in the `timings` variable which is declared at the start of the code. For most of the school days, the `normal` item is used whereas on a day with alternative timings the `alternative` item is used. The alternative day can be declared in the class initialisation code. An example day timing may look like:
```python
'normal': {'P1': [[8,50],[9,50]],'P2': [[9,53],[10,53]],'P3': [[11,33],[12,33]],'P4': [[13,11],[14,11]],'P5': [[14,14],[15,14]]}
```
Each of the periods timings are stored in each of their respective values. The structure of each periods timing is an array containing 2 arrays, the first being the start time of the period and the second being the end time of the period. Timings **must** be inputted without any leading 0's e.g: `[8, 50]` for 08:50.
### Class Initialisation
The class is initialised in this piece of code:
```python
TT = timetableOutput(timetable, timings, 'Wednesday', "#ffffff", "#000000")
```
1. The timetable dictionary
2. The timings dictionary
3. The day to use for alternative timings
4. The primary colour for the UI
5. The secondary color for the UI
### Updating Colour
To update the colour of the elements as the code is running call `TT.setColour('primary','secondary')` replacing `primary` and `secondary` with [HEX Codes](http://www.color-hex.com/).
#### Example
```python
def rainbowMode():            
    colours = ['#ff3e3e', '#ff703e', '#ffa23e', '#ffd53e', '#f7ff3e', '#c4ff3e', '#92ff3e', '#5fff3e', '#3eff4e',
                '#3eff81', '#3effb3', '#3effe6', '#3ee6ff', '#3eb3ff', '#3e81ff', '#3e4eff', '#5f3eff', '#923eff',
                '#c43eff', '#f73eff', '#ff3ed5', '#ff3ea2', '#ff3e70', '#ff3e3e']            
    for x in range(0, 5):
	    for i in range(0, len(colours)):
	        primary = colours[i]
	        secondary = '#000000'
	        TT.setColour(primary, secondary)
	        time.sleep(0.1)
rainbowMode()
```
**Note:** As of right now, this example is fairly buggy. This shouldn’t be run in a widget setting as you may face resource usage errors due to the high consumption of the finite resources allocated within a today widget.
