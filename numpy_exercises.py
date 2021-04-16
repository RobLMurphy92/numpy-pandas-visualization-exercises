am = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

### 1.) How many negative numbers are there?
negative_numbers = am[am < 0]
negative_numbers

countneg = 0
for x in am:
    if x < 0:
        countneg += 1

countneg

### 2.) How many positive numbers are there?
positive_numbers = am[am > 0]
positive_numbers

countpos = 0
for x in am:
    if x > 0:
        countpos += 1

len(am_add_3_pos)

### 3.) How many even positive numbers are there?
am_even = am[am % 2 == 0]  
am_even
am_even[am_even >0]
len(am_even[am_even >0])

### 4.) If you were to add 3 to each data point, how many positive numbers would there be?
am_add_3 = am+3
am_add_3

am_add_3_pos = am_add_3[am_add_3 > 0]
am_add_3_pos

### 5.) If you squared each number, what would the new mean and standard deviation be?
am_squared = am ** 2
am_squared

am_std = am_squared.std()
am_std

am_squared_mean = am_squared.mean()
am_squared_mean

# 6.)A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. 
# Center the data set. See this link for more on centering.

am_mean = am.mean()
am_mean 

centered_am = am - am_mean
centered_am

cent_mean = centered_am.mean()
cent_mean


#Calculate the z-score for each data point. Recall that the z-score is given by:
#Z = (x - μ)/ σ

am_mean = am.mean()
am_mean 

am_std = am.std()
am_std

zscore = (am - am_mean)/(am_std)
zscore