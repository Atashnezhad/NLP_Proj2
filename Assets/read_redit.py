#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time



# In[ ]:


#function from: https://github.com/scaress21/reddit_and_quibi/blob/master/code/01A_Gathering_Reddit_Data.ipynb
#Function to get posts from reddit
def get_posts(subreddit, num, t, size_limi):
    #Setting the base url and first "before" time
    base_url = 'https://api.pushshift.io/reddit/submission/search'
    bef_time = t
    
    #list to hold the dataframes to concat
    to_concat = []
    
    #While loop that keeps gathering until the number of desired posts is reached
    while len(to_concat) < (num / size_limi):
        params = {
            'subreddit' : subreddit,
            'size' : size_limi,
            'before' : bef_time,
            'lang' : True,
            'author': '![deleted]'
                }
        get = requests.get(base_url, params)
        data = get.json()['data']
        df = pd.DataFrame(data)
        bef_time = df['created_utc'].min()
        to_concat.append(df)
        
        #If statement to print out updates every 5000 posts including the time of the earliest post
        if len(to_concat) % (5) == 0:
            #Converting the epoch time into a more readable, datetime format
            print_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(bef_time))
            print(f'{len(to_concat)*size_limi} posts have been gathered, oldest post is from {print_time}')
    
    #Once the while loop is done, concat the dataframes together and reset the index
    master = pd.concat(to_concat, axis=0)
    master.reset_index(inplace=True)
    
    #Making sure the posts are unique with unique ID's
    duplicates = master['id'].duplicated().sum()
    
    #Final update confirming how many posts were gathered and if there are duplicates
    print(f'Final DataFrame shape: {master.shape}, there are {duplicates} duplicates')
    
    #Return the final dataframe
    return master

