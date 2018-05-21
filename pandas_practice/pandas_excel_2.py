import pandas as pd

data_file = '/home/swamy/Documents/Sample_pandas_data.xlsx'
data1 = pd.ExcelFile(data_file) 
# read_excel() method is used to read data from excel file in pandas
print "^^"*20
df = pd.DataFrame(data1)
# print data1.parse()
# parse() is used to get all data from excel file
print df