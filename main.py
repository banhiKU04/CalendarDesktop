import tkinter as tk
from controller.calendar_gui import CalendarGUI
from Model.schedule import Schedule

def main():
    root = tk.Tk()
    root.title("Desktop Calendar")

    schedule_manager = Schedule()
    calendar_gui = CalendarGUI(root, schedule_manager)

    root.mainloop()

if __name__ == "__main__":
    main()
