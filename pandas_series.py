#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# ### 1.) Use pandas to create a Series named fruits from the following list:

# In[7]:


fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", 
                    "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", 
                    "blackberry", "gooseberry", "papaya"])


# ### 2.) Use Series attributes and methods to explore your fruits Series.

# In[4]:


type(fruits)


# In[6]:


fruits.values


# In[8]:


fruits.dtype


# In[9]:


fruits.size


# In[11]:


fruits.shape


# ### 3.) Determine the number of elements in fruits.

# In[10]:


fruits.size


# ### 4.) Output only the index from fruits.

# In[12]:


fruits.index


# ### 5.) Output only the values from fruits.

# In[13]:


fruits.values


# ### 6.) Confirm the data type of the values in fruits.

# In[16]:


type(fruits.values)


# In[18]:


fruits.dtype


# ### 7.) Output only the first five values from fruits. Output the last three values. Output two random values from fruits.

# In[19]:


fruits.head()


# In[21]:


fruits.tail(3)


# In[22]:


fruits.sample(2)


# ### 8.) Run the .describe() on fruits to see what information it returns when called on a Series with string values.

# In[27]:


#pd.Series([3, 4, 5, 6]).astype('str')

fruits.describe()


# ### 9.) Run the code necessary to produce only the unique string values from fruits.

# In[31]:


fruits.unique()


# ### 10.) Determine how many times each unique string value occurs in fruits.

# In[35]:


fruits.value_counts()


# ### Determine the string value that occurs most frequently in fruits.

# In[43]:


fruits.value_counts().nlargest()


# In[45]:


fruits.count()


# In[48]:


fruits.value_counts()


# ### Determine the string value that occurs least frequently in fruits.

# In[44]:


fruits.value_counts().nsmallest()

