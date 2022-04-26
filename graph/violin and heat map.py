# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:12:23 2022

@author: Student
"""
## All purpose
import pandas as pd 
import numpy as np
from dateutil.parser import parse

## Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px
import plotly.graph_objects as go


df = pd.read_parquet(r"C:\Users\Student\Desktop\tableau_dataset\Nationality_parquet", engine="pyarrow")
df = pd.read_parquet(r"C:\Users\Student\Desktop\Nationality_parquet",engine="pyarrow")
df = pd.read_csv(r"C:\Users\Student\Desktop\tableau_dataset\Nationality.csv")
df.info()
df.head()
df.isnull().sum()
df.dropna(inplace=True)
df = df[["Total_Rating","Trip_Type"]]
def year(x):
    y = x.split("-")[0]
    return y
def month(x):
    y = x.split("-")[1]
    return y

df = df[["Stay_Date","Total_Rating"]]

df.groupby("Stay_Date2").sum()
df['year'] = df["Stay_Date"].apply(year)
df['month'] = df["Stay_Date"].apply(month)
#noli = ["2022","2021","2020","2019","2018","2017","2016","2015","2014","2013","2012","2011"]
noli = ["2021","2020","2019","2018","2017","2016","2015","2014"]
filt = df["year"].isin(noli)
df2 = df.loc[filt,["Total_Rating","Stay_Date"]]
df2['year'] = df2["Stay_Date"].apply(year)
df2['month'] = df2["Stay_Date"].apply(month)

df2.info()
print(x)
sns.set(rc={'figure.figsize':(11.7,8.27)},style="white")


x=df["Reviewer_Region"]
y=df["Total_Rating"]
# violin
sns.set(rc={'figure.figsize':(18,9)},style="white")
ax=sns.violinplot(x=x, y=y, data=df)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.figure(dpi=3000)
ax.set_ylabel("Rating",size=18)
ax.set_xlabel("Region",size=18)
#Year vs Month
##Target_type vs Year
a=df2.groupby(['year','month']).size()
a
b=a.unstack(level=0)
e=b.replace(np.nan,0)
e=e.astype(int)
e.to_csv(r"C:\Shared\Final\monthyear.csv", index=False)
import matplotlib.gridspec as gridspec
fig = plt.figure(figsize=(9, 9)) 
gs = gridspec.GridSpec(1, 2, width_ratios=[5, 1.5]) 
ax0 = plt.subplot(gs[0])
sns.heatmap(e,annot=True,fmt='d',linewidths=.5,ax=ax0, cbar=True,annot_kws={"size":10})
ax1 = plt.subplot(gs[1],sharey=ax0)
sns.heatmap(pd.DataFrame(e.sum(axis=1)),annot=True,fmt='d',linewidths=.5,ax=ax1,cbar=True,annot_kws={"size":10})
plt.setp(ax1.get_yticklabels(), visible=False)
plt.setp(ax1.set_ylabel([]),visible=False)
plt.setp(ax0.yaxis.get_majorticklabels(),rotation=0)
ax0.tick_params(axis='y',labelsize=16)
ax0.tick_params(axis='x',labelsize=16)
ax0.set_ylabel("Month",size=18)
ax0.set_xlabel("Year",size=18)
ax1.set_xticklabels(["Total"],size=16)
ax0.set_title("Year vs Month ",size=22,y=1.05,x=0.5)
#ax3=plt.subplot(gs[3])
#cb1 = matplotlib.colorbar.ColorbarBase(ax3, cmap="RdBu_r")


plt.show()


# single-heat map
import matplotlib.gridspec as gridspec
fig = plt.figure(figsize=(9, 9)) 
gs = gridspec.GridSpec(1, 1, width_ratios=[5]) 
ax0 = plt.subplot(gs[0])
sns.heatmap(e,annot=True,fmt='d',linewidths=.5,ax=ax0,cmap="rocket_r", cbar=True,annot_kws={"size":10})
#ax1 = plt.subplot(gs[1],sharey=ax0)
#sns.heatmap(pd.DataFrame(e.sum(axis=1)),annot=True,fmt='d',linewidths=.5,ax=ax1,cbar=True,annot_kws={"size":10})
#plt.setp(ax1.get_yticklabels(), visible=False)
#plt.setp(ax1.set_ylabel([]),visible=False)
plt.setp(ax0.yaxis.get_majorticklabels(),rotation=0)
ax0.tick_params(axis='y',labelsize=16)
ax0.tick_params(axis='x',labelsize=16)
ax0.set_ylabel("Month",size=18)
ax0.set_xlabel("Year",size=18)
#ax1.set_xticklabels(["Total"],size=16)
ax0.set_title("Year vs Month ",size=22,y=1.05,x=0.5)
#ax3=plt.subplot(gs[3])
#cb1 = matplotlib.colorbar.ColorbarBase(ax3, cmap="RdBu_r")


plt.show()



