import tkinter as tk
from tkinter import ttk
from components.tabs.summaryTab import SummaryTab
from components.tabs.breakdownTab import BreakdownTab
from components.tabs.timelineTab import TimelineTab
from components.tabs.configurationTab import ConfigurationTab


class Tabs(ttk.Notebook):
    def __init__(self, container):
        super().__init__(container, style='lefttab.TNotebook')

        summaryTab = SummaryTab(self)
        newCasesTab = BreakdownTab(self)
        timelineTab = TimelineTab(self)
        configurationTab = ConfigurationTab(self)
        self.add(summaryTab, text='Summary')
        self.add(newCasesTab, text='Breakdown')
        self.add(timelineTab, text='Timeline')
        self.add(configurationTab, text='Configuration')


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

        asOfDateLabel = ttk.Label(self, text='COVID Data updated as of *date*', font='arial 10 italic')
        asOfDateLabel.pack(anchor='e')

        tabs = Tabs(self)
        tabs.pack(expand=1, fill="both")


if __name__ == '__main__':
    app = App()
    app.mainloop()
