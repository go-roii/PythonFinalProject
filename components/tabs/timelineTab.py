import tkinter as tk
from tkinter import ttk
import json
from turtle import bgcolor
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
        super().__init__(container, padding=24, style='tabFrame.TFrame')

        # create a figure
        self.figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)

        # create the toolbar
        NavigationToolbar2Tk(self.figure_canvas, self)
        for button in NavigationToolbar2Tk.winfo_children(self):
            button.config(background='red')

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
        self.axes.plot(sortedData.keys(), sortedData.values(), color='#94e2d5')
        self.axes.set_title(title, color='#94e2d5')
        self.axes.set_ylabel(yAxisLabel, color='#cdd6f4')

        # graph bg
        self.figure.set_facecolor('#1e1e2e')
        self.axes.set_facecolor('#1e1e2e')

        self.axes.tick_params(colors='#94e2d5', labelcolor='#cdd6f4', which='both')
        
        # frame bg
        for spine in self.axes.spines.values():
            spine.set_edgecolor('#94e2d5')

        if rotate:
            self.axes.set_xticklabels(sortedData.keys(), rotation=rotation, ha=alignment)

        self.axes.grid(True, color='#313244')

        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)