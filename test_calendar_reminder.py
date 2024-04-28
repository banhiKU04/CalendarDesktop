import unittest
from datetime import datetime, timedelta
from Model.reminder import ReminderManager

class TestReminderManager(unittest.TestCase):
    def test_set_reminder(self):

        reminder_manager = ReminderManager()


        reminder_time = datetime.now() + timedelta(minutes=5)
        reminder_manager.set_reminder("Reminder message", reminder_time)

        current_time = datetime.now()
        time_difference = (reminder_time - current_time).total_seconds()
        self.assertLessEqual(time_difference, 300)