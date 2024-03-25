import tkinter as tk
import calendar
from threading import Thread
from datetime import datetime, timedelta
from alarm import AlarmManager
from todolist import TodoManager
from reminder import ReminderManager
from birthday import BirthdayManager
from navigation import Navigation
from updateCalendar import UpdateManager
from displayEvent import DisplayManager
from setupGui import gui
from event import Event


class CalendarGUI(tk.Tk, AlarmManager, ReminderManager, TodoManager, BirthdayManager, Navigation, UpdateManager, DisplayManager, gui, Event):
    def __init__(self, master, schedule_manager):
        self.master = master
        self.schedule_manager = schedule_manager
        self.current_date = datetime.now()
        self.selected_date = None

        self.setup_gui()
