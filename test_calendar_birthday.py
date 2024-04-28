import tkinter as tk
import unittest
from Model.birthday import BirthdayManager


class TestBirthdayManager(unittest.TestCase):
    def test_add_birthday_with_name(self):

        birthday_manager = BirthdayManager(tk.Text())
        def mock_askstring(title, prompt):
            return "John Doe"

        birthday_manager.askstring = mock_askstring
        birthday_manager.add_birthday()