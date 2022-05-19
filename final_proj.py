import tkinter as tk
from tkinter import ttk
from tkinter import *
import platform


class Tabs(ttk.Notebook):
    def __init__(self, container):
        super().__init__(container, style='lefttab.TNotebook')

        summaryTab = ttk.Frame(self, style='lefttab.TNotebook')
        regionTab = ttk.Frame(self, style='lefttab.TNotebook')
        dateTab = ttk.Frame(self, style='lefttab.TNotebook')
        self.add(summaryTab, text='Summary')
        self.add(regionTab, text='Region')
        self.add(dateTab, text='Date')

        label1 = Label(regionTab, text='test')
        label1.pack()

        self.pack(expand=1, fill="both")


# root
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('COVID Data')
        if platform.system() == 'Windows':
            self.state('zoomed')
        else:
            self.attribute('zoomed', True)

        style = ttk.Style(self)
        style.configure('lefttab.TNotebook', tabposition='wn')
        style.configure('TNotebook.Tab', width=15)

        tabs = Tabs(self)


if __name__ == '__main__':
    app = App()
    app.mainloop()
