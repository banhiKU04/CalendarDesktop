import tkinter as tk
import unittest
from Model.todolist import TodoManager

class TestTodoManager(unittest.TestCase):
    def test_add_todo_with_entry(self):

        todo_manager = TodoManager()

        todo_manager.manage_todo_list()

        todo_manager.new_todo_entry.insert(0, "Buy groceries")

        todo_manager.add_todo()

        todo_display_text = todo_manager.todo_display.get("1.0", tk.END)

        self.assertIn("Buy groceries", todo_display_text)