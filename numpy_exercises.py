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

am_std = np.std(am_squared)
am_std

am_squared_mean = np.mean(am_squared)
am_squared_mean

# 6.)A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. 
# Center the data set. See this link for more on centering.

am_mean = np.mean(am)
am_mean

centered_am = am - am_mean
centered_am

cent_mean = np.mean(centered_am)
cent_mean


#Calculate the z-score for each data point. Recall that the z-score is given by:
#Z = (x - μ)/ σ

am_mean = np.mean(am)
am_mean 

am_std = np.std(am)
am_std

zscore = (am - am_mean)/(am_std)
zscore



# MORE EXERCISES

# SETUP 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = 0
for row in a:
    sum_of_a += row
sum_of_a

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
min_of_a

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
max_of_a

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
product_of_a = 1
for numb in a:
        product_of_a *= numb
product_of_a

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for numb in a:
        product_of_a *= numb
product_of_a

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = []
for numb in a:
    squares_of_a.append(numb ** 2)
squares_of_a

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = []
for numb in a:
    if numb % 2 != 0:
        odds_in_a.append(numb)
        
odds_in_a
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evenss_in_a = []
for numb in a:
    if numb % 2 == 0:
        evens_in_a.append(numb)
        
odds_in_a
########################

#########################
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_of_b = np.sum(b)
sum_of_b

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b = np.min(b)
min_of_b

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])


max_of_b = np.max(b)
max_of_b



# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))


mean_of_b = np.mean(b)
mean_of_b


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_of_b = np.prod(b)
product_of_b

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b = np.square(b)
squares_of_b 


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = b[~b%2==0]
odds_in_b

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

evens_in_b = b[b % 2 ==0]
evens_in_b

# Exercise 9 - print out the shape of the array b.
print(np.shape(b))
# Exercise 10 - transpose the array b.
np.transpose(b)
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.reshape(1,6)
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b.reshape(6,1)


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array(c)


# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c_min = np.min(c)
c_min

c_max = np.max(c)
c_max

c_sum = np.sum(c)
c_sum

c_prod = np.prod(c)
c_prod

# Exercise 2 - Determine the standard deviation of c.

c_std = np.std(c)
c_std

# Exercise 3 - Determine the variance of c.

c_var = np.var(c)
c_var

c.var()
# Exercise 4 - Print out the shape of the array c

c.shape

# Exercise 5 - Transpose c and print out transposed result.

c_trans = np.transpose(c)
print(c_trans)


c.transpose()
# Exercise 6 - Get the dot product of the array c with c. 
c_dot = np.dot(c,c)
c_dot

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
sum(sum(c * np.transpose(c)))


(c * c.transpose()).sum()
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
np.prod(np.transpose(c * c))

(c*c.transpose()).prod()


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]


d = np.array(d)
d
# Exercise 1 - Find the sine of all the numbers in d
sined = np.sin(d)
sined
# Exercise 2 - Find the cosine of all the numbers in d
cosin = np.cos(d)
cosin
# Exercise 3 - Find the tangent of all the numbers in d
tand = np.tan(d)
tand
# Exercise 4 - Find all the negative numbers in d
t_neg = d[d<0]
t_neg
# Exercise 5 - Find all the positive numbers in d
t_pos = d[d>0]
t_pos
# Exercise 6 - Return an array of only the unique numbers in d.
uniqd = np.unique(d)
uniqd
# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))


np.unique(d).shape[0]


# Exercise 8 - Print out the shape of d.
print(np.shape(d))
# Exercise 9 - Transpose and then print out the shape of d.
print(np.transpose(d))
# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9,2)


d.reshape(9, -1)