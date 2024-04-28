import unittest
from datetime import datetime
from View.displayEvent import DisplayManager
from unittest.mock import MagicMock

class TestDisplayManager(unittest.TestCase):
    def setUp(self):
        self.mock_event_display = MagicMock()

        self.display_manager = DisplayManager()

        self.display_manager.event_display = self.mock_event_display

    def test_display_regular_events(self):
        selected_date = datetime(2024, 4, 15)

        events = [

            ("Project presentation", False, None)
        ]

        self.display_manager.display_regular_events(selected_date, events)
        self.mock_event_display.insert.assert_called_with('end', 'Project presentation (None)\n')