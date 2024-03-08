from event import Event
from datetime import datetime

class Schedule:
    def __init__(self):
        self.event_manager = Event()

    def set_event(self, date, description, is_birthday=False, person_name=None):
        self.event_manager.add_event(date, description, is_birthday, person_name)

    def get_events(self, date):
        return self.event_manager.get_events(date)

    def show_events(self, date):
        events = self.get_events(date)
        if events:
            return "\n".join([f"{event[0]} ({event[2]})" for event in events])
        else:
            return "No events on this day."

    def show_all_events(self, month):
        return self.event_manager.show_all_events(month)
