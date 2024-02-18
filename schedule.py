from datetime import datetime, timedelta
from event import Event
import calendar

class Schedule:
    def __init__(self):
        self.event_manager = Event()

    def set_event(self, date, description):
        self.event_manager.add_event(date, description)

    def get_events(self, date):
        return self.event_manager.get_events(date)

    def show_events(self, date):
        events = self.get_events(date)
        if events:
            return "\n".join(events)
        else:
            return "No events on this day."

    def show_all_events(self, month):
        all_events = []
        for day in range(1, calendar.monthrange(month.year, month.month)[1] + 1):
            date = datetime(month.year, month.month, day).date()
            events = self.get_events(date)
            if events:
                event_text = f"Events for {date}:\n" + "\n".join(events)
                all_events.append(event_text)
        return "\n".join(all_events)
