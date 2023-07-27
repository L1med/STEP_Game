import nltk
from textblob import TextBlob
from newspaper import Article
nltk.download('punkt')
url = 'https://freddy-fazbears-pizza.fandom.com/wiki/Nightmarionne' #insert url of a site in the ''
article = Article(url)
article.download()
article.parse()
article.nlp()
text= article. summary #gives you a summary
print (text)
blob= TextBlob(text)
sentiment = blob.sentiment.polarity # -1(negative) - 1(positive) and 0 is netural. Basically the rating
print (sentiment)