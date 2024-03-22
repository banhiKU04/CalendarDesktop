import tkinter as tk
import calendar
from threading import Thread

class gui:


  def setup_gui(self):
    self.master.title("Desktop Calendar")
    self.master.geometry("800x700")

    modern_font = ("Helvetica", 14)

    # Create a frame for the month and year label
    label_frame = tk.Frame(self.master, bg="#EFEFEF")  # Light Gray
    label_frame.pack(pady=25)

    # Display the month and year label
    self.label_month_year = tk.Label(label_frame, text="", font=("Arial", 36),
                                     bg="#FFFFE0")  # Adjust font style and size
    self.label_month_year.pack()

    # Create a frame for the calendar
    self.calendar_frame = tk.Frame(self.master, bg="#FFFFFF")
    self.calendar_frame.pack()

    # Display the days of the week above the dates
    days_of_week = [calendar.day_abbr[i] for i in range(7)]
    for col, day in enumerate(days_of_week):
        day_label = tk.Label(self.calendar_frame, text=day, fg="blue",
                             bg="#E0E0E0")
        day_label.grid(row=0, column=col, padx=10)

    # Create a frame for the navigation buttons
    nav_button_frame = tk.Frame(self.master, bg="#E0E0E0")
    nav_button_frame.pack(pady=10)

    # Add navigation buttons
    self.prev_year_button = tk.Button(nav_button_frame, text="Previous Year", command=self.prev_year,
                                      bg="#FFD700", relief=tk.FLAT, font=modern_font)
    self.prev_year_button.pack(side=tk.LEFT, padx=5, pady=5)

    self.prev_month_button = tk.Button(nav_button_frame, text="Previous Month", command=self.prev_month,
                                       bg="#98FB98", font=modern_font)
    self.prev_month_button.pack(side=tk.LEFT, padx=5)

    self.next_month_button = tk.Button(nav_button_frame, text="Next Month", command=self.next_month,
                                       bg="#98FB98", font=modern_font)  # Pale Green
    self.next_month_button.pack(side=tk.RIGHT, padx=5)

    self.next_year_button = tk.Button(nav_button_frame, text="Next Year", command=self.next_year, bg="#FFD700",
                                      font=modern_font)
    self.next_year_button.pack(side=tk.RIGHT, padx=5)

    # Create a frame for the additional buttons
    additional_button_frame = tk.Frame(self.master, bg="#E0E0E0")
    additional_button_frame.pack(pady=10)

    self.todo_button = tk.Button(additional_button_frame, text="To-Do List", command=self.manage_todo_list,
                                 bg="#87CEEB", font=modern_font)
    self.todo_button.pack(side=tk.LEFT, padx=5)

    self.add_birthday_button = tk.Button(additional_button_frame, text="Add Birthday", command=self.add_birthday,
                                         bg="#98FB98", font=modern_font)
    self.add_birthday_button.pack(side=tk.LEFT, padx=5)

    self.set_alarm_button = tk.Button(additional_button_frame, text="Set Alarm", command=self.set_alarm,
                                      bg="#87CEEB", font=modern_font)
    self.set_alarm_button.pack(side=tk.RIGHT, padx=5)

    self.show_all_events_button = tk.Button(additional_button_frame, text="Show All Events",
                                            command=self.show_all_events, bg="#98FB98", font=modern_font)
    self.show_all_events_button.pack(side=tk.RIGHT, padx=5)

    # Create a frame for the event display
    event_display_frame = tk.Frame(self.master, bg="#FFFFFF")
    event_display_frame.pack(pady=10)

    # Display the event text box
    self.event_display = tk.Text(event_display_frame, height=10, width=40, wrap=tk.WORD, bg="#FFFFFF",
                                 font=("Arial", 12))
    self.event_display.pack(pady=5)

    # Create a frame for the save event button
    save_event_frame = tk.Frame(self.master, bg="#E0E0E0")  # Light Gray
    save_event_frame.pack()

    # Add the save event button
    self.save_event_button = tk.Button(save_event_frame, text="Save Event", command=self.save_event,
                                       bg="#FFD700", font=modern_font)  # Gold
    self.save_event_button.pack(side=tk.RIGHT, padx=5)

    self.check_birthday_button = tk.Button(additional_button_frame, text="Check Birthday",
                                           command=self.check_birthday, bg="#e74c3c", font=modern_font,
                                           fg="white")
    self.check_birthday_button.pack(side=tk.LEFT, padx=5)

    reminder_frame = tk.Frame(self.master, bg="#E0E0E0")
    reminder_frame.pack(pady=10)

    # Add entry for reminder message
    self.reminder_entry = tk.Entry(reminder_frame, width=40, font=("Arial", 12))
    self.reminder_entry.pack(side=tk.LEFT, padx=5)

    # Add button to set reminder
    set_reminder_button = tk.Button(reminder_frame, text="Set Reminder", command=self.set_reminder,
                                    bg="#87CEEB", font=("Arial", 12))
    set_reminder_button.pack(side=tk.LEFT, padx=5)

    self.update_calendar()
