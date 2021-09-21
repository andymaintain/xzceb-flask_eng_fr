# import the required modules
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# create a connection that communicates .env file
apikey = os.environ['apikey']
url = os.environ['url']

# create a connection to the ibmcloud api
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# create a function that recieves text in english and translates it to french
def english_to_french(english_text):
    # code that used the ibmwatson translator to convert the text from english to french
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text=translation['translations'][0]['translation']
    return french_text


# create a function that recieves text in french and translates it to english
def french_to_english(french_text):
    #code that uses the ibmwatson translator to convert the text from french to english
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text=translation['translations'][0]['translation']
    return english_text
