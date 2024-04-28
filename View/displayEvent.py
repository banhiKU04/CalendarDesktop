import tkinter as tk
import calendar
from threading import Thread
from datetime import datetime, timedelta

class DisplayManager:


    def get_person_name(self, description):
        name_start = description.rfind("(")
        name_end = description.rfind(")")
        if name_start != -1 and name_end != -1:
            return description[name_start + 1:name_end]
        else:
            return None
    def select_date(self, day):
        self.selected_date = day
        self.display_events()

    def display_events(self):
        self.event_display.delete(1.0, tk.END)

        if not self.selected_date:
            self.event_display.insert(tk.END, "Select a date to display events.")
            return

        selected_date = datetime(self.current_date.year, self.current_date.month, self.selected_date).date()
        events = self.schedule_manager.get_events(selected_date)

        switch = {
            self.is_birthday_today(events): self.display_birthday,
            bool(events): self.display_regular_events,
            selected_date in self.schedule_manager.public_holidays: self.display_public_holiday
        }

        for condition, function in switch.items():
            if condition:
                function(selected_date, events)
                break
        else:
            self.event_display.insert(tk.END, f" {selected_date}")

    def display_birthday(self, selected_date, events):
        birthday_person = self.get_birthday_person(events)
        self.event_display.insert(tk.END, f"Happy Birthday, {birthday_person}!\n")
        self.event_display.tag_add("birthday", "1.0", tk.END)
        self.event_display.tag_config("birthday", foreground="red")

    def display_regular_events(self, selected_date, events):
        for event, _, person_name in events:
            event_text = f"{event} ({person_name})"
            self.event_display.insert(tk.END, f"{event_text}\n")
            self.event_display.tag_add("event", "1.0", tk.END)
            self.event_display.tag_config("event", foreground="blue")

    def display_public_holiday(self, selected_date, _):
        holiday_name = self.schedule_manager.public_holidays[selected_date]
        self.event_display.insert(tk.END, f"Public Holiday: {holiday_name}\n")
        self.event_display.tag_add("public_holiday", "1.0", tk.END)
        self.event_display.tag_config("public_holiday", foreground="green")
