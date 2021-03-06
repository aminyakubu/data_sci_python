#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:34:29 2019

@author: amin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Indexing DataFrames
# =============================================================================

datafile = 'data/sales.csv'

sales = pd.read_csv(datafile, header = None, delimiter = ' ',
                    names = ['month', 'eggs', 'salt', 'spam'],
                    index_col = 0)

# 1. Indexing using square brackets. df['column labe']['row label']

sales['salt']['Jan']

# 2. Using column attribute and row label 
# Columns may also be reffered to as attributes of a DataFrame if their labels
# are valid python identifiers

sales.eggs['Mar']
sales.eggs[['Mar','May']]
sales.eggs['Mar':'May']

# 3. Using the .loc and .iloc accessors. 
# eg. df.loc['row specifier', 'column specifier']

sales.loc['May','spam']
sales.iloc[4, 2]

## Selecting only some columns 

sales[['salt','eggs']]

# exercise

election = pd.read_csv('data/election.csv',
                       index_col = 'county')

election.loc['Bedford', 'winner']

#Positional and labeled indexing

# Assign the row position of election.loc['Bedford']: x
x = 4

# Assign the column position of election['winner']: y
y = 4

# Print the boolean equivalence
print(election.iloc[x, y] == election.loc['Bedford', 'winner'])

# Indexing and column rearrangement
# Create a separate dataframe with the columns ['winner', 'total', 'voters']: results
results = election[['winner', 'total', 'voters']]

# Print the output of results.head()
print(results.head())


#Slicing DataFrames

sales['eggs'] # Selecting one column with one pair of [] a series object. 

#A series is a one - dimentional array with a labelled index (like a hyrid 
#between a numpy array and a dictionary)

sales['eggs'][1:4]
sales.loc[:, 'eggs':'salt']
sales.loc['Jan':'Apr', :]
sales.loc['Mar':'May', 'salt':'spam']

sales.iloc[2:5, 1:]

# using lists rather than slices

sales.loc['Jan':'May', ['eggs','spam']]

sales.iloc[[0,4,5], 0:2]

#Slicing rows

# Slice the row labels 'Perry' to 'Potter': p_counties
p_counties = election.loc['Perry':'Potter']

# Print the p_counties DataFrame
print(p_counties)

#Slice the row labels 'Potter' to 'Perry' in reverse order. 
#To do this for hypothetical row labels 'a' and 'b', you could use a 
#stepsize of -1 like so: df.loc['b':'a':-1]

# Slice the row labels 'Potter' to 'Perry' in reverse order: p_counties_rev
p_counties_rev = election.loc['Potter':'Perry':-1]

# Print the p_counties_rev DataFrame
print(p_counties_rev)

#Slicing columns

# Slice the columns from the starting column to 'Obama': left_columns
left_columns = election.loc[:,:'Obama']

# Print the output of left_columns.head()
print(left_columns.head())

# Slice the columns from 'Obama' to 'winner': middle_columns
middle_columns = election.loc[:,'Obama':'winner']

# Print the output of middle_columns.head()
print(middle_columns.head())

# Slice the columns from 'Romney' to the end: 'right_columns'
right_columns = election.loc[:,'Romney':]

# Print the output of right_columns.head()
print(right_columns.head())

#Subselecting DataFrames with lists

# Create the list of row labels: rows
rows = ['Philadelphia', 'Centre', 'Fulton']

# Create the list of column labels: cols
cols = ['winner', 'Obama', 'Romney']

# Create the new DataFrame: three_counties
three_counties = election.loc[rows, cols]

# Print the three_counties DataFrame
print(three_counties)

# Filtering DataFrames

# Creating a boolean series 
enough_salt_sold = sales.salt > 60

sales[enough_salt_sold]

# OR

sales[sales.salt > 60]

# Combining filters

sales[(sales.salt > 60) & (sales.eggs < 200)] # Both conditions

sales[(sales.salt >= 50) | (sales.eggs < 200)] # Either condition

#Dataframes with zeros and NaNs

sales1 = sales.copy()
sales1['bacon'] = [0, 0, 50, 60, 70, 80]

print(sales1)

# Selecting columns with all nonzero (non-zeros) entries 

sales1.loc[:, sales1.all()]

# Selecting columns with any nonzero (non - zeros) entry

sales1.loc[:, sales1.any()] # in this case, there are no all zero column, so all of sales1 is return

# Selecting columns with any NaNs

sales1.loc[:, sales1.isnull().any()]

# Selecting columns without NaNs

sales1.loc[:, sales1.notnull().all()]

# Drop rows with missing data ( with any NaNs)

sales1.dropna(how = 'any')

# using how = 'any' drops the row 'May' because it has a NaN entry
# by contrast how = 'all' will keep this row

sales1.dropna(how = 'all')

# Filtering a column based on another

sales.eggs[sales.salt > 55]

# This type of filtering allows us to calculate one column based on another

# Modifying a column based on another
sales.eggs[sales.salt > 55] += 5

# Create the boolean array: high_turnout
high_turnout = election.turnout > 70

# Filter the election DataFrame with the high_turnout array: high_turnout_df
high_turnout_df = election[high_turnout]

# Print the high_turnout_results DataFrame
print(high_turnout_df)

# =============================================================================
# Filtering columns using other columns
# 
# The election results DataFrame has a column labeled 'margin' which 
# expresses the number of extra votes the winner received over the losing 
# candidate. This number is given as a percentage of the total votes cast. 
# It is reasonable to assume that in counties where this margin was less 
# than 1%, the results would be too-close-to-call.
# 
# Your job is to use boolean selection to filter the rows where the margin 
# was less than 1. You'll then convert these rows of the 'winner' column 
# to np.nan to indicate that these results are too close to declare a winner
# =============================================================================

# Create the boolean array: too_close
too_close = election.margin < 1

# Assign np.nan to the 'winner' column where the results were too close to call
election.winner[too_close] = np.nan

