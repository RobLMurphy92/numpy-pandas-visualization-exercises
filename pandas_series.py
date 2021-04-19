#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# ### Exercise 1

# ### 1.) Use pandas to create a Series named fruits from the following list:

# In[80]:


fruit = (["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", 
                    "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", 
                    "blackberry", "gooseberry", "papaya"])

fruits = pd.Series(fruit)
fruits


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

# In[81]:


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


# In[95]:


fruits.value_counts().idxmax()


# ### Determine the string value that occurs least frequently in fruits.

# In[93]:


fruits.value_counts().idxmin()


# ### Exercises Part II

# ### .) Explore more attributes and methods while you continue to work with the fruits Series.

# ### 1.) Capitalize all the string values in fruits.

# In[61]:


fruits.str.title()


# ### 2.) Count the letter "a" in all the string values (use string vectorization).

# In[97]:


fruits.str.count('a')


# ### 3.) Output the number of vowels in each and every string value.

# In[141]:


#apply method
def is_vowel(letter):
    count = 0
    for char in letter:
        if char.lower() in 'aeiou':
            count += 1
    return count


# In[237]:


fruits.apply(is_vowel)


# ### 4.) Write the code to get the longest string value from fruits.
# 

# In[197]:


fruits[fruits.str.len().idxmax()]


# ### 5.) Write the code to get the string values with 5 or more letters in the name.

# In[217]:


def string_count(word):
    if len(word) >= 5:
        return word
    else:
        return None
       


# In[254]:


fruits.apply(string_count)


# In[216]:


fruits[fruits.str.len()>=5]


# ### 6.) Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
# 

# In[230]:



fruits[fruits.apply(lambda m: m.count('o') >= 2)]


# ### 7.) Write the code to get only the string values containing the substring "berry".

# In[232]:


fruits[fruits.str.contains('berry')]


# ### 8.) Write the code to get only the string values containing the substring "apple".

# In[233]:


fruits[fruits.str.contains('apple')]


# ### 9.) Which string value contains the most vowels?

# In[253]:


fruits[fruits.apply(is_vowel).idxmax()]


# In[ ]:


# ### Exercises Part III

# In[50]:


letter = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'


# In[51]:


letterlist = list(letter)
letters = pd.Series(letterlist)


# ### 1.) Which letter occurs the most frequently in the letters Series?

# In[52]:


letters.value_counts().nlargest(1)


# ### 2.) Which letter occurs the Least frequently?

# In[53]:


letters.value_counts().nsmallest(2)


# ### 3.) How many vowels are in the Series?

# In[59]:


letters.apply(is_vowel).sum()


# ### 4.) How many consonants are in the Series?

# In[81]:


letters.apply(lambda x: False if x in 'aeiou' else True).sum()


# ### 5.) Create a Series that has all of the same letters but uppercased.





# In[ ]:





# In[ ]:




