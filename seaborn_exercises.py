#!/usr/bin/env python
# coding: utf-8

# ## Exercises

# Create a file named seaborn_exercises.py or seaborn_exercises.ipynb for this exercise.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pydataset import data


# Use the iris database to answer the following quesitons:

# In[2]:


print(sns.get_dataset_names())


# In[3]:


iris = sns.load_dataset('iris')
iris.head()


# In[4]:


data('iris', show_doc = True)


# 1.) What does the distribution of petal lengths look like?

# In[5]:


sns.displot(iris.petal_length)


# 2.) Is there a correlation between petal length and petal width?

# In[6]:


sns.relplot(data = iris, x = 'petal_width', y = 'petal_length')


# There appears to be a relationship between petal width and petal length. A positive trend indicates that petal width increases as petal length increases

# 3.) Would it be reasonable to predict species based on sepal width and sepal length?

# No, there is no relationship between species prediction and sepal width and length if you are trying to distinguish between veriscolor and virginica.  Possibly could use it for predicting the species setosa from the other two species.

# In[7]:


sns.relplot(data = iris, x = 'sepal_width', y = 'sepal_length', hue = 'species')


# 4.) Which features would be best used to predict species?
# Petal length and width would be the best features to use in prediction. Different species could have petal lengths which correalate to the petal width. Meaning some species with small widths have small lengths, etc..
# 

# ## Part 2

# 1.) Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. What do you notice?

# In[8]:


print(sns.get_dataset_names())


# In[9]:


anscombe = sns.load_dataset('anscombe')
anscombe.head()


# In[10]:


anscombe.groupby('dataset').describe().T


# I notice that the dataset it broken down into the x and y . In the x dataset the dataset has the same value for the mean, std.

# In[ ]:





# 2.) Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

# In[11]:


sns.relplot(data = anscombe, x = 'x', y = 'y', col = 'dataset')


# 3.) Load the InsectSprays dataset and read it's documentation. Create a boxplot that shows the effectiveness of the different insect sprays.

# In[ ]:





# In[12]:


InsectSprays = data('InsectSprays')
InsectSprays.head()


# In[13]:


data('InsectSprays', show_doc = True)


# In[14]:


sns.boxplot(data = InsectSprays, y = 'spray', x = 'count', hue = 'spray')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# 4.) Load the swiss dataset and read it's documentation. Create visualizations to answer the following questions:

# In[15]:


swiss = data('swiss')
swiss.head()


# In[16]:


data('swiss', show_doc = True)


# 3.) Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. (Choose a cutoff point for what constitutes catholic)
# 
# 
#   
#    - a.) Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.

# In[17]:


swiss['is_catholic'] = swiss['Catholic'] > 50


# In[18]:


swiss.head()


# b.) Does whether or not a province is Catholic influence fertility?

# In[19]:


sns.boxplot(data = swiss, x = 'is_catholic', y = 'Fertility')


# In[20]:


swiss.head()


# c.) What measure correlates most strongly with fertility?

# In[21]:


swiss.corr().Fertility


# In[22]:


labels = ['Fertility', 'Agriculture', 'Examination', 'Education', 'Catholic']


# In[23]:


swiss.corr().iloc[:,:-2]


# In[24]:


plt.figure(figsize = (10,10))
sns.heatmap(swiss.corr().iloc[:-2,:-2], cmap = 'Blues', vmax = 1, vmin = -1, center = 0, linewidth = 1,
           annot = True, fmt = '.2f', xticklabels = labels, yticklabels = labels)


#  4.) Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.

# In[25]:


from env import host, user, password


# In[26]:


def get_db_url(user, host, password, db):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[27]:


url = f'mysql+pymysql://{user}:{password}@{host}/chipotle'


# In[28]:


chipotle_df = pd.read_sql('SELECT * FROM orders', url)


# In[29]:


chipotle_df['item_price_float'] = chipotle_df['item_price'].str.replace('$', '').astype(float)


# In[ ]:





# In[30]:


item_name_float = chipotle_df.groupby('item_name').item_price_float.agg(['sum']).sort_values(by = ['sum'])
item_name_float


# In[31]:


top_four_items = chipotle_df.groupby('item_name').quantity.agg(['sum']).sort_values(by=['sum'], ascending = False).head(4)


# In[32]:


top_four_items


# In[33]:


top_four_float =top_four_items.merge(item_name_float, how='inner', on= 'item_name')


# In[34]:


top_four_float.rename(columns={'sum_x': 'Sold', 'sum_y': 'Revenue'})


# In[35]:


chipotle_df[chipotle_df['item_name'].isin(top_four_items.index)]


# In[42]:


top_four_rev = chipotle_df[chipotle_df['item_name'].isin(top_four_items.index)].groupby('item_name').item_price_float.agg(['sum'])


# In[53]:


top_four_rev = top_four_rev.rename(columns = {'sum': 'Revenue'})


# In[55]:


plt.figure(figsize = (10,10))

sns.barplot(data = top_four_rev, x = top_four_rev.index, y = 'Revenue')


# 5.) Load the sleepstudy data and read it's documentation. Use seaborn to create a line chart of all the individual subject's reaction times and a more prominant line showing the average change in reaction time.

# sleepstudy = data('sleepstudy')
# sleepstudy

# In[70]:


subject = sleepstudy.groupby('Subject').Reaction.agg(['mean'])


# In[69]:


subject = 


# In[79]:


plt.figure(figsize = (10,10))
sns.lineplot(data = sleepstudy, x = 'Days', y = 'Reaction', ci = None,linewidth = 4 )
sns.lineplot(data = sleepstudy, x = 'Days', y = 'Reaction', hue = 'Subject', legend = 'full', palette=("bright"))
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[ ]:


sleepstudy


# In[56]:



sleepstudy.head()


# In[ ]:





# In[57]:


data('sleepstudy', show_doc = True)

