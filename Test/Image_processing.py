import requests
import json
from colorama import init, Fore
from dotenv import load_dotenv
import os

#load .env
load_dotenv()

#colorama init
init(convert=True)

azure_service_address = 'https://pythoncv.cognitiveservices.azure.com/'

SUBSCRIPTION_KEY = os.getenv('SUBSCRIPTION_KEY')

image_processing_address = azure_service_address + 'vision/v2.0/analyze'

parameters = {
    # Request parameters
    'visualFeatures': 'Description',
    'language': 'en',
}


headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
}

image_url = input('Enter an image URL to analyse: ')
# image_response = requests.get(image_url)
# image_data = Image.open(BytesIO(image_response.content))
image_data = {'url':image_url}

# According to the documentation for the analyze image function
# we use HTTP POST to call this function
response = requests.post(image_processing_address, headers=headers, params=parameters, json=image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(Fore.BLUE + json.dumps(results['description']['captions'][0]['text']))