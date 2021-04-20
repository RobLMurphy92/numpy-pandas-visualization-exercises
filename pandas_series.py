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

letter_cap = pd.Series(letter).str.upper()
letter_cap


# ### 6.) Create a bar plot of the frequencies of the 6 most commonly occuring letters.

# In[ ]:





# In[71]:


six_most = letters.value_counts().nlargest(n=6)
six_most


# In[91]:


six_most.plot.bar(title = 'Six Most Frequent Letters', rot =0 ).set(xlabel = '$Letter$', ylabel = '$Count$')


plt.show()
   


# In[47]:


number = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']


# In[49]:


numberslist = list(number)
numbers = pd.Series(numberslist)


# ### 1.) What is the data type of the numbers Series?

# In[52]:


numbers.dtype


# ### 2.) How many elements are in the number Series?

# In[51]:


numbers.size


# ### 3.) Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.

# In[124]:


numbers.str.replace('$', '').str.replace(',', '').astype(float).sort_values()


# In[114]:





# ### 4.) Run the code to discover the maximum value from the Series.

# In[56]:


new_numbers.max()


# ### 5.) Run the code to discover the minimum value from the Series.

# In[57]:


new_numbers.min()


# ### 6.) What is the range of the values in the Series?

# In[59]:


new_numbers_range = new_numbers.max() - new_numbers.min()
new_numbers_range


# ### 7.) Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.

# In[66]:


pd.cut(new_numbers.sort_values(), 4).value_counts()


# ### 8.) Plot the binned data in a meaningful way. Be sure to include a title and axis labels.

# In[102]:


pd.cut(new_numbers.sort_values(), 4).value_counts().plot.barh(title = '$Quartered Dollar Ranges$', xlabel = '$Dollar Ranges$', ylabel = 'Count')


# ### Exercise 3 Part II

# In[73]:


exam_scores = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]


# In[75]:


exam_scores = pd.Series(list(exam_scores))
exam_scores


# ### 1.) How many elements are in the exam_scores Series?

# In[76]:


exam_scores.size


# ### 2.) Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.

# In[77]:


exam_scores.describe()


# ### 3.) Plot the Series in a meaningful way and make sure your chart has a title and axis labels.

# In[ ]:





# ### 4.) Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.

# ### 5.) Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.

# ### 6.) Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.





