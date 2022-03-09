# -*- coding: utf-8 -*-
"""
Name:aschoe
Biophysics 117: W2019
Exercise name : .py

Description

Created on MM/DD/2019
"""
import re 
#import tweepy 
#from tweepy import OAuthHandler 
from textblob import TextBlob 
import got3


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'
        
def get_tweets():
    #ONLY FOR USE WITH PREMADE TWEET FILES
    tweetFile = open('2018_uofm_tweets.csv', encoding="utf-8")
    fetched_tweets = tweetFile.readlines()
    tweets = []
    for tweet in fetched_tweets:
        thisTweet = tweet.split(';')
        if thisTweet[0] != "username":
            parsed_tweet = {}
            parsed_tweet['text'] = thisTweet[4]
            parsed_tweet['sentiment'] = get_sentiment(thisTweet[4])
            parsed_tweet['date'] = thisTweet[1]
            
            if int(tweet[2]) > 0:
                if parsed_tweet not in tweets:
                    tweets.append(parsed_tweet)
            else:
                tweets.append(parsed_tweet)
    return tweets

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    tweets = get_tweets()
    positives = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    
    
    year = {}
    outs = [1000, 10000, 20000, 30000, 40000, 50000, 60000, 65000]
    monthNums = []
    dayNums = []
    numChecked = 0
    for i in range(len(tweets)):
        month = tweets[i]['date'][5:7]
        
        if month not in monthNums: 
            monthNums.append(month)
            
        day = tweets[i]['date'][8:10]
        
        if day not in dayNums:
            dayNums.append(day)
            
        sentiment = tweets[i]['sentiment']
        
        if month not in year.keys():
            year[month] = dict()
            year[month][day] = 0
        elif day not in year[month].keys():
            year[month][day] = 0
    
        if sentiment == 'positive':
            year[month][day] += 1
        elif sentiment == 'negative':
            year[month][day] -= 1
            
        numChecked += 1
        if numChecked in outs:
            print("%s tweets read in" % numChecked)
    #x-axis is day of year (1-365)
    #y-axis is the sums
    #print(year)
    #print('\n')
    assocs = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
    x = np.arange(1,366)
    y = []
    for month in monthNums:
        for day in dayNums:
            if(int(day) <= assocs[month]):
                y.append(year[month][day])
    plt.clf()
    plt.plot(x, y, 'r')
    plt.xlabel('Day of the year')
    plt.ylabel('Positivity score')
    plt.savefig('fig.png')
    
    
# =============================================================================
#     
#     for i in range(len(positives)):
#         print(positives[i]['date'].month)
#     
# =============================================================================