# Print the output of election.info()
print(election.info())

# =============================================================================
# Filtering using NaNs
# 
# In certain scenarios, it may be necessary to remove rows and columns with 
# missing data from a DataFrame. The .dropna() method is used to perform this 
# action
# =============================================================================

titanic = pd.read_csv('data/titanic.csv')

#you will note that there are many NaNs. 
#You will focus specifically on the 'age' and 'cabin' columns in this exercise.
# Your job is to use .dropna() to remove rows where any of these two columns 
# contains missing data and rows where all of these two columns contain 
# missing data.

# Select the 'age' and 'cabin' columns: df
df = titanic[['age', 'cabin']]

# Print the shape of df
print(df.shape)

# Drop rows in df with how='any' and print the shape
print(df.dropna(how = 'any').shape)

# Drop rows in df with how='all' and print the shape
print(df.dropna(how = 'all').shape)

#use the thresh= keyword argument to drop columns from the full dataset 
#that have less than 1000 non-missing values

# Drop columns in titanic with less than 1000 non-missing values
print(titanic.dropna(thresh =1000, axis='columns').info())

# =============================================================================
# Transforming DataFrames
# =============================================================================

#The best way to transform data in pandas dataframes is the methods inherent to
#pandas dataframes. 

#Next best is to use Numpy unfuncs or Universal functions to transform entire 
#columns of data "elementwise". 

#Suppose we want to convert sales numbers into units of whole dozens (rounded
#down) rather than individual item count. The most efficient way to do this 
#is to use a Pandas built-in method like floordiv. This arithmetic is applied to
#every entry in the dataframe.

sales.floordiv(12) # Convert to dozens unit

# Another way is to use the numpy floor divide function
np.floor_divide(sales, 12)

# We can make a custom function to do this

def dozens(n):
    return n//12

sales.apply(dozens)

# We can also use a lambda function

sales.apply(lambda n: n//12)

# Storing transformations

#All of the preceding computations returned a new DataFrame without altering
#the original dataframe. 
#
#To preserve a computed result we can create a new column storing calculations. 

sales['dozens_of_eggs'] = sales.eggs.floordiv(12)

# Working with string values

#Dataframes, series, index objects come with a handy .str attribute as a kind
#of accessor for vectorized string transformations. 
#
#Here, we reassign the index using .index.str.upper() to all the index uppercase

sales.index = sales.index.str.upper()

# For the index, there is no apply method. The relevant method is called map

sales.index = sales.index.map(str.lower)

# Defining columns using other columns 

sales['salty_eggs'] = sales.salt + sales.dozens_of_eggs

# =============================================================================
# Using apply() to transform a column
# The .apply() method can be used on a pandas DataFrame to apply an 
# arbitrary Python function to every element.
# =============================================================================

pitts = pd.read_csv('data/pitt_weather2013.csv')

# Write a function to convert degrees Fahrenheit to degrees Celsius: to_celsius
def to_celsius(F):
    return 5/9*(F - 32)

# Apply the function over 'Mean TemperatureF' and 'Mean Dew PointF': df_celsius
df_celsius = pitts[['Mean TemperatureF', 'Mean Dew PointF']].apply(to_celsius)

# Reassign the columns df_celsius
df_celsius.columns = ['Mean TemperatureC', 'Mean Dew PointC']

# Print the output of df_celsius.head()
print(df_celsius.head())

# =============================================================================
# Using .map() with a dictionary
# 
# The .map() method is used to transform values according to a Python dictionary look-up.
# 
# use a dictionary to map the values 'Obama' and 'Romney' in the 'winner' 
# column to the values 'blue' and 'red', and assign the output to the 
# new column 'color'
# =============================================================================

# Create the dictionary: red_vs_blue. Assign values based on a column. It can also 
#be used to create factors based on a different column

red_vs_blue = {'Obama':'blue', 'Romney':'red'}

# Use the dictionary to map the 'winner' column to the new column: election['color']
election['color'] = election.winner.map(red_vs_blue)

# Print the output of election.head()
print(election.head())

# =============================================================================
# Using vectorized functions
# 
# When performance is paramount, you should avoid using .apply() and .map() 
# because those constructs perform Python for-loops over the data stored in a 
# pandas Series or DataFrame. By using vectorized functions instead, you can 
# loop over the data at the same speed as compiled code (C, Fortran, etc.)! 
# NumPy, SciPy and pandas come with a variety of vectorized functions 
# (called Universal Functions or UFuncs in NumPy).
# 
# You can even write your own vectorized functions.
# 
# In this exercise you're going to import the zscore function from scipy.stats 
# and use it to compute the deviation in voter turnout in Pennsylvania from 
# the mean in fractions of the standard deviation. 
# 
# In statistics, the z-score is the number of standard deviations by which an 
# observation is above the mean - so if it is negative, it means the 
# observation is below the mean.
# 
# Instead of using .apply() as you did in the earlier exercises, 
# the zscore UFunc will take a pandas Series as input and return a NumPy array. 
# You will then assign the values of the NumPy array to a new column in the 
# DataFrame
# =============================================================================

# Import zscore from scipy.stats
from scipy.stats import zscore

# Call zscore with election['turnout'] as input: turnout_zscore
turnout_zscore = zscore(election['turnout'])

# Print the type of turnout_zscore
print(type(turnout_zscore))

# Assign turnout_zscore to a new column: election['turnout_zscore']
election['turnout_zscore'] = turnout_zscore

# Print the output of election.head()
print(election.head())

# =============================================================================
# Advanced indexing
# =============================================================================

#To learn more about indexing, we need to understand what indexes are.
#The key building blocks in pandas are indexes, series and dataframes. 
#
#Index: sequence of labels 
#Series: one-dimensional numpy arrays coupled with an index with fancy labels.
#Dataframes: 2D tables comprising series as columns sharing common indexes. 

#Like the dictionary keys, pandas indexes are immutable. Like NumPy arrays,
#indexes are homogenous in datatype.

# Creating series

prices = [10.70, 10.86, 10.74, 10.71, 10.79] 
shares = pd.Series(prices) 

print(shares)
print(shares.index)

# Creating indexes

days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
shares = pd.Series(prices, index=days)

# Examine an index. We can index and slice just as with python lists
print(shares.index)

print(shares.index[2])

print(shares.index[:2])
print(shares.index[-2:])
print(shares.index.name)

# Modifying index name

shares.index.name = 'weekday'
print(shares)

# An exception is raised when attempting to assign to individual index entries
# or index slices.

shares.index[2] = 'Wednesday'
shares.index[:4] = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']

# This is because index entries are immutable (like dictionary keys). This
#restriction helps pandas optimize operations on Series and dataframes.

#It is possible to reassign an index by overwriting it all at once. Notice that
# doing so also erases the name of the index.

shares.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] 
print(shares) 

