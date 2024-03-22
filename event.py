from datetime import datetime
import calendar
import tkinter as tk

class Event:
    def __init__(self):
        self.events = {}

    def add_event(self, date, description, is_birthday=False, person_name=None):
        if date not in self.events:
            self.events[date] = []
        self.events[date].append({"description": description, "is_birthday": is_birthday, "person_name": person_name})

    def get_events(self, date):
        return [(event["description"], event["is_birthday"], event["person_name"]) for event in self.events.get(date, [])]



    def show_all_events(self, month):
        all_events = []
        today_date = datetime.today().date()

        for day in range(1, calendar.monthrange(month.year, month.month)[1] + 1):
            date = datetime(month.year, month.month, day).date()
            events = self.get_events(date)

            if events:
                for event in events:
                    person_name = event[2] if event[2] is not None else ''
                    event_text = f"{event[0]} ({date} - {calendar.day_name[date.weekday()]} - {person_name})"

                    switch = {
                        event[1]: f" - Next year on {datetime(month.year + 1, month.month, day).date()}",
                        date == today_date: " - Today is the birthday!"
                    }

                    for condition, message in switch.items():
                        if condition:
                            event_text += message
                            break

                    all_events.append(event_text)

        return "\n".join(all_events)

    def save_event(self):
        if self.selected_date:
            description = self.event_display.get("1.0", tk.END).strip()
            if description:
                selected_date = datetime(self.current_date.year, self.current_date.month, self.selected_date)
                is_birthday = "Happy Birthday!" in description
                person_name = self.get_person_name(description)
                self.schedule_manager.set_event(selected_date.date(), description, is_birthday, person_name)
                self.update_calendar()




    def save_events_to_file(self, filename):
        with open(filename, 'w') as file:
            for date, events in self.events.items():
                for event in events:
                    file.write(f"{date}: {event['description']}, {event['is_birthday']}, {event['person_name']}\n")
