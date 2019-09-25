import csv
import numpy as np
import pandas as pd

dataFrame = pd.read_csv('DRD2_subset_data.csv', delimiter=',')#dtype={'AGE':float,'female_1':float, 'P':float, 'Q':float, 'VS':float, 'Obesity':float, 'LABID':float})
#data = dataFrame.dropna(subset=['P','Q','VS','DRD2'])
#data = dataFrame.dropna()


#dataFrame[~dataFrame.isin(['NaN', 'NaT']).any(axis=1)]

dataFrame.replace('        NaN', 'NaN')
dataFrame = dataFrame.dropna()

#dataFrame.isnull().describe(pd.set_option('display.max_rows',466))
print(dataFrame)