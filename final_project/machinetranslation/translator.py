import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def englishToFrench(english_text):
    """ Translate the text input in English to French and return the French text """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator)

    language_translator.set_service_url(url)

    french_text = language_translator.translate(
        text = english_text,
        model_id = 'en-fr'
    ).get_result()

    french_text = json.dumps(french_text, indent=2, ensure_ascii=False)
    french_text = json.loads(french_text)
    return french_text['translations'][0]['translation']


def frenchToEnglish(french_text):
    """  translate the text input in French to English and return the English text """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator)

    language_translator.set_service_url(url)

    english_text = language_translator.translate(
        text = french_text,
        model_id = 'fr-en'
    ).get_result()

    english_text = json.dumps(english_text, indent=2, ensure_ascii=False)
    english_text = json.loads(english_text)
    return english_text['translations'][0]['translation']


englishToFrench('hello')

frenchToEnglish('bonjour')
