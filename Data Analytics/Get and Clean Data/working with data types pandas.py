# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 08:59:02 2023

@author: geron
"""

#you can check for datatype of column using the .dtypes
#print(column_name.dtypes)

#You might also need to change the datatype as well.  Use .astype for this
# df['column_name'] = df['column_name'].astype('data_type')


# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("netflix_movies.csv")

# View the first five rows of the dataframe
print(movies.head())

# Print the data types
print(movies.dtypes)

# Fill in the missing cast_count values with 0
movies['cast_count'].fillna(0, inplace = True)

# Change the type of the cast_count column
movies['cast_count'] = movies['cast_count'].astype('int64')

# Check the data types of the columns again. 
print(movies.dtypes)


import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv("netflix_movies.csv")

# View the first five rows of the dataframe
print(movies.head())

# Print the data types of dataframe 
print(movies.dtypes)

# Add the variables you plan to change to this list
change = ['title']

# Change the title variable to a "string"
movies['title'] = movies['title'].astype('string')
# Change any other variables
movies['country'] = movies['country'].astype('string')
# Print the data types again
print(movies.dtypes)



import pandas as pd

# Import dataset as a Pandas Dataframe
movies = pd.read_csv('netflix_movies.csv')

# View the first five rows of the dataframe
print(movies.head())

# Print the unique values of the rating column
print(movies['rating'].unique())

# Change the data type of `rating` to category
movies['rating'] = pd.Categorical(movies['rating'], ['NR', 'G', 'PG', 'PG-13', 'R'], ordered=True)

# Recheck the values of `rating` with .unique()
print(movies['rating'].unique())


#.get_dummies is called one-hot encoding for dealing with categorical variables
import pandas as pd

# Import dataset as a Pandas Dataframe
cereal = pd.read_csv('cereal.csv', index_col=0)

# Show the first five rows of the `cereal` dataframe
print(cereal.head())

# Create a new dataframe with the `mfr` variable One-Hot Encoded
cereal = pd.get_dummies(cereal, columns = ['mfr'])

# Show first five rows of new dataframe
print(cereal.head(5))





# Return the first 10 rows of the auto dataframe.

# Return the data types of the auto dataframe with the .dtypes attribute.

# Change the price category from int to float with the .astype() method, then recheck the data types with .dtypes.

# Convert the engine_size variable to the category data type with an order of [‘small’, ‘medium’, ‘large’], and check the order with the .unique() method.

# Create a new variable called engine_codes which contains the numerical codes associated with each category in the engine_size variable with the .cat.codes accessor. Check the new values with the .head() method.

# One-Hot Encode the body-style category in the auto dataframe. Then check the dataframe with .head().


import pandas as pd

# Import dataset as a Pandas Dataframe
auto = pd.read_csv('autos.csv', index_col=0)

# Print the first 10 rows of the auto dataset
print(auto.head(10))

# Print the data types of the auto dataframe
print(auto.dtypes)

# Change the data type of price to float
auto['price'] = auto['price'].astype('float')
print(auto.dtypes)

# Set the engine_size data type to category
auto['engine_size'] = pd.Categorical(auto['engine_size'], ['small', 'medium', 'large'], ordered=True)
print(auto['engine_size'].unique())
# Create the engine_codes variable by encoding engine_size - seems to be used on data types of category caled label encoding
auto['engine_codes'] = auto['engine_size'].cat.codes
print(auto.head())

# One-Hot Encode the body-style variable
auto = pd.get_dummies(auto, columns=['body-style'])
print(auto.head(5))