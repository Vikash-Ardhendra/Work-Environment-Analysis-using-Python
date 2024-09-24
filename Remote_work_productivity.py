#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


# In[2]:


df = pd.read_csv('C://Users//DELL//Downloads//remote_work_productivity.csv')
df


# In[3]:


df.describe()


# In[4]:


df.isna().sum()


# ### Label Encoding

# In[5]:


df['Employment_Type'] = df['Employment_Type'].astype('category').cat.codes
df


# In[6]:


data = df.iloc[:,1:]
data


# In[7]:


sns.displot(df['Productivity_Score'])
plt.show()


# In[8]:


sns.displot(df['Hours_Worked_Per_Week'])
plt.show()


# In[9]:


sns.boxplot(data['Well_Being_Score'])
plt.show()


# In[10]:


sns.boxplot(data['Productivity_Score'])
plt.show()


# ### Checking the employee working hours whose Productive_Score is between 80 to 100

# In[11]:


a = df[(df['Productivity_Score']>=80) &(df['Productivity_Score']<=100)]
display(a)


# In[12]:


sns.boxplot(a['Hours_Worked_Per_Week'])
plt.show()


# ### Removing Outliers

# In[13]:


q1 = data['Productivity_Score'].quantile(0.25)
q3 = data['Productivity_Score'].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr


# In[14]:


ds = data[(data['Productivity_Score'] >= lower)  & (data['Productivity_Score'] <= upper)]
ds


# In[15]:


sns.boxplot(ds['Productivity_Score'])
plt.show()


# In[16]:


q1 = data['Well_Being_Score'].quantile(0.25)
q3 = data['Well_Being_Score'].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr


# In[17]:


ds = ds[(ds['Well_Being_Score'] >= lower)  & (data['Well_Being_Score'] <= upper)]
ds


# In[18]:


sns.boxplot(ds['Well_Being_Score'])
plt.show()


# In[19]:


ds.describe()


# In[20]:


plt.figure(figsize=(20,20))
sns.catplot(data = ds, x = 'Hours_Worked_Per_Week', y = 'Productivity_Score',hue= 'Employment_Type')
plt.show()


# In[21]:


b = ds[ds['Hours_Worked_Per_Week']<=40]


# In[22]:


b.describe()


# In[23]:


ds_corr = ds.corr()
ds_corr


# In[24]:


# There is no correlation between variables


# In[25]:


sns.boxplot(data = b, x = 'Employment_Type', y = 'Productivity_Score')
plt.show()


# In[26]:


sns.boxplot(data = b, x = 'Employment_Type', y = 'Well_Being_Score')
plt.show()


# In[27]:


sns.boxplot(data = b, x = 'Employment_Type', y = 'Hours_Worked_Per_Week')
plt.show()
# In Remote working type, majority of employees work between 30 to 35 hours


# In[28]:


plt.figure(figsize=(20,9.5))
sns.barplot(data = b, hue = 'Employment_Type', x = 'Hours_Worked_Per_Week',y='Productivity_Score')
plt.show()


# In[29]:


plt.figure(figsize=(15,4))
sns.pointplot(data = b, hue = 'Employment_Type', x = 'Hours_Worked_Per_Week',y='Productivity_Score')
plt.show()
plt.figure(figsize=(15,4))
sns.pointplot(data = b, hue = 'Employment_Type', x = 'Hours_Worked_Per_Week',y='Well_Being_Score')
plt.show()


# In[30]:


for x in [29,30,31,32,33,34,35]:
    c = ds[(ds['Hours_Worked_Per_Week']==x) & (ds['Employment_Type']==1)].sum()
    print(x,'hours:',c)


# ### From the graph analysis,
# 1. Employee who works in Remote work type has high productivity and well being scores.
# 
# 2. Most of the remote type employees work between 30 to 35 hours per week.
# 
# 3. In that employees who work for 34 hours per week has the highest average productivity score and well being score based on dividing the productivity score / head count and Well_being_score / head count.
#  Eg : 34 hours : 1764 / 24 & 1748 / 24
# 
# 4. I suggest company to follow  34 hours work per week &  remote type employment. 
