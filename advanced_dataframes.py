#!/usr/bin/env python
# coding: utf-8

# 1.) Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url connection string formatted like in the example at the start of this lesson.

# In[2]:


import pandas as pd
import numpy as np


# In[5]:


from env import host, user, password


# In[57]:

def get_db_url(user, host, password, db):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[58]:

sql_query = 'select * from employees'
sql_query


# In[59]:


def get_employees_data(db):
    return pd.read_sql(sql_query, get_db_url(db))


# In[61]:


employee_db = get_employees_data('employees')


# 2.) Use your function to obtain a connection to the employees database.

# In[54]:


url = f'mysql+pymysql://{user}:{password}@{host}/employees'  # have to define a url to use with read_sql!!


# In[55]:


employees = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)
employees


# In[ ]:





# 3.) Once you have successfully run a query:
# 
# a. Intentionally make a typo in the database url. What kind of error message do you see?
# 
# b. Intentionally make an error in your SQL query. What does the error message look like?

# In[25]:


#a.)
url_error = pd.read_sql('SELECT * FROM employes LIMIT 5 OFFSET 50', url)


# In[92]:


employees_error = pd.read_sql('SELCT * FROM employees LIMIT 5 OFFSET 50', url)


# 4.) Read the employees and titles tables into two separate DataFrames.
# 

# In[29]:


employees_df = pd.read_sql('SELECT * FROM employees', url)
employees_df


# In[30]:


titles_df = pd.read_sql('SELECT * FROM titles', url)
titles_df


# 5.) How many rows and columns do you have in each DataFrame? Is that what you expected?

# In[55]:


employees_df.shape


# In[47]:


titles_df.shape


# 6.) Display the summary statistics for each DataFrame.
# 

# In[46]:


employees_df.describe(include = 'all')


# In[62]:


titles_df.describe(include = 'all')


# 7.) How many unique titles are in the titles DataFrame?

# In[48]:


titles_df['title'].value_counts()


# In[67]:


titles_df['title'].unique()


# 8.) What is the oldest date in the to_date column?

# In[50]:


titles_df.head()


# In[71]:


titles_df['to_date'].min()


# In[52]:


titles_df.to_date.sort_values().head(5)


# In[53]:


min(titles_df['to_date'])


# In[86]:


oldest_date = '''
SELECT to_date, min(to_date) as old
from titles
GROUP BY to_date
ORDER BY old ; 
'''


# In[91]:


oldest_date = pd.read_sql(oldest_date,url)
oldest_date


# 9.) What is the most recent date in the to_date column?

# In[79]:


to_date = '''
select to_date
from titles
where to_date LIKE '%9999%';
'''

