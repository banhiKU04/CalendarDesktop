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

    # Inside the Event class in event.py

    def show_all_events(self, month):
        all_events = []
        today_date = datetime.today().date()

        for day in range(1, calendar.monthrange(month.year, month.month)[1] + 1):
            date = datetime(month.year, month.month, day).date()
            events = self.get_events(date)

            if events:
                for event in events:
                    person_name = event[2] if event[2] is not None else ''  # Return empty string if the name is None
                    event_text = f"{event[0]} ({date} - {calendar.day_name[date.weekday()]} - {person_name})"

                    if event[1]:
                        next_year_date = datetime(month.year + 1, month.month, day).date()
                        event_text += f" - Next year on {next_year_date}"
                    elif date == today_date:
                        event_text += " - Today is the birthday!"

                    all_events.append(event_text)

        return "\n".join(all_events)


