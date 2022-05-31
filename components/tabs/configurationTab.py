import pandas as pd
import os
import numpy as np
from matplotlib import pyplot as plt
import json
from datetime import datetime
from cProfile import label
import tkinter as tk
from tkinter import ttk, filedialog


class ConfigurationTab(ttk.Frame):

    summary = {
        'cases': 0,
        'active': 0,
        'recovered': 0,
        'deaths': 0,
        'fatality_rate': '',
        'recovery_rate': '',
    }

    time_series = []

    # assign directory
    directory = ''

    # iterate over files in
    # that directory
    files = []

    def __init__(self, container):
        super().__init__(container, padding=12, style='tabFrame.TFrame')
        self.selected_folder = ''

        labelFrame = ttk.LabelFrame(self, text='Select data directory', padding=20)

        selectDataDirectoryButton = ttk.Button(labelFrame, text='Select', command=self.getDirectory)
        selectDataDirectoryButton.pack(pady=(0, 12))

        labelFrame.pack(expand=1, anchor='s', pady=(0, 24))

        labelFrame2 = ttk.LabelFrame(self, text='Process Data', padding=20)

        self.directoryLabel = ttk.Label(labelFrame2, text='no folder selected yet...', font=('arial 10 italic'), padding=(0, 0, 0, 12))
        self.directoryLabel.pack()

        processData = ttk.Button(labelFrame2, text='Process', command=self.processData)
        processData.pack(pady=(0, 12))

        labelFrame2.pack(expand=1, anchor='n')

    def getDirectory(self):
        self.selected_folder = filedialog.askdirectory()
        self.directoryLabel.config(text=self.selected_folder)
        self.directory = self.selected_folder

    def writeJSON(self, data, fileName, decode=True):

        if decode:
            jsonString = json.dumps(json.JSONDecoder().decode(data), indent=4)
        else:
            jsonString = json.dumps(data, indent=4)

        # jsonfile = open(f'/../JSONData/{fileName}.json', 'w')
        jsonfile = open(f'./JSONData/{fileName}.json', 'w')

        jsonfile.write(jsonString)
        jsonfile.close()

    def processData(self):
        for filename in os.listdir(self.selected_folder):
            f = os.path.join(self.selected_folder, filename)
            # checking if it is a file
            if os.path.isfile(f):
                path = f

                # add the files reference to files list
                self.files.append(f'{path}')

        # print(files)
        result = pd.concat([pd.read_csv(f, low_memory=False, skip_blank_lines=True, parse_dates=True,
                                        infer_datetime_format=True, na_values=[], na_filter=True) for f in self.files],
                           ignore_index=True)

        self.summary['cases'] = int(len(result.axes[0]))
        self.summary['recovered'] = int(result[result.RemovalType == 'RECOVERED'].shape[0])
        self.summary['deaths'] = int(result[result.RemovalType == 'DIED'].shape[0])
        self.summary['active'] = int(result['RemovalType'].isna().sum())
        self.summary['fatality_rate'] = float(round((self.summary['deaths'] / self.summary['recovered']) * 100, 2))
        self.summary['recovery_rate'] = float(round((self.summary['recovered'] / self.summary['cases']) * 100, 2))

        result['DateRepConf'] = pd.to_datetime(result['DateRepConf']).dt.strftime('%b. %Y')

        # result['DateRepConf'].dt.strftime('%m/%Y')
        # # time_series = result['DateRepConf'].to_json(orient='records')

        # sample dataframe
        df = pd.DataFrame(result)
        cases_by_month_count = df['DateRepConf'].value_counts().to_json()
        cases_by_region_count = df['RegionRes'].value_counts().to_json()
        cases_by_province_count = df['ProvRes'].value_counts().to_json()
        cases_by_age_group = df['AgeGroup'].value_counts().to_json()
        cases_by_sex = df['Sex'].value_counts().to_json()

        self.writeJSON(self.summary, 'cases_summary', False)
        self.writeJSON(cases_by_month_count, 'cases_by_month')
        self.writeJSON(cases_by_region_count, 'cases_by_region')
        self.writeJSON(cases_by_province_count, 'cases_by_province')
        self.writeJSON(cases_by_age_group, 'cases_by_age_group')
        self.writeJSON(cases_by_sex, 'cases_by_sex')


