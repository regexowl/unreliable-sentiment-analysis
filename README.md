# Totally Unreliable Sentiment Analysis
###  === THIS PROJECT IS A WORK IN PROGRESS ===

My first journey into the wonderful world of sentiment analysis. 
Do not trust this sentiment analysis script under any circumstances! 
The results are most probably as dependable as a dice roll.

## Setup
This project uses twint for Twitter scraping and Natural Language Toolkit for the sentiment analysis part. Specifically the VADER (Valence Aware Dictionary for sEntiment Reasoning) sentiment analysis tools. 

`pip3 install --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint`
`pip3 install nltk pandas`

### Citations
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.