from time import time


class AlarmClock:
    def __init__(self):
        self.time = '12:30'
        self.alarm_is_on = True
        self.alarm_time = '13:30'
    def alarm_toggle(self):
        if self.alarm_is_on == True:
            self.alarm_is_on = False
            print("alarm is now off")
        else:
            self.alarm_is_on = True
            print('alarm is now on')
    def time_set(self):
        new_time = input('Enter the current time...')
        self.time = new_time
        print(f'Time is set to {new_time}')
    
    