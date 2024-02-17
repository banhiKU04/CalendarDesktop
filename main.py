import tkinter as tk
from calendar_gui import CalendarGUI

def main():
    root = tk.Tk()
    root.title("Desktop Calendar")

    calendar_gui = CalendarGUI(root)

    root.mainloop()

if __name__ == "__main__":
    main()
