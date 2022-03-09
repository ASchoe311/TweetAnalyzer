This project take in all tweets containing a specific key word or set of key words for a certain time interval,
rate the positivity of the tweet, and gives a positivity score for each day of the given interval year. This data
is then displayed on a graph where the user can see when in the year the certain term was more or less popular.

Requirements:
re, textblob, matplotlib, numpy, getOldTweets library(included)

How to use:
generate tweets for a full year using the getOldTweets library and then point the tweet file in analysis.py at the generated csv and run