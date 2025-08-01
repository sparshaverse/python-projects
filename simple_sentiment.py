from textblob import Textblob

text = "Data Science is incredibly exciting and powerful."
blob = Textblob(text)

print("Sentiment polarity:", blob.sentiment.polarity)