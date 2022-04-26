# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:49:40 2022

@author: Student
"""

import pandas as pd



df = pd.read_parquet(r"C:\Shared\example_parquet")
df.info()
review_text = df.iloc[0,0]
token = df.iloc[0,1]
spell = df.iloc[0,2]
normal = df.iloc[0,3]
stopword = df.iloc[0,4]
lemma = df.iloc[0,5]
print(df.iloc[0,0])
