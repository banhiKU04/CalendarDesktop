import tkinter as tk
from datetime import datetime
from Model.alarm import AlarmManager
from Model.todolist import TodoManager
from Model.reminder import ReminderManager
from Model.birthday import BirthdayManager
from controller.navigation  import Navigation
from updateCalendar import UpdateManager
from View.displayEvent import DisplayManager
from View.setupGui import gui
from Model.event import Event


class CalendarGUI(tk.Tk, AlarmManager, ReminderManager, TodoManager, BirthdayManager, Navigation, UpdateManager, DisplayManager, gui, Event):
    def __init__(self, master, schedule_manager):
        self.master = master
        self.schedule_manager = schedule_manager
        self.current_date = datetime.now()
        self.selected_date = None

        self.setup_gui()
