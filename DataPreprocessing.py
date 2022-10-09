import numpy as np
import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import pandas as pd


def DataPProcess(data):
    data = re.sub(r'https?://[^ ]+', '', data)
    data = re.sub(' +', ' ', data)

    data = re.sub(r'@[^ ]+', '', data)

    data = re.sub(r'#', '', data) 

    data = re.sub(r'([A-Za-z])\1{2,}', r'\1', data)

    data = re.sub(r' 0 ', 'zero', data)
    data = re.sub(r'[^A-Za-z ]', '', data)

    data = data.lower() #Lower casing
    # tokens = word_tokenize(data)
    # for token in tokens: 
    #     if token in stopwords.words('english'):
    #         tokens.remove(token)
    # print(tokens)
    return data


df = pd.read_csv("UnProcesseddata.csv")


df['Examples'].replace('', np.nan, inplace=True)
df = df.dropna()
examples = df["Examples"].tolist()
df = df[~df['Examples'].astype(str).str.startswith(',')]

for i in range(0,len(examples)):
    examples[i]= examples[i].replace(",",".")
    # examples[i]= examples[i].replace(" ","",1)
    examples[i] = DataPProcess(examples[i])


examples = pd.DataFrame(examples)

df['Examples'] = examples
# df = df.dropna()

print(df)

df.to_csv("Processeddata.csv")

# DataPProcess("No Topic Maps talks at the Balisage Markup Conference 2009   Program online at http://tr.im/mL6Z (via @bobdc) #topicmaps")
# transf = re.sub(r'https?://[^ ]+', '', tweet_1) # Remove the URLs

# transf = re.sub(r'@[^ ]+', '', tweet_2) # Remove the usernames

# transf = re.sub(r'#', '', tweet_3) # Remove from hashtages

# transf = re.sub(r'([A-Za-z])\1{2,}', r'\1', transf) # Character normalization

# transf = re.sub(r' 0 ', 'zero', tweet_2)
# transf = re.sub(r'[^A-Za-z ]', '', tweet_2) # Punctuation, special characters and numbers

# transf = tweet_2.lower() #Lower casing
# import nltk
# from nltk import word_tokenize
# from nltk.corpus import stopwords
# tokens = word_tokenize(tweet_1)
# for token in tokens: # Removing stop words
#     if token in stopwords.words('english'):
#         tokens.remove(token)
        
# print(tokens)