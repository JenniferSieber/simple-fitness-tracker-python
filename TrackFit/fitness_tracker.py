""" Fitness Tracker using helper.py and dateutils - parser"""
from dateutil import parser
from helper import gpsDistance
emojis = ['🚶', '🧗‍♀️', '🤩', '🏃‍♀️', '🏊‍♀️', '😓', '🧎‍♀️', '🚴‍♀️', '🤸‍♀️', '⌚', '⏱️']

class Workout(object) :
    cal_per_hr = 200 
    def __init__(self, start, end, calories=None) :
        self.start = parser.parse(start)
        self.end = parser.parse(end)
        self.calories = calories
        self.icon = emojis[2][0]
        self.kind = 'Workout'

    def get_duration(self) :
        return self.end - self.start  
    
    def get_calories(self) :
        if self.calories == None :
            return Workout.cal_per_hr*(self.end - self.start).total_seconds() / 3600
        else :    
            return self.calories   
            
    def get_start(self) :
        return self.start   
    
    def get_end(self) :
        return self.end    
    
    def get_calories(self) :
        if self.calories == None :
            return Workout.cal_per_hr*(self.end - self.start).total_seconds() / 3600
        else :    
            return self.calories 
          
    def get_kind(self) :
        return self.kind
        
    def set_calories(self, calories) :
        self.calories = calories
        
    def set_start(self, start) :
        self.start = start
        
    def set_end(self, end) :
        self.end = end

    # Screen View
    def __str__(self) :
        width = 16
        iconLen = 0
        duration_str = str(self.get_duration())
        cal_str = f'{self.get_calories():.0f}'
        view = F" {'_'*(width + 2)}\n"
        view += F'| {' '*width} |\n'
        view += F'| {self.icon} {' '*(width-3)} |\n'
        view += F'| {self.kind} {' '*(width-len(self.kind)-1)} |\n'
        view += F'| {' ' *width} |\n'
        view += F'| {duration_str} {' '* (width - len(duration_str)-1)} |\n'
        view += F'| {cal_str} Calories {' '* (width - len(cal_str)-10)} |\n'
        view += F'| {' ' *width} |\n'
        # view += F'| {' ' *width} |\n'
        view += F"|{'_'*(width + 2)}|\n"
        return view
    
    # workouts equality dunder method
    def __eq__(self, other) :
        s_duration = self.get_duration()
        o_duration = other.get_duration()
        # print(s_duration, o_duration, type(self), type(other))
        return type(self) == type(other) and \
        s_duration == o_duration and \
        self.kind == other.kind and \
        self.get_calories() == other.get_calories() 
    


class RunWorkout(Workout) :
    cals_per_km = 100
    def __init__(self, start, end, elev=0, calories=None, route_gps_points=None) :
        super().__init__(start, end, calories) 
        self.icon = emojis[3][0]
        self.kind = 'Running'
        self.elev = elev
        self.route_gps_points = route_gps_points

    def get_elevation(self) :
        return self.elev

    def set_elevation(self, e) :
        self.elev = e

    def get_calories(self) :
        if (self.route_gps_points != None) :
            dist = 0
            lastP = self.route_gps_points[0]
            for p in self.route_gps_points[1:] :
                dist += gpsDistance(lastP, p)
                lastP = p
            return dist * RunWorkout.cals_per_km
        else :
            return super().get_calories()
            
    # Override Parent 
    def __eq__(self, other) :
        return super().__eq__(other) and self.elev == other.elev
        
class WalkWorkout(Workout) :
    def __init__(self, start, end, elev=0, calories=None) :
        super().__init__(start, end, calories) 
        self.icon = emojis[0][0]
        self.kind = 'Walking'
        self.elev = elev

    def get_elevation(self) :
        return self.elev

    def set_elevation(self, e) :
        self.elev = e

class HikeWorkout(Workout) :
    def __init__(self, start, end, elev=0, calories=None) :
        super().__init__(start, end, calories) 
        self.icon = emojis[1][0]
        self.kind = 'Hiking'
        self.elev = elev
    
    def get_elevation(self) :
        return self.elev

    def set_elevation(self, e) :
        self.elev = e

class SwimWorkout(Workout) :
    # redefine class variable cal_per_hr
    cal_per_hr = 400
    
    def __init__(self, start, end, pace, calories=None) :
        super().__init__(start,end,calories)
        self.icon = emojis[4][0]
        self.kind = 'Swimming'
        self.pace = pace

    def get_pace(self) :
        return self.pace
    
    def get_calories(self) :
        if (self.calories == None):
            return SwimWorkout.cal_per_hr * (self.end - self.start).total_seconds() / 3600.0
        else:
            return self.calories

# Helper functions for totalled values: calories and elevation
def total_calories(workouts) :
    cals = 0
    for w in workouts:
      cals += w.get_calories()
    #return cals
    cals_str = F'🤩 Calories: {cals:.0f}'
    return cals_str

def total_elevation(run_workouts) :
    elev = 0
    for w in run_workouts:
      elev += w.get_elevation()
    elev_str = F'🤩 Elevation: {elev}'
    return elev_str

w1 = Workout('9/30/2021 1:35 PM','9/30/2021 2:05 PM', 500)
w2 = Workout('9/30/2021 1:35 PM','9/30/2021 2:05 PM') # cal are 200 by default
w3 = Workout('9/30/2021 1:35 PM','9/30/2021 2:05 PM', 100)
w4 = Workout('9/29/2021 1:35 PM','9/29/2021 2:05 PM', 100)
print(w3)
print(w4)

rw0 = RunWorkout('9/30/2021 1:35 PM','9/30/2021 2:05 PM', 100)
rw1 = RunWorkout('9/30/2021 1:35 PM','9/30/2021 3:05 PM', 100)
print(rw0)
print(rw1)
rw2 = RunWorkout('9/30/2021 1:35 PM','9/30/2021 3:05 PM', 200)
rw3 = RunWorkout('9/30/2021 1:35 PM','9/30/2021 3:05 PM', 100)
print(w4 == rw0)  # False -dates not same
print(w3 == w4)  # False -dates not same
print('')
print(w1 == w2)  # False since only length of workout is the same
# print(w1 == w3)  # False since only length of workout is the same
print(w2 == w3)  # True since the length and calories are equal






