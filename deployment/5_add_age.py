#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Loading Libraries
import pandas as pd
import numpy as np
from tabulate import tabulate

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split as ttsplit

import constants

RANDOM_STATE = constants.RANDOM_STATE


# ---
# # Dumping user wise age features train data

# In[2]:


# Loading training data
df_train = pd.read_csv(constants.OUTPUT_FILE)
print(df_train.shape)
df_train.head()


# ## Loading Lookup dataFrame
# 

# In[3]:


# Loading skills table to create a lookup to create feature from
df_age = pd.read_csv(constants.DATA_PATH+'user_ages.csv')
df_age.head()


# In[4]:


# dropping duplicates
df_age.drop_duplicates(inplace=True)
df_age.dropna(axis=0, inplace=True)


# In[5]:


# Preview
df_age[ df_age['user_id']==151]


# ### Creating features

# In[6]:


# Dumping userA purposes
temp = df_age.add_prefix('userA_').rename(columns={'userA_user_id': 'userA_id'})
df_train = pd.merge(df_train, temp, how='outer', on='userA_id')
#
# # Dumping userB purposes
temp = df_age.add_prefix('userB_').rename(columns={'userB_user_id': 'userB_id'})
df_train = pd.merge(df_train, temp, how='outer', on='userB_id')


# In[9]:


# Dealing with missing values
df_train = df_train.dropna(subset=['from-to']).fillna(0)


# In[10]:


# Preview of new features
df_train.head()


# --- 
# Writing to file
# ---

# In[11]:


# Writing to output
df_train.to_csv(constants.OUTPUT_FILE,
                index=False,
                header=True)