#Unemployment data

unemployment = pd.read_csv('data/unemployment.csv', delimiter = ' ')
unemployment.head() 

unemployment.info()

# We see that the dataframe is indexed exactly as a numpy array

# it's better to use the zipcode column as the index instead

unemployment.index = unemployment['Zip']

unemployment.head()

# We can now delete the redundant column using del

del unemployment['Zip']

# Examing indexes and columns

print(unemployment.index) 

print(unemployment.index.name) 

print(type(unemployment.index)) 

print(unemployment.columns) 

# We could have done

unemployment = pd.read_csv('data/unemployment.csv', delimiter = ' ',
                           index_col = 'Zip')

sales = pd.read_csv('data/sales.csv', header = None, delimiter = ' ',
                    names = ['month', 'eggs', 'salt', 'spam'],
                    index_col = 0)

#Changing index of a DataFrame
#
#As you saw in the previous exercise, indexes are immutable objects. 
#This means that if you want to change or modify the index in a DataFrame, 
#then you need to change the whole index. You will do this now, using a list 
#comprehension to create the new index.

#A list comprehension is a succinct way to generate a list in one line

#The following are equivalent

cubes = [i**3 for i in range(10)]

cubes = []
for i in range(10):
    cubes.append(i**3)

# Create the list of new indexes: new_idx
new_idx = [i.upper() for i in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)

#Changing index name labels

# Assign the string 'MONTHS' to sales.index.name
sales.index.name = 'MONTHS'

# Print the sales DataFrame
print(sales)

# Assign the string 'PRODUCTS' to sales.columns.name 
sales.columns.name = 'PRODUCTS'

# Print the sales dataframe again
print(sales)

#Building an index, then a DataFrame

# Generate the list of months: months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Assign months to sales.index
sales.index = months

# Print the modified sales DataFrame
print(sales)

#Hierarchical indexing

stocks = pd.read_csv('data/stocks.csv', delimiter = ' ') 
print(stocks)

# you can see that the date is repeated 3 times for each stock symbol

# Notice the default index is an integer range. The rows are not sorted sensibly
# There are repeated values in the Date and Symbol columns

# WE would prefer to use a meaningful index that uniquely identifies each row.
# Individually, both the date and symbol are inappropriate due to repetitions.
# We can use a tuple of symbol and date to represent each record in the table 
# uniquely

stocks = stocks.set_index(['Symbol','Date'])
print(stocks)

print(stocks.index)

# We have a multi - index or hierarchical index composed of the entries from
# the original Date and Symbol columns

print(stocks.index.name) # Gives none

print(stocks.index.names)

# Sorting index

# We need to call sort_index() to sort the dataframe. 

stocks = stocks.sort_index() # Sorting is required for indexing and slicing

#Indexing (individual row). Use tuple

stocks.loc[('CSCO', '2016-10-04')]

stocks.loc[('CSCO', '2016-10-04'), 'Volume']

# Slicing outermost index

stocks.loc['AAPL'] # REturns all rows corresponding to AAPL

stocks.loc['CSCO':'MSFT']

#Fancy indexing (outermost index)
stocks.loc[(['AAPL', 'MSFT'], '2016-10-05'), :] 

stocks.loc[(['AAPL', 'MSFT'], '2016-10-05'), 'Close'] 

stocks.loc[('CSCO', ['2016-10-05', '2016-10-03']), :] 


# Slicing (both indexes)

#The tuple used for the index does not recognize slicing with colons natively.
#To force that to work, we need to use python builtin slice explicitly

stocks.loc[(slice(None), slice('2016-10-03', '2016-10-04')),:] 

# This will extract all symbols for the dates 2016-10-03 to 2016-10-04 inclusive

# Exercises

sales_h = pd.read_csv('data/sales_hier.csv', 
                      index_col = ['state','month'])

#Extracting elements from the outermost level of a MultiIndex is just like 
#in the case of a single-level Index. You can use the .loc[] accessor

# Print sales.loc[['CA', 'TX']]
print(sales_h.loc[['CA', 'TX']])

# Print sales['CA':'TX']
print(sales_h['CA':'TX'])

#Setting & sorting a MultiIndex

sales_h = pd.read_csv('data/sales_hier.csv')

# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state', 'month'])

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print the sales DataFrame
print(sales)

#Using .loc[] with nonunique indexes
sales_h = pd.read_csv('data/sales_hier.csv')

# Set the index to the column 'state': sales
sales_h = sales_h.set_index('state')

# Print the sales DataFrame
print(sales_h)

# Access the data from 'NY'
print(sales_h.loc['NY'])

#Indexing multiple levels of a MultiIndex

sales_h = pd.read_csv('data/sales_hier.csv', 
                      index_col = ['state','month'])


# Look up data for NY in month 1: NY_month1
NY_month1 = sales_h.loc[('NY', 1), :]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales_h.loc[(['CA', 'TX'], 2), :]

# Look up data for all states in month 2: all_month2
all_month2 = sales_h.loc[(slice(None), 2), :]

# Chapter 3: Rearranging and reshaping data

