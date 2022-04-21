'''
   -------------------------------------------------
   Totally Unreliable Sentiment Analysis
   Author: regexowl
   Updated: 21-04-2022
   -------------------------------------------------

   My first journey into the wonderful world of sentiment analysis. 
   Do not trust this sentiment analysis script under any circumstances!
   The results are most probably as dependable as a dice roll.

'''

import os
from datetime import date, datetime, timedelta
import twint as tw # Twitter scraping
import pandas as pd # csv processing
import nltk # sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon') # downloads resources for sentiment analysis

# Scrape Twitter for a tweet dataset based on the username and the date
def scrapeTweets(outfile, username, sinceDate):
    # Configure twint
    c = tw.Config()
    c.Username = username
    c.Since = sinceDate # set date of the tweet
    c.Until = (datetime.strptime(sinceDate, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d') # set until date automatically
    c.Store_csv = True # store results in csv
    c.Output = "./" + outfile # set csv filename
    c.Hide_output = True # hide terminal output
    # Run the search
    tw.run.Search(c)

# Run sentiment analysis on the dataset of tweets
def sentimentAnalysis(outfile, username, sinceDate):
    # Read the csv file
    tweets = pd.read_csv(outfile)
    tweets = tweets.drop_duplicates(subset=['tweet'])

    # Initialise sentiment analyser
    sia = SentimentIntensityAnalyzer()

    # Compute sentiment scores and the final compound
    #   -1 most extreme negative
    #   +1 most extreme positive
    tweets['neg'] = tweets['tweet'].apply(lambda x:sia.polarity_scores(x)['neg'])
    tweets['neu'] = tweets['tweet'].apply(lambda x:sia.polarity_scores(x)['neu'])
    tweets['pos'] = tweets['tweet'].apply(lambda x:sia.polarity_scores(x)['pos'])
    tweets['compound'] = tweets['tweet'].apply(lambda x:sia.polarity_scores(x)['compound'])

    print(tweets[['tweet', 'neg', 'neu', 'pos', 'compound']])

    # Print the mean compound for tweets of the day
    vaderComp = tweets['compound'].mean()
    print("\nThe average polarity of", username + "'s tweets is", vaderComp, "\n")

    # Call function that prints results
    howDoTheyFeel(vaderComp, username, sinceDate)

# Print the resulting sentiment
def howDoTheyFeel(vaderComp, username, sinceDate):
    # Set tense of the verb
    if sinceDate == date.today().strftime("%Y-%m-%d"):
        tense = "is"
    else:
        tense = "was"

    # Format the date to another format
    datetimeObject = datetime.strptime(sinceDate, "%Y-%m-%d")
    printableDate = datetimeObject.strftime("%A %b %d %Y")

    # Positive
    if vaderComp >= 0.05:
        print(username, tense, "a happy bean on", printableDate, "\n")
    # Negative
    elif vaderComp <= -0.05:
        print(username, tense, "a sad sad bean on", printableDate, ":'(", "\n")
    # Neutral
    else:
        print(username, tense, "neutral on", printableDate, "\n")

# MAIN
def main():
    # TODO username exists check
    username = "elonmusk" #input("Username: ") # read username from the input
    # TODO date format check
    sinceDate = "2022-04-20" #input("Date (YYYY-MM-DD): ") # read date from the input
    outfile = "results.csv"

    scrapeTweets(outfile, username, sinceDate)
    sentimentAnalysis(outfile, username, sinceDate)

    # Delete the csv file
    if os.path.exists(outfile):
        os.remove(outfile)
    else:
        print("File not found") 

if __name__ == "__main__":
	main()