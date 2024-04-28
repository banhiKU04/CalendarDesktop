import unittest
from datetime import date, datetime
from Model.event import Event



class TestEvent(unittest.TestCase):
    def setUp(self):
        self.event_manager = Event()
    def test_add_event(self):
        event_manager = Event()
        event_manager.add_event(date(2024, 4, 1), "Meeting with client")
        self.assertEqual(event_manager.get_events(date(2024, 4, 1)), [("Meeting with client", False, None)])

    def test_show_all_events(self):
        self.event_manager.add_event(datetime(2024, 4, 1), " ")

        april_2024 = datetime(2024, 4, 1)
        all_events_text = self.event_manager.show_all_events(april_2024)

        expected_output = ('')
        self.assertEqual(all_events_text, expected_output)

    def test_get_events(self):
        event_manager = Event()

        event_manager.add_event(date(2024, 4, 1), "Meeting with client")
        event_manager.add_event(date(2024, 4, 1), "Team meeting", person_name="Banhi")
        event_manager.add_event(date(2024, 4, 2), "Project presentation", is_birthday=True, person_name="Redwan")

        events_2024_04_01 = event_manager.get_events(date(2024, 4, 1))
        events_2024_04_02 = event_manager.get_events(date(2024, 4, 2))
        events_2024_04_03 = event_manager.get_events(date(2024, 4, 3))

        self.assertEqual(events_2024_04_01, [("Meeting with client", False, None), ("Team meeting", False, "Banhi")])
        self.assertEqual(events_2024_04_02, [("Project presentation", True, "Redwan")])
        self.assertEqual(events_2024_04_03, [])