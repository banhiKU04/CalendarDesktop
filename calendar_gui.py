import tkinter as tk
import calendar
from datetime import datetime, timedelta

class CalendarGUI:
    def __init__(self, master):
        self.master = master
        self.current_date = datetime.now()

        self.setup_gui()

    def setup_gui(self):
        self.label_month_year = tk.Label(self.master, text="")
        self.label_month_year.pack()

        self.calendar_frame = tk.Frame(self.master)
        self.calendar_frame.pack()

        self.update_calendar()

        prev_button = tk.Button(self.master, text="Previous Month", command=self.prev_month)
        prev_button.pack(side=tk.LEFT)

        next_button = tk.Button(self.master, text="Next Month", command=self.next_month)
        next_button.pack(side=tk.RIGHT)

    def update_calendar(self):
        self.label_month_year.config(text=calendar.month_name[self.current_date.month] + " " + str(self.current_date.year))

        month_calendar = calendar.monthcalendar(self.current_date.year, self.current_date.month)

        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        for week in month_calendar:
            for day in week:
                if day == 0:
                    label = tk.Label(self.calendar_frame, text="")
                else:
                    label = tk.Label(self.calendar_frame, text=str(day))
                    if datetime(self.current_date.year, self.current_date.month, day).date() == datetime.today().date():
                        label.config(bg="yellow")

                label.grid(row=month_calendar.index(week), column=week.index(day))

    def prev_month(self):
        self.current_date = self.current_date.replace(day=1)
        self.current_date -= timedelta(days=1)
        self.update_calendar()

    def next_month(self):
        self.current_date = self.current_date.replace(day=28)
        self.current_date += timedelta(days=7)
        self.current_date = self.current_date.replace(day=1)
        self.update_calendar()
