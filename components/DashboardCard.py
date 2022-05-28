import tkinter as tk
from tkinter import ttk

class DashboardCard(tk.Frame):
    def __init__(self, container, title, data):
        bgColor='#1e1e2e'
        accentColor='#94e2d5'

        super().__init__(
            container,
            height=150,
            width=350,
            bg=bgColor,
            highlightthickness=2,
            highlightbackground=accentColor,
            padx=16,
            pady=20
        )
        self.pack_propagate(0)

        titleLabel = tk.Label(self, text=title, font='arial 12', bg=bgColor, fg='#c6d0f5')
        titleLabel.pack(anchor='w', expand=1)

        graph = tk.Frame(self, bg=bgColor)
        graph.pack(expand=1, fill=tk.BOTH)

        dataLabel = tk.Label(graph, text=data, font='arial 26 bold', bg=bgColor, fg=accentColor)
        dataLabel.pack(anchor='w')

        comparePreviousDataLabel = tk.Label(graph, text='10.7% VS PREV. 28 DAYS', bg=bgColor, fg='#7b819d')
        comparePreviousDataLabel.pack(anchor='w')