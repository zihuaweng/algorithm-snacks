from datetime import date, timedelta, datetime
from enum import Enum

class MedicationName(Enum):
    MEDICATION_1, MEDICATION_2, MEDICATION_3 = 1, 2, 3


class Medication:
    def __init__(self, name: MedicationName, start_date: str, end_date: str, frequency: int, dose: int):
        self.__name = name.name
        self.__start_date = date.fromisoformat(start_date)
        self.__end_date = date.fromisoformat(end_date)
        self.__frequency = frequency
        self.__dose = dose
        self.__week_schedule = {}

    def get_name(self):
        return self.__name

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_frequency(self):
        return self.__frequency

    def set_frequency(self, frequency):
        return frequency

    def get_today_schedule(self):
        today = date.today()
        day_string = today.strftime("%y-%m-%d")
        if day_string not in self.week_schedule:
            self.update_week_schedule()

        return self.week_schedule[day_string]

    def get_week_schedule(self):
        today = date.today()
        day_string = today.strftime("%y-%m-%d")
        if day_string not in self.week_schedule:
            self.update_week_schedule()

        return self.week_schedule

    def update_week_schedule(self): 
        self.week_schedule = {}
        day = date.today()
        weekday = day.weekday()
        delta = timedelta(days=1)
        while weekday <= 6:
            times = self.get_times(day)
            if times == 0:
                break
            day_string = day.strftime("%y-%m-%d")
            self.week_schedule[day_string] = times
            if weekday == 6:
                break
            day += delta
            weekday = day.weekday()

    def get_times(self, day):
        if self.__end_date and day <= self.__end_date:
            return self.__frequency
        if self.__dose:
            days = (day-self.start_date).days
            dose_today = (self.__dose - days *self.__frequency) % self.__frequency
            return dose_today
        return 0


class MedicationSchedule:
    def __init__(self):
        self.__medications = set()
        # store schedule for the week
        self.__week_schedule = {}

    def add_medication(self, medication: MedicationName):
        if medication not in self.__medications:
            self.__medications.add(medication)
        self.update_week_schedule()

    def get_today_schedule(self):
        today = date.today()
        day_string = today.strftime("%y-%m-%d")
        if day_string not in self.week_schedule:
            self.update_week_schedule()

        return self.week_schedule[day_string]

    def get_week_schedule(self):
        today = date.today()
        day_string = today.strftime("%y-%m-%d")
        if day_string not in self.week_schedule:
            self.update_week_schedule()

        return self.week_schedule
    
    def update_week_schedule(self):
        self.week_schedule = {}
        day = date.today()
        weekday = day.weekday()
        delta = timedelta(days=1)
        while weekday <= 6:
            day_string = day.strftime("%y-%m-%d")
            self.week_schedule[day_string] = {}
            for medication in self.__medications:
                name = medication.get_name()
                week_schedule = medication.get_week_schedule()
                if not week_schedule:
                    self.__medications.remove(medication)
                    continue
                self.week_schedule[day_string][name] = week_schedule[day_string]
            day += delta
            weekday = day.weekday()
            if weekday == 6:
                break

m1 = Medication(MedicationName.MEDICATION_1, "2020-09-02", "2020-11-02", 3, 1)
m2 = Medication(MedicationName.MEDICATION_2, "2020-09-02", "2020-11-02", 3, 1)
m3 = Medication(MedicationName.MEDICATION_3, "2020-09-02", "2020-10-01", 3, 1)

schedule = MedicationSchedule()
schedule.add_medication(m1)
schedule.add_medication(m2)
schedule.add_medication(m3)

print(schedule.get_today_schedule())
print('-------')
print(schedule.get_week_schedule())
