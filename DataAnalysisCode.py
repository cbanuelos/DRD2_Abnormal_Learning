import numpy as np

data = np.loadtxt('DRD2_subset_data.dat', 
					dtype = {'names': ('AGE','female_1', 'P', 'Q', 'VS','Obesity', 'DRD2','LABID'),
							 'formats':('S1', 'S1', 'S1', 'S1','S1', 'S1', 'S1', 'S1')},
					delimiter="	  ")
data
