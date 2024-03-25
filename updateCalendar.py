import tkinter as tk
import calendar
from datetime import datetime, timedelta

class UpdateManager:
    def update_calendar(self):
        self.label_month_year.config(
            text=calendar.month_name[self.current_date.month] + " " + str(self.current_date.year))

        month_calendar = calendar.monthcalendar(self.current_date.year, self.current_date.month)

        # Display the days of the week above the dates
        days_of_week = [calendar.day_abbr[i] for i in range(7)]
        for col, day in enumerate(days_of_week):
            day_label = tk.Label(self.calendar_frame, text=day, fg="blue")
            day_label.grid(row=0, column=col)

        for week in month_calendar:
            for day in week:
                if day != 0:
                    label = tk.Label(self.calendar_frame, text=str(day))
                    label.bind("<Button-1>", lambda event, d=day: self.select_date(d))


                    if week.index(day) == 5:
                        label.config(bg="Red")
                    elif week.index(day) == 4:
                        label.config(bg="Red")

                    current_date = datetime(self.current_date.year, self.current_date.month, day).date()

                    # Check if the date is a public holiday
                    if current_date in self.schedule_manager.public_holidays:
                        label.config(bg="LightGreen")

                    if current_date == datetime.today().date():
                        label.config(bg="yellow")

                    label.grid(row=month_calendar.index(week) + 1, column=week.index(day))

        self.display_events()


