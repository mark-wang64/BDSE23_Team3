# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:44:16 2022

@author: Student
"""

import pandas as pd
df = pd.read_parquet(r"C:\Users\Student\Desktop\Nationality_parquet",engine = "fastparquet")

#df=pd.read_csv(r"C:\Shared\tfidf\Nationality\nationality2.csv")

df.groupby("Region").count()


df.to_csv(r"C:\Shared\Triptype.csv",index= False)
df=df[["Country","Trip_Type_BUSINESS","Trip_Type_COUPLES","Trip_Type_FAMILY","Trip_Type_FRIENDS","Trip_Type_SOLO"]]
token
for i,x in enumerate(df["output"]):
    tokens = nltk.word_tokenize(x)
    
    
    
    
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(min_df=1)
vectorizer.fit_transform()
