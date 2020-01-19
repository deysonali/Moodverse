import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import language_v1
from google.cloud.language_v1 import enums

## Authenticate
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../../../../Moodverse-26a3ab24482a.json"

# Instantiates a client
client = language.LanguageServiceClient()

def normalize_sentiment(score):
    return (score+1)/2

def get_entity_sentiment(text_content): 
                                                    
    """
    Analyzing Entity Sentiment in a String
    Args:
      text_content The text content to analyze

    """

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8
    response = client.analyze_entity_sentiment(document, encoding_type=encoding_type)


    result = []
    for entity in response.entities:
        e_result = {}
        e_result["name"] = entity.name
        e_result["type"] = enums.Entity.Type(entity.type).name
        e_result["score"] = normalize_sentiment(entity.sentiment.score)
        result.append(e_result)

    return result

def fine_worst_entity(text_content):

    all_e = get_entity_sentiment(text_content)
    lowest_score = 3
    lowest_ent = None
    
    for ent in all_e:
      if ent["Score"] < lowest_score:
        lowest_score = ent["Score"]
        lowest_ent = ent
  
    return lowest_ent

def get_sentiment(text_content):
    
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """
    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_sentiment(document, encoding_type=encoding_type)
    # Get overall sentiment of the input document
    sentiment_score = response.document_sentiment.score

    return normalize_sentiment(sentiment_score)
