import tkinter as tk
from tkinter import ttk
import json
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from datetime import datetime

matplotlib.use('TkAgg')

class TimelineTab(ttk.Frame, tk.Tk):
    def __init__(self, container):
        super().__init__(container, padding=24)

        # create a figure
        self.figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)

        # create the toolbar
        NavigationToolbar2Tk(self.figure_canvas, self)

        # create axes
        self.axes = self.figure.add_subplot()
        self.createBarGraph('cases_by_month', 'Timeline of Cases by Month', 'Number of Cases', rotate=True)


    def createBarGraph(self, fileName, title, yAxisLabel, rotate=False, rotation=45, alignment='right'):
        file = open(f'./JSONData/{fileName}.json')
        data = json.load(file)

        # sort data by date
        sorted_date = sorted(data.items(), key=lambda x: datetime.strptime(x[0], '%b. %Y'))

        # populate a new dict from the sorted list
        sortedData = {}
        for x in sorted_date:
            sortedData[x[0]] = x[1]

        # create the barchart
        self.axes.plot(sortedData.keys(), sortedData.values())
        self.axes.set_title(title)
        self.axes.set_ylabel(yAxisLabel)

        if rotate:
            self.axes.set_xticklabels(data.keys(), rotation=rotation, ha=alignment)

        self.axes.grid(True)

        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)