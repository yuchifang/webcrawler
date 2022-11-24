import pandas as pd
import os
current_directory = os.getcwd()
print(current_directory)
readData = pd.read_csv(current_directory+'/test.csv')
print(readData)