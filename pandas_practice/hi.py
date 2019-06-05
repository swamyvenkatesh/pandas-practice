
# coding: utf-8

# In[100]:

classwords_list = ['Rate']
groups = ['']
classwords_dict1 = {'Rate':{ 
                            'HIGHPI':['Credit Bureau'],
                            'CNFD':['Basel','Federal','Credit']
                        }
                  }
classwords_dict = {'Rate':['Credit Bureau','Basel','Federal','Credit']}


# In[43]:

classwords_list


# In[44]:

import pandas as pd


# In[45]:

classwords_DF = pd.read_excel(r'I:\\code\\MT\\DataOps.xlsx',sheetname='Sheet1')


# In[46]:

colnames = ['Table Name','Column Name','Logical_Name','Data Type','Definition']


# In[50]:

classwords_DF.head(3)


# In[51]:

df2 = classwords_DF['Logical_Name']


# In[52]:

df3 = classwords_DF[classwords_DF.Logical_Name.isin(classwords_list)]


# In[107]:

matched_list = []
credit_bureau_list = []
for i in df2:
    for j in classwords_dict.keys():
        if str(i).__contains__(j):
            matched_list.append(i)
        #print (classwords_dict[j])
        for kk in matched_list:
            for value in classwords_dict[j]:
                if str(kk).__contains__(value):
                    #print (kk)
                    credit_bureau_list.append(kk)
                        

       


# In[108]:

result = classwords_DF[classwords_DF.Logical_Name.isin(matched_list)]


# In[104]:

len(matched_list)


# In[110]:

len(list(set(credit_bureau_list)))


# In[101]:

#result


# In[ ]:



