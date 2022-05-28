from tkinter import *
import tkinter as tk
from tkinter import ttk
import platform
import json
from turtle import back, bgcolor


from components.DashboardCard import DashboardCard


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
        super().__init__(container, padding=24)

        spacing = 8

        label = tk.Label(self, text='tae')

        totalCasesCard = DashboardCard(self, title='Total Cases', data=summaryData['cases'])
        totalCasesCard.grid(padx=spacing, pady=spacing)

        activeCasesCard = DashboardCard(self, title='Active Cases', data=summaryData['active'])
        activeCasesCard.grid(row=0, column=1, padx=spacing, pady=spacing)

        recoveredCasesCard = DashboardCard(self, title='Recovered Cases', data=summaryData['recovered'])
        recoveredCasesCard.grid(row=1, padx=spacing, pady=spacing)

        recoveryRateCard = DashboardCard(self, title='Recovery Rate', data=f"{summaryData['recovery_rate']}%")
        recoveryRateCard.grid(row=1, column=1, padx=spacing, pady=spacing)

        deathCasesCard = DashboardCard(self, title='Death Cases', data=summaryData['deaths'])
        deathCasesCard.grid(row=2, padx=spacing, pady=spacing)

        fatalityRateCard = DashboardCard(self, title='Fatality Rate', data=f"{summaryData['fatality_rate']}%")
        fatalityRateCard.grid(row=2, column=1, padx=spacing, pady=spacing)


class BreakdownTab(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, padding=24)

        filterComboList = ['Filter by', 'Age Group', 'Sex', 'Region', 'Province']
        filterCombobox = ttk.Combobox(self, state="readonly", values=filterComboList)
        filterCombobox.current(0)
        filterCombobox.bind("<<ComboboxSelected>>", lambda e: filterCombobox.select_clear())
        filterCombobox.pack(side=TOP, anchor='ne')

        frameContainer = ttk.Frame(self, padding=8)
        frameContainer.pack(expand=1, fill=BOTH)

        
class TimelineTab(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, padding=24)
    

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

        tabs = Tabs(self)
        tabs.pack(expand=1, fill="both")


if __name__ == '__main__':
    app = App()
    app.mainloop()

