#!/usr/bin/env python
# coding: utf-8

# # Task-3: Exploratory Data Analysis - Retail

# ### import libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### Reading the data from the dataset

# In[4]:


data = pd.read_csv(r"C:\Users\Ashok\Documents\data science\SampleSuperstore.csv")
data.head()


# ### Exploring the Data

# In[5]:


data.info()


# In[6]:


data.describe()


# ### Checking for null values in the dataset

# In[7]:


data.isnull().sum()


# In[8]:


data.shape


# ### Checking for duplicates in the dataset

# In[9]:


sum(data.duplicated(subset = None, keep = 'first'))


# ### We can notice that there are 17 duplicate rows in out dataset. Let's remove those rows before moving further.

# In[10]:


data.drop_duplicates(subset = None, keep = 'first', inplace = True)


# ### Thus now only 13 rows are remaning which all are non duplicate

# In[11]:


data.shape


# In[12]:


def getUnique(data,  target_variable, sort_by, color, threshold_categories = 10):
    
    total_cols = [i for i in data.columns.values if len(data[i].unique()) < threshold_categories and len(data[i].unique()) > 1]
    
    fig = plt.figure(figsize = (20,20))
    rows = len(total_cols) // 2
    cols = len(total_cols) // 2
    
    for i, num in zip(total_cols, range(1,len(total_cols)+1)):
        ax = fig.add_subplot(rows,cols,num)
        data.groupby(i)[target_variable].sum().sort_values(by = sort_by, ascending = False).plot(kind = 'bar', ax = ax, title = i, color = color)

    plt.tight_layout(pad = 3.0)
    plt.show()


# In[15]:


num_categories = 20
target_variable = ["Sales","Profit"]
sort_by = "Sales"
color = ["black", "red"]
getUnique(data, target_variable, sort_by, color, num_categories)


# ## OBSERVATION:
# 

# ##### 1) The profits for Tables and Bookcases sub-category are very less but the profit for Copiers is very high. So, we should focus on increasing the sales of the copiers.

# #### 2) The profits for the Office Supplies is high, but the sales of the Office Supplies is less. So, we should focus on increasing the sales for Office Supplies.
# 
# 

# In[16]:


data.State.unique()


# In[17]:


plt.rcParams["figure.figsize"] = [25,10]
data.groupby("State")[["Sales", "Profit"]].sum().sort_values(by = "Sales", ascending = False).plot(kind = "bar", color = ["black", "blue"])
plt.title("Sales and Profits for each State")
plt.show()


# ### OBSERVATION: The states with high sales are generating less profit.
# 
# 

# In[18]:


data.groupby("State").sum()['Discount'].sort_values(ascending = False)


# ### By comparing the barplot and the above dataframe, we can observe that the states that are offered high discounts are generating less profit.

# In[19]:


states_df = data.groupby("State")[["Sales","Profit","Discount"]].sum().sort_values(by = "Sales", ascending = False)
states_df


# In[20]:


states_df['Discount'][states_df['Profit'] < 0].sort_values(ascending = True)


# ### The states with less profit are allowed with more Profit.
# 
# 

# In[21]:


sns.lineplot(x = "Discount", y = "Profit", data = data, color = "blue")
plt.show()


# In[ ]:




