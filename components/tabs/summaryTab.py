from tkinter import ttk
import json
import matplotlib
from components.dashboardCard import DashboardCard

matplotlib.use('TkAgg')

f = open('./JSONData/cases_summary.json')
summaryData = json.load(f)

class SummaryTab(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, padding=12, style='tabFrame.TFrame')

        spacing = 12

        dashboardCards = [
            {
                'title': 'Total Cases',
                'data': self.addCommas(summaryData['cases']),
                'accentColor': '#94e2d5'
            },
            {
                'title': 'Active Cases',
                'data': self.addCommas(summaryData['active']),
                'accentColor': '#94e2d5'
            },
            {
                'title': 'Recovered Cases',
                'data': self.addCommas(summaryData['recovered']),
                'accentColor': '#f9e2af'
            },
            {
                'title': 'Recovery Rate',
                'data': f"{summaryData['recovery_rate']}%", 
                'accentColor': '#f9e2af'
            },
            {
                'title': 'Death Cases', 
                'data': self.addCommas(summaryData['deaths']),
                'accentColor': '#cba6f7'
            },
            {
                'title': 'Fatality Rate', 
                'data': f"{summaryData['fatality_rate']}%",
                'accentColor': '#cba6f7'
            }
        ]
        
        i = 0
        column = 2
        row = 3
        for y in range(row):
            for x in range(column):
                dashboardCard = DashboardCard(self, dashboardCards[i]['title'], dashboardCards[i]['data'], dashboardCards[i]['accentColor'])
                dashboardCard.grid(column=x, row=y, padx=spacing, pady=spacing, sticky='nsew')
                i += 1
            if i == len(dashboardCards):
                break

        self.columnconfigure(tuple(range(column)), weight=1)
        self.rowconfigure(tuple(range(row)), weight=1)


    def addCommas(self, number):
        return '{:,}'.format(number)