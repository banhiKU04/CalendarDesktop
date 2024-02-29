from datetime import datetime


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
                # Handle invalid date strings
                print(f"Invalid date string: {event}")

    return False


def get_birthday_person(events):
    for event in events:
        if event[1]:
            return event[2]
    return None
