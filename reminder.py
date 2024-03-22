import tkinter as tk
from datetime import datetime, timedelta
from tkinter.simpledialog import askstring
from tkinter import messagebox
from threading import Thread


class ReminderManager:
    def set_reminder(self):
        reminder_message = self.reminder_entry.get().strip()

        if reminder_message:
            try:
                reminder_time_str = askstring("Set Reminder Time", "Enter reminder time (hh:mm AM/PM):")

                if reminder_time_str:
                    reminder_datetime = datetime.strptime(reminder_time_str, "%I:%M %p").time()

                    reminder_thread = Thread(target=self.run_reminder, args=(reminder_message, reminder_datetime))
                    reminder_thread.start()

                    messagebox.showinfo("Reminder Set", f"Reminder set for {reminder_time_str}")

            except ValueError:
                messagebox.showerror("Invalid Time", "Please enter a valid time in the format hh:mm AM/PM")

    def run_reminder(self, reminder_message, reminder_datetime):
        current_datetime = datetime.now()
        current_time = current_datetime.time()
        reminder_time = datetime.combine(datetime.today(), reminder_datetime)

        if current_datetime >= reminder_time:
            messagebox.showwarning("Invalid Time", "Please set the reminder for a future time.")
        else:
            delay_seconds = (reminder_time - current_datetime).total_seconds()
            delay_seconds = max(0, delay_seconds)

            import time
            time.sleep(delay_seconds)

            messagebox.showinfo("Reminder", reminder_message)

