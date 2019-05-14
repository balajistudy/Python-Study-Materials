import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

# Series nothing but one dimensional array
s = pd.Series([1,3,5,np.nan,6,8])
# To chage the index of the Series
s.index=['a','b','c','d','e','f']

print (s)
#To get the itemsize ie idividual element size
"""
==> for float64 --> 64/8 = 8 itemsize
==> for int32 --> 32/8 = 4 itemsize
"""
print (s.itemsize)

# TO get the dimension
print (s.ndim)

#TO get the data frame values
print (s.values)    

# To count the number of not null values ie ignore the Nan value
print (s.count())

# To get the shape of the matrix or data frame
print (s.shape)

# TO get the length of data frame
print (len(s))


# Random numbers generation
print (np.random.randn(6,4))

print ('###################################')
# creating the data frame using dictionary
df2 = pd.DataFrame({ 'A' : 1.,
                      'B' : pd.Timestamp('20130102'),
                      'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                      'D' : np.array([3] * 4,dtype='int32'),
                      'E' : pd.Categorical(["test","train","test","train"]),
                      'F' : 'foo' })

print (df2)
print ('-------------------------')
#To get what are the attributes and methods associated to the object
print (dir(df2))
print ('-------------------------')
#To get the data type of the data frame object
print (df2.dtypes)
print ('-------------------------')
# To access the individual cols from data frame
print (df2.get('B')) # can get only one colum at a time
print (df2[['A','B']]) # Can get more than one column
print ('-------------------------')

#To plot the number column for eg: here i am plotting the col A from df2.
df2.A.plot()
#plt.show()
print ('--- Data Plotted ---------')
print ('-------------------------')
# To show the last 3 records
print (df2.tail(3))
print ('-------------------------')
# To show the first 3 records
print (df2.head(3))
print ('-------------------------')

#/*----------------------------------------------------------------*/
"""
Display the index, columns, and the underlying NumPy data:
"""

print ('Display the index, columns, and the underlying NumPy data:')
#TO get the index information
print (df2.index)
print ('--------- To get the columns inforamtion ----------------')
#To get the columns inforamtion
print (df2.columns)
print ('-------- To get the values of data frame -----------------')
# To get the values of data frame
print (df2.values[0:3]) # it is possible to slice the values
print ('-------------------------')

"""
describe() shows a quick statistic summary of your data:
        It will give the count,min,max ,std,mean,..etc
"""
print (df2)
print (df2.describe().count)

print ('########################################################')

"""Transposing your data"""
print ('-------------- Transposing your data -------- ')
print (df2.T)
a=df2.T
print (a.columns)

print ("""Sorting by an axis \n""")

print (df2.sort_index(axis=1, ascending=False))
''' Here Axis 1 rep the column , axis 0 rep the row '''
'''And we can sort by specifc value'''
df2.sort_values(by='B')
print ('-------------------------\n')

print ('\n')
print ('############### Selecting the data ####################')
'''
The optimized pandas data access methods, .at, .iat, .loc and .iloc.
'''
'''
Selecting a single column, which yields a Series, equivalent to df.A:

'''
print (df2['A'])
print ('-------------------------\n')
'''
Selecting via [], which slices the rows.
'''
print (df2[0:3])
'''Here we can slice with the string index if
                    we use int index the to_index will be exclusive
                    whereas in string index the to_index will be inclusive
                    for example : df.loc['20130102':'20130104',['A','B']]'''

print('------- Returns all the rows with columns A and B ------------------ \n')
print(df2.loc[:,['A','B']])
'''Returns all the rows with columns A and B ie (Selecting on a multi-axis by label:)'''
print('-------- Returns every 3rd rows with columns A and B -----------------\n')
print(df2.loc[::3,['A','B']])
'''Returns every 3rd rows with columns A and B '''
print ('--------- Returns upto the 2nd row with all the columns ----------------\n')
print(df2.loc[:2,:])
''' Returns upto the 2nd row with all the columns''' 


print (df2.iloc[3])

'''
By integer slices, acting similar to numpy/python:
'''
print ( df2.iloc[3:5,0:2])

'''
By lists of integer position locations, similar to the numpy/python style:
'''
print (df2.iloc[[1,2],[0,2]])

'''
For slicing rows explicitly:
'''
print (df2.iloc[1:3,:])
'''
For slicing columns explicitly:
'''
print (df2.iloc[:,1:3])
'''
For getting a particular value explicitly from the data frame
'''
print (df2.iloc[1,4])


print ('############  Boolean Indexing    ################## \n')
'''Using a single column’s values to select data. '''
print ('Using a single column’s values to select data.  df2[df2.A > 0]  \n')
print(df2[df2.A > 0])
print ('\n')

'''
Selecting values from a DataFrame where a boolean condition is met.
'''
print ('---Selecting values from a DataFrame where a boolean condition is met.  df2[df2 > 0] ---------\n')

print (df2[df2 > 0])

df2.loc[4] = [2, '2018-07-01',3,4,'Balaji','Masilamani']
df2.loc[5] = [3, '2018-07-01',4,5,'Balaji1','Masilamani1']
#df2.loc[6] = [4, '2018-07-01',5,6,'Balaji2','Masilamani2']


print (df2)
'''
Using the isin() method for filtering:
'''

df2['G'] = ['one', 'one',np.nan,'three','four','three'] # inserting new column into data frame
print (df2)

df2.iloc[0,3]=np.nan    # Upadting specified position in the data frame based on the element location
df2.iloc[0,4]=np.nan

#df2.replace(True)

print (df2)
'''using isin () method '''
print (df2[df2['G'].isin(['two','four'])])
print (df2[df2['F'].isin(['Balaji','Masilamani'])])


print ('#################### Setting a new column automatically aligns the data by the indexes.######### \n')
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
print (s1)
s2 = pd.Series([1,2,3,4,5,6], index=np.arange(6))
print(s2)
s3 = pd.Series([1,2,3,4,5,6], index=[1,2,3,4,5,6])
print(s3)

print (df2)

df2['F'] = s3

print (df2)

print ('#################### A where operation with setting. ######### \n')

print (df2[df2['A']>0])
print (df2.count())
print (df2['A']+5)
#df2[df2['A']>0] = df2['A']+5
df2['A']=df2['A']+5
print (df2)


""" Missing Data  """
print ('-------------Missing Data----------------\n')
'''
pandas primarily uses the value np.nan to represent missing data. It is by default not included in computations.
'''
'''
Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data.
'''
#df1 = df2.reindex(index=[1,2], columns=list(df2.columns) + ['E'])
#print (df1)
'''
To drop any rows that have missing data.
'''
df2.dropna(how='any')
print (df2)
df2.fillna(value=5,inplace=True)
print (df2)
