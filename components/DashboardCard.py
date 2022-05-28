from tkinter import *
import tkinter as tk
from tkinter import ttk

class DashboardCard(ttk.Frame):
    def __init__(self, container, title, data):
        super().__init__(
            container,
            height=200,
            width=400,
            padding=20,
        )
        self.pack_propagate(0)

        titleLabel = Label(self, text=title, font='arial 12', bg='#44475a', fg='#f8f8f2')
        titleLabel.pack(anchor='w')

        graph = Frame(self, bg='#44475a')
        graph.pack(expand=1, fill=BOTH)

        dataLabel = Label(graph, text=data, font='arial 24 bold', bg='#44475a', fg='#f8f8f2')
        dataLabel.pack(expand=1)