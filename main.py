#!/usr/bin/env python
from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt
import config as cfg
from tweepy import Stream  # Useful in Step 3
from tweepy.streaming import StreamListener  # Useful in Step 3
import json


def percentage(part, whole):
    return 100 * float(part) / float(whole)


auth = tweepy.OAuthHandler(cfg.consumer_key, cfg.consumer_secret)
auth.set_access_token(cfg.access_token, cfg.access_token_secret)
api = tweepy.API(auth)

searchTerm = input("Digite a hashtag ou palavra-chave que deseja analisar: ")
noOfSearchTerms = int(input("Quantos tweets com esse parâmetro você deseja analisar? "))

tweets = tweepy.Cursor(api.search, q=searchTerm, lang="pt").items(noOfSearchTerms)

positive = 0
neutral = 0
negative = 0
polarity = 0

for tweet in tweets:
    # print(tweet.text)

    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if analysis.sentiment.polarity < 0.00:
        negative += 1
    elif analysis.sentiment.polarity == 0:
        neutral += 1
    elif analysis.sentiment.polarity > 0.00:
        positive += 1

negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
positive = percentage(positive, noOfSearchTerms)

negative = format(negative, '.2f')
neutral = format(neutral, '.2f')
positive = format(positive, '.2f')

print(
    "Como as pessoas estão se sentindo sobre " + str(searchTerm) + " depois de analisarmos "
    + str(noOfSearchTerms) + " tweets:")

if polarity < 0.00:
    print("Negativas.")
elif polarity == 0.00:
    print("Neutras.")
elif polarity > 0.00:
    print("Positivas.")

labels = ['Negativos [' + str(negative) + '%]', 'Neutros [' + str(neutral) + '%]', 'Positivos [' + str(positive) + '%]']
sizes = [negative, neutral, positive]
colors = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title(
    "Como as pessoas estão se sentindo sobre " + str(searchTerm) + " depois de analisarmos " +
    str(noOfSearchTerms) + " tweets:")
plt.axis('equal')
plt.tight_layout()
plt.show()
