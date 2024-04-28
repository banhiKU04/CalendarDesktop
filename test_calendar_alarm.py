import unittest
from datetime import datetime, timedelta
from Model.alarm import AlarmManager

class TestAlarmManager(unittest.TestCase):
    def test_set_alarm(self):

        alarm_manager = AlarmManager()


        alarm_time = datetime.now() + timedelta(minutes=5)
        alarm_manager.set_alarm(alarm_time)


        current_time = datetime.now()
        time_difference = (alarm_time - current_time).total_seconds()
        self.assertLessEqual(time_difference, 300)