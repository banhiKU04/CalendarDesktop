import unittest
from datetime import datetime
from controller.navigation import Navigation
from unittest.mock import MagicMock

class TestNavigation(unittest.TestCase):
    def setUp(self):

        self.mock_schedule_manager = MagicMock()
        self.mock_event_display = MagicMock()

        self.navigation = Navigation(self.mock_schedule_manager, self.mock_event_display)
    def update_calendar(self):
        # Add your implementation to update the calendar here
        pass


    def test_prev_month(self):

        self.navigation.current_date = datetime(2024, 4, 15)


        self.navigation.prev_month()

        expected_date = datetime(2024, 3, 31)
        self.assertEqual(self.navigation.current_date, expected_date)

    def test_next_month(self):

        self.navigation.current_date = datetime(2024, 4, 15)

        self.navigation.next_month()

        expected_date = datetime(2024, 5, 1)
        self.assertEqual(self.navigation.current_date, expected_date)

    def test_prev_year(self):

        self.navigation.current_date = datetime(2024, 4, 15)

        self.navigation.prev_year()

        expected_date = datetime(2023, 12, 31)
        self.assertEqual(self.navigation.current_date, expected_date)

    def test_next_year(self):

        self.navigation.current_date = datetime(2024, 4, 15)

        self.navigation.next_year()

        expected_date = datetime(2025, 1, 31)
        self.assertEqual(self.navigation.current_date, expected_date)

    def test_show_all_events(self):
        self.navigation.current_date = datetime(2024, 4, 15)

        self.navigation.show_all_events()

        self.mock_schedule_manager.show_all_events.assert_called_once_with(datetime(2024, 4, 15))