#Pivoting DataFrames

trials = pd.read_csv('data/trials_01.csv', delimiter = ' ')

# Reshaping by pivoting. 
# We may want to make it easier to see the relationship between the variables.

# the pivot method allows us to specify which columns to use as the index,
#and which to use as columns in the new dataframe. we specifiy values = 'response'
#to identify values to use in the reshaped dataframe.
#
#Unique values of gender become column names.

trials.pivot(index = 'treatment',
             columns = 'gender',
             values = 'response')

# When we leave out values, all the remaining values are used  as values. The
#resulting dataframe has multi-index columns with ID and responses stratified
#by gender

z = trials.pivot(index = 'treatment',
             columns = 'gender')

z.info()

#Exercises

users = pd.read_csv('data/users.csv', delimiter = ' ')

# Remove leading and lagging spaces from column names

users.columns = users.columns.str.strip()

# Pivot the users DataFrame: visitors_pivot
visitors_pivot = users.pivot(index = 'weekday',
                             columns = 'city',
                             values = 'visitors')



# Print the pivoted DataFrame
print(visitors_pivot)

#Pivoting all variables
#If you do not select any particular variables, all of them will be pivoted

# Pivot users with signups indexed by weekday and city: signups_pivot
signups_pivot = users.pivot(index = 'weekday', 
                            columns = 'city', 
                            values = 'signups')

# Print signups_pivot
print(signups_pivot)

# Pivot users pivoted by both signups and visitors: pivot
pivot = users.pivot(index = 'weekday', columns = 'city')

# Print the pivoted DataFrame
print(pivot)

#Stacking & unstacking DataFrames

trials = pd.read_csv('data/trials_01.csv', delimiter = ' ')

trials = trials.set_index(['treatment','gender'])

# The pivot method won't work directly with this dataframe because of the 
# multilevel index. In this case, we might want to move some of our index 
#levels to columns, making our dataframe shorter and wider (more columns, few rows)

trials_by_gender = trials.unstack(level = 'gender')
trials_by_gender = trials.unstack(level = 1)

# the data are now divided in colums by gender. This gives a similar result
#as the pivot method. The principal difference is now that we have hierarchial
#columns

# Stacking 

#The opposite of unstack is stack. This can be used to make a wide dataframe
#thinner and longer. With unstack, you specifiy the hierarchical columns to be
#moved to the index. 

stacked = trials_by_gender.stack(level = 'gender')

# WE get back to the dataframe with multi level indexing 

# Suppose you want to have gender level outermost and treatment level innermost.
#to switch index levels inplace, we use the swaplevel method. 

swapped = stacked.swaplevel(0, 1) # We specify we want to swap the first and second level here

# The index is still not sorted. 

sorted_trials = swapped.sort_index()

# EXERCISES

users = pd.read_csv('data/users.csv', delimiter = ' ',
                    index_col = ['city', 'weekday'])

# Unstack users by 'weekday': byweekday
byweekday = users.unstack(level = 'weekday')

# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
print(byweekday.stack('weekday'))

# Unstack users by 'city': bycity
bycity = users.unstack(level = 'city')

# Print the bycity DataFrame
print(bycity)

# Stack bycity by 'city' and print it
print(bycity.stack(level = 'city'))

# Stack 'city' back into the index of bycity: newusers
newusers = bycity.stack(level = 'city')

# Swap the levels of the index of newusers: newusers
newusers = newusers.swaplevel(0, 1)

# Print newusers and verify that the index is not sorted
print(newusers)

# Sort the index of newusers: newusers
newusers = newusers.sort_index()

# Print newusers and verify that the index is now sorted
print(newusers)

# Verify /check that the new DataFrame is equal to the original (comparing that the two dataframes are the same)
print(newusers.equals(users))

# MELTING

new_trials = pd.read_csv('data/trials_02.csv', delimiter = ' ')

# id_vars: columns that should remain in the dataframe. use lists
# value_vars: columns to convert to values 

# if we don't like the generic names variable and values, the use 
# var_name and value_name

pd.melt(new_trials,
        id_vars = ['treatment'],
        value_vars = ['F', 'M'],
        var_name = 'gender',
        value_name = 'response')

users = users.reset_index()
visitors_by_city_weekday  = users.pivot(index = 'weekday',
                                        columns = 'city',
                                        values = 'visitors')

# Reset the index: visitors_by_city_weekday
visitors_by_city_weekday = visitors_by_city_weekday.reset_index()

# Print visitors_by_city_weekday
print(visitors_by_city_weekday)

# Melt visitors_by_city_weekday: visitors
visitors = pd.melt(visitors_by_city_weekday, id_vars=['weekday'], 
                   value_name='visitors')

# Print visitors
print(visitors)

#Going from wide to long
#
#You can move multiple columns into a single column 
#(making the data long and skinny) by "melting" multiple columns

# Melt users: skinny
skinny = pd.melt(users, id_vars=['weekday' ,'city'])

# Print skinny
print(skinny)

# =============================================================================
# Obtaining key-value pairs with melt()
# 
# Sometimes, all you need is some key-value pairs, and the context does 
# not matter. If said context is in the index, you can easily obtain what 
# you want. For example, in the users DataFrame, the visitors and signups 
# columns lend themselves well to being represented as key-value pairs. 
# So if you created a hierarchical index with 'city' and 'weekday' columns as 
# the index, you can easily extract key-value pairs for the 'visitors' and 
# 'signups' columns by melting users and specifying col_level=0
# =============================================================================

# Set the new index: users_idx
users_idx = users.set_index(['city', 'weekday'])

# Print the users_idx DataFrame
print(users_idx)

# Obtain the key-value pairs: kv_pairs
kv_pairs = pd.melt(users_idx, col_level=0)

# Print the key-value pairs
print(kv_pairs)

