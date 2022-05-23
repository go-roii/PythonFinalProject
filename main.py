import tkinter as tk
from tkinter import ttk
from tkinter import *
import platform
import json


f = open('./JSONData/cases_summary.json')
summaryData = json.load(f)


class Tabs(ttk.Notebook):
    def __init__(self, container):
        super().__init__(container, style='lefttab.TNotebook')

        spacing = 8

        summaryTab = ttk.Frame(self, style='lefttab.TNotebook', padding=spacing)
        regionTab = ttk.Frame(self, style='lefttab.TNotebook', padding=spacing)
        dateTab = ttk.Frame(self, style='lefttab.TNotebook', padding=spacing)
        self.add(summaryTab, text='Summary')
        self.add(regionTab, text='Region')
        self.add(dateTab, text='Date')

        totalCasesCard = DashboardCard(summaryTab, title='Total Cases', data=summaryData['cases'])
        totalCasesCard.grid(padx=spacing, pady=spacing)

        activeCasesCard = DashboardCard(summaryTab, title='Active Cases', data=summaryData['active'])
        activeCasesCard.grid(row=0, column=1, padx=spacing, pady=spacing)

        recoveredCasesCard = DashboardCard(summaryTab, title='Recovered Cases', data=summaryData['recovered'])
        recoveredCasesCard.grid(row=1, padx=spacing, pady=spacing)

        recoveryRateCard = DashboardCard(summaryTab, title='Recovery Rate', data=f"{summaryData['recovery_rate']}%")
        recoveryRateCard.grid(row=1, column=1, padx=spacing, pady=spacing)

        deathCasesCard = DashboardCard(summaryTab, title='Death Cases', data=summaryData['deaths'])
        deathCasesCard.grid(row=2, padx=spacing, pady=spacing)

        fatalityRateCard = DashboardCard(summaryTab, title='Fatality Rate', data=f"{summaryData['fatality_rate']}%")
        fatalityRateCard.grid(row=2, column=1, padx=spacing, pady=spacing)


class DashboardCard(tk.Frame):
    def __init__(self, container, title, data):
        super().__init__(
            container,
            bg='#44475a',
            height=200,
            width=400,
            padx=20,
            pady=20
        )
        self.pack_propagate(0)

        titleLabel = Label(self, text=title, font='arial 14', bg='#44475a', fg='#f8f8f2')
        titleLabel.pack(anchor='w')

        graph = Frame(self, bg='#44475a')
        graph.pack(expand=1, fill=BOTH)

        dataLabel = Label(graph, text=data, font='arial 18 bold', bg='#44475a', fg='#f8f8f2')
        dataLabel.pack(expand=1)


# root
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('COVID Data')
        # if platform.system() == 'Windows':
        #     self.state('zoomed')
        # else:
        #     self.attributes('-zoomed', True)

        # wthm = ttk.Style()
    
        # wthm.theme_create('wtheme', parent='default', settings=
        # {
        #     'TNotebook.Tab': {
        #         'configure': {'focuscolor':{
        #                             'configure':{
        #                                 '.':'#f00'}
        #                         }}
        #     }
        # })

        # wthm.theme_use('wtheme')

        style = ttk.Style(self)
        style.configure('lefttab.TNotebook', tabposition='wn', background='#282a36', borderwidth=0, padding=4)
        style.configure('TNotebook.Tab', width=15, borderwidth=0, tearoff='off')

        tabs = Tabs(self)
        tabs.pack(expand=1, fill="both")


if __name__ == '__main__':
    app = App()
    app.mainloop()
