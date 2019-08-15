import re

with open('train_v1.txt') as file:
    data=file.readlines()
    new=open('train_v2.txt','w+')
    for num,rec in enumerate(data):
            #if '<' in rec or '>' in rec:
            #print (rec)
            #print ('##################')
            #print (re.sub('[<|>|/|(|)]',' ',rec))
            #print ('##################')
            abc=re.sub("Which MSS instance are you reporting this issue for MSS  hWIN & TSG  What type of issue are you reporting Another issue Description of problem  attach screenshots of any errors, etc.",'',rec)
            abc1=re.sub("Alternate contact phone number for yourself, if applicable  Which MSS instance are you reporting this issue for MSS  hWIN & TSG  What type of issue are you reporting Another issue Description of problem  attach screenshots of any errors, etc.",'',abc)
            abc2=re.sub("What is your MSS Login ID",'',abc1)
            abc3=re.sub("Customer Acct Number",'',abc2)
            abc4=" ".join(abc3.split())
            new.write(re.sub('[<|>|/|(|)]',' ',abc4))
            new.write('\n')
        
   
'''
import pandas as pd

df = pd.read_csv("C:/Users/ELCOT/Downloads/train_v1.txt")

print (df.info())

print (df.isnull().sum())

df.dropna(inplace=True,subset=['label'])

df.label=df.label.str.replace(' ','_')
df.reset_index(inplace=True)

print (df.label.value_counts())
'''