# =============================================================================
# Setting up a pivot table
# 
# Recall from the video that a pivot table allows you to see all of your 
# variables as a function of two other variables. In this exercise, you will use 
# the .pivot_table() method to see how the users DataFrame entries appear 
# when presented as functions of the 'weekday' and 'city' columns. 
# That is, with the rows indexed by 'weekday' and the columns indexed by 'city'.
# =============================================================================

# Create the DataFrame with the appropriate pivot table: by_city_day
by_city_day = users.pivot_table(index='weekday', columns='city')

# Print by_city_day
print(by_city_day)

# =============================================================================
# Using other aggregations in pivot tables
# 
# You can also use aggregation functions within a pivot table by specifying 
# the aggfunc parameter. In this exercise, you will practice using the 'count' 
# and len aggregation functions - which produce the same result - on the users DataFrame.
# 
# =============================================================================

# Use a pivot table to display the count of each column: count_by_weekday1
count_by_weekday1 = users.pivot_table(index='weekday', aggfunc='count')

# Print count_by_weekday
print(count_by_weekday1)

# Replace 'aggfunc='count'' with 'aggfunc=len': count_by_weekday2
count_by_weekday2 = users.pivot_table(index='weekday', aggfunc=len)

# Verify that the same result is obtained
print('==========================================')
print(count_by_weekday1.equals(count_by_weekday2))


# =============================================================================
# Using margins in pivot tables
# 
# Sometimes it's useful to add totals in the margins of a pivot table. 
# You can do this with the argument margins=True. In this exercise, you will 
# practice using margins in a pivot table along with a new aggregation function: sum.
# =============================================================================

# Create the DataFrame with the appropriate pivot table: signups_and_visitors
signups_and_visitors = users.pivot_table(index='weekday', aggfunc=sum)

# Print signups_and_visitors
print(signups_and_visitors)

# Add in the margins: signups_and_visitors_total 
signups_and_visitors_total = users.pivot_table(index='weekday', aggfunc=sum, margins=True)

# Print signups_and_visitors_total
print(signups_and_visitors_total)


# =============================================================================
# Categoricals and groupby
# =============================================================================

sales = pd.DataFrame(
        {'weekday':['Sun', 'Sun', 'Mon','Mon'],
         'city':['Austin','Dallas','Austin','Dallas'],
         'bread':[139, 237, 326, 456],
         'butter':[20, 45,70,98]})

# WE could do boolean filtering
    
sales.loc[sales['weekday']== 'Sun'].count()

# Better to do Groupby

sales.groupby('weekday').count()

sales.groupby('weekday')['bread'].sum()

sales.groupby('weekday')[['bread', 'butter']].sum()

sales.groupby(['weekday', 'city']).mean()

# Take note, we can use any pandas series  with the same index values 
# in the groupby argument 

customers = pd.Series(['Alice', 'Bob', 'Dave', 'Alice'])

# Customers has an identical index as sales which is a range starting from 0. 

sales.groupby(customers)['bread'].sum()

# Categorical data 

sales['weekday'].unique()

# Returns an array with distinct entries

sales['weekday'].value_counts()

# Here we get the number of entries for each distinct category

# Converting to categorical type
sales['weekday'] = sales['weekday'].astype('category')

# =============================================================================
# Grouping by multiple columns
# =============================================================================

titanic = pd.read_csv("data/titanic.csv")

# Group titanic by 'pclass'
by_class = titanic.groupby('pclass')

# Aggregate 'survived' column of by_class by count
count_by_class = by_class['survived'].count()

# Print count_by_class
print(count_by_class)

# Group titanic by 'embarked' and 'pclass'
by_mult = titanic.groupby(['embarked','pclass'])

# Aggregate 'survived' column of by_mult by count
count_mult = by_mult['survived'].count()

# Print count_mult
print(count_mult)

# =============================================================================
# Grouping by another series
# =============================================================================

# Read life_fname into a DataFrame: life
life = pd.read_csv('data/life_expectancy_years.csv', index_col='country')

# Read regions_fname into a DataFrame: regions
regions = pd.read_csv('data/regions_fname', index_col = 'country')

# Group life by regions['region']: life_by_region
life_by_region = life.groupby(regions['region'])

# Print the mean over the '2010' column of life_by_region
print(life_by_region['2010'].mean())

#=========================

sales.groupby('city')[['bread','butter']].max()

# Multiple aggregation 

sales.groupby('city')[['bread','butter']].agg(['max', 'sum'])

# The result is displayed using a multilevel index

# agg method also accepts user-defined functions or library functions 

def data_range(series):
    return series.max() - series.min()

# This takes a series 
    
sales.groupby('city')[['bread','butter']].agg(data_range)

# arg method also accepts dictionary as input. The dictionary keys are column
# names the values are aggregation functions to apply to each column

sales.groupby(customers)[['bread','butter']].agg({'bread':'sum', 'butter':data_range})

# =============================================================================
# Computing multiple aggregates of multiple columns
# =============================================================================

#The .agg() method can be used with a tuple or list of aggregations as input. 
#When applying multiple aggregations on multiple columns, the aggregated DataFrame 
#has a multi-level column index.

# Group titanic by 'pclass': by_class
by_class = titanic.groupby('pclass')

# Select 'age' and 'fare'
by_class_sub = by_class[['age','fare']]

# Aggregate by_class_sub by 'max' and 'median': aggregated
aggregated = by_class_sub.agg(['max', 'median'])

# Print the maximum age in each class
print(aggregated.loc[:, ('age','max')])

# Print the median fare in each class
print(aggregated.loc[:, ('fare', 'median')])

# =============================================================================
# Aggregating on index levels/fields
# =============================================================================

# Read the CSV file into a DataFrame and sort the index: gapminder
gapminder = pd.read_csv('data/gapminder.csv', 
                        index_col = ['Year', 'region', 'Country']).sort_index()

# Group gapminder by 'Year' and 'region': by_year_region
by_year_region = gapminder.groupby(level = ['Year', 'region'])

