#!/usr/bin/env python
# coding: utf-8

# ---
# # Split `from-to` user pairs

# In[5]:


# Loading Libraries
import pandas as pd
import numpy as np
from tabulate import tabulate

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split as ttsplit
import constants

RANDOM_STATE = 53


# In[6]:


# Loading Data
df = pd.read_csv('test.csv')
df.shape, df.head()


# In[7]:


# finding datatypes
df.dtypes


# In[8]:


#Separating the `from-to` column
temp = np.array(df['from-to'].apply(lambda x: x.split('-')).to_list())
df['userA_id'] = temp[:, 0]
df['userB_id'] = temp[:, 1]
df.head()


# In[11]:


# Writing csv
df.to_csv(constants.OUTPUT_FILE,
                index=False,
                header=True)

