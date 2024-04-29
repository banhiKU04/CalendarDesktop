import os
import time
from datetime import datetime, timedelta
from threading import Thread
import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter import messagebox


class ReminderManager:
    REMINDER_FILE_PATH = "reminders.txt"  # Path to save reminders

    def __init__(self):
        self.reminder_entry = tk.Entry()  # Default Entry widget
        self.reminders = self.load_reminders()  # Load existing reminders

    def set_reminder(self):
        """
        Set a new reminder based on user input for message and time.
        """
        reminder_message = self.reminder_entry.get().strip()

        if not reminder_message:
            messagebox.showerror("Error", "Reminder message cannot be empty.")
            return

        reminder_time_str = askstring("Set Reminder Time", "Enter reminder time (hh:mm AM/PM)")

        if reminder_time_str:
            try:
                reminder_time = datetime.strptime(reminder_time_str, "%I:%M %p").time()

                # Start a thread to handle the reminder
                reminder_thread = Thread(target=self.run_reminder, args=(reminder_message, reminder_time))
                reminder_thread.start()

                # Save the reminder to the file
                self.save_reminder(reminder_message, reminder_time_str)

                messagebox.showinfo("Reminder Set", f"Reminder set for {reminder_time_str}")

            except ValueError:
                messagebox.showerror("Invalid Time", "Please enter a valid time in the correct format.")

    def run_reminder(self, reminder_message, reminder_time):
        """
        Wait for the reminder time and then display the reminder message.
        """
        delay_seconds = max(0, (datetime.combine(datetime.today(), reminder_time) - datetime.now()).total_seconds())

        time.sleep(delay_seconds)  # Wait until the reminder time

        messagebox.showinfo("Reminder", reminder_message)

    def save_reminder(self, reminder_message, reminder_time_str):
        """
        Save a reminder message and time to the specified file.
        """
        try:
            with open(self.REMINDER_FILE_PATH, "a") as file:
                file.write(f"{reminder_message}, {reminder_time_str}\n")  # Write data to file
        except Exception as e:
            print(f"Error while saving reminder: {e}")
            messagebox.showerror("Error", "Failed to save reminder.")

    def load_reminders(self):
        """
        Load reminders from the specified file.
        """
        reminders = []
        if os.path.exists(self.REMINDER_FILE_PATH):
            with open(self.REMINDER_FILE_PATH, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue  # Skip empty lines
                    message, time_str = line.split(",")
                    reminder_time = datetime.strptime(time_str.strip(), "%I:%M %p").time()
                    reminders.append({
                        "message": message.strip(),
                        "time": reminder_time
                    })
        return reminders
