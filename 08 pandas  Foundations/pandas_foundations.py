#importing pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Reading in the dataset
apple = pd.read_csv('data/aapl.csv', index_col = 0)

# check how many rows and columns
apple.shape

#check the column names
apple.columns

# the apple.columns attribute is a pandas index
type(apple.columns)

# the apple.index attribute is a special kind of index called the Datetimeindex
type(apple.index)

# Dataframes can be sliced like numpy arrays

apple.iloc[:5,:]

apple.iloc[-5:,:]

apple.head(7)

apple.info()

#pandas dataframes slices also support broadcasting

# This selects every 3 row starting from 0 of the last column and assigns them to nan
apple.iloc[::3, -1] = np.nan

apple.head(6)

# The columns of a dataframe are themselves a specialized pandas structure called a series

low = apple['Low']
type(low)

# =============================================================================
# Notice that the Series extracted has its own head() method and inherits its 
# name attribute from the dataframe column.
# 
# To extract the numerical entries from the series, use the values attribute. 
# The data in the Series actually form a numpy array which is what the values attribute yields. 
# 
# A pandas series is a one dimensional labelled Numpy array and a dataframe is a 2 dimensional 
# labelled array whose columns are series. 
# =============================================================================

# =============================================================================
# NumPy and pandas working together
# Pandas depends upon and interoperates with NumPy, the Python library for fast 
# numeric array computations. For example, you can use the DataFrame 
# attribute .values to represent a DataFrame df as a NumPy array. 
# You can also pass pandas data structures to NumPy methods. 
# In this exercise, we have imported pandas as pd and loaded world population 
# data every 10 years since 1960 into the DataFrame df. 
# This dataset was derived from the one used in the previous exercise.
# =============================================================================

year = [1960, 1970, 1980, 1990, 2000, 2010 ]
population = [3.034971e+09, 3.684823e+09, 4.436590e+09, 5.282716e+09, 6.115974e+09, 6.924283e+09]

world = {'population':population}

world_df = pd.DataFrame.from_dict(world)

world_df.index = year

# Create array of DataFrame values: np_vals
np_vals = world_df.values

# Create new array of base 10 logarithm values: np_vals_log10
np_vals_log10 = np.log10(np_vals)

# Create array of new DataFrame by passing df to np.log10(): df_log10
df_log10 = np.log10(world_df)


# Print original and new data containers
[print(x, 'has type', type(eval(x))) for x in ['np_vals', 'np_vals_log10', 'world_df', 'df_log10']]

# =============================================================================
# Building DataFrames from scratch
# =============================================================================
cities = ['Austin', 'Dallas', 'Austin', 'Dallas']
signups = [7, 12, 3, 5]
visitors = [139, 237, 326, 456]
weekdays = ['Sun', 'Sun', 'Mon', 'Mon']

# creating labels
list_labels = ['city', 'signups', 'visitors', 'weekday']

list_col = [cities, signups, visitors, weekdays]

zipped = list(zip(list_labels, list_col))

data = dict(zipped)

users = pd.DataFrame(data)

# =============================================================================
# # BROADCASTING
# =============================================================================

users['fees'] = 0 #Broadcast to the entire column

# we can change the columns and index labels using the columns and index attribute

result.columns = ['height', 'sex'] # has to be of suitable length

# Zip the 2 lists together into one list of (key,value) tuples: zipped
list_keys = ['Country', 'Total']
list_values = [['United States', 'Soviet Union', 'United Kingdom'], [1118, 473, 273]]
zipped = list(zip(list_keys, list_values))

# Inspect the list using print()
print(zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)

# =============================================================================
# Labeling your data
# You can use the DataFrame attribute df.columns to view and assign new 
# string labels to columns in a pandas DataFrame.
# =============================================================================

# Build a list of labels: list_labels
list_labels = ['year','artist','song','chart weeks']

# Assign the list of labels to the columns attribute: df.columns
df.columns = list_labels

# =============================================================================
# Building DataFrames with broadcasting
# You can implicitly use 'broadcasting', a feature of NumPy, 
# when creating pandas DataFrames. In this exercise, you're going to create a 
# DataFrame of cities in Pennsylvania that contains the city name in one column
#  and the state name in the second. We have imported the names of 15 cities as 
#  the list cities
# =============================================================================

cities = ['Manheim', 'Preston park', 'Biglerville', 'Indiana', 'Curwensville', 
          'Crown', 'Harveys lake', 'Mineral springs', 'Cassville', 'Hannastown', 
          'Saltsburg', 'Tunkhannock', 'Pittsburgh', 'Lemasters', 'Great bend']


# Make a string with the value 'PA': state
state = 'PA'

# Construct a dictionary: data
data = {'state': state, 'city': cities}

# Construct a DataFrame from dictionary data: df
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# =============================================================================
# Importing & exporting data
# =============================================================================

filepath = 'data/SN_d_tot_V2.0.csv'

sunspots = pd.read_csv(filepath, sep = ';', header = None)

sunspots.info()

# let use iloc to view a slice in the middle of the data

sunspots.iloc[10:20,:]

# =============================================================================
# Column 1-3: Gregorian calendar date - year, month, day
# Column 4: Date in fraction of year.
# Column 5: Daily total sunspot number.
# A value of -1 indicates that no number is available for that day (missing value).
# Column 6: Daily standard deviation of the input sunspot numbers from individual stations.
# Column 7: Number of observations used to compute the daily value.
# Column 8: Definitive/provisional indicator. 
# '1' indicates that the value is definitive. '0' indicates that the value is still provisional.
# 
# =============================================================================

col_names = ['year', 'month', 'day', 'dec_date', 'sunspots', 'std', 'observations', 'definite']

sunspots = pd.read_csv(filepath, sep = ';', header = None, 
                       names = col_names,
                       na_values = '  -1') 
# The na_values would work but will affect other columns as well. We can use the different
# method below to select different columns and their different NA value coding

sunspots = pd.read_csv(filepath, sep = ';', header = None, 
                       names = col_names,
                       na_values = {'sunspots':['  -1']},
                       parse_dates = [[0,1,2]]) # since these columns contain year, month and day

sunspots.iloc[10:20,:]

sunspots.index = sunspots['year_month_day']
sunspots.index.name = 'date'

sunspots.info()

# Trimming redundant columns

cols = ['sunspots', 'definite']
sunspots = sunspots[cols]