# Define the function to compute spread: spread
def spread(series):
    return series.max() - series.min()

# Create the dictionary: aggregator
aggregator = {'population':'sum', 'child_mortality':'mean', 'gdp':spread}

# Aggregate by_year_region using the dictionary: aggregated
aggregated = by_year_region.agg(aggregator)

# Print the last 6 entries of aggregated 
print(aggregated.tail(6))

# =============================================================================
# Grouping on a function of the index
# 
# Groupby operations can also be performed on transformations of the index values. 
# In the case of a DateTimeIndex, we can extract portions of the datetime over which to group
# 
# =============================================================================

# Read file: sales
sales = pd.read_csv('data/sales-feb-2015.csv', index_col= 'Date', parse_dates=True)

#Is there a day of the week that is more popular for customers? 
#To find out, you're going to use .strftime('%a') to transform the 
#index datetime values to abbreviated days of the week.

# Create a groupby object: by_day
by_day = sales.groupby(sales.index.strftime('%a'))

# Create sum: units_sum
units_sum = by_day['Units'].sum()

# Print units_sum
print(units_sum)

# =============================================================================
# Groupby and transformation
# =============================================================================


#  We often want to group data and apply distinct transformations to distinct groups.
#  Instead of aggregating after the grouping we can apply a transform method instead.
#  This changes the dataframe entries according to a specified function in-place 
#  without changing the index. 

# As an example let's compute a z-score. The z score of a value is its distance
# from the mean of its population measured in units of standard deviation

def zscore(series):
    return (series - series.mean())/series.std()

#This function is a transformation in that it accepts a Series as input and 
#returns a conforming Series. 
    
auto = pd.read_csv('data/auto-mpg.csv')

# we apply the zscore function to the columns of auto dataframe. 

zscore(auto['mpg']).head()

# As an alternative, we might want to normalize the mpg data independently 
# by year instead of over the whole population. 

auto.groupby('model year')['mpg'].transform(zscore).head()

#In this case, normalized by year, the MPG rating for Buick Skylark 320 is 
#0.503753 standard deviation below average amongs cars manufactured in 1970.

# The agg method applies reduction and the transform method applies a function
# element-wise to groups. 

#In some cases, split-apply-combine operations do not neatly fall into aggregation
#or transformation. For those cases, we use apply method. 

def zscore_with_year_and_name(group):
    df = pd.DataFrame({
            'mpg':zscore(group['mpg']),
            'year':group['model year'],
            'name':group['car name']})
    return df

# This transformation is too complicated for transform. So we use apply. 
    
auto.groupby('model year').apply(zscore_with_year_and_name).head()


#Excercises

# =============================================================================
# Detecting outliers with Z-Scores
# =============================================================================

# you can apply a .transform() method after grouping to apply a function to 
# groups of data independently. 
# The z-score is also useful to find outliers: a z-score value of +/- 3 is 
# generally considered to be an outlier.

# Import zscore
from scipy.stats import zscore

# Read the CSV file into a DataFrame
gapminder = pd.read_csv('data/gapminder.csv')
                        
# Group gapminder_2010: standardized
standardized = gapminder.groupby('region')['life','fertility'].transform(zscore)

# Construct a Boolean Series to identify outliers: outliers
outliers = (standardized['life'] < -3) | (standardized['fertility'] > 3)

# Filter gapminder_2010 by the outliers: gm_outliers
gm_outliers = gapminder.loc[outliers]

# Print gm_outliers
print(gm_outliers)

# =============================================================================
# Filling missing data (imputation) by group
# =============================================================================

#Many statistical and machine learning packages cannot determine the best 
#action to take when missing data entries are encountered. 
#Dealing with missing data is natural in pandas (both in using the default 
#behavior and in defining a custom behavior). 
#You can use .groupby() and .transform() to fill missing data appropriately for each group

# Create a groupby object: by_sex_class
by_sex_class = titanic.groupby(['sex', 'pclass'])

# Write a function that imputes median
def impute_median(series):
    return series.fillna(series.median())

# Impute age and assign to titanic['age']
titanic.age = by_sex_class['age'].transform(impute_median)

# Print the output of titanic.tail(10)
print(titanic.tail(10))

# =============================================================================
# Other transformations with .apply
# =============================================================================

#The .apply() method when used on a groupby object performs an arbitrary 
#function on each of the groups. These functions can be aggregations, 
#transformations or more complex workflows. The .apply() method will then combine 
#the results in an intelligent way.

#In this exercise, you're going to analyze economic disparity within regions of 
#the world using the Gapminder data set for 2010. To do this you'll define a 
#function to compute the aggregate spread of per capita GDP in each region 
#and the individual country's z-score of the regional per capita GDP. You'll 
#then select three countries - United States, Great Britain and China - to 
#see a summary of the regional GDP and that country's z-score against the 
#regional mean.

# Read the CSV file into a DataFrame 
gapminder = pd.read_csv('data/gapminder.csv', index_col = 'Country')

gapminder_2010 = gapminder[gapminder['Year']==2010]

# Group gapminder_2010 by 'region': regional
regional = gapminder_2010.groupby('region')

def disparity(gr):
    # Compute the spread of gr['gdp']: s
    s = gr['gdp'].max() - gr['gdp'].min()
    # Compute the z-score of gr['gdp'] as (gr['gdp']-gr['gdp'].mean())/gr['gdp'].std(): z
    z = (gr['gdp'] - gr['gdp'].mean())/gr['gdp'].std()
    # Return a DataFrame with the inputs {'z(gdp)':z, 'regional spread(gdp)':s}
    return pd.DataFrame({'z(gdp)':z , 'regional spread(gdp)':s})


# Apply the disparity function on regional: reg_disp
reg_disp = regional.apply(disparity)

# Print the disparity of 'United States', 'United Kingdom', and 'China'
print(reg_disp.loc[['United States','United Kingdom','China']])

# =============================================================================
# Groupby and filtering
# =============================================================================

