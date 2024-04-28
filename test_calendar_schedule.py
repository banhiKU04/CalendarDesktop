import unittest
from datetime import date
from Model.schedule import Schedule

class TestSchedule(unittest.TestCase):
    def test_set_event(self):
        schedule_manager = Schedule()
        schedule_manager.set_event(date(2024, 4, 1), "Meeting with client")
        self.assertEqual(schedule_manager.get_events(date(2024, 4, 1)), [("Meeting with client", False, None)])


    def test_public_holidays(self):

        schedule_manager = Schedule()

        expected_holidays = {
            date(2024, 3, 17): "National children Day",
            date(2024, 3, 26): "Independence Day",
            date(2024, 4, 14): "Bengali new year Day",
            date(2024, 12, 16): "Victory Day",
            date(2024, 4, 11): "Eid-Ul-Fitor",

        }

        actual_holidays = schedule_manager.public_holidays

        self.assertDictEqual(actual_holidays, expected_holidays)