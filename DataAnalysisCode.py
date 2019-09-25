import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot
import seaborn as sb

pd.set_option('display.max_columns', 8)




data = pd.read_csv('DRD2_subset_data.csv', delimiter=',')
data = data.dropna(subset=['P','Q','VS','DRD2'])


age_summary = data.AGE.describe()
sex_summary = data.female_1.describe()
all_summary = data.describe()


print('AGE\n', age_summary)
print('\nSEX\n', sex_summary)
print('\n\n', all_summary)

IGT_violin = sb.violinplot(data=data.iloc[:,2:4], palette='Blues')
VS_Ob_violin = sb.violinplot(data=data.iloc[:,4:6], palette='Blues')
AGE_violin = sb.violinplot(y='AGE', data=data, palette='Blues')

IGT_violin
VS_Ob_violin
AGE_violin
pyplot.show()
# if DRD2 == 1, subjects are DRD2 deletion carriers --> low D2 receptors --> High DA
# if DRD2 == 0, subjects are DRD2 insertion carriers --> normal D2 receptors --> Low DA

