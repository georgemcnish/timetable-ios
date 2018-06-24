# Python Timetable V2
# By George McNish
# https://github.com/georgemcnish/timetable-ios

from datetime import date, datetime
import calendar, time, ui, appex

week = 'A'

# Timetable Dictionary - Stores all of the Lessons
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

# Day Structure - Stores all of the Timings of the Day
timings = {'normal': {'P1': [[00,00],[00,00]],'P2': [[00,00],[00,00]],'P3': [[00,00],[00,00]],'P4': [[00,00],[00,00]],'P5': [[00,00],[00,00]]},
           'alternative': {'P1': [[00,00],[00,00]],'P2': [[00,00],[00,00]],'P3': [[00,00],[00,00]],'P4': [[00,00],[00,00]],'P5': [[00,00],[00,00]]}}

# Main class, used to interface with the user interface
class timetableOutput:
    # On initialisation of the class, the view is created and all default values are entered
    def __init__(self, timetable, timings, alternative, colour_primary, colour_secondary):
        # Create a list of all of the weekdays, to cross-reference with the various UI elements
        self.dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        # Create a list of all the selectable weeks, to cross-reference with the various UI elements
        self.weekList = ['A', 'B']
        # Load the View
        self.view = ui.load_view()
        # Set the timing switch to true (displaying lessons)
        self.switch = True
        # Set the default colour of all the elements
        self.setColour(colour_primary, colour_secondary)
        # Set the day to the current one
        self.day = [calendar.day_name[date.today().weekday()], week]
        # Set timetable to input from class declaration
        self.timetable = timetable
        # Set the alternative day to input from class declaration
        self.alternative = alternative
        # Set timings to input from class declaration
        self.timings = timings
        # Perform initial timetable generation
        self.generateTimetable(self.timetable, self.day)
        
    # This is used to update the view, such as the labels
    def updateLabels(self, values):
        # Populate the labels to display the lessons
        for i in range(0,5):
            # Loops through each label, updating their text
            self.view['lbl_out'+str(i)].text = 'P{}: '.format(i+1) + values[i]

    def setColour(self, colour_primary, colour_secondary):
        # Set the output labels and interactive buttons to the primary colour
        for i in range(0,5):
            # Loops through each label, updating their colour
            self.view['lbl_out'+str(i)].text_color = colour_primary
        self.view['lbl_title'].text_color = colour_primary
        
        self.view['seg_day'].border_color = colour_primary
        self.view['seg_day'].tint_color = colour_primary
        self.view['seg_week'].border_color = colour_primary
        self.view['seg_week'].tint_color = colour_primary
        
        self.view['btn_switch'].border_color = colour_primary
        self.view['btn_switch'].tint_color = colour_primary
        # Set the background to the secondary colour
        self.view.background_color = colour_secondary 

    def switchText(self, sender):
        # Create a blank values template, so it can be inserted into the view
        values = []
        # Choose which day timings to use, depending on the current day
        if self.day[0] == self.alternative: times = self.timings['alternative']
        else: times = self.timings['normal']
        # Check if the Lessons or Timings are displayed, True = Lessons, False = Timings
        if self.switch == True:
            self.switch = False
            # Loop through each lesson
            for i in range(0,5):
                # Start of Lesson
                # Get the start times of the lesson into an array
                startTimeValues = times['P'+str(i+1)][0]
                # Format that time with leading zeros and a colon
                startTime = "{}:{}".format(str(startTimeValues[0]).zfill(2), str(startTimeValues[1]).zfill(2))
                # End of Lesson
                # "
                endTimeValues = times['P'+str(i+1)][1]
                # "
                endTime = "{}:{}".format(str(endTimeValues[0]).zfill(2), str(endTimeValues[1]).zfill(2))
                # Merge both the start and end time into a single string
                completeTime = "{} - {}".format(startTime, endTime)
                # Append these timings to the values array
                values.append(completeTime)
            # Force the view to update the text outputs
            self.updateLabels(values)
        else:
            self.switch = True
            # Re-generate the lessons
            self.generateTimetable(self.timetable, self.day)
    
    def generateTimetable(self, timetable, day):
        # Create a blank values template, so it can be inserted into the view
        values = []
        # Overwrite the bool which judges if the lessons are being displayed, to prevent direct time > lesson bug
        self.switch = True
        # Update the day & week selector to match current day
        self.view['seg_day'].selected_index = self.dayList.index(day[0])
        self.view['seg_week'].selected_index = self.weekList.index(day[1])
        # Loop through every lesson
        for i in range(0,5):
            # Append the current lesson to an array, to then display
            values.append(timetable[day[0] + day[1]]['P'+str(i+1)])
        # Forward array onto the update function, which updates the values of each of the labels
        self.updateLabels(values)
        
    def switchDay(self, sender):
        # Get the SwitchView's currently selected index
        selectedIndex = sender.selected_index
        # Store a copy of the current week
        currentWeek = self.day[1]
        # Update the day variable with the new day and current week
        self.day = [self.dayList[selectedIndex], currentWeek]
        # Request for a new timetable to be generated with the new day parameters
        self.generateTimetable(self.timetable, self.day)
    
    def switchWeek(self, sender):
        # Get the SwitchView's currently selected index
        selectedIndex = sender.selected_index
        # Store a copy of the current week
        currentDay = self.day[0]
        # Update the day variable with the new day and current week
        self.day = [currentDay, self.weekList[selectedIndex]]
        # Request for a new timetable to be generated with the new day parameters
        self.generateTimetable(self.timetable, self.day)
        
TT = timetableOutput(timetable, timings, 'Wednesday', "#ffffff", "#000000")

# Set all of the UI element's actions to the class
TT.view['btn_switch'].action = TT.switchText
TT.view['seg_day'].action = TT.switchDay
TT.view['seg_week'].action = TT.switchWeek

appex.set_widget_view(TT.view)
