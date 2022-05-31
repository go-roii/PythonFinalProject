from cProfile import label
import tkinter as tk
from tkinter import ttk, filedialog

class ConfigurationTab(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, padding=12, style='tabFrame.TFrame')

        labelFrame = ttk.LabelFrame(self, text='Select data directory', padding=20)

        selectDataDirectoryButton = ttk.Button(labelFrame, text='Select', command=self.getDirectory)
        selectDataDirectoryButton.pack(pady=(0, 12))

        labelFrame.pack(expand=1, anchor='s', pady=(0, 24))



        labelFrame2 = ttk.LabelFrame(self, text='Process Data', padding=20)

        self.directoryLabel = ttk.Label(labelFrame2, text='no folder selected yet...', font=('arial 10 italic'), padding=(0, 0, 0, 12))
        self.directoryLabel.pack()

        processData = ttk.Button(labelFrame2, text='Process')
        processData.pack(pady=(0, 12))

        labelFrame2.pack(expand=1, anchor='n')


    def getDirectory(self):
        self.selected_folder = filedialog.askdirectory()
        self.directoryLabel.config(text=self.selected_folder)

        