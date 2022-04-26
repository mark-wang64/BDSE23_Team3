# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 16:45:04 2022

@author: Student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_parquet(r"C:\Users\Student\Desktop\filter_data_parquet",engine="fastparquet")
df.info()
wordlist = df["output"].to_list()

# assumen positive
nightend = np.zeros(len(df))
for j in range(len(df)):
    if ( "night end" in wordlist[j]):
        nightend[j] = 1
df["nighy end"] = nightend 
bed = np.zeros(len(df))
for j in range(len(df)):
    if ( "bed comfortable" in wordlist[j]) or ("comfortable bed" in wordlist[j]):
        bed[j] = 1
df["bed comfortable"] = bed        
friendly = np.zeros(len(df))
for j in range(len(df)):
    if ( "friendly helpful" in wordlist[j]) or ( "helpful friendly" in wordlist[j]):
        friendly[j] = 1 
df["friendly"] = friendly        
staff = np.zeros(len(df))
for j in range(len(df)):
    if ( "staff friendly" in wordlist[j]) or ( "staff helpful" in wordlist[j]) or ( "staff great" in wordlist[j]) or ('friendly staff' in wordlist[j]) or ( "helpful staff" in wordlist[j] ):
        staff[j] = 1 
df["staff"] = staff
customer = np.zeros(len(df))
for j in range(len(df)):
    if ( "customer service" in wordlist[j]):
        customer[j] = 1         
df["customer"] = customer     
        
minute = np.zeros(len(df))
for j in range(len(df)):
    if ( "minute walk" in wordlist[j]) or ( "short walk" in wordlist[j]) or ("walking distance" in wordlist[j]) or ("with walking" in wordlist[j]):
        minute[j] = 1         
df["minute"] = minute
recommend = np.zeros(len(df))
for j in range(len(df)):
    if ( "highly recommend" in wordlist[j]) or ( "definitely recommend" in wordlist[j]):
        recommend[j] = 1           
df["rec"] = recommend
defi = np.zeros(len(df))
for j in range(len(df)):
    if ( "would definitely" in wordlist[j]):
        defi[j] = 1   
df["defi"] = defi
clean = np.zeros(len(df))
for j in range(len(df)):
    if ( "clean comfortable" in wordlist[j]) or ( "spotlessly clean" in wordlist[j]) or ( "clean" in wordlist[j]):
        clean[j] = 1  
df["clean"] = clean 
nice = np.zeros(len(df))
for j in range(len(df)):
    if ( "really nice" in wordlist[j]):
        nice[j] = 1  
df["nice"] = nice
bar = np.zeros(len(df))
for j in range(len(df)):
    if ( "bar restaurant" in wordlist[j]):
        bar[j] = 1  
df["bar restaurant"] = bar
locat = np.zeros(len(df))
for j in range(len(df)):
    if ( "perfect location" in wordlist[j]) or ( "location perfect" in wordlist[j]) or  ( "location great" in wordlist[j]) or ( "great location" in wordlist[j]) :
        locat[j] = 1  
df["location perfect"] = locat
nexti = np.zeros(len(df))
for j in range(len(df)):
    if ( "next time" in wordlist[j]):
        nexti[j] = 1
df["next time"] = nexti
made = np.zeros(len(df))
for j in range(len(df)):
    if ( "made feel" in wordlist[j]):
        made[j] = 1
df["made feel"] = made
value = np.zeros(len(df))
for j in range(len(df)):
    if ( "value money" in wordlist[j]):
        value[j] = 1
df["value money"] = value
buf = np.zeros(len(df))
for j in range(len(df)):
    if ( "breakfast buffet" in wordlist[j]):
        buf[j] = 1
df["breakfast buffet"] = buf
city = np.zeros(len(df))
for j in range(len(df)):
    if ( "city centre" in wordlist[j]) or  ( "city center" in wordlist[j]):
        city[j] = 1
df["city center"] = city
tea = np.zeros(len(df))
for j in range(len(df)):
    if ( "tea coffee" in wordlist[j]) or  ( "coffee tea" in wordlist[j]):
        tea[j] = 1
df["tea coffee"] = tea
wifi = np.zeros(len(df))
for j in range(len(df)):
    if ( "free wifi" in wordlist[j]):
        wifi[j] = 1
df["free wifi"] = wifi
wou = np.zeros(len(df))
for j in range(len(df)):
    if ( "would highly" in wordlist[j]):
        wou[j] = 1
df["would highly"] = wou
good = np.zeros(len(df))
for j in range(len(df)):
    if ( "really good" in wordlist[j])  or ( "one best" in wordlist[j]):
        good[j] = 1
df["one best"] = good
train = np.zeros(len(df))
for j in range(len(df)):
    if ( "train station" in wordlist[j]):
        train[j] = 1
df["train station"] = train
need = np.zeros(len(df))
for j in range(len(df)):
    if ( "everything need" in wordlist[j]):
        need[j] = 1
