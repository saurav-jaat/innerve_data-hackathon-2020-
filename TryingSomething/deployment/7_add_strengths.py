#!/usr/bin/env python
# coding: utf-8

# ---
# # Dumping user wise strengths features train data

# In[6]:


# Loading Libraries
import pandas as pd
import numpy as np
from tabulate import tabulate

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split as ttsplit

import constants

RANDOM_STATE = constants.RANDOM_STATE


# In[7]:


# Loading training data
df_train = pd.read_csv(constants.OUTPUT_FILE)
print(df_train.shape)
df_train.head()


# ## Loading Lookup dataFrame
# 

# In[8]:


# Loading skills table to create a lookup to create feature from
df_strengths = pd.read_csv(constants.DATA_PATH+'user_strengths.csv')
df_strengths.head()


# In[9]:


# dropping duplicates
df_strengths.drop_duplicates(inplace=True)
df_strengths.dropna(axis=0, inplace=True)


# In[10]:


# Preview
df_strengths[ df_strengths['user_id']==151]


# ### Creating features

# In[11]:


# Dumping userA purposes
temp = df_strengths.add_prefix('userA_').rename(columns={'userA_user_id': 'userA_id'})
df_train = pd.merge(df_train, temp, how='outer', on='userA_id')
#
# Dumping userB purposes
temp = df_strengths.add_prefix('userB_').rename(columns={'userB_user_id': 'userB_id'})
df_train = pd.merge(df_train, temp, how='outer', on='userB_id')


# In[12]:


# Preview of new features
df_train.head()


# In[13]:


# Delaing with missing values
df_train = df_train.dropna(subset=['from-to']).fillna(0)


# In[14]:


# Preview of new features
df_train.head()


# --- 
# Writing to file
# ---

# In[15]:


# Writing to output
df_train.to_csv(constants.OUTPUT_FILE,
                index=False,
                header=True)

