# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 03:31:33 2022

@author: Student
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import TweetTokenizer
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
df.dropna(subset=["Reviewer_Region"],inplace=True)
df.fillna(0)
top5 = ["hotel","room","rooms","hotels"]
df2 = df.iloc[:30]
df.fillna(0, inplace= True)
#df = pd.read_parquet(r'C:\Shared\example_parquet2',engine="fastparquet")
df2 = pd.read_csv(r'C:\Users\Student\Desktop\Spain.csv')
df = pd.read_parquet(r'C:\Users\Student\Desktop\Triptype_Review_parquet',engine="fastparquet")
df.iloc[1,[4,5]]
df.iloc[2,5]
df["wordCount"].head()
'''
df_1 = df[df["Total_Rating"] == 1]
df_2 = df[df["Total_Rating"] == 2]
df_3 = df[df["Total_Rating"] == 3]
df_4 = df[df["Total_Rating"] == 4]
df_5 = df[df["Total_Rating"] == 5]
df_af = df[df["Region"] == "Africa"]
df_oc = df[df["Region"] == "Oceania"]
df_co_good = df_eu[df_eu["Total_Rating"] == 5]
df_co_bad = df_eu[df_eu["Total_Rating"] == 1]
'''
df_bu = df[df["Trip_Type_BUSINESS"] == 1]
df_co = df[df["Trip_Type_COUPLES"] == 1]
df_fa = df[df["Trip_Type_FAMILY"] == 1]
df_fr = df[df["Trip_Type_FRIENDS"] == 1]
df_so = df[df["Trip_Type_SOLO"] == 1]
df_co_good = df_co[df_co["Total_Rating"] == 5]
df_co_bad = df_co[df_co["Total_Rating"] == 1]
df.info()


df5 = df1[df1["Total_Rating"] == 1]
df = ", ".join(df.output)
df2 = df
s3.to_csv("")
Total_Word_Count = df 
s1 = df_5[:len(df_5)//2]
s2 = df_5[len(df_5)//2:]



data2 = df_co_good.copy()
data2 = data2["output"]

# stopwords  
def removing_stop_words(txt):
    for x in top5:
        txt = txt.replace(x,"")
    stop_words = set(stopwords.words('english')) 

    word_tokens = word_tokenize(txt) 

    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
     
    return filtered_sentence
    
data2["output"] = data2["output"].apply(removing_stop_words)
#pd.set_option('display.max_colwidth', None)
#data2["output"].head(20)

# Lemmatizer
lemmatizer = WordNetLemmatizer() 
def lemmatize(data):
    lema_data=[]
    for j in data:
        x=j.lower()
        x=lemmatizer.lemmatize(j,pos='n')
        x=lemmatizer.lemmatize(j,pos='v')
        x=lemmatizer.lemmatize(j,pos='a')
        x=lemmatizer.lemmatize(j,pos='r')
        x=lemmatizer.lemmatize(x)
        lema_data.append(x)
    return lema_data
data2["output"] = data2["output"].apply(lemmatize)
data2["output"] = data2["output"].apply(lambda x:" ".join(token for token in x))
data2.head()
from sklearn.feature_extraction.text import TfidfVectorizer
#vectorizer = TfidfVectorizer(use_idf=True, max_df=0.9,min_df=0.2, ngram_range=(1,1))
vectorizer = TfidfVectorizer(use_idf=True, max_df=0.9,min_df=0.02, ngram_range=(2,2))
vectors = vectorizer.fit_transform(data2['output'])
dict_of_tokens={i[1]:i[0] for i in vectorizer.vocabulary_.items()}

tfidf_vectors = []  # all deoc vectors by tfidf


for row in vectors:
  tfidf_vectors.append({dict_of_tokens[column]:value for (column,value) in zip(row.indices,row.data)})
doc_sorted_tfidfs =[]  # list of doc features each with tfidf weight
#sort each dict of a document


for dn in tfidf_vectors:
  newD = sorted(dn.items(), key=lambda x: x[1], reverse=True)

  newD = dict(newD)
  doc_sorted_tfidfs.append(newD)

tfidf_kw = [] # get the keyphrases as a list of names without tfidf values
word=[]
score=[]
d_dropna = list(filter(None,doc_sorted_tfidfs)) 


for doc_tfidf in d_dropna:
    key = list(doc_tfidf.keys())[0]
    value = list(doc_tfidf.values())[0]
    word.append(key)
    score.append(value)



#df = " ".join(df_co_bad.output)
#df = df.split(" ")



result = pd.DataFrame(
    {'word':word,
     'tf-idf': score
    })
result = result.sort_values(by=['tf-idf'], ascending=False)


result2=result.drop_duplicates(subset=('word'))
# 增加tf值
negative = data2["output"].to_list()
tf = []
for i in result2["word"]:
    x = np.zeros(len(data2))
    for j in range(len(data2)):
        if ( i in negative[j]):
            x[j] = 1
    tf.append(np.sum(x))
result2["tf"] = tf



result2.to_csv(r'C:\Users\Student\Desktop\so.csv',index = False)