current_date = pd.read_sql(to_date,url)
current_date.head(5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Exercises II

# 1.) Copy the users and roles DataFrames from the examples above.

# In[6]:


users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users


# In[5]:


roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles


# 2.) What is the result of using a right join on the DataFrames?

# In[12]:


right_join = users.merge(roles, how='right', left_on= 'role_id', right_on='id', indicator=True)
right_join


# In[ ]:





# 3.) What is the result of using an outer join on the DataFrames?

# In[24]:


pd.concat([users, roles],axis=0, join='outer')


# In[14]:


out_join = users.merge(roles, how='outer', left_on= 'role_id', right_on='id', indicator=True)
out_join


# 4.) What happens if you drop the foreign keys from the DataFrames and try to merge them?

# In[25]:


userdrop = users.drop(columns = 'role_id')
rolesdrop = roles.drop(columns = 'id')


# In[27]:


userdrop.merge(rolesdrop, how='inner', on=None, left_on=None, right_on=None, indicator=True)


# 5.) Load the mpg dataset from PyDataset.

# In[ ]:





# In[28]:


from pydataset import data


# In[29]:


mpg = data('mpg')


# 6.) Output and read the documentation for the mpg dataset.

# In[37]:


data('mpg', show_doc = True)


# 7.) How many rows and columns are in the dataset?

# In[32]:


mpg.shape


# In[38]:


mpg.describe


# In[41]:


mpg.columns


# 8.) Check out your column names and perform any cleanup you may want on them.

# In[40]:


mpg.head(3)


# In[52]:


mpg_new_df = mpg.rename(columns={'cty': 'city', 'hwy': 'highway', 'drv': 'drive', 'cyl': 'cylinder', 'fl': 'fuel type'})
mpg_new_df


# 9.) Display the summary statistics for the dataset.

# In[51]:


mpg_new_df.describe()


# 10.) How many different manufacturers are there?

# In[69]:


len(mpg['manufacturer'].value_counts())


# In[61]:


mpg.manufacturer.unique()


# In[60]:


number_of_manufacturers = len(mpg.manufacturer.unique())
number_of_manufacturers


# 11.) How many different models are there?

# In[72]:


len(mpg.model.unique())


# In[73]:


number_models = len(mpg.model.unique())


# 12.) Create a column named mileage_difference like you did in the DataFrames exercises; this column should contain the difference between highway and city mileage for each car.

# In[78]:


mpg_new['mileage_difference'] = mpg_new['highway'] - mpg_new['city']
mpg_new


# df['passing_math'] = np.where(df.math < 70, 'failing', 'passing')
# 
# df

# 13.) Create a column named average_mileage like you did in the DataFrames exercises; this is the mean of the city and highway mileage.
# 
# 

# In[80]:


mpg_new['average_mileage'] = (mpg_new['highway'] + mpg_new['city'])/2
mpg_new


# 14.) Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has an automatic transmission.

# In[92]:


# if contain auto return true.
mpg_new.trans.value_counts()


# In[91]:


bools_auto = mpg_new.trans.str.startswith('a')
bools_auto


# In[94]:


mpg_new['is_automatic'] = bools_auto
mpg_new


# In[ ]:





# 15.) Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?

# In[118]:


mpg_new.groupby('manufacturer').average_mileage.agg(['mean']).sort_values(by = 'mean', ascending = False)


# 16.) Do automatic or manual cars have better miles per gallon?

# In[120]:


mpg_new.groupby('is_automatic').average_mileage.agg(['mean']).sort_values(by = 'mean', ascending = False)

# ### Exercises III

# 1.) Use your get_db_url function to help you explore the data from the chipotle database.

# In[ ]:


from env import host, user, password


# In[ ]:


def get_db_url(user, host, password, db):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[ ]:


url = f'mysql+pymysql://{user}:{password}@{host}/chipotle'


# In[ ]:


chipotle_df = pd.read_sql('SELECT * FROM orders', url)


# In[ ]:


chipotle_df.drop(columns = 'revenue')


# 2.) What is the total price for each order?

# In[ ]:


chipotle_df['item_price_float'] = chipotle_df['item_price'].str.replace('$', '').astype(float)


# In[ ]:


chipotle_df.groupby('order_id').item_price_float.agg('sum')


# 3.) What are the most popular 3 items?

# In[ ]:


chipotle_df.groupby('item_name').quantity.agg(['sum']).sort_values(by=['sum'], ascending = False).head(3)


# 4.) Which item has produced the most revenue?

# In[ ]:


chipotle_df.groupby('item_name').item_price_float.agg(['sum']).nlargest(3, 'sum', keep ='all')


# 5.) Using the titles DataFrame, visualize the number of employees with each title.

# In[10]:


url = f'mysql+pymysql://{user}:{password}@{host}/employees'


# In[12]:


titles_df = pd.read_sql('SELECT * FROM titles', url)
titles_df


# In[13]:


titles_df.title.value_counts()


# 6.) Join the employees and titles DataFrames together.

# In[11]:


employees_df = pd.read_sql('SELECT * FROM employees', url)
employees_df


# In[14]:


emp_title = employees_df.merge(titles_df, how='outer', on='emp_no', indicator=True)
emp_title.head()


# 7.) Visualize how frequently employees change titles.
# 

# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:





# In[31]:


title_count = emp_title.groupby('emp_no').title.count().value_counts()


# In[ ]:





# In[32]:


employee_title = pd.crosstab(emp_title.emp_no, emp_title.title, margins = True)
employee_title


# 8.) For each title, find the hire date of the employee that was hired most recently with that title.`

# In[36]:


emp_title


# In[37]:


emp_title.groupby('title').hire_date.agg('max')


# 9.) Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas code to perform the manipulations.)

# In[20]:


title_dept = '''
select de.emp_no, d.dept_name,d.dept_no, t.title
from dept_emp as de
join departments as d 
ON de.dept_no = d.dept_no
join titles as t 
ON de.emp_no = t.emp_no;
'''


# In[39]:


title_by_depart = pd.read_sql(title_dept, url)
title_by_depart.head(10)


# In[35]:


title_by_depart.groupby('dept_name').title.count()


# In[40]:


pd.crosstab(title_by_depart.dept_name, title_by_depart.title, margins = True)

