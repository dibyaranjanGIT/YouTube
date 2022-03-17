
# Importing necessary libraries
import pandas as pd
import numpy as np





# Reading the data files
movies = pd.read_csv('data/imdb_1000.csv')
drinks = pd.read_csv('data/drinks.csv')
drinks2 = pd.read_csv('data/drinks2.csv')
titanic = pd.read_csv('data/titanic.csv')
ufo = pd.read_csv('data/ufo.csv')



# Select columns by data type
ufo
ufo.dtypes
ufo.select_dtypes(include='number').head()

# Order the data frame
movies.index.sort_values()

# To get the unique values
movies.genre.unique()
movies.genre.nunique()

# Filter data by largest categories
counts = movies.genre.value_counts()
counts
counts.nlargest(3)

# Find the missing values 
ufo.isnull().sum()

# Reduce the dataFrame size 
pd.read_csv('movies.csv',use_cols=['title','genre'])

# Filter the data with more than one column
movies[(movies.duration >=200) & (movies.genre == 'Drama')]
movies[(movies.duration >=200) | (movies.genre == 'Drama')].head()

# pass the string 'all' to describe all columns
drinks.describe(include='all')

# How to use the axis column
drinks.drop('continent', axis=1).head()
drinks.drop(2, axis=0).head()

# How to use the string method contains
movies.actor_list.str.contains('Christian Bale').head()

# How to use the groupby 
drinks.groupby('continent').beer_servings.mean()

# How to use index column
drinks.set_index('country', inplace=True)
drinks.head()

# How to use loc
ufo.loc[0:2, :]

# How to use pd.get_dummies function
pd.get_dummies(titanic.Embarked, prefix='Embarked').head(10)

# How to find duplicate records


# How to display the max_rows 
pd.set_option('display.max_rows', None)
drinks

# How to use merge funcitonality
pd.merge(drinks, drinks2, left_on='m_id').head()

# How to use Concat funcitonlity
pd.concat([drinks, drinks2], axis = 1)

# Build a DataFrame from multiple files 

from glob import glob
stock_files = sorted(glob('data/stocks*.csv'))
stock_files
# To read the data row wise
pd.concat((pd.read_csv(file) for file in stock_files), ignore_index=True)
# To read the data column wise
pd.concat((pd.read_csv(file) for file in stock_files), axis='columns').head()
