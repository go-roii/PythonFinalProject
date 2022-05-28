import tkinter as tk
from tkinter import ttk

class DashboardCard(tk.Frame):
    def __init__(self, container, title, data):
        super().__init__(
            container,
            height=200,
            width=400,
            bg='#1e1e2e',
            highlightthickness=2,
            highlightbackground='#94e2d5',
            padx=12,
            pady=12
        )
        self.pack_propagate(0)

        titleLabel = tk.Label(self, text=title, font='arial 10', bg='#1e1e2e', fg='#c6d0f5')
        titleLabel.pack(anchor='w')

        graph = tk.Frame(self, bg='#1e1e2e')
        graph.pack(expand=1, fill=tk.BOTH)

        dataLabel = tk.Label(graph, text=data, font='arial 24 bold', bg='#1e1e2e', fg='#94e2d5')
        dataLabel.pack(expand=1)