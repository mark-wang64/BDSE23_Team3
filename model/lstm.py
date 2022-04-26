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


#df = pd.read_csv(r"C:\Shared\Final\Review.csv")

df = pd.read_parquet(r"C:\Shared\Final\Review",engine='fastparquet')

df.to_parquet(r"C:\Shared\Final\Review",engine='pyarrow')

#df = pd.read_parquet(r'C:\Shared\Triptype_Review_parquet',engine="fastparquet")

df=df[["Country","output","Trip_Type_BUSINESS","Trip_Type_COUPLES","Trip_Type_FAMILY","Trip_Type_FRIENDS","Trip_Type_SOLO"]]

df.groupby("Country").count()

df.to_csv(r"C:\Shared\Triptype.csv",index= False)

df.info()
df.loc[(df.Country == 'italy'),'Country']='Italy'
df.loc[(df.Country == 'United Kindom'),'Country']='United Kingdom'
df.loc[(df.Country == 'UnitedKingdom'),'Country']='United Kingdom'
df.to_csv(r"C:\Users\Student\Desktop\Trip_Type.csv",index=False)

df_uk = df[df["Country"] == "Portugal"]
df_uk.info
df_uk.groupby("Trip_Type_SOLO").count()
df_uk.groupby("Trip_Type_FAMILY").count()
df_uk.groupby("Trip_Type_COUPLES").count()
df_uk.groupby("Trip_Type_FRIENDS").count()
df_uk.groupby("Trip_Type_BUSINESS").count()



df.head()

fig, ax = plt.subplots()
sns.set(rc={'figure.figsize':(12,9)})
length_dist = df["wordCount"]
plt.xticks(fontsize=20)
ax.set_xticks(range(0,550,50))
ax.set_yticks(range(0,160000,20000))
plt.yticks(fontsize=20)
sns.histplot(length_dist,palette="pastel")
ax.set_ylabel("Amount of Reviews",fontsize=20)
ax.set_xlabel("Count of Words",fontsize=20)
ax.patch.set_visible(False)
ax.set_xlim(0,500)
ax.set_ylim(0,160000)
ax.set_title("Sentence Length Distribution",fontsize=32);
plt.show()
df_filtered = df[df['wordCount'] > 108]

df_hotel["Review_Text"].mean()
# 飯店評論數>60(mean)取:df.list
df_list = df_list[df_list['Review_Text'] > 60]
print(df_list["Review_Text"].sum())
df_list = pd.read_csv(r"C:\Users\Student\Desktop\list.csv")