# Writing files. Saving csv. exporting files

out_csv = 'data/sunspots.csv'
sunspots.to_csv(out_csv)

out_tsv = 'data/sunspots.tsv'
sunspots.to_csv(out_tsv, sep = '\t')

out_xlsx = 'data/sunspots.xlsx'
sunspots.to_excel(out_xlsx)


# Read in the file: df1
df1 = pd.read_csv(data_file)

# Create a list of the new column labels: new_labels
new_labels = ['year', 'population']

# Read in the file, specifying the header and names parameters: df2
df2 = pd.read_csv(data_file, header=0, names=new_labels)

# Print both the DataFrames
print(df1)
print(df2)

# Read the raw file as-is: df1
df1 = pd.read_csv('/usr/local/share/datasets/messy_stock_data.tsv')

# Print the output of df1.head()
print(df1.head())

# Read in the file with the correct parameters: df2
df2 = pd.read_csv('/usr/local/share/datasets/messy_stock_data.tsv',
                  delimiter=' ', 
                  header=3, 
                  comment='#')

# Print the output of df2.head()
print(df2.head())

# Save the cleaned up DataFrame to a CSV file without the index
df2.to_csv('tmp_clean_stock_data.csv', index=False)

# Save the cleaned up DataFrame to an excel file without the index
df2.to_excel('file_clean.xlsx', index=False)


# =============================================================================
# Plotting with pandas
# =============================================================================

apple = pd.read_csv('data/aapl.csv', 
                   index_col = 'Date', 
                   parse_dates = True)

apple.head(6)

apple.info()

close_arr = apple['Close'].values

plt.plot(close_arr)
plt.show()

# we can plot pandas series directly 
close_series = apple['Close']
plt.plot(close_series)
plt.show()

# Another even nice method is to apply the plot method directly

close_series.plot()
plt.show()

# We can plot all series at once 
apple.plot()
plt.yscale('log') # log scale on the y axis because volume is so much bigger 
plt.show()

# Another method

plt.plot(apple)
plt.show()

# Customizing plots

apple['Open'].plot(color = 'b', style = '.-', legend = True)

apple['Close'].plot(color = 'r', style = '.', legend = True)

# We zoom the axis in to the year 2014 with the vertical scale  from 0 to 100
# and we explicitly place a legend

plt.axis(('2014', '2015', 0, 100))
plt.show()

# SAVing plots
apple.loc['2015':'2017', ['Open', 'Close', 'High', 'Low']].plot()

plt.savefig('data/apple.png')
plt.savefig('data/apple.jpg')
plt.savefig('data/apple.pdf')

plt.show()

# Another example
# Create a plot with color='red'
df.plot(color = 'red')

# Add a title
plt.title('Temperature in Austin')

# Specify the x-axis label
plt.xlabel('Hours since midnight August 1, 2010')

# Specify the y-axis label
plt.ylabel('Temperature (degrees F)')

# Display the plot
plt.show()

# =============================================================================
# Comparing data from several columns can be very illuminating. 
# Pandas makes doing so easy with multi-column DataFrames. 
# By default, calling df.plot() will cause pandas to over-plot all
#  column data, with each column as a single line. 
# =============================================================================

# Plot all columns (default)
df.plot()
plt.show()

# Plot all columns as subplots. To do so, you need to specify subplots=True inside .plot()
# Plot all columns as subplots
df.plot(subplots = True)
plt.show()

# Plot just the Dew Point data
column_list1 = ['Dew Point (deg F)']
df[column_list1].plot()
plt.show()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['Temperature (deg F)','Dew Point (deg F)']
df[column_list2].plot()
plt.show()

# =============================================================================
# Visual exploratory data analysis
# =============================================================================

url = 'https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv'
iris = pd.read_csv(url)

print(iris.shape)

# plot 
iris.plot(x = 'sepal_length', y = 'sepal_width', 
          kind = 'scatter')
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()

# Boxplot
iris.plot(y = 'sepal_length', 
          kind = 'box')
plt.ylabel('sepal width (cm)')
plt.show()

# Histogram
iris.plot(y = 'sepal_length', bins = 15,
          kind = 'hist')
plt.xlabel('sepal length (cm)')
plt.show()


# =============================================================================
# Histogram options
# ● bins (integer): number of intervals or bins
# ● range (tuple): extrema of bins (minimum, maximum)
# ● normed (boolean): whether to normalize to one
# ● cumulative (boolean): compute Cumulative Distribution
# Function (CDF) 
# =============================================================================

iris.plot(y='sepal_length', kind='hist',
          bins=30, 
          range=(4,8), 
          normed=False)
plt.xlabel('sepal length (cm)')
plt.show()

# cumulative (boolean): compute Cumulative Distribution
# Function (CDF) . Both normed and cumulative must be True
iris.plot(y='sepal_length', kind='hist',
          bins=30, 
          cumulative = True, 
          normed=True)
plt.xlabel('sepal length (cm)')
plt.show()

#CDF is computed by adding up the areas of the rectangles under a normalized
#histogram. CDFs are used to compute the probability of observing a value 
#in a given range. For instance a sepal width between 2 and 4 cm. Intuitively,
#the CDF evaluated at, say, sepal length of 5cm is returns the probability of
#observing a flower with sepal length of up to 5cm. A CDF is often somewhat 
#a smooth curve increasing from 0 to 1. 

# 3 Different methods of plotting in pandas

iris.plot(kind = 'hist')
plt.show()

iris.plot.hist()
plt.show()

# The results differ
iris.hist(grid = False)
plt.show()


month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ibm = [153.309998, 161.940002, 160.500000,171.289993, 169.649994,
       162.660004,161.990005,147.889999,144.970001,140.080002,139.419998,137.619995]
aapl= [117.160004, 128.460007,124.430000,125.150002,130.279999,125.430000,
        121.300003, 112.760002,110.300003,119.500000,118.300003,105.260002]

goog = [534.522445,558.402511,548.002468,537.340027,532.109985,520.510010,
        625.609985,618.250000,608.419983,710.809998,742.599976,758.880005]

list_cols = ['month', 'ibm', 'aapl', 'goog']
list_vals = [month, ibm, aapl, goog]

zipped = list(zip(list_cols, list_vals))
diction = dict(zipped)

df = pd.DataFrame(diction)


# =============================================================================
# pandas line plots
# =============================================================================