auto = pd.read_csv('data/auto-mpg.csv')

# We can group all 390 automobiles by year, select the mpg column, and compute
# the average over each year. 

auto.groupby('model year')['mpg'].mean()

# What if we want the yearly average only for cars built by Chevrolet?
# We have to filter the groups before aggregating. 

# We save the output of grouping by as splitting 

splitting = auto.groupby('model year')

type(splitting)

type(splitting.groups)
# We see that the returned groupby object has an attribute splitting.groups 
# that is really a dictionary. 

print(splitting.groups.keys())

# the keys are the years and its values are the corresponding rows of the original Dataframe. 

# We can iterate over the splitting object and carry out computations 

for group_name, group in splitting:
    avg = group['mpg'].mean()
    print(group_name, avg)

# having a dataframe group for each year means we can filter before aggregating 

for group_name, group in splitting:
    avg = group.loc[group['car name'].str.contains('chevrolet'), 'mpg'].mean()
    print(group_name, avg)


# We can rewrite the loop as a dictionary comprehension. Saving that dictionary,
#the keys are the years(group_names) and the values are the filter averages as computed before.
#We can then use that dictionary to construct a pandas series with this data. 

chevy_means = {year:group.loc[group['car name'].str.contains('chevrolet'), 'mpg'].mean() \
                              for year, group in splitting}

# Boolean groupby

# Using a boolean series with the same index in the .groupby(), we can perform one-to-all
# comparison. 

chevy = auto['car name'].str.contains('chevrolet')

auto.groupby(['model year', chevy])['mpg'].mean()

# =============================================================================
# Grouping and filtering with .apply()
# =============================================================================

#By using .apply(), you can write functions that filter rows within groups. 
#The .apply() method will handle the iteration over individual groups and 
#then re-combine them back into a Series or DataFrame.

#In this exercise you'll take the Titanic data set and analyze survival rates from 
#the 'C' deck, which contained the most passengers. To do this you'll group 
#the dataset by 'sex' and then use the .apply() method on a provided user defined 
#function which calculates the mean survival rates on the 'C' deck

# Create a groupby object using titanic over the 'sex' column: by_sex
by_sex = titanic.groupby('sex')


def c_deck_survival(gr):
    c_passengers = gr['cabin'].str.startswith('C').fillna(False)
    return gr.loc[c_passengers, 'survived'].mean()

# Call by_sex.apply with the function c_deck_survival
c_surv_by_sex = by_sex.apply(c_deck_survival)

# Print the survival rates
print(c_surv_by_sex)

# =============================================================================
# Grouping and filtering with .filter()
# =============================================================================

#You can use groupby with the .filter() method to remove whole groups of rows
# from a DataFrame based on a boolean condition.
#
#In this exercise, you'll take the February sales data and remove entries 
#from companies that purchased less than or equal to 35 Units in the whole month

#First, you'll identify how many units each company bought for verification. 
#Next you'll use the .filter() method after grouping by 'Company' to remove all 
#rows belonging to companies whose sum over the 'Units' column was less than or 
#equal to 35. Finally, verify that the three companies whose total Units purchased 
#were less than or equal to 35 have been filtered out from the DataFrame.

# Read the CSV file into a DataFrame: sales
sales = pd.read_csv('data/sales-feb-2015.csv', index_col='Date', parse_dates=True)

# Read the CSV file into a DataFrame: sales
sales = pd.read_csv('sales.csv', index_col='Date', parse_dates=True)

# Group sales by 'Company': by_company
by_company = sales.groupby('Company')

# Compute the sum of the 'Units' of by_company: by_com_sum
by_com_sum = by_company['Units'].sum()
print(by_com_sum)

# Filter 'Units' where the sum is > 35: by_com_filt
by_com_filt = by_company.filter(lambda g:g['Units'].sum() > 35)
print(by_com_filt)

# =============================================================================
# Filtering and grouping with .map()
# =============================================================================

#Sometimes, you may instead want to group by a function/transformation of a column. 
#The key here is that the Series is indexed the same way as the DataFrame. 
#You can also mix and match column grouping with Series grouping.

#In this exercise your job is to investigate survival rates of passengers on the 
#Titanic by 'age' and 'pclass'. In particular, the goal is to find out what 
#fraction of children under 10 survived in each 'pclass'. 

# Create the Boolean Series: under10
under10 = titanic['age'] < 10
under10 = under10.map({True:'under 10', False:'over 10'})

# Group by under10 and compute the survival rate
survived_mean_1 = titanic.groupby(under10)['survived'].mean()
print(survived_mean_1)

# Group by under10 and pclass and compute the survival rate
survived_mean_2 = titanic.groupby([under10, 'pclass'])['survived'].mean()
print(survived_mean_2)

# =============================================================================
# Chapter 5
# 
# Case Study - Summer Olympics
# =============================================================================

medals = pd.read_csv('data/all_medals.csv')

# =============================================================================
# Using .value_counts() for ranking
# =============================================================================

#For this exercise, you will use the pandas Series method .value_counts() to 
#determine the top 15 countries ranked by total number of medals.
#
#Notice that .value_counts() sorts by values by default.

# Select the 'NOC' column of medals: country_names
country_names = medals['NOC']

# Count the number of medals won by each country: medal_counts
medal_counts = country_names.value_counts()

# We could use groupby as well
medal_counts = medals.groupby(country_names)['Medal'].count()

# Print top 15 countries ranked by medals
print(medal_counts.head(15))

# =============================================================================
# Using .pivot_table() to count medals by type
# 
# Rather than ranking countries by total medals won and showing that list, 
# you may want to see a bit more detail. You can use a pivot table to compute 
# how many separate bronze, silver and gold medals each country won. 
# That pivot table can then be used to repeat the previous computation to rank by 
# total medals won.
# =============================================================================

# Construct the pivot table: counted
counted = medals.pivot_table(index = 'NOC', 
                             values= 'Athlete',columns= 'Medal', aggfunc='count')

