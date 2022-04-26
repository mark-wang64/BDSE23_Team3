# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
## All purpose
import pandas as pd 
import numpy as np
## Deeplearning/ML
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_parquet(r'C:\Shared\Final\Tripadvisor_parquet',engine="fastparquet")


df.info()
df2 = df[["Hotel_Name","Total_Rating","Review_Text"]]



df_filtered = df[df['wordCount'] > 108]






df_hotel["Review_Text"].mean()
# 飯店評論數>60(mean)取:df.list
df_list = df2.groupby("Hotel_Name").count()
df_list = df_list[df_list['Review_Text'] > 60]
df_filtered = pd.read_csv(r"C:\Users\Student\Desktop\filter_data.csv")


hotel_list=df_list.index



mask = df2.Hotel_Name.apply(lambda x: any(item for item in hotel_list if item in x))
df_filtered2 = df2[mask]
df_filtered2.to_csv(r"C:\Users\Student\Desktop\filter_trip_data.csv",index=False)
df_filtered.to_csv(r"C:\Users\Student\Desktop\filter_trip_data.csv",index=False)
df_filtered2 =df2[df2["Hotel_Name"] == (x for x in df_list)]
#df_filtered2=df_filtered[pd.DataFrame(df_filtered.Hotel_Name.tolist()).isin(namelist).any(1).values]
df_filtered2.groupby("Total_Rating").count()
df_list2.head()
# check version number
import imblearn
print(imblearn.__version__)


