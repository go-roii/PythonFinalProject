# import pandas as pd
# import os
# import numpy as np
# from matplotlib import pyplot as plt
# import json
# from datetime import datetime
#
# summary = {
#     'cases': 0,
#     'active': 0,
#     'recovered': 0,
#     'deaths': 0,
#     'fatality_rate': '',
#     'recovery_rate': '',
# }
#
# time_series = []
#
# # assign directory
# directory = '../files'
#
# # iterate over files in
# # that directory
# files = []
#
# for filename in os.listdir(directory):
#
#     f = os.path.join(directory, filename)
#     # checking if it is a file
#     if os.path.isfile(f):
#         path = f.split('files')[1]
#
#         # add the files reference to files list
#         files.append(f'../files/{path}')
#
#         # print(path)
#
# # print(files)
# result = pd.concat([pd.read_csv(f, low_memory=False, skip_blank_lines=True, parse_dates=True,
#                                 infer_datetime_format=True, na_values=[], na_filter=True) for f in files], ignore_index=True)
#
# summary['cases'] = int(len(result.axes[0]))
# summary['recovered'] = int(result[result.RemovalType == 'RECOVERED'].shape[0])
# summary['deaths'] = int(result[result.RemovalType == 'DIED'].shape[0])
# summary['active'] = int(result['RemovalType'].isna().sum())
# summary['fatality_rate'] = float(round((summary['deaths']/summary['recovered'])*100, 2))
# summary['recovery_rate'] = float(round((summary['recovered']/summary['cases'])*100, 2))
#
# result['DateRepConf'] = pd.to_datetime(result['DateRepConf']).dt.strftime('%b. %Y')
#
# # result['DateRepConf'].dt.strftime('%m/%Y')
# # # time_series = result['DateRepConf'].to_json(orient='records')
#
# # sample dataframe
# df = pd.DataFrame(result)
# cases_by_month_count = df['DateRepConf'].value_counts().to_json()
# cases_by_region_count = df['RegionRes'].value_counts().to_json()
# cases_by_province_count = df['ProvRes'].value_counts().to_json()
# cases_by_age_group = df['AgeGroup'].value_counts().to_json()
# cases_by_sex = df['Sex'].value_counts().to_json()
#
#
# print(cases_by_age_group)
#
# # fig, ax = plt.subplots(figsize=(36, 10))
# # ax.plot(count, label="date")
# # ax.legend()
# #
# # plt.show()
#
#
# # def writeJSON(data, fileName, decode=True):
# #     jsonString = ''
# #
# #     if decode:
# #         jsonString = json.dumps(json.JSONDecoder().decode(data), indent=4)
# #     else:
# #         jsonString = json.dumps(data, indent=4)
# #
# #     jsonfile = open(f'../JSONData/{fileName}.json', 'w')
# #     jsonfile.write(jsonString)
# #     jsonfile.close()
#
#
# writeJSON(summary, 'cases_summary', False)
# writeJSON(cases_by_month_count, 'cases_by_month')
# writeJSON(cases_by_region_count, 'cases_by_region')
# writeJSON(cases_by_province_count, 'cases_by_province')
# writeJSON(cases_by_age_group, 'cases_by_age_group')
# writeJSON(cases_by_sex, 'cases_by_sex')
#
#
# # f = open('millions.json')
# # data = json.load(f)
# #
# #
# # # series = np.array(a)
# #
# # fig, ax = plt.subplots(figsize=(36, 10))
# # ax.hist(data, bins=36)
# #
# # # Show plot
# # plt.show()
# #
# # # print(series)
