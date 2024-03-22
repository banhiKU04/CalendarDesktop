import tkinter as tk
from datetime import datetime, timedelta
from tkinter.simpledialog import askstring
from tkinter import messagebox
from threading import Thread

class TodoManager:

    def manage_todo_list(self):
        # Create a new window for managing to-do list
        todo_window = tk.Toplevel(self.master)
        todo_window.title("To-Do List")

        # Create a Text widget for displaying to-do items
        self.todo_display = tk.Text(todo_window, height=10, width=40, wrap=tk.WORD)
        self.todo_display.pack()

        # Create an entry for adding new to-do items
        self.new_todo_entry = tk.Entry(todo_window, width=40)
        self.new_todo_entry.pack()

        # Create a button to add a new to-do item
        add_todo_button = tk.Button(todo_window, text="Add To-Do", command=self.add_todo)
        add_todo_button.pack()

    def add_todo(self):
        new_todo = self.new_todo_entry.get().strip()
        if new_todo:
            self.todo_display.insert(tk.END, f"{new_todo}\n")
            self.new_todo_entry.delete(0, tk.END)