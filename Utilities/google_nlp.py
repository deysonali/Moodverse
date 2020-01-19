import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

## Authenticate
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../../Moodverse-26a3ab24482a.json"

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u'Hello, world!'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))