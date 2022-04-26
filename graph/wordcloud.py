# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 21:12:50 2022

@author: Student
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS

#df = pd.read_parquet(r'C:\Users\Student\Desktop\Triptype_Review_parquet',engine="fastparquet")
df["Country"].mask(df["Country"]=="italy","Italy",inplace=True)
df.groupby("Country").count()
df.to_csv(r"C:\Shared\Final\Spark\Trip_Type.csv", index=False)
df=pd.read_csv(r"C:\Shared\Final\Location.csv")
pd.set_option('display.max_columns', None)
df.info()
df.head()

df.isnull().count()
df2 = df.groupby("Region").mean("Total_Rating")
df.to_csv(r'C:\Users\Student\Desktop\Nationality.csv',index=False)
tes2=df[df['Region']=="Europe"]
tes2=tes2["output"]
test3=' '.join(tes2)
stopwords = set(STOPWORDS)
stopwords.update(["stayed","stay"])

    
wc = WordCloud(width = 800, height = 800,background_color="white",min_font_size = 10,\
    repeat=True,stopwords=stopwords)
wc.generate(test3)
plt.figure(figsize = (8, 8), facecolor = None) 
plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.title('Europe Reviews',fontsize=32)





















df.groupby("Country").count()
freq = df['Country'].value_counts() 
sort = freq.sort_values(ascending=False)
top20= sort[0:9]
top20.index=[]
print(freq)
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from colorspacious import cspace_converter
country = top20.index
count = top20
x = np.arange(len(country))
plt.bar(x, count)
plt.xticks(fontsize= 8)
plt.xticks(x,country)
plt.xlabel('Country')
plt.ylabel('Count')
plt.title('')
plt.show()