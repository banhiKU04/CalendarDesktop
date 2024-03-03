import tkinter as tk
from datetime import datetime, timedelta
from tkinter.simpledialog import askstring
from tkinter import messagebox
from threading import Thread
import calendar
import winsound

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

        self.set_alarm_button = tk.Button(self.master, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack()

        self.prev_year_button = tk.Button(self.master, text="Previous Year", command=self.prev_year)
        self.prev_year_button.pack(side=tk.LEFT)

        self.next_year_button = tk.Button(self.master, text="Next Year", command=self.next_year)
        self.next_year_button.pack(side=tk.RIGHT)

        self.prev_month_button = tk.Button(self.master, text="Previous Month", command=self.prev_month)
        self.prev_month_button.pack(side=tk.LEFT)

        self.next_month_button = tk.Button(self.master, text="Next Month", command=self.next_month)
        self.next_month_button.pack(side=tk.RIGHT)



        self.update_calendar()

    # Inside the CalendarGUI class in calendar_gui.py

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
                if day != 0:
                    label = tk.Label(self.calendar_frame, text=str(day))
                    label.bind("<Button-1>", lambda event, d=day: self.select_date(d))

                    # Set background color for Saturdays (index 5) and Fridays (index 4)
                    if week.index(day) == 5:  # Saturday
                        label.config(bg="Red")
                    elif week.index(day) == 4:  # Friday
                        label.config(bg="Red")

                    current_date = datetime(self.current_date.year, self.current_date.month, day).date()

                    # Check if the date is a public holiday
                    if current_date in self.schedule_manager.public_holidays:
                        label.config(bg="LightGreen")  # Adjust color as needed

                    if current_date == datetime.today().date():
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

            if self.is_birthday_today(events):
                birthday_person = self.get_birthday_person(events)
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
                self.event_display.insert(tk.END, f" {selected_date}")

                if selected_date in self.schedule_manager.public_holidays:
                    holiday_name = self.schedule_manager.public_holidays[selected_date]
                    self.event_display.insert(tk.END, f"Public Holiday: {holiday_name}\n")
                    self.event_display.tag_add("public_holiday", "1.0", tk.END)
                    self.event_display.tag_config("public_holiday", foreground="green")
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

    def set_alarm(self):
        alarm_time_str = askstring("Set Alarm", "Enter alarm time (hh:mm AM/PM):")
        if alarm_time_str:
            try:
                alarm_time = datetime.strptime(alarm_time_str, "%I:%M %p").time()
                self.schedule_alarm(alarm_time)
                messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time_str}")
            except ValueError:
                messagebox.showerror("Invalid Time", "Please enter a valid time in the format hh:mm AM/PM")

    def schedule_alarm(self, alarm_time):
        current_date = datetime.now().date()
        current_time = datetime.now().time()
        alarm_datetime = datetime.combine(current_date, alarm_time)

        # Check if the alarm time is in the past
        if current_date == alarm_datetime.date() and current_time >= alarm_time:
            messagebox.showwarning("Invalid Time", "Please set the alarm for a future time.")
        else:
            alarm_thread = Thread(target=self.run_alarm, args=(alarm_datetime,))
            alarm_thread.start()

    def run_alarm(self, alarm_datetime):
        current_datetime = datetime.now()
        delay_seconds = (alarm_datetime - current_datetime).total_seconds()
        delay_seconds = max(0, delay_seconds)

        import time
        time.sleep(delay_seconds)

        winsound.Beep(2000, 2000)
        messagebox.showinfo("Alarm", "Time to wake up!")
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