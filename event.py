# event.py
from datetime import datetime
import calendar

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
        for day in range(1, calendar.monthrange(month.year, month.month)[1] + 1):
            date = datetime(month.year, month.month, day).date()
            events = self.get_events(date)
            if events:
                event_text = f"Events for {date}:\n" + "\n".join([f"{event[0]} ({event[2]})" for event in events])
                all_events.append(event_text)
        return "\n".join(all_events)
