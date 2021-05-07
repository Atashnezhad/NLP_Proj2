#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports
import pandas as pd
import regex as re
import warnings
warnings.filterwarnings('ignore')
from nltk.corpus import stopwords # Import the stopword list

from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk
import pickle


# In[2]:


def Apply(df_reddit):

    def text_cleaning(item):

        #Removing "\n" characters
        item = re.sub("\n", " ", item)
        #Removing the [removed] characters
        item = item.replace("[removed]", " ")
        # Use regular expressions to do a find-and-replace
        item = re.sub("[^a-zA-Z]", " ", item)
        #Making all characters lower case
        item = item.lower()
        #Replacing multiple spaces
        item = " ".join(item.split())
        #Removing stopwords
        
        stops = nltk.corpus.stopwords.words('english')
        newStopWords = ['http', 'https', 'would', 'com', 'www', 'youtube', 'org','space', 
                        'earth', 'nasa', 'moon', 'time', 'amp', 'star', 'year', 'planet', 
                        'like', 'mar', 'launch', 'could', 'new', 'first', 'black', 'one', 
                        'way', 'know', 'look', 'see', 'orbit', 'get', 'solar', 'sun', 'use', 
                        'think', 'make', 'imag', 'system', 'telescop', 'find', 'go', 'us', 'rocket', 
                        'mission', 'take', 'astronaut', 'video', 'question', 'human', 'want', 'work', 
                        'photo', 'pictur', 'help', 'say', 'watch', 'anyon', 'also', 'found', 'peopl', 
                        'live', 'made', 'test', 'view', 'land', 'day', 'realli', 'apollo', 'back', 'need']
        
        stops.extend(newStopWords)
        
#         stops = stopwords.words("english")
        
        
        
        words = [w for w in item.split() if w not in stops]#stops
        # Instantiate object of class PorterStemmer and stemming.
        p_stemmer = PorterStemmer()
        words = [p_stemmer.stem(i) for i in words]
        # Adding space to stitch the words together
        words = " ".join(list(words)) 

        return words
    
    df_reddit["text_merged"] = df_reddit["text_merged"].apply(text_cleaning)
    
    return df_reddit






