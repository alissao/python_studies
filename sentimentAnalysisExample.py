# using python3 on terminal
from textblob import TextBlob

a = TextBlob("I am the worst student ever!")
a.sentiment.polarity

a = TextBlob("I am a student!")
a.sentiment.polarity

a = TextBlob("I am the best student in the world!")
a.sentiment.polarity