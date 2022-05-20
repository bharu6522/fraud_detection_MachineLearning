# -*- coding: utf-8 -*-
"""Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ykHaV-yKA5AUMvNEwkTV-b7sLGEcZR6d
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
df = pd.read_csv('/content/creditcard.csv')
df

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df

df.head()

df.tail()

df.shape

df.info()

df.isnull().sum()
# there is no column in which null value exist .

df.select_dtypes(include = ['int64', 'float64']).columns

type('Time')

df['Class'].value_counts()
#there are two type of classes 1 and 0 . 1 represent fraud transaction and 0 represent normal transaction

#lets seperate the data into legit and fraud where legit represent class as 0 and fraud represent class as 1
legit = df[df.Class == 0] 
fraud = df[df.Class == 1]

fraud

fraud.shape

legit.shape

df['Amount'].describe()
# we found out statistic for whole data frame

legit['Amount'].describe()
# statics for legal data

fraud['Amount'].describe()
# statics for fraud data

df.groupby('Class').mean()
# we counted mean value for each column diffrentiating them according to class

#there is no missing vlaue /Nan vlaue so no need to do further cleaning
