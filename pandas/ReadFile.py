import pandas as pd
import os
current_directory = os.getcwd()
readData = pd.read_csv(current_directory+'/pandas/test.csv')
print(readData.info())
# print(readData.head())