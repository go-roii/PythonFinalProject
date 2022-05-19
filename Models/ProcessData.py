import pandas as pd
import os

# assign directory
directory = './'

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)

# data = pd.read_csv('../files/input.csv')
# print (data)