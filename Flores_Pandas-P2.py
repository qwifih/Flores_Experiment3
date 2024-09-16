#!/usr/bin/env python
# coding: utf-8

# ## Problem 2

# In[5]:


import pandas as pd


# In[7]:


car = pd.read_csv('cars.csv')
car


# ### a.)

# In[21]:


car.loc[[1,3,5,7,9]]


# ### b.)

# In[24]:


car.loc[car['Model']=='Mazda RX4']


# ### c.)

# In[27]:


car.loc[car['Model']=='Camaro Z28', ['Model','cyl']]


# ### d.)

# In[31]:


car.loc[car['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic']),['Model','cyl','gear']]


# In[ ]:




