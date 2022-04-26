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
from matplotlib.pyplot import MultipleLocator

df = pd.read_parquet(r'C:\Users\Student\Desktop\Total_Review_parquet',engine="fastparquet")
#df = pd.read_csv(r'C:\Users\Student\Desktop\hotel_review_amount.csv')
df_list.describe()
df.info()
df = df[["Hotel_Name","wordCount"]]
df_list = df.groupby("Hotel_Name").count()
x=df["wordCount"]
df["wordCount"].describe()
fig, ax = plt.subplots()
sns.set(rc={'figure.figsize':(16,12)})
#length_dist = x
sns.histplot(x,palette="pastel", shrink=.9)
ax.patch.set_visible(False)
ax.set_xlim(0,500)
ax.set_ylim(0,150000)
ax.set_title("Review Amount of Hotels",fontsize=20);
plt.xlabel('Amount of Reviews')
plt.ylabel('Amount of Hotels')
#a = np.arange(0,24000,2500)
b = np.arange(0,550,50)
plt.xticks(b,fontsize=25)
plt.yticks(fontsize=25)
plt.show()

df_list.to_csv(r'C:\Users\Student\Desktop\tableau dataset\data\hotel_review_amount')


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


