from datetime import datetime
from tkinter import *
import tkinter as tk
from tkinter import ttk
import json
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from components.DashboardCard import DashboardCard

matplotlib.use('TkAgg')


f = open('./JSONData/cases_summary.json')
summaryData = json.load(f)


class Tabs(ttk.Notebook):
    def __init__(self, container):
        super().__init__(container, style='lefttab.TNotebook')

        summaryTab = SummaryTab(self)
        newCasesTab = BreakdownTab(self)
        timelineTab = TimelineTab(self)
        self.add(summaryTab, text='Summary')
        self.add(newCasesTab, text='Breakdown')
        self.add(timelineTab, text='Timeline')


class SummaryTab(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, padding=12, style='tabFrame.TFrame')

        spacing = 12

        totalCasesCard = DashboardCard(self, title='Total Cases', data=self.addCommas(summaryData['cases']))
        totalCasesCard.grid(padx=spacing, pady=spacing)

        activeCasesCard = DashboardCard(self, title='Active Cases', data=self.addCommas(summaryData['active']))
        activeCasesCard.grid(row=0, column=1, padx=spacing, pady=spacing)

        recoveredCasesCard = DashboardCard(self, title='Recovered Cases', data=self.addCommas(summaryData['recovered']), accentColor='#f9e2af')
        recoveredCasesCard.grid(row=1, padx=spacing, pady=spacing)

        recoveryRateCard = DashboardCard(self, title='Recovery Rate', data=f"{summaryData['recovery_rate']}%", accentColor='#f9e2af')
        recoveryRateCard.grid(row=1, column=1, padx=spacing, pady=spacing)

        deathCasesCard = DashboardCard(self, title='Death Cases', data=self.addCommas(summaryData['deaths']), accentColor='#cba6f7')
        deathCasesCard.grid(row=2, padx=spacing, pady=spacing)

        fatalityRateCard = DashboardCard(self, title='Fatality Rate', data=f"{summaryData['fatality_rate']}%", accentColor='#cba6f7')
        fatalityRateCard.grid(row=2, column=1, padx=spacing, pady=spacing)

    def addCommas(self, number):
        return '{:,}'.format(number)


class BreakdownTab(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, padding=24)

        # filterComboList = ['Filter by', 'Age Group', 'Sex', 'Region', 'Province']
        # filterCombobox = ttk.Combobox(self, state="readonly", values=filterComboList)
        # filterCombobox.current(0)
        # filterCombobox.bind("<<ComboboxSelected>>", lambda e: filterCombobox.select_clear())
        # filterCombobox.pack(side=TOP, anchor='ne')
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
        # self.createBarGraph('cases_by_province', 'Cases by Province', 'Number of Cases', rotate=True)
        # self.createBarGraph('cases_by_age_group', 'Cases by age group', 'Number of Cases')
        # self.createBarGraph('cases_by_sex', 'Cases by Sex', 'Number of Sex')

        # call this method to create a graph

    def createBarGraph(self, fileName, title, yAxisLabel, rotate=False, rotation=45, alignment='right'):
        file = open(f'./JSONData/{fileName}.json')
        data = json.load(file)

        # create the barchart
        self.axes.bar(data.keys(), data.values())
        self.axes.set_title(title)
        self.axes.set_ylabel(yAxisLabel)

        if rotate:
            self.axes.set_xticklabels(data.keys(), rotation=rotation, ha=alignment)

        self.axes.grid(True)

        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


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


# root
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('COVID Data')
        # self.geometry('1024x720+200+200')

        # if platform.system() == 'Windows':
        #     self.state('zoomed')
        # else:
        #     self.attributes('-zoomed', True)

        self.tk.call("source", "sun-valley.tcl")
        self.tk.call("set_theme", "dark")

        style = ttk.Style(self)
        # style.configure('lefttab.TNotebook', tabposition='wn')
        # style.configure('TNotebook.Tab', width=15)
        style.configure('dashboardCard.TFrame', background='#1e1e2e')
        style.configure('tabFrame.TFrame', background='#181825')

        tabs = Tabs(self)
        tabs.pack(expand=1, fill="both")


if __name__ == '__main__':
    app = App()
    app.mainloop()