# Create a list of y-axis column names: y_columns. Selecting multiple columns
y_columns = ['aapl', 'ibm']

# Generate a line plot
df.plot(x='month', y=y_columns)

# Add the title
plt.title('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# Display the plot
plt.show()

# =============================================================================
# pandas scatter plots
# =============================================================================

url = 'data/auto-mpg.csv'

df = pd.read_csv(url)

df.horsepower = pd.to_numeric(df['horsepower'], errors = 'coerce')

# Creating a new variable which is the result of weight/100
df['weight1'] = df.weight.apply(lambda x: x/100)

# Generate a scatter plot
df.plot(kind='scatter', x='horsepower', y='mpg', s=df['weight1'])

# Add the title
plt.title('Fuel efficiency vs Horse-power')

# Add the x-axis label
plt.xlabel('Horse-power')

# Add the y-axis label
plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
plt.show()

# =============================================================================
# pandas box plots
# =============================================================================
# Make a list of the column names to be plotted: cols
cols = ['weight', 'mpg']

# Generate the box plots
df.plot(subplots = True, kind = 'box', y = cols)

# Display the plot
plt.show()

# Another way

# Generate the box plots
df[cols].plot(kind='box', subplots=True)

# Display the plot
plt.show()

# =============================================================================
# pandas hist, pdf and cdf
# 
# Pandas relies on the .hist() method to not only generate histograms, 
# but also plots of probability density functions (PDFs) and 
# cumulative density functions (CDFs).
# =============================================================================

tips = sns.load_dataset("tips")

# Creating fraction 
tips['fraction'] = tips['tip']/tips['total_bill']


# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)

# Plot the PDF: probability density functions (PDFs) 
# ax=axes[0] means that this plot will appear in the first row.
tips.fraction.plot(ax=axes[0], 
                   kind='hist', 
                   bins=30, 
                   density=True, 
                   range=(0,.3))

# Plot the CDF: cumulative density functions (CDFs).
# to make the CDF appear on the second row, you need to specify ax=axes[1]

tips.fraction.plot(ax=axes[1], 
                   kind='hist', 
                   bins=30, 
                   density=True, 
                   cumulative=True, 
                   range=(0,.3))
plt.show()

# =============================================================================
# Statistical exploratory data analysis
# =============================================================================

# summarizing with describe()

iris.describe()

# Let's look in more detail the results of describe()

iris['sepal_length'].count() # Applied to series

iris[['petal_length', 'petal_width']].count() # Applied to dataframes

## AVERAGES 

iris['sepal_length'].mean() # applied to series

iris.mean() # Applied to dataframes

# Standard deviation. measures the spread. 
iris.std()

# The mean measures the tendency to a central value of a measurement. The std 
# measure it's spread. 

# Median

iris.median()

# Quaniles
# the quantile method computes the median by default
iris.quantile()

# we can specify what is to be computed. it accepts a list or arrays of values
# between 0 and 1

# This returns the interquartile range (IQR)
q = [0.25, 0.75]
iris.quantile(q)

# RAnge

# range is the interval between the max and min observations.

iris.min()
iris.max()

# Print the minimum value of the Engineering column
print(df['Engineering'].min())

# Print the maximum value of the Engineering column
print(df['Engineering'].max())

# Construct the mean percentage per year: mean
# Construct the mean percentage per year with .mean(axis='columns')
mean = df.mean(axis = 'columns')

# Plot the average percentage per year
mean.plot()

# Display the plot
plt.show()

# Print summary statistics of the fare column with .describe()
print(df.fare.describe())

# Generate a box plot of the fare column
df.fare.plot(kind = 'hist')

# Show the plot
plt.show()

# Print the number of countries reported in 2015
print(df['2015'].count())

# Print the 5th and 95th percentiles
print(df.quantile([0.05, 0.95]))

# Generate a box plot
years = ['1800','1850','1900','1950','2000']
df[years].plot(kind='box')
plt.show()

# Print the mean of the January and March data
print(january.mean(), march.mean())

# Print the standard deviation of the January and March data
print(january.std(), march.std())

# =============================================================================
# Separating populations with Boolean indexing
# =============================================================================

iris['species'].describe()

# Shows the unique or the distinct values
iris['species'].unique()

# Filtering by species

indices_1 = iris['species'] == 'setosa'
setosa = iris.loc[indices_1, :] # Extract the new dataframe

indices_2 = iris['species'] == 'virginica'
virginica = iris.loc[indices_2, :] 

indices_3 = iris['species'] == 'versicolor'
versicolor = iris.loc[indices_3, :]

setosa.head(2)
virginica.head(2)
versicolor.head(2)

# =============================================================================
# Visual EDA: all data
# =============================================================================
iris.plot(kind= 'hist', bins=50, range=(0,8), alpha=0.3)
plt.title('Entire iris data set')
plt.xlabel('[cm]')
plt.show()

# =============================================================================
# Visual EDA: individual factors
# =============================================================================
setosa.plot(kind='hist', bins=50, range=(0,8), alpha=0.3)
plt.title('Setosa data set')
plt.xlabel('[cm]')

versicolor.plot(kind='hist', bins=50, range=(0,8), alpha=0.3)
plt.title('Versicolor data set')
plt.xlabel('[cm]')

virginica.plot(kind='hist', bins=50, range=(0,8), alpha=0.3)
plt.title('Virginica data set')
plt.xlabel('[cm]')

plt.show()

# =============================================================================
# Statistical EDA: describe()
# =============================================================================

# Let's see which one is better...using describe for other individual factors (groups)
# or putting everything together

describe_all = iris.describe()

describe_setosa = setosa.describe()
describe_versicolor = versicolor.describe()
describe_virginica = virginica.describe()

#Computing errors

error_setosa = 100 * np.abs(describe_setosa - describe_all)

error_setosa = error_setosa/describe_setosa

error_versicolor = 100 * np.abs(describe_versicolor - describe_all)
error_versicolor = error_versicolor/describe_versicolor

error_virginica = 100 * np.abs(describe_virginica - describe_all)
error_virginica = error_virginica / describe_virginica

# =============================================================================
# Filtering and counting
# =============================================================================

path = 'data/auto-mpg.csv'
fuel = pd.read_csv(path)
fuel.horsepower = pd.to_numeric(df['horsepower'], errors = 'coerce')

indices = fuel['origin'] == 2

fuel.loc[indices, :].count()

# =============================================================================
# Separate and summarize
# =============================================================================
#Let's use population filtering to determine how the automobiles in the 
#US differ from the global average and standard deviation. 
#How does the distribution of fuel efficiency (MPG) for the US differ from 
#the global average and standard deviation?

# Compute the global mean and global standard deviation: global_mean, global_std
global_mean = fuel.mean()
global_std = fuel.std()

# Filter the US population from the origin column: us
us = df.loc[fuel['origin'] == 1, :]

# Compute the US mean and US standard deviation: us_mean, us_std
us_mean = us.mean()
us_std = us.std()

# Print the differences
print(us_mean - global_mean)
print(us_std - global_std)

# =============================================================================
# Separate and plot
# =============================================================================

# Display the box plots on 3 separate rows and 1 column
fig, axes = plt.subplots(nrows=3, ncols=1)

# Generate a box plot of the fare prices for the First passenger class
titanic.loc[titanic['pclass'] == 1].plot(ax=axes[0], y='fare', kind='box')

# Generate a box plot of the fare prices for the Second passenger class
titanic.loc[titanic['pclass'] == 2].plot(ax=axes[1], y='fare', kind='box')

# Generate a box plot of the fare prices for the Third passenger class
titanic.loc[titanic['pclass'] == 3].plot(ax=axes[2], y='fare', kind='box')

# Display the plot
plt.show()

# =============================================================================
# Indexing pandas time series
# =============================================================================

#The pd.read_csv function can read strings into datetime objects. The 
#parse_dates = True option helps transform dates & times in ISO 8601 format 
#from specified columns into datetime objects. The ISO 8601 format reads like this:
#yyyy-mm-dd hh:mm:ss. read_csv can also flexibly read from many date & time formats.

#As an example, consider some sales data from a company that sells Hardward, 
#Sofware and Service products. 

# Creating data to illustrate the point
Date = ['2015-02-02 08:30:00','2015-02-02 21:00:00', '2015-02-03 14:00:00',
        '2015-02-04 15:30:00', '2015-02-04 22:00:00', '2015-02-05 02:00:00',
        '2015-02-05 22:00:00']

Company = ['Hooli', 'Mediacore', 'Initech',
           'Streeplex', 'Acme Coporation','Amin','Apple' ]

Product = ['Software', 'Hardware','Software', 'Software', 'Hardware', 'Software',
           'Hardware']

Units = [3,9,13,13,14,19,10]

list_cols = ['Date','Company', 'Product', 'Units']
list_vals = [Date, Company, Product, Units]
zipped = list(zip(list_cols, list_vals))
data = dict(zipped)

sales = pd.DataFrame(data)

sales['Date'] = pd.to_datetime(sales['Date'])

sales.index = sales['Date']

del(sales['Date'])

# The date column contain datetime information in ISO 8601 format

# if we were importing the data :
    
sales = pd.read_csv('sales-feb-2015', 
                    parse_dates = True, index_col = 'Date')

# Datetime indexes are very useful for date exploration

sales.info()

# Selecting a single datetime

# Remember the .loc method can be used to select data by row and column
# so with the datetime in the index we can do very sophisticated selection

# We can select the company the made a purchase at this specific time
sales.loc['2015-02-02 21:00:00', 'Company'] 

# Selecting a whole day 

sales.loc['2015-02-04'] # we didn't specify a column name so all columns will be returned
# This is called partial string selection

# Alternative formats 

sales.loc['February 4, 2015']
sales.loc['2015-Feb-4']

# Whole months

sales.loc['2015-2']

# Whole years
sales.loc['2015']

# We can slice between partial datetimes

sales.loc['2015-2-1':'2015-2-20']

# The pandas to_datetime function can convert strings in ISO 8601 format to 
# pandas datetime objects

evening_2_11 = pd.to_datetime(['2015-2-11 20:00', '2015-2-11 21:00', 
                               '2015-2-11 22:00', '2015-2-11 23:00']) 

# Sometimes we need to reindex a series of a dataframe. Reindexing
#involves providing a new index and matching data as required. 
#
#Here, the reindex method returns a new dataframe with four rows corresponding 
#to the times in evening_2_11. 

sales.reindex(evening_2_11)

# Times without matches will be filled with NaN by default
#We can override the default behavior of filling with NaN. 
#Using the argument method = 'ffill' (which means forward fill), the empty 
#entries are filled using the nearest preceding non-null entry in each column.
#
#We can also specify method = 'bfill' (for backward fill) which is the opposite 
#of forward fill which may be better depending on the context. 

# =============================================================================
# Creating and using a DatetimeIndex
# 
# The pandas Index is a powerful way to handle time series data, 
# so it is valuable to know how to build one yourself. 
# Pandas provides the pd.to_datetime() function for just this task. 
# For example, if passed the list of strings 
# ['2015-01-01 091234','2015-01-01 091234'] and a 
# format specification variable, such as format='%Y-%m-%d %H%M%S, 
# pandas will parse the string into the proper datetime elements and 
# build the datetime objects.
# =============================================================================

time = pd.read_csv('data/times.csv', header = None)
time_list = list(time[0])

temp = pd.read_csv('data/temp_list.csv', header = None)
temp_list = list(temp[0])

press = pd.read_csv('data/pressure.csv', header = None)
press_list = list(press[0])

dp = pd.read_csv('data/dewpoint.csv', header = None)
dp_list = list(dp[0])

# Prepare a format string: time_format
time_format='%Y-%m-%d %H:%M'

 # format isn't working

# Convert date_list into a datetime object: my_datetimes
my_datetimes = pd.to_datetime(time_list, format=time_format)

# Construct a pandas Series using temperature_list and my_datetimes: time_series
time_series = pd.Series(temp_list,  index=my_datetimes)

# Naming index
time_series.index.name = 'Date'

# =============================================================================
# Partial string indexing and slicing
# 
# Pandas time series support "partial string" indexing. 
# What this means is that even when passed only a portion of the datetime, 
# such as the date but not the time, pandas is remarkably good at doing 
# what one would expect. 
# Pandas datetime indexing also supports a wide variety of 
# commonly used datetime string formats, even when mixed.
# =============================================================================
# Extract the hour from 9pm to 10pm on '2010-10-11': ts1
ts1 = time_series.loc['2010-01-14 21:00:00':'2010-01-14 22:00:00']

# Extract '2010-07-04' from ts0: ts2
ts2 = time_series.loc['2010-01-04']

# Extract data from '2010-12-15' to '2010-12-31': ts3
ts3 = time_series.loc['2010-01-15':'2010-01-20']

# =============================================================================
# Reindexing the Index
# 
# Reindexing is useful in preparation for adding or otherwise combining 
# two time series data sets. To reindex the data, we provide a new 
# index and ask pandas to try and match the old data to the new index. 
# If data is unavailable for one of the new index dates or times, you must 
# tell pandas how to fill it in. Otherwise, pandas will fill with NaN by default.
# 
# =============================================================================

# Reindex without fill method: ts3
ts3 = ts2.reindex(ts1.index)

# Reindex with fill method, using forward fill: ts4
ts4 = ts2.reindex(ts1.index, method ='ffill')

# Combine ts1 + ts2: sum12
sum12 = ts1 + ts2

# Combine ts1 + ts3: sum13
sum13 = ts1 + ts3

# Combine ts1 + ts4: sum14
sum14 = ts1 + ts4

# =============================================================================
# Resampling pandas time series
# =============================================================================

apple = pd.read_csv('data/aapl.csv', 
                   index_col = 'Date', 
                   parse_dates = True)

apple.info()

apple.head()

# using a process called resampling we can apply statistical methods, for 
#instance mean, sum, count, computed over different time intervals. 
#
#In the context of resampling, downsampling means reindexing a time series with
#equally spaced times of lower frequency (like going from daily to weekly)
#
#Downsampling: reducing dateime rows to slower frequency. 
#
#Upsampling is the opposite like going from daily to hourly. 
#
#Upsampling: increase datetime rows to faster frequency. 

#Here, we will use resample to get daily averages in February. 

daily_mean = sales.resample('D').mean()

# 3 important things to notice here

#first, the method resample needs a string specifying the frequency, here 'D' stands
#for daily. 
#    
#second, the resample method is chained with the mean method. It is best practice
#to always follow resample with some statistical method in this way. 
#
#Third, the result is a dataframe with daily frequency for February, 2015 with 
#the average number of units sold each day. the columns company and product are 
#non-numerical and hence are ignored. Missing days are filled with NaN but that 
#can be changed. 

# Verifying

print(daily_mean.loc['2015-02-02'])

print(sales.loc['2015-02-02', 'Units'])

print(sales.loc['2015-02-02', 'Units'].mean())

# Method Chaining

# We can build long chains of methods if we want
sales.resample('D').sum().max()

# Weekly. 
sales.resample('W').count()

# The result has 3 columns because the count() method accounts for strings also

# Sampling frequencies

#'min', 'T' -- minute
#'H' -- Hour
#'D' -- Daily
#'B' -- Business day 
#'W' -- Weekly
#'M' -- Monthly
#'Q' -- Quarter
#'A' -- year/annual
#
#We can use integer multiples of these frequencies 

sales.loc[:,'Units'].resample('2W').sum()

# Notice the first entry is Feb 8; this is the same value as the first row 
#when using 'W'. By default, the '2W' offset is aligned by Sundays and Feb 8 was 
#the second Sunday of the month in 2015. 
#
#Up till now, we've been downsampling. Downsampling uses a coarser time index with
#fewer samples (for instance downsampling a statistic from daily to weekly data)]
#the opposite is upsampling; making a finer time index with more samples(for instance 
#upsampling from daily to hourly data)

two_day = sales.loc['2015-2-4':'2015-2-5', 'Units']

two_day.resample('4H').sum()

two_day.resample('4H').ffill()

# chaining the ffill() method fills in the number of sales using the forward -fill
#method that you've already seen. The technical term for this is interpolation. 
#We can also use bfill() or other methods. The resulting index the represents
#the starting time of each 4 hour increment. 

# Excercies

# Creating a dataframe
dictionary = {'temperature':temp_list, 'pressure':press_list, 'dewpoint':dp_list}

weather = pd.DataFrame(dictionary)

weather.index = my_datetimes

weather.index.name = 'datetime'

weather.to_csv('data/austin_weather.csv')

# Downsample to 6 hour data and aggregate by mean: df1
df1 = weather.loc[:, 'temperature'].resample('6H').mean()

# Downsample to daily data and count the number of data points: df2
df2 = weather.loc[:, 'temperature'].resample('D').count()

# Extract temperature data for january: january
january = weather.loc['2010-01', 'temperature']

# Downsample to obtain only the daily highest temperatures in August: august_highs
january_highs = january.resample('D').max()

# Extract temperature data for February: february
february = weather.loc['2010-02', 'temperature']

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()

# =============================================================================
# Rolling mean and frequency
# =============================================================================

#Rolling means (or moving averages) are generally used to smooth out 
#short-term fluctuations in time series data and highlight long-term trends. 
#
#To use the .rolling() method, you must always use method chaining, 
#first calling .rolling() and then chaining an aggregation method after it. 
#For example, with a Series hourly_data, hourly_data.rolling(window=24).mean()
# would compute new values for each hourly point, based on a 24-hour window 
# stretching out behind each point. 
# The frequency of the output data is the same: it is still hourly. 
# Such an operation is useful for smoothing time series data.

# Extract data from 2010-Jan-01 to 2010-Jan-15: unsmoothed
unsmoothed = weather['temperature']['2010-Jan-01':'2010-Jan-15']

# Apply a rolling mean with a 24 hour window: smoothed
smoothed = unsmoothed.rolling(window=24).mean()

# Create a new DataFrame with columns smoothed and unsmoothed: jan
jan = pd.DataFrame({'smoothed':smoothed, 'unsmoothed':unsmoothed})

# Plot both smoothed and unsmoothed data using jan.plot().
jan.plot()
plt.show()


# =============================================================================
# Resample and roll with it
# 
# As of pandas version 0.18.0, the interface for applying rolling 
# transformations to time series has become more consistent and flexible, 
# and feels somewhat like a groupby (If you do not know what a groupby is, 
# don't worry, you will learn about it in the next course!).
# 
# You can now flexibly chain together resampling and rolling operations.
# =============================================================================

# Extract the August 2010 data: january
january = weather['temperature']['2010-01']

# Resample to daily data, aggregating by max: daily_highs
daily_highs = january.resample('D').max()

# Use a rolling 7-day window with method chaining to smooth the daily high temperatures in August
daily_highs_smoothed = daily_highs.rolling(window = 7).mean()
print(daily_highs_smoothed)

# =============================================================================
# Manipulating pandas time series
# =============================================================================

# unlike previously, we won't use the date as the index
sales_df = pd.DataFrame(data)
sales_df['Date'] = pd.to_datetime(sales_df['Date'])

# sales_df contains two columns of strings

# String methods

# Transform all the company names to capital letters

sales_df['Company'].str.upper()

# String matching

sales_df['Product'].str.contains('ware')

sales_df['Product'].str.contains('ware').sum()

# Datetime methods

sales_df['Date'].dt.hour # 0 midnight and 23 is 11pm

# Setting timezones and converting from timezones

# Here we are setting the timezone to US/Central. This makes the datetime
# timezone-aware
central = sales_df['Date'].dt.tz_localize('US/Central')

# we can now convert to US/Eastern time

central.dt.tz_convert('US/Eastern')

# We can perform everything at once

sales_df['Date'].dt.tz_localize('US/Central').dt.tz_convert('US/Eastern')

# Interpolation

# CReating dataframe for interpolation illustration

world = pd.read_csv('data/world_population.csv')

world['month'] = 12
world['day'] = 31

#Saving csv
world.to_csv('data/world_pop.csv', index = False)

world_df = pd.read_csv('data/world_pop.csv', 
                       parse_dates = [[0,2,3]], 
                       index_col = 'Year_month_day')

# Using broadcasting to select every 10th year
population = world_df.iloc[::10, :]

#Upsample population
# here we use resample to upsample the data for every year between 1960 to 2010

population.resample('A').first()

# by extracting the first value from every decade with the first() method, 
#we see that pandas fills in NaN for years in between. Rather than ffill(), it
#is better to use other interpolation schemes to fill the unsampled time series.

# Interpolate missing data 

# the method interpolate('linear') chained with resample applies linear 
# interpolation to fill values in. 

population.resample('A').first().interpolate('linear')

# this yields a smooth time series with a reasonable model of yearly world
# population. 

# Exercises

# Method chaining and filtering

# Strip extra whitespace from the column names: df.columns
df.columns = df.columns.str.strip()

# Extract data for which the destination airport is Dallas: dallas
dallas = df['Destination Airport'].str.contains('DAL')

# Compute the total number of Dallas departures each day: daily_departures
daily_departures = dallas.resample('D').sum()

# Generate the summary statistics for daily Dallas departures: stats
stats = daily_departures.describe()


#Missing values and interpolation

# CReating data data for illustration

ts1 =pd.read_csv('data/ts1.csv', delimiter = '\s+', 
                 header = None,
                 index_col = 0,
                 parse_dates = True)

ts2 =pd.read_csv('data/ts2.csv', delimiter = '    ',
                 header = None,
                 index_col = 0,
                 engine = 'python',
                 parse_dates = True)

# Reset the index of ts2 to ts1, and then use linear interpolation 
# to fill in the NaNs: ts2_interp
ts2_interp = ts2.reindex(ts1.index).interpolate(how = 'linear')

# Compute the absolute difference of ts1 and ts2_interp: differences 
differences = np.abs(ts1 - ts2_interp)

# Generate and print summary statistics of the differences
print(differences.describe())

# Build a Boolean mask to filter out all the 'LAX' departure flights: mask
mask = df['Destination Airport'] == 'LAX'

# Use the mask to subset the data: la
la = df[mask]

# Concatenate / Combine two columns of data to create a datetime series: times_tz_none 
times_tz_none = pd.to_datetime( la['Date (MM/DD/YYYY)'] + ' ' + la['Wheels-off Time'] )

# Localize the time to US/Central: times_tz_central
times_tz_central = times_tz_none.dt.tz_localize('US/Central')

# Convert the datetimes from US/Central to US/Pacific
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')

# =============================================================================
# Visualizing pandas time series
# =============================================================================

# pandas plot
apple['Close'].plot(title = 'Apple Stock')
plt.ylabel('Closing price (US Dollars)')
plt.show()

# one week
apple.loc['2014-4-1':'2014-4-7','Close'].plot(style = 'k.--', 
         title = 'Apple Stock')
plt.ylabel('Closing price (US Dollars)')
plt.show()


# Style formatting. 
#The style format consist of 3 characters. The first one is the color (k: black)
#The second is the marker (. is for dot) and the last character controls the 
#line style (- for solid line)

# =============================================================================
# Color       Marker      Line
# b: blue     o: circle   : dotted
# g: green    *: star     –- : dashed
# r: red      s: square
# c: cyan     +: plus
# 
# =============================================================================

apple.loc['2014-4-1':'2014-4-7','Close'].plot(style = 'g*--', 
         title = 'Apple Stock')
plt.ylabel('Closing price (US Dollars)')
plt.show()

# Area plot

# using kind = 'area' plots the closing price at the end of each month, first 
#by resampling the data

apple['Close'].plot(kind = 'area', 
         title = 'Apple Stock')
plt.ylabel('Closing price (US Dollars)')
plt.show()

# plotting multiple columns 

apple.loc['2015', ['Close','Volume']].plot(title='Apple Stock')
plt.show()

# Subplots 

apple.loc['2015', ['Close','Volume']].plot(subplots = True)
plt.show()

# Excercises

# Plot the raw data before setting the datetime index
df.plot()
plt.show()

# Convert the 'Date' column into a collection of datetime objects: df.Date
df.Date = pd.to_datetime(df.Date)

# Set the index to be the converted 'Date' column.
#Set the index to this updated 'Date' column, 
#using df.set_index() with the optional keyword 
#argument inplace=True, so that you don't have to assign the result 
#back to df

df.set_index('Date', inplace=True)

# Re-plot the DataFrame to see that the axis is now datetime aware!
df.plot()
plt.show()

#Plotting date ranges, partial indexing

austin = pd.read_csv('data/austin_weather.csv', parse_dates = True)
austin.set_index('datetime', inplace = True)


# Plot the summer data
df.Temperature['2010-Jun':'2010-Aug'].plot()
plt.show()
plt.clf()

# Plot the one week data
df.Temperature['2010-06-10':'2010-06-17'].plot()
plt.show()
plt.clf()

# =============================================================================
# Case Study - Sunlight in Austin
# =============================================================================

#Datasets
#Climate normals of Austin, Texas from 1981 to 2010.

url = 'https://raw.githubusercontent.com/wblakecannon/DataCamp/master/11-pandas-foundations/_datasets/weather_data_austin_2010.csv'

austin_norm = pd.read_csv(url, parse_dates = True, index_col = 'Date')

print(austin_norm.head())
# Hourly Weather data from 2011

url_2 = 'https://raw.githubusercontent.com/wblakecannon/DataCamp/master/11-pandas-foundations/_datasets/NOAA_QCLCD_2011_hourly_13904.txt'

austin_noaa = pd.read_csv(url_2, header = None)

column_labels = 'Wban,date,Time,StationType,sky_condition,sky_conditionFlag,visibility,visibilityFlag,wx_and_obst_to_vision,wx_and_obst_to_visionFlag,dry_bulb_faren,dry_bulb_farenFlag,dry_bulb_cel,dry_bulb_celFlag,wet_bulb_faren,wet_bulb_farenFlag,wet_bulb_cel,wet_bulb_celFlag,dew_point_faren,dew_point_farenFlag,dew_point_cel,dew_point_celFlag,relative_humidity,relative_humidityFlag,wind_speed,wind_speedFlag,wind_direction,wind_directionFlag,value_for_wind_character,value_for_wind_characterFlag,station_pressure,station_pressureFlag,pressure_tendency,pressure_tendencyFlag,presschange,presschangeFlag,sea_level_pressure,sea_level_pressureFlag,record_type,hourly_precip,hourly_precipFlag,altimeter,altimeterFlag,junk'

#Convert the comma separated string column_labels to a list of 
#strings using .split(','). Assign the result to column_labels_list

# Split on the comma to create a list: column_labels_list
column_labels_list = column_labels.split(',')

# Assign the new column labels to the DataFrame: df.columns
austin_noaa.columns = column_labels_list

list_to_drop = ['sky_conditionFlag',
 'visibilityFlag',
 'wx_and_obst_to_vision',
 'wx_and_obst_to_visionFlag',
 'dry_bulb_farenFlag',
 'dry_bulb_celFlag',
 'wet_bulb_farenFlag',
 'wet_bulb_celFlag',
 'dew_point_farenFlag',
 'dew_point_celFlag',
 'relative_humidityFlag',
 'wind_speedFlag',
 'wind_directionFlag',
 'value_for_wind_character',
 'value_for_wind_characterFlag',
 'station_pressureFlag',
 'pressure_tendencyFlag',
 'pressure_tendency',
 'presschange',
 'presschangeFlag',
 'sea_level_pressureFlag',
 'hourly_precip',
 'hourly_precipFlag',
 'altimeter',
 'record_type',
 'altimeterFlag',
 'junk']

# Remove the appropriate columns: df_dropped
a_noaa_dropped = austin_noaa.drop(list_to_drop, axis = 'columns')

# Print the output of df_dropped.head()
print(a_noaa_dropped.head())

#Cleaning and tidying datetime data

# Convert the date column to string: df_dropped['date']
a_noaa_dropped['date'] = a_noaa_dropped.date.astype(str)

# Add leading zeros to the 'Time' column. 
# Pad leading zeros to the Time column: df_dropped['Time']

a_noaa_dropped['Time'] = a_noaa_dropped['Time'].apply(lambda x:'{:0>4}'.format(x))

# Concatenate the new date and Time columns: date_string

date_string = a_noaa_dropped['date'] + a_noaa_dropped['Time']

# Convert the date_string Series to datetime: date_times
date_times = pd.to_datetime(date_string, format='%Y%m%d%H%M')

# Set the index to be the new date_times container: df_clean
austin_noaa_clean = a_noaa_dropped.set_index(date_times)

# Print the output of df_clean.head()
print(austin_noaa_clean.head())

#Cleaning the numeric columns
#The numeric columns contain missing values labeled as 'M'. 
#In this exercise, your job is to transform these columns such that 
#they contain only numeric values and interpret missing data as NaN.
#
#The pandas function pd.to_numeric() is ideal for this purpose: 
#It converts a Series of values to floating-point values. 
#Furthermore, by specifying the keyword argument errors='coerce', 
#you can force strings like 'M' to be interpreted as NaN


# Print the dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011

print(austin_noaa_clean.loc['2011-Jun-20 08:00':'2011-Jun-20 09:00', 'dry_bulb_faren'])

# Convert the dry_bulb_faren column to numeric values: df_clean['dry_bulb_faren']
austin_noaa_clean['dry_bulb_faren'] = pd.to_numeric(austin_noaa_clean['dry_bulb_faren'], 
                 errors='coerce')

# Print the transformed dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(austin_noaa_clean.loc['2011-Jun-20 08:00':'2011-Jun-20 09:00', 'dry_bulb_faren'])

# Convert the wind_speed and dew_point_faren columns to numeric values
austin_noaa_clean['wind_speed'] = pd.to_numeric(austin_noaa_clean['wind_speed'], 
        errors='coerce')

austin_noaa_clean['dew_point_faren'] = pd.to_numeric(austin_noaa_clean['dew_point_faren'], 
        errors='corece')

#Statistical exploratory data analysis

#Signal min, max, median

# Print the median of the dry_bulb_faren column
print(austin_noaa_clean['dry_bulb_faren'].median())

# Print the median of the dry_bulb_faren column for the time range '2011-Apr':'2011-Jun'
print(austin_noaa_clean.loc['2011-Apr':'2011-Jun', 'dry_bulb_faren'].median())

# Print the median of the dry_bulb_faren column for the month of January
print(austin_noaa_clean.loc['2011-Jan', 'dry_bulb_faren'].median())

#Signal variance

#You're now ready to compare the 2011 weather data with the 30-year 
#normals reported in 2010. You can ask questions such as, on average, 
#how much hotter was every day in 2011 than expected from the 30-year average?
#
#
#Your job is to first resample austin_noaa_clean and austin_norm by day and aggregate 
#the mean temperatures. You will then extract the temperature related columns 
#from each - 'dry_bulb_faren' in df_clean, and 'Temperature' 
#in df_climate - as NumPy arrays and compute the difference.
#
#Notice that the indexes of df_clean and df_climate 
#are not aligned - df_clean has dates in 2011, while df_climate has 
#dates in 2010. This is why you extract the temperature 
#columns as NumPy arrays. An alternative approach is to use 
#the pandas .reset_index() method to make sure the Series align properly. 
#You will practice this approach as well.

# Downsample df_clean by day and aggregate by mean: daily_mean_2011
daily_mean_2011 = austin_noaa_clean.resample('D').mean()

# Extract the dry_bulb_faren column from daily_mean_2011 using .values: daily_temp_2011
daily_temp_2011 = daily_mean_2011['dry_bulb_faren'].values

# Downsample df_climate by day and aggregate by mean: daily_climate
daily_climate = austin_norm.resample('D').mean()

# Extract the Temperature column from daily_climate using .reset_index(): daily_temp_climate
daily_temp_climate = daily_climate.reset_index()['Temperature']

# Compute the difference between the two arrays and print the mean difference
difference = daily_temp_2011 - daily_temp_climate
print(difference.mean())

#Sunny or cloudy

#On average, how much hotter is it when the sun is shining? 
#In this exercise, you will compare temperatures on sunny days 
#against temperatures on overcast days.
#
#Your job is to use Boolean selection to filter out sunny and 
#overcast days, and then compute the difference of the mean daily 
#maximum temperatures between each type of day.
#
#The DataFrame austin_noaa_clean from previous exercises has been provided
#for you. The column 'sky_condition' provides information about whether 
#the day was sunny ('CLR') or overcast ('OVC').

# Using df_clean, when is sky_condition 'CLR'?
is_sky_clear = austin_noaa_clean['sky_condition']=='CLR'

# Filter df_clean using is_sky_clear
sunny = austin_noaa_clean[is_sky_clear]

# Resample sunny by day then calculate the max
sunny_daily_max = sunny.resample('D').max()

# See the result
sunny_daily_max.head()

# Using df_clean, when does sky_condition contain 'OVC'?
is_sky_overcast = austin_noaa_clean['sky_condition'].str.contains('OVC')

# Filter df_clean using is_sky_overcast
overcast = austin_noaa_clean[is_sky_overcast]

# Resample overcast by day then calculate the max
overcast_daily_max = overcast.resample('D').max()

# See the result
overcast_daily_max.head()

# From previous steps
is_sky_clear = austin_noaa_clean['sky_condition']=='CLR'
sunny = austin_noaa_clean.loc[is_sky_clear]
sunny_daily_max = sunny.resample('D').max()
is_sky_overcast = austin_noaa_clean['sky_condition'].str.contains('OVC')
overcast = austin_noaa_clean.loc[is_sky_overcast]
overcast_daily_max = overcast.resample('D').max()

# Calculate the mean of sunny_daily_max
sunny_daily_max_mean = sunny_daily_max.mean()

# Calculate the mean of overcast_daily_max
overcast_daily_max_mean = overcast_daily_max.mean()

# Print the difference (sunny minus overcast)
print(sunny_daily_max_mean - overcast_daily_max_mean)

#Weekly average temperature and visibility
#Is there a correlation between temperature and visibility? 

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

austin_noaa_clean.visibility = pd.to_numeric(austin_noaa_clean['visibility'],
                                             errors = 'coerce')

# Select the visibility and dry_bulb_faren columns and resample them: weekly_mean
weekly_mean = austin_noaa_clean[['visibility', 'dry_bulb_faren']].resample('W').mean()

# Print the output of weekly_mean.corr()
print(weekly_mean.corr())

# Plot weekly_mean with subplots=True
weekly_mean.plot(subplots=True)
plt.show()

#Daily hours of clear sky

#The 'sky_condition' column is recorded hourly. Your job is to resample 
#this column appropriately such that you can extract the number of sunny 
#hours in a day and the number of total hours. Then, you can divide the 
#number of sunny hours by the number of total hours, and generate a box 
#plot of the resulting fraction.


is_sky_clear = austin_noaa_clean['sky_condition'] == 'CLR'
resampled = is_sky_clear.resample('D')
sunny_hours = resampled.sum()
total_hours = resampled.count()
sunny_fraction = sunny_hours / total_hours

# Make a box plot of sunny_fraction
sunny_fraction.plot(kind='box')
plt.show()

#Heat or humidity

#Dew point is a measure of relative humidity based on pressure and 
#temperature. A dew point above 65 is considered uncomfortable while a 
#temperature above 90 is also considered uncomfortable.
#
#In this exercise, you will explore the maximum temperature and dew 
#point of each month. The columns of interest are 'dew_point_faren' and 
#'dry_bulb_faren'. After resampling them appropriately to get the maximum 
#temperature and dew point in each month, generate a histogram of these 
#values as subplots. Uncomfortably, you will notice that the maximum dew 
#point is above 65 every month!

# Resample dew_point_faren and dry_bulb_faren by Month, aggregating the maximum values: monthly_max
monthly_max = austin_noaa_clean[['dew_point_faren','dry_bulb_faren']].resample('M').max()

# Generate a histogram with bins=8, alpha=0.5, subplots=True
monthly_max.plot(kind='hist', bins=8, alpha=0.5, subplots=True)

# Show the plot
plt.show()

#Probability of high temperatures
#
#We already know that 2011 was hotter than the climate normals for the 
#previous thirty years. In this final exercise, you will compare the 
#maximum temperature in August 2011 against that of the August 2010 climate 
#normals. More specifically, you will use a CDF plot to determine the 
#probability of the 2011 daily maximum temperature in August being above 
#the 2010 climate normal value.

#Your job is to select the maximum temperature in August in df_climate, 
#and then maximum daily temperatures in August 2011. You will then filter 
#out the days in August 2011 that were above the August 2010 maximum, and 
#use this to construct a CDF plot.
#
#Once you've generated the CDF, notice how it shows that there was a 
#50% probability of the 2011 daily maximum temperature in August being 5 
#degrees above the 2010 climate normal value!

# Extract the maximum temperature in August 2010 from df_climate: august_max
august_max = austin_norm.loc['2010-Aug','Temperature'].max()
print(august_max)

# Resample August 2011 temps in df_clean by day & aggregate the max value: august_2011
august_2011 = austin_noaa_clean.loc['2011-Aug','dry_bulb_faren'].resample('D').max()

# Filter for days in august_2011 where the value exceeds august_max: august_2011_high

august_2011_high = august_2011.loc[august_2011 > august_max]

# Construct a CDF of august_2011_high
august_2011_high.plot(kind='hist', density=True, cumulative=True, bins=25)

# Display the plot
plt.show()
















