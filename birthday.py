from datetime import datetime
from tkinter import messagebox
import tkinter as tk
from tkinter.simpledialog import askstring

class BirthdayManager:
    def __init__(self):
        pass

    def add_birthday(self):
        person_name = askstring("Input", "Enter person's name:")
        if person_name:
            birthday_description = f"Happy Birthday! ({person_name})"
            # Assuming you have a reference to event_display in your CalendarGUI
            # You may need to pass it as a parameter or set it after creating the CalendarGUI object
            self.event_display.delete(1.0, tk.END)
            self.event_display.insert(tk.END, birthday_description)
            self.save_event()

    def check_birthday(self):
        if self.selected_date:
            selected_date = datetime(self.current_date.year, self.current_date.month, self.selected_date).date()
            events = self.schedule_manager.get_events(selected_date)
            if any(event[1] for event in events):  # Check if there are birthdays
                messagebox.showinfo("Birthday Checker", "This date has birthdays!")
            else:
                messagebox.showinfo("Birthday Checker", "No birthdays on this date.")
        else:
            messagebox.showinfo("Birthday Checker", "Select a date to check birthdays.")

    @staticmethod
    def is_birthday_today(events):
        today = datetime.today().date()

        for event, is_birthday, person_name in events:
            if is_birthday:
                try:
                    birthdate_str = event.split("(")[-1].split(")")[0].strip()
                    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
                    if birthdate.day == today.day and birthdate.month == today.month:
                        return True
                except ValueError:
                    print(f"Invalid date string: {event}")

        return False

    @staticmethod
    def get_birthday_person(events):
        for event in events:
            if event[1]:
                return event[2]
        return None
