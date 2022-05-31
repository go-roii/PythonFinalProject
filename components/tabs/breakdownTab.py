import tkinter as tk
from collections import OrderedDict
from tkinter import ttk
import json
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

matplotlib.use('TkAgg')


class BreakdownTab(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, padding=24)

        filterComboList = ['Region', 'Province', 'Age Group', 'Sex']
        filterCombobox = ttk.Combobox(self, state="readonly", values=filterComboList)
        filterCombobox.current(0)
        filterCombobox.bind("<<ComboboxSelected>>", self.filterCases)
        filterCombobox.pack(side=tk.TOP, anchor='ne', pady=(0, 24))
        #
        # frameContainer = ttk.Frame(self, padding=8)
        # frameContainer.pack(expand=1, fill=BOTH)

        font = {
            'size': 8
        }

        matplotlib.rc('font', **font)

        # create a figure
        self.figure = Figure(figsize=(10, 5), dpi=120)

        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)

        # create the toolbar
        NavigationToolbar2Tk(self.figure_canvas, self)

        # create axes
        self.axes = self.figure.add_subplot()

        self.createBarGraph('cases_by_region', 'Cases by Region', 'Number of Cases', rotate=True, rotation=15)

    def createBarGraph(self, fileName, title, yAxisLabel, rotate=False, rotation=45,
                       alignment='right', sort=False, trimLabels=False):
        file = open(f'./JSONData/{fileName}.json')
        data = json.load(file)



        trimmed = {}
        if trimLabels:

            # sort data by date
            sort_data = sorted(data.items(), key=lambda x: int(x[1]), reverse=True)

            for x in sort_data:
                newLabel = x[0].split(':')

                if len(newLabel) > 1:
                    trimmed[newLabel[1]] = x[1]
                else:
                    trimmed[newLabel[0]] = x[1]

        if sort:
            # sort data by date
            data = OrderedDict(sorted(data.items(), key=lambda t: int(t[0][0:2])))

        # create the barchart
        if trimLabels:
            self.axes.bar(trimmed.keys(), trimmed.values(), color='#94e2d5')
        else:
            self.axes.bar(data.keys(), data.values(), color='#94e2d5')

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
            if trimLabels:
                self.axes.set_xticklabels(trimmed.keys(), rotation=rotation, ha=alignment)
            else:
                self.axes.set_xticklabels(data.keys(), rotation=rotation, ha=alignment)

        self.axes.grid(True, color='#313244')

        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    def filterCases(self, event):
        self.axes.clear()

        match event.widget.get():
            case 'Region':
                self.createBarGraph('cases_by_region', 'Cases by Region', 'Number of Cases', rotate=True, rotation=15, trimLabels=True)
            case 'Province':
                self.createBarGraph('cases_by_province', 'Cases by Province', 'Number of Cases', rotate=True)
            case 'Age Group':
                self.createBarGraph('cases_by_age_group', 'Cases by age group', 'Number of Cases', sort=True)
            case 'Sex':
                self.createBarGraph('cases_by_sex', 'Cases by Sex', 'Number of Sex')

        self.figure_canvas.draw() 

        event.widget.select_clear()
