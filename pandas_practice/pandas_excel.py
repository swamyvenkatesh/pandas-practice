import pandas as pd

data1 = pd.read_excel('/home/swamy/Documents/Sample_pandas_data.xlsx') 
# read_excel() method is used to read data from excel file in pandas
print "^^"*20
print data1
# ================ output =================
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#    S.NO    NAMES   COLLEGE
# 0     1  SUNITHA      BSIT
# 1     2   ANITHA      CSIT
# 2     3  NAMITHA     JNTUH
# 3     4  KAIVTHA      MIST
# 4     5     RAVI      CBIT
# 5     6    SWAMY      KIET
# 6     7  SUNITHA    OXFORD
# 7     8     RAVI  NARAYANA
# 8     9    SWAMY        PR
# 9    10  SUNITHA        DQ
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
data = pd.read_excel('/home/swamy/Documents/Sample_pandas_data.xlsx', sheet_name=0,index_col=0) 

# we have many parameters for read_excel, in those few are following(filepath, sheetname=1,index_col=0)
print "^^"*20
print data.head()
# head() method can return first five rows from read data
# ========== output =========
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#         NAMES COLLEGE
# S.NO                 
# 1     SUNITHA    BSIT
# 2      ANITHA    CSIT
# 3     NAMITHA   JNTUH
# 4     KAIVTHA    MIST
# 5        RAVI    CBIT
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# print data

print data.head()[2:6]
# head()[2:6] - slicing concept used to get particular rows
# ========= ouput is ============
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#         NAMES COLLEGE
# S.NO                 
# 3     NAMITHA   JNTUH
# 4     KAIVTHA    MIST
# 5        RAVI    CBIT
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


print "^^"*20
print data.tail()
# tail() method can return last(from bottom) five rows from read data
#============== output =================
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#         NAMES   COLLEGE
# S.NO                   
# 6       SWAMY      KIET
# 7     SUNITHA    OXFORD
# 8        RAVI  NARAYANA
# 9       SWAMY        PR
# 10    SUNITHA        DQ
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
print data1.shape
# shape can return number of rows and columns
# ====== output is ============
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(10, 3)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sorted_by_gross = data.sort_values(['NAMES'], ascending=True)
# sorted_by_gross = data.sort_values(['NAMES'], ascending=False)

# sorted_by_gross["Gross Earnings"].head(10)
# 
print sorted_by_gross['NAMES'].head()

# =========== output is ==============
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# 2     ANITHA
# 4    KAIVTHA
# 3    NAMITHA
# 5       RAVI
# 8       RAVI
# Name: NAMES, dtype: object
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