# Create the new column: counted['totals']
counted['totals'] = counted.sum(axis = 'columns')

# Sort counted by the 'totals' column
counted = counted.sort_values(by = 'totals',ascending= False)

# Print the top 15 rows of counted
print(counted.head(15))

# =============================================================================
# Applying .drop_duplicates()
# =============================================================================

#What could be the difference between the 'Event_gender' and 'Gender' columns? 
#You should be able to evaluate your guess by looking at the unique values of the 
#pairs (Event_gender, Gender) in the data. In particular, you should not see 
#something like (Event_gender='M', Gender='Women')

# Select columns: ev_gen
ev_gen = medals[['Event_gender', 'Gender']]

# Drop duplicate pairs: ev_gen_uniques
ev_gen_uniques = ev_gen.drop_duplicates()

# Print ev_gen_uniques
print(ev_gen_uniques)

# =============================================================================
# Finding possible errors with .groupby()
# =============================================================================

#You will now use .groupby() to continue your exploration. 
#Your job is to group by 'Event_gender' and 'Gender' and count the rows.

# Group medals by the two columns: medals_by_gender
medals_by_gender = medals.groupby(['Event_gender','Gender'])

# Create a DataFrame with a group count: medal_count_by_gender
medal_count_by_gender = medals_by_gender.count()

# Print medal_count_by_gender
print(medal_count_by_gender)

#Locating suspicious data
#You will now inspect the suspect record by locating the offending row.

# Create the Boolean Series: sus
sus = (medals.Event_gender == 'W') & (medals.Gender == 'Men')

# Create a DataFrame with the suspicious row: suspect
suspect = medals[sus]

# Print suspect
print(suspect)

# =============================================================================
# Constructing alternative country rankings
# =============================================================================

# Using .nunique() to rank by distinct sports

#You may want to know which countries won medals in the most distinct sports. 
#The .nunique() method is the principal aggregation here. Given a categorical 
#Series S, S.nunique() returns the number of distinct categories

# Group medals by 'NOC': country_grouped
country_grouped = medals.groupby("NOC")

# Compute the number of distinct sports in which each country won medals: Nsports
Nsports = country_grouped['Sport'].nunique()

# Sort the values of Nsports in descending order
Nsports = Nsports.sort_values(ascending=False)

# Print the top 15 rows of Nsports
print(Nsports.head(15))

#Interestingly, the USSR is not in the top 5 in this category, while the USA 
#continues to remain on top. What could be the cause of this? We will compare 
#the medal counts of USA vs. USSR more closely. 

# =============================================================================
# Counting USA vs. USSR Cold War Olympic Sports
# =============================================================================

#Your goal in this exercise is to aggregate the number of distinct sports in which 
#the USA and the USSR won medals during the Cold War years(between 1952 and 1988)

# Extract all rows for which the 'Edition' is between 1952 & 1988: during_cold_war
during_cold_war = (medals['Edition'] >= 1952) & (medals['Edition'] <= 1988)

# Extract rows for which 'NOC' is either 'USA' or 'URS': is_usa_urs
is_usa_urs = medals.NOC.isin(['USA', 'URS'])

# Use during_cold_war and is_usa_urs to create the DataFrame: cold_war_medals
cold_war_medals = medals.loc[during_cold_war & is_usa_urs]

# Group cold_war_medals by 'NOC'
country_grouped = cold_war_medals.groupby('NOC')

# Create Nsports
Nsports = country_grouped['Sport'].nunique().sort_values(ascending = False)

# Print Nsports
print(Nsports)

#As you can see, the USSR is actually higher than the US when you look only at 
#the Olympic competitions between 1952 and 1988!

# =============================================================================
# Counting USA vs. USSR Cold War Olympic Medals
# =============================================================================

#For this exercise, you want to see which country, the USA or the USSR, won the
# most medals consistently over the Cold War period.

# Create the pivot table: medals_won_by_country
medals_won_by_country = medals.pivot_table(index = 'Edition', 
                                           values = "Athlete", 
                                           columns= 'NOC', aggfunc= 'count')

# Slice medals_won_by_country: cold_war_usa_urs_medals
cold_war_usa_urs_medals = medals_won_by_country.loc[1952:1988, ['USA','URS']]

# Create most_medals 
most_medals = cold_war_usa_urs_medals.idxmax(axis = 'columns')

# Print most_medals.value_counts()
print(most_medals.value_counts())

#Here, once again, the USSR comes out on top

# =============================================================================
# Visualizing USA Medal Counts by Edition: Line Plot
# =============================================================================

# Create the DataFrame: usa
usa = medals[medals.NOC == 'USA']

# Group usa by ['Edition', 'Medal'] and aggregate over 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level = 'Medal')


# Plot the DataFrame usa_medals_by_year
usa_medals_by_year.plot()
plt.show()


#Visualizing USA Medal Counts by Edition: Area Plot

#visualize the medal counts by 'Edition' for the USA. 
#This time, you will use an area plot to see the breakdown better. 

# Create an area plot of usa_medals_by_year
usa_medals_by_year.plot.area()
plt.show()


#Visualizing USA Medal Counts by Edition: Area Plot with Ordered Medals

#You may have noticed that the medals are ordered according to a 
#lexicographic (dictionary) ordering: Bronze < Gold < Silver. 
#However, you would prefer an ordering consistent with the Olympic 
#rules: Bronze < Silver < Gold.
#
#You can achieve this using Categorical types

# Redefine 'Medal' as an ordered categorical
medals.Medal = pd.Categorical(values = medals.Medal, categories=['Bronze', 
'Silver', 'Gold'], ordered = True)
    
#After this, you can verify that the type has changed using 
    
medals.info()

# Create the DataFrame: usa
usa = medals[medals.NOC == 'USA']

# Group usa by 'Edition', 'Medal', and 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

# Create an area plot of usa_medals_by_year
usa_medals_by_year.plot.area()
plt.show()

