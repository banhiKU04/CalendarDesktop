import tkinter as tk
import calendar
from datetime import datetime, timedelta
from event import Event

class CalendarGUI:
    def __init__(self, master, schedule_manager):
        self.master = master
        self.schedule_manager = schedule_manager
        self.current_date = datetime.now()
        self.selected_date = None

        self.setup_gui()

    def setup_gui(self):
        self.label_month_year = tk.Label(self.master, text="")
        self.label_month_year.pack()

        self.calendar_frame = tk.Frame(self.master)
        self.calendar_frame.pack()

        self.event_display = tk.Text(self.master, height=10, width=40, wrap=tk.WORD)
        self.event_display.pack()

        self.save_event_button = tk.Button(self.master, text="Save Event", command=self.save_event)
        self.save_event_button.pack(side=tk.RIGHT)

        self.show_all_events_button = tk.Button(self.master, text="Show All Events", command=self.show_all_events)
        self.show_all_events_button.pack()

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
                    label.bind("<Button-1>", lambda event, d=day: self.select_date(d))
                    if datetime(self.current_date.year, self.current_date.month, day).date() == datetime.today().date():
                        label.config(bg="yellow")

                label.grid(row=month_calendar.index(week), column=week.index(day))

        self.display_events()

    def prev_month(self):
        self.current_date = self.current_date.replace(day=1)
        self.current_date -= timedelta(days=1)
        self.update_calendar()

    def next_month(self):
        self.current_date = self.current_date.replace(day=28)
        self.current_date += timedelta(days=7)
        self.current_date = self.current_date.replace(day=1)
        self.update_calendar()

    def save_event(self):
        if self.selected_date:
            description = self.event_display.get("1.0", tk.END).strip()
            if description:
                selected_date = datetime(self.current_date.year, self.current_date.month, self.selected_date)
                self.schedule_manager.set_event(selected_date.date(), description)
                self.update_calendar()

    def select_date(self, day):
        self.selected_date = day
        self.display_events()

    def display_events(self):
        self.event_display.delete(1.0, tk.END)
        if self.selected_date:
            selected_date = datetime(self.current_date.year, self.current_date.month, self.selected_date).date()
            events = self.schedule_manager.get_events(selected_date)
            if events:
                event_text = "\n".join(events)
                self.event_display.insert(tk.END, f"Events for {selected_date}:\n{event_text}")
                self.event_display.tag_add("event", "3.0", tk.END)
                self.event_display.tag_config("event", foreground="blue")
            else:
                self.event_display.insert(tk.END, f"No events for {selected_date}.")
        else:
            self.event_display.insert(tk.END, "Select a date to display events.")

    def show_all_events(self):
        all_events = self.schedule_manager.show_all_events(self.current_date.replace(day=1).date())
        self.event_display.delete(1.0, tk.END)
        self.event_display.insert(tk.END, all_events)
        self.event_display.tag_add("event", "1.0", tk.END)
        self.event_display.tag_config("event", foreground="green")
