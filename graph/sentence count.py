# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:13:35 2022

@author: Student
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import nltk.util import ngrams


#function to calculate the average sentence length across a piece of text.
def avg_sentence_len(text):
  sentences = text.split(".") #split the text into a list of sentences.
  words = text.split(" ") #split the input text into a list of separate words
  average_sentence_length = len(words) / len(sentences)
  print(average_sentence_length)
  return average_sentence_length #returning avg length of sentence
df = pd.read_parquet(r'C:\Users\Student\Desktop\Final\Total_Review_parquet',engine="fastparquet")
df.info()
df = df[["Review_Text"]] 
df["Sentence"] =  avg_sentence_len(x for x in df["Review_Text"])
print(ans) #printing result
sentence=[]
for i,x in enumerate(df["Review_Text"]):
    sentence.append(avg_sentence_len(x))

from itertools import groupby
for k,g in groupby(sorted(sentence),key = lambda x: x//10):
    print('{}-{}:{}'.format(k*10,(k+1)*10,len(list(g))))




fig, ax = plt.subplots()
sns.set(rc={'figure.figsize':(12,9)})
plt.xlabel("Count of Words", size = 25)
plt.ylabel("Amount of Reviews", size = 25)
#length_dist = [len(x.split(" ")) for x in sentence]
sns.histplot(sentence,palette="pastel")
ax.patch.set_visible(True)
ax.set_xlim(0,60)
ax.set_ylim(0,175000)
ax.set_title("Sentence Length Distribution",fontsize=25);
plt.show()