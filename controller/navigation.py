import tkinter as tk
import calendar
from datetime import datetime, timedelta


class Navigation:
    def __init__(self, schedule_manager, event_display):
        self.schedule_manager = schedule_manager
        self.event_display = event_display
        self.current_date = datetime.now()



    def prev_month(self):
        self.current_date = self.current_date.replace(day=1)
        self.current_date -= timedelta(days=1)
        self.update_calendar()

    def next_month(self):
        self.current_date = self.current_date.replace(day=28)
        self.current_date += timedelta(days=7)
        self.current_date = self.current_date.replace(day=1)
        self.update_calendar()

    def prev_year(self):
        self.current_date = self.current_date.replace(
            year=self.current_date.year - 1,
            month=12,
            day=calendar.monthrange(self.current_date.year - 1, 12)[1]
        )
        self.update_calendar()

    def next_year(self):
        self.current_date = self.current_date.replace(
            year=self.current_date.year + 1,
            month=1,
            day=calendar.monthrange(self.current_date.year + 1, 1)[1]
        )
        self.update_calendar()

    def show_all_events(self):
        all_events_text = self.schedule_manager.show_all_events(self.current_date)
        if all_events_text:
            self.event_display.delete(1.0, tk.END)
            self.event_display.insert(tk.END, all_events_text)
            self.event_display.tag_add("event", "1.0", tk.END)
            self.event_display.tag_config("event", foreground="green")

