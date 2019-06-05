
# coding: utf-8

# In[183]:

groups = ['HIGHPI', 'CNFD','CNFDPI', 'INTL']
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


# In[141]:

matched_list = []
for i in df2:
    for j in classwords_dict.keys():
        if str(i).__contains__(j):
            matched_list.append(i)        


# In[108]:

result = classwords_DF[classwords_DF.Logical_Name.isin(matched_list)]


# In[142]:

len(matched_list)


# In[175]:

HIGHPI_Df = pd.DataFrame()
highpi_list = []
cnfd_list = []


# In[101]:

#result


# In[182]:

classwords_dict1.values()


# In[184]:

for i in groups:
    for key, value in classwords_dict1.items():
        if key == 'Rate':            
            if i == 'HIGHPI':                
                for jk in value[i]:                   
                    for kkk in matched_list:
                        if kkk.__contains__(jk):                            
                            highpi_list.append(kkk)
            elif i == 'CNFD':
                for jk in value[i]:                   
                    for kkk in matched_list:
                        if kkk.__contains__(jk):                            
                            cnfd_list.append(kkk)

            
        
        
    


# In[177]:

highpi_result = classwords_DF[classwords_DF.Logical_Name.isin(highpi_list)]


# In[178]:

cnfd_result = classwords_DF[classwords_DF.Logical_Name.isin(cnfd_list)]


# In[179]:

cnfd_list_result


# In[180]:

cnfd_list


# In[ ]:



