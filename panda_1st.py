'''since if I want to use pandas I have to import panda module
why do we use panda we use panda because it is very good for the '''

'''the panda will have two main types  of data structure:
1] Series- a series is a one-dimensional array that can hold any data type. It is similar to a column in a spreadsheet or a database table.
 Each element in a series has an associated index, which can be used to access the elements.
 1-dimensional

Has index + values

Similar to a column in Excel

2] DataFrame- dataframe is a two-dimensional data structure that can hold data of different types (e.g., integer, float, string). 
It is similar to a table in a relational database or a spreadsheet. A dataframe consists of rows and columns, where each column can be
 considered as a series. Dataframes also have an associated index for both rows and columns, which can be used to access the data.

'''
import pandas as pd
s=pd.Series([1,2,3,423,123,242])
print(s)
'''in pandas the Series is the labeled array and list is unlabeled array
we can also give the index to the series according to our need 
which will update the indexes of the series'''
a=pd.Series([1,23,4,52,35,3] ,index=['a','b','c','d','e','f'])
print(a)

'''now we move towards the dataframes'''
df=pd.DataFrame({'name':['Ram','Raj','Rajat'],'marks':[13,23,53]})
print(df)