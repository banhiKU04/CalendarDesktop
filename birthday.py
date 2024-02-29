from datetime import datetime


def is_birthday_today(events):
    today = datetime.today().date()
    for event in events:
        if isinstance(event[0], str) and 'Happy Birthday!' in event[0]:
            # Extract the birthdate from the string and compare it with today's date
            birthdate_str = event[0].split('(')[-1].split(')')[0].strip()
            birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
            return today == birthdate
        elif isinstance(event[0], datetime):  # Make sure event[0] is a datetime object
            event_date = event[0].date()
            if event_date == today and event[1]:
                return True
    return False


def get_birthday_person(events):
    for event in events:
        if event[1]:
            return event[2]
    return None
