import json
import platform
import tkinter as tk
from datetime import datetime
from tkinter import ttk
from components.tabs.configurationTab import ConfigurationTab
import os


class Tabs(ttk.Notebook):
    def __init__(self, container):
        super().__init__(container, style='lefttab.TNotebook')


# root
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('COVID Data Tracker')
        # self.geometry('1024x720+200+200')

        if platform.system() == 'Windows':
            self.state('zoomed')
        else:
            self.attributes('-zoomed', True)

        self.tk.call("source", "sun-valley.tcl")
        self.tk.call("set_theme", "dark")

        style = ttk.Style(self)
        style.configure('dashboardCard.TFrame', background='#1e1e2e')
        style.configure('tabFrame.TFrame', background='#181825')

        tabs = Tabs(self)

        # Path
        path = './JSONData/last_update.json'

        # Check whether the
        # specified path is
        # an existing file
        isFile = os.path.isfile(path)
        print(isFile)

        if isFile:
            from components.tabs.summaryTab import SummaryTab
            from components.tabs.breakdownTab import BreakdownTab
            from components.tabs.timelineTab import TimelineTab
            summaryTab = SummaryTab(tabs)
            newCasesTab = BreakdownTab(tabs)
            timelineTab = TimelineTab(tabs)
            tabs.add(summaryTab, text='Summary')
            tabs.add(newCasesTab, text='Breakdown')
            tabs.add(timelineTab, text='Timeline')

            f = open('./JSONData/last_update.json')
            lastUpdateData = json.load(f)

            date = datetime.strptime(lastUpdateData['last_update'], '%B %d, %Y').strftime('%B %d, %Y')
            print(lastUpdateData)

            asOfDateLabel = ttk.Label(self, text=f'COVID Data updated as of {date}', font='arial 10 italic')
            asOfDateLabel.pack(anchor='e', padx=(0, 6))

        configurationTab = ConfigurationTab(tabs)
        tabs.add(configurationTab, text='Configuration')

        tabs.pack(expand=1, fill="both")


if __name__ == '__main__':
    app = App()
    app.mainloop()
