# introduction to pandas series
lst = [10,20,30,40,50]
print(lst)

import pandas as pd 

s1 = pd.Series([10,20,30,40,50])
print(s1)

s2 = pd.Series([10,20,30,40,50], index = ('a','b','c','d','e'))
s1.shape
print(s2)

# labeling and selection

marks = pd.Series([90,85,76], index = ('math','science','biology'))

print(marks[['math']])
print(marks[['math','science']])

marks['math'] = 45

print(marks)

# boolean masking in series 

score = pd.Series([10,20,30,40,50,60,70,80,90])
passed = score[score > 60]
failed = score[score < 60]
print(passed)
print(failed)

first = score[(score > 40) & (score < 80)]
print(first)

scolar = score[(score > 40 )| (score < 80)]
print(scolar)

# TASK 1

import pandas as pd

values = pd.Series([700,150,300], index = ('Laptop', 'Mouse', 'Keyboard'))
print(values)
print(values[['Laptop']])
print(values[0:2])


#TASK 2

import numpy as np 
import pandas as pd

values = pd.Series([85, None, 92, 45, None, 78, 55])

print(values.isnull())
print(values.fillna(0))

greater_than_60 = values[values > 60] 
print(greater_than_60)
print(values)
print(values.fillna(0))
print(greater_than_60)

# TASK 3

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
print(usernames)
strip = usernames.str.strip()
print(strip)
lower = usernames.str.lower()
print(lower)
print(usernames.str.contains('a'))


print(strip)
print(lower)
print(usernames.str.contains('a'))








