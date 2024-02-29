import tkinter as tk
import calendar
from datetime import datetime, timedelta
from event import Event
from schedule import Schedule
from tkinter.simpledialog import askstring
from tkinter import messagebox
from birthday import is_birthday_today, get_birthday_person


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

        self.add_birthday_button = tk.Button(self.master, text="Add Birthday", command=self.add_birthday)
        self.add_birthday_button.pack(side=tk.LEFT)

        self.check_birthday_button = tk.Button(self.master, text="Check Birthday", command=self.check_birthday)
        self.check_birthday_button.pack()

        self.prev_year_button = tk.Button(self.master, text="Previous Year", command=self.prev_year)
        self.prev_year_button.pack(side=tk.LEFT)

        self.next_year_button = tk.Button(self.master, text="Next Year", command=self.next_year)
        self.next_year_button.pack(side=tk.RIGHT)

        self.update_calendar()

    def update_calendar(self):
        self.label_month_year.config(
            text=calendar.month_name[self.current_date.month] + " " + str(self.current_date.year))

        month_calendar = calendar.monthcalendar(self.current_date.year, self.current_date.month)

        # Display the days of the week above the dates
        days_of_week = [calendar.day_abbr[i] for i in range(7)]
        for col, day in enumerate(days_of_week):
            day_label = tk.Label(self.calendar_frame, text=day, fg="blue")  # Change the color to blue
            day_label.grid(row=0, column=col)

        for week in month_calendar:
            for day in week:
                if day == 0:
                    label = tk.Label(self.calendar_frame, text="")
                else:
                    label = tk.Label(self.calendar_frame, text=str(day))
                    label.bind("<Button-1>", lambda event, d=day: self.select_date(d))
                    if datetime(self.current_date.year, self.current_date.month, day).date() == datetime.today().date():
                        label.config(bg="yellow")

                label.grid(row=month_calendar.index(week) + 1, column=week.index(day))

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

    def prev_year(self):
        self.current_date = self.current_date.replace(year=self.current_date.year - 1)
        self.update_calendar()

    def next_year(self):
        self.current_date = self.current_date.replace(year=self.current_date.year + 1)
        self.update_calendar()

    def save_event(self):
        if self.selected_date:
            description = self.event_display.get("1.0", tk.END).strip()
            if description:
                selected_date = datetime(self.current_date.year, self.current_date.month, self.selected_date)
                is_birthday = "Happy Birthday!" in description
                person_name = self.get_person_name(description)
                self.schedule_manager.set_event(selected_date.date(), description, is_birthday, person_name)
                self.update_calendar()

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
        if self.selected_date:
            selected_date = datetime(self.current_date.year, self.current_date.month, self.selected_date).date()
            events = self.schedule_manager.get_events(selected_date)

            if is_birthday_today(events):
                birthday_person = get_birthday_person(events)
                self.event_display.insert(tk.END, f"Happy Birthday, {birthday_person}!\n")
                self.event_display.tag_add("birthday", "1.0", tk.END)
                self.event_display.tag_config("birthday", foreground="red")

            elif events:
                for event, _, person_name in events:
                    event_text = f"{event} ({person_name})"
                    self.event_display.insert(tk.END, f"{event_text}\n")
                    self.event_display.tag_add("event", "1.0", tk.END)
                    self.event_display.tag_config("event", foreground="blue")
            else:
                self.event_display.insert(tk.END, f"No events for {selected_date}")
        else:
            self.event_display.insert(tk.END, "Select a date to display events.")

    def show_all_events(self):
        all_events_text = self.schedule_manager.show_all_events(self.current_date)
        self.event_display.delete(1.0, tk.END)
        if all_events_text:
            self.event_display.insert(tk.END, all_events_text)
            self.event_display.tag_add("event", "1.0", tk.END)
            self.event_display.tag_config("event", foreground="green")

    def add_birthday(self):
        person_name = askstring("Input", "Enter person's name:")
        if person_name:
            birthday_description = f"Happy Birthday! ({person_name})"
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

if __name__ == "__main__":
    import tkinter as tk
    from schedule import Schedule

    def main():
        root = tk.Tk()
        root.title("Desktop Calendar")

        schedule_manager = Schedule()
        calendar_gui = CalendarGUI(root, schedule_manager)

        root.mainloop()

    main()