df["everyhting need"] = need
# negative
air = np.zeros(len(df))
for j in range(len(df)):
    if ( "air condition" in wordlist[j]):
        air[j] = 1
df["air condition"] = air
front = np.zeros(len(df))
for j in range(len(df)):
    if ( "front desk" in wordlist[j]):
        front[j] = 1
df["front desk"] = front
even = np.zeros(len(df))
for j in range(len(df)):
    if ( "even though" in wordlist[j]):
        even[j] = 1
df["even though"] = even
didn = np.zeros(len(df))
for j in range(len(df)):
    if ( "didnt work" in wordlist[j]) or ( "dont work" in wordlist[j]) or ( "not work" in wordlist[j]) or ( "no work" in wordlist[j]):
        didn[j] = 1
df["not work"] = didn
credit = np.zeros(len(df))
for j in range(len(df)):
    if ( "credit card" in wordlist[j]):
        credit[j] = 1
df["credit card"] = credit
rude = np.zeros(len(df))
for j in range(len(df)):
    if ( "staff rude" in wordlist[j]) or ( "rude staff" in wordlist[j]):
        rude[j] = 1
df["rude staff"] = rude
ne = np.zeros(len(df))
for j in range(len(df)):
    if ( "worst ever" in wordlist[j]) or  ( "would never" in wordlist[j]):
        ne[j] = 1
df["worst ever"] = ne
told = np.zeros(len(df))
for j in range(len(df)):
    if ( "told would" in wordlist[j]) or ( "said would" in wordlist[j]):
        told[j] = 1
df["told would"] = told
hot = np.zeros(len(df))
for j in range(len(df)):
    if ( "hot water" in wordlist[j]):
        hot[j] = 1
df["hot water"] = hot
double = np.zeros(len(df))
for j in range(len(df)):
    if ( "double" in wordlist[j]):
        double[j] = 1
df["double bed"] = double
win = np.zeros(len(df))
for j in range(len(df)):
    if ( "window open" in wordlist[j]) or ( "open window" in wordlist[j]):
        win[j] = 1
df["open window"] = win
some = np.zeros(len(df))
for j in range(len(df)):
    if ( "somewhere else" in wordlist[j]):
        some[j] = 1
df["somewhere else"] = some
came = np.zeros(len(df))
for j in range(len(df)):
    if ( "came back" in wordlist[j]):
        came[j] = 1
df["came back"] = came
nex = np.zeros(len(df))
for j in range(len(df)):
    if ( "next door" in wordlist[j]):
        nex[j] = 1
df["next door"] = nex
night = np.zeros(len(df))
for j in range(len(df)):
    if ( "night sleepr" in wordlist[j]):
        night[j] = 1
df["night sleep"] = night
know = np.zeros(len(df))
for j in range(len(df)):
    if ( "dont know" in wordlist[j]):
        know[j] = 1
df["dont know"] = know

even = np.zeros(len(df))
for j in range(len(df)):
    if ( "dont even" in wordlist[j]) or ( "didnt even" in wordlist[j]):
        even[j] = 1
df["dont even"] = even

df.groupby("told would").mean()
plt.figure()
name=[]
withA=[]
noA=[]
diff=[]
for x,i in enumerate(df.columns):
    print(x)
    if x > 4:
        bed_avg=df.groupby(i)['Total_Rating'].mean()
        print(bed_avg)
        name.append(i)
        if len(bed_avg) == 1:
            noA.append(bed_avg[0])
            withA.append(0)
            diff.append(0)
        else:    
            withA.append(bed_avg[1])
            noA.append(bed_avg[0])
            diff.append(bed_avg[1]-bed_avg[0] )
        Index = [0,1]
        plt.bar(Index,bed_avg)
        plt.xticks(Index,['Not mentioned','mentioned'],rotation=45)
        plt.ylabel('Average Reviewer Score')
        plt.xlabel('Is'+i+'comfortable mentioned ?')
        plt.title(i)
        plt.show()
        
feature = pd.DataFrame({'name' : name,'mentioned' : withA,'not mentioned' : noA, 'difference': diff }, columns=['Name','mentioned', 'not mentioned', 'difference'])
feature['Name']=name
feature.drop(columns="name", inplace=True)
df.groupby("bed").mean()        
df.groupby("bar").mean()
feature.to_csv(r"C:\Users\Student\Desktop\feature.csv", index=False)        
df.to_csv(r"C:\Users\Student\Desktop\data_set.csv", index=False)           

bed_avg=df.groupby('bar')['Total_Rating'].mean()
Index = [0,1]
plt.bar(Index,bed_avg)
plt.xticks(Index,['Not mentioned','mentioned'],rotation=45)
plt.ylabel('Average Reviewer Score')
plt.xlabel('Is bed comfortable mentioned ? ')
plt.title('bed comfortable')