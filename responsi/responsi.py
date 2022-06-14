#install dari dataset data.csv
'''
import numpy as np
import pandas as pd
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
%matplotlib inline
'''

#Kemudian menggunakan data data.csv yang saya dapatkan dari dataset
df = pd.read_csv('data.csv')
df.head()
#output
'''
 	type_school 	school_accreditation 	gender 	interest 	residence 	parent_age 	parent_salary 	house_area 	average_grades 	parent_was_in_college 	in_college
0 	Academic 	A 	Male 	Less Interested 	Urban 	56 	6950000 	83.0 	84.09 	False 	True
1 	Academic 	A 	Male 	Less Interested 	Urban 	57 	4410000 	76.8 	86.91 	False 	True
2 	Academic 	B 	Female 	Very Interested 	Urban 	50 	6500000 	80.6 	87.43 	False 	True
3 	Vocational 	B 	Male 	Very Interested 	Rural 	49 	6600000 	78.2 	82.12 	True 	True
4 	Academic 	A 	Female 	Very Interested 	Urban 	57 	5250000 	75.1 	86.79 	False 	False
'''

#Kemudian menampilkan tampilan info dari dataset
df.info()
#output
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 11 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   type_school            1000 non-null   object 
 1   school_accreditation   1000 non-null   object 
 2   gender                 1000 non-null   object 
 3   interest               1000 non-null   object 
 4   residence              1000 non-null   object 
 5   parent_age             1000 non-null   int64  
 6   parent_salary          1000 non-null   int64  
 7   house_area             1000 non-null   float64
 8   average_grades         1000 non-null   float64
 9   parent_was_in_college  1000 non-null   bool   
 10  in_college             1000 non-null   bool   
dtypes: bool(2), float64(2), int64(2), object(5)
memory usage: 72.4+ KB
'''
