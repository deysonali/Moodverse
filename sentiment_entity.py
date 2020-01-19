from google.cloud import language_v1
from google.cloud.language_v1 import enums
import os
import pandas as pd

credential_path = 'REDACTED'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def sample_analyze_entity_sentiment(text_content):
    """
    Analyzing Entity Sentiment in a String
    Args:
      text_content The text content to analyze

    """

    client = language_v1.LanguageServiceClient()


    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_entity_sentiment(document, encoding_type=encoding_type)

    # Loop through entitites returned from the API

    result = []
    for entity in response.entities:
        e_result = []
        # print(u"Representative name for the entity: {}".format(entity.name))
        e_result.append(entity.name)
        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        # print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
        e_result.append(enums.Entity.Type(entity.type).name)

        # Get the salience score associated with the entity in the [0, 1.0] range
        # print(u"Salience score: {}".format(entity.salience))
        # Get the aggregate sentiment expressed for this entity in the provided document.
        # e_result.append(entity.salience)

        sentiment = entity.sentiment
        e_result.append(entity.sentiment.score)

        # print(u"Entity sentiment score: {}".format(sentiment.score))
        # print(u"Entity sentiment magnitude: {}".format(sentiment.magnitude))
        # e_result.append(entity.sentiment.magnitude)

        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        # for metadata_name, metadata_value in entity.metadata.items():
            # print(u"{} = {}".format(metadata_name, metadata_value))

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        # for mention in entity.mentions:
            # print(u"Mention text: {}".format(mention.text.content))
            # Get the mention type, e.g. PROPER for proper noun
            # print(
            #     u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name)
            # )

        result.append(e_result)

    return result #list of lists

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    # print(u"Language of the text: {}".format(response.language))

from google.cloud import language_v1
from google.cloud.language_v1 import enums


def sample_analyze_sentiment(text_content): #ASSUMES SINGLE SENTENCE
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

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
    # Get sentiment for all sentences in the document
    # for sentence in response.sentences:
    #     print(u"Sentence text: {}".format(sentence.text.content))
    #     print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
    #     print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    # print(u"Language of the text: {}".format(response.language))
    return sentiment_score

def update_self_score(result, entity_dict):
    entity_dict["self"].append(result) #adds on the new number
    return entity_dict

def update_entities(result, entity_dict):
    for set in result:
        entity = set[0]
        score = set[2]
        if entity in entity_dict:
            entity_dict[entity].append(score)
        else:
            entity_dict[entity] = [score]
        return entity_dict

self_words = ["me", "I", "myself", "my", "My", "Me", "Myself"]
entity_dict = {"self" : []}

input = "I am disappointed in myself."

result = sample_analyze_entity_sentiment(input)

if result == []:
    for word in input.split():
        if word in self_words:
            self_sentiment = sample_analyze_sentiment(input)
            update_self_score(self_sentiment, entity_dict)
            break
else:
    update_dict(result, entity_dict)

print(entity_dict)

