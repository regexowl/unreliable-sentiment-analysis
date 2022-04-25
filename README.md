# Totally Unreliable Sentiment Analysis

🚧 **PLEASE BE AWARE THAT THIS PROJECT IS A WORK IN PROGRESS** 🚧

My first journey into the wonderful world of sentiment analysis. 
Do not trust this sentiment analysis script under any circumstances! 
The results are most probably as dependable as a dice roll.

## Setup
This project uses twint for Twitter scraping and Natural Language Toolkit for the sentiment analysis part. Specifically the VADER (Valence Aware Dictionary for sEntiment Reasoning) sentiment analysis tools. Pandas module is also needed 🐼

`pip3 install --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint`

`pip3 install nltk pandas`

## Use
`python3 scraper.py username date`

`username` being the Twitter handle of a user you'd like to analyse

`date` being the day you'd like to analyse

### Citations
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
