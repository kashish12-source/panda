'''when we want to read the files which contains the excel sheet and the jason sheet 
the pandas will have the builtin functions for that'''
import pandas as pd
df=pd.read_csv('c:/pythonkv/customer.csv')
print(df)
import os
print(os.path.exists("C:/pythonkv/customer.csv"))
'''this will show all the data of the customer excel sheet or csv sheet'''
'''if you use df.head()
it will show only the first 5 data of the sheet
and if you use the df .tail()
it will give you the last  5 data of the sheet
 
apart from this it will have another method called describe()
if you write df.describe()
it will describe the data of the sheet gives some details about count,mean,std,min etc

another method is df.Info()
it will tells about the range of the sheet and no. of rows and no. of columns and type

'''

'''another intersting thing is we can get information about the specific coulumn using the data selection
df['id]
it will show all the id of the sheet
if i write 
df['name']
it will show all the names that are present in the sheet
we can also get the multiple data at the same time
df[['id','name']]




another method is 
iloc[0]
df.iloc[0]
If we write this we will write this it will show all the description about the 1st row  
and its type is series 

'''
'''implementaion of the methods'''

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df['Name'])
print([['Age','Name']])
print(df.iloc[0])
''' if the file contain some row with the data which is not fill then if we print the data it will show the NaN 
which is not good so we have two methods to overcome from this:
1] df.dropna() : it will drop all those rows which contain the blank data or colulmns 
2] df.fillna('the value you want to show', inplace=True) genrally we donot use the inplace key word beacuase it will change the original data of the 
sheet '''
print(df)
print(df.dropna())


print(df.fillna('############'))


'''
we can also change the headings of the coulumns by using the method column
df.rename(columns={'old name':'new name'}, inplace=True)
'''

print(df.rename(columns={'Name':'naaam'}))

'''
in this case also we donot use the inplace keyword

if we want to change the datatype of the column we can use the method astype()
df['age']=df['age'].astype('float')

'''
print(df['Age'].astype('string'))
'''
this will change the datatype of the age column to float or any other

to get the no. of rows in the data frame we use 
len(df)
to get the no. of columns in the data frame we use

we can also add the new column in the data frame by using the method insert()
df.insert(loc=2, column='new column name', value='the value you want to add')
this will add the new column in the data frame at the location 2 and the value ofq  the column will be the value you want to add


'''
print(len(df))
print(len(df.columns))


df.insert(loc=2,column='hello',value=0)
print(df)
# df1=pd.DataFrame({'name':['raj','kashish','naman'],'marks':[12,32,43]})
# print(df1)

# df2=pd.DataFrame({'name':['raj','kashish','naman'], 'rollnumber':[12,4,2]})
# print(df2)

# a=pd.concat([df1,df2])
# print(a)

# b=pd.merge(df1,df2,on='name')
# print(b)


