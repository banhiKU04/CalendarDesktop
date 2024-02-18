class Event:
    def __init__(self):
        self.events = {}

    def add_event(self, date, description):
        if date not in self.events:
            self.events[date] = []
        self.events[date].append(description)

    def get_events(self, date):
        return self.events.get(date, [])

    def show_all_events(self, month):
        all_events = []
        for day in range(1, calendar.monthrange(month.year, month.month)[1] + 1):
            date = datetime(month.year, month.month, day).date()
            events = self.get_events(date)
            if events:
                event_text = f"Events for {date}:\n" + "\n".join(events)
                all_events.append(event_text)
        return "\n".join(all_events)
