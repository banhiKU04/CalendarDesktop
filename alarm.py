import winsound
from datetime import datetime
from threading import Thread
from tkinter.simpledialog import askstring
from tkinter import messagebox
import os

class AlarmManager:
    def set_alarm(self):
        alarm_time_str = askstring("Set Alarm", "Enter alarm time (hh:mm AM/PM):")
        if alarm_time_str:
            try:
                alarm_time = datetime.strptime(alarm_time_str, "%I:%M %p").time()
                self.schedule_alarm(alarm_time)
                messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time_str}")
            except ValueError:
                messagebox.showerror("Invalid Time", "Please enter a valid time in the format hh:mm AM/PM")

    def schedule_alarm(self, alarm_time):
        current_date = datetime.now().date()
        current_time = datetime.now().time()
        alarm_datetime = datetime.combine(current_date, alarm_time)

        # Check if the alarm time is in the past
        if current_date == alarm_datetime.date() and current_time >= alarm_time:
            messagebox.showwarning("Invalid Time", "Please set the alarm for a future time.")
        else:
            alarm_thread = Thread(target=self.run_alarm, args=(alarm_datetime,))
            alarm_thread.start()

    def run_alarm(self, alarm_datetime):
        try:
            current_datetime = datetime.now()
            delay_seconds = (alarm_datetime - current_datetime).total_seconds()
            delay_seconds = max(0, delay_seconds)

            import time
            time.sleep(delay_seconds)


            winsound.PlaySound(
                r"C:\Users\Lenovo\Downloads\Music\Free Intro Track - East River (Intro A - 6 seconds).wav",
                winsound.SND_FILENAME)

            messagebox.showinfo("Alarm", "Time to wake up!")

        except Exception as e:
            messagebox.showerror("Alarm Error", f"An error occurred while running the alarm: {str(e)}")
