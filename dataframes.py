#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pydataset import data


# In[2]:


import pandas as pd
import numpy as np


# In[3]:


np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})


# 1.)Copy the code from the lesson to create a dataframe full of student grades.
# 
# - Create a column named passing_english that indicates whether each student has a passing grade in english.
# - Sort the english grades by the passing_english column. How are duplicates handled?
# - Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
# - Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
# - Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

# #### a.) Create a column named passing_english that indicates whether each student has a passing grade in english.

# In[4]:


df['passing_english'] = df.english >= 70


# In[5]:


df


# #### b.) Sort the english grades by the passing_english column. How are duplicates handled?

# In[6]:


df.sort_values(by = 'passing_english', ascending = False) # duplicates are ordered by index number!


# #### c.) Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)

# In[7]:


df.sort_values(by = ['passing_english','name'], ascending = [True,True])


# #### d.) Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.

# In[8]:


df.sort_values(by = ['passing_english','english'], ascending = [True,True])


# #### e.) Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

# In[9]:


df['overall_grade'] = (df['math']+ df['english']+ df['reading'])/3
df



# 2.) Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
# 
# - How many rows and columns are there?
# - What are the data types of each column?
# - Summarize the dataframe with .info and .describe
# - Rename the cty column to city.
# - Rename the hwy column to highway.
# - Do any cars have better city mileage than highway mileage?
# - Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
# - Which car (or cars) has the highest mileage difference?
# - Which compact class car has the lowest highway mileage? The best?
# - Create a column named average_mileage that is the mean of the city and highway mileage.
# - Which dodge car has the best average mileage? The worst?

# #### a.) Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

# In[10]:


mpg = data('mpg')


# b.) How many rows and columns are there?

# In[11]:


mpg.info()

#234 rows, 11 columns


# #### c.)  What are the data types?

# In[12]:


mpg.dtypes
# object, float, int


# #### d.) Summarize the dataframe with .info and .describe

# In[13]:


mpg.describe()


# In[14]:


mpg.info()


# #### e.) Rename the cty column to city.

# In[15]:


mpg


# In[16]:


mpg = mpg.rename(columns={'cty': 'city'})


# In[17]:


mpg


# #### f.) Rename the hwy column to highway.

# In[18]:


mpg = mpg.rename(columns = {'hwy': 'highway'})


# In[19]:


mpg


# #### g.) Do any cars have better city mileage than highway mileage?

# In[20]:


mpg[mpg.city > mpg.highway]


# #### h.) Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.

# In[21]:


mpg['mileage_difference'] = mpg['highway'] - mpg['city']
mpg


# #### i.) Which car (or cars) has the highest mileage difference?

# In[22]:


mpg.sort_values(by = 'mileage_difference', ascending = False).head(5)


# #### j.) Which compact class car has the lowest highway mileage? The best?

# In[23]:


compact_class_low= mpg[mpg['class']== 'compact'].sort_values(by = 'highway').head(10)


# In[24]:


compact_class_low


# In[25]:


compact_class_high= mpg[mpg['class']== 'compact'].sort_values(by = 'highway', ascending = False).head(10)


# In[26]:


compact_class_high


# #### k.) Create a column named average_mileage that is the mean of the city and highway mileage.

# In[27]:


mpg['average_mileage'] = mpg['city']+ mpg['highway']/2
mpg


# #### l.) Which dodge car has the best average mileage? The worst?

# In[28]:


dodge_worst_avg= mpg[mpg['manufacturer']== 'dodge'].sort_values(by = 'average_mileage').nsmallest(1, 'average_mileage', keep ='all')


# In[29]:


dodge_worst_avg


# In[30]:


dodge_best_avg= mpg[mpg['manufacturer']== 'dodge'].sort_values(by = 'average_mileage', ascending = False).nlargest(1,'average_mileage', keep = 'all')


# In[31]:


dodge_best_avg


# #### Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

# In[32]:


Mammals = data('Mammals')
Mammals


# a.) How many rows and columns are there?

# In[33]:


Mammals.shape


# #### b.) What are the data types?

# In[34]:


Mammals.dtypes


# #### c.) Summarize the dataframe with .info and .describe

# In[35]:


Mammals.info()


# In[36]:


Mammals.describe


# #### d.) What is the the weight of the fastest animal?

# In[37]:


Mammals.sort_values(by = ['speed', 'weight'], ascending = [False,True]).head(1)


# #### e.) What is the overal percentage of specials?

# In[38]:


Mammals_specials1 = Mammals['specials'] == True
Mammals_spec_true = Mammals_specials1.sum()
Mammals_spec_true


# In[39]:


Mammals_specials2 = Mammals['specials'] == False
Mammals_spec_false = Mammals_specials2.sum()
Mammals_spec_false


# In[40]:


percentage_specials = Mammals_spec_true/(Mammals_spec_true + Mammals_spec_false)
percentage_specials*100


# #### f.) How many animals are hoppers that are above the median speed? What percentage is this?

# In[41]:


#median = 48 


# In[42]:


(Mammals['hoppers'] == True).sum() # 11 hoppers out of 107 animals


# In[43]:


Hoppers_over_median = (((Mammals.hoppers == True) & (Mammals.speed > 48)).sum()) # hoppers and over 48 = 7
Hoppers_over_median


# In[44]:


Hoppers_over_median_percentage = ((((Mammals.hoppers == True) & (Mammals.speed > 48)).sum())/ len(Mammals))*100


# In[45]:


Hoppers_over_median_percentage

