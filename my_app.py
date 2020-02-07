# Sam Hinds 2019
# Language translate API

import requests
API_KEY = 'trnsl.1.1.20191112T215743Z.477a420465e8c67b.7999c06a217a0d6aa13d11c2c65535b6683da6d9'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

# Define valid language options
langDict = {'Azerbaijan': 'az', 'Albanian': 'sq', 'Amharic': 'am', 'English': 'en', 'Arabic': 'ar',
        'Armenian': 'hy', 'Afrikaans': 'af', 'Basque': 'eu', 'Burmese': 'my', 'Hungarian': 'hu',
        'Vietnamese': 'vi', 'Greek': 'el', 'Georgian': 'ka', 'Hebrew': 'he', 'Indonesian': 'id',
        'Irish': 'ga', 'Italian': 'it', 'Icelandic': 'is', 'Spanish': 'es', 'Chinese': 'zh',
        'Korean': 'ko', 'Latin': 'la', 'Latvian': 'lv', 'Mongolian': 'mn', 'German': 'de',
        'Norwegian': 'no', 'Punjabi': 'pa', 'Polish': 'pl', 'Portuguese': 'pt',
        'Russian': 'ru', 'Serbian': 'sr', 'Swahili': 'sw', 'Thai': 'th', 'Ukrainian': 'uk',
        'French': 'fr', 'Croatian': 'hr', 'Czech': 'cs', 'Swedish': 'sv', 'Estonian': 'et',
        'Japanese': 'ja'}

# Process input phrase
print('\n')
wordInput = input('Enter a phrase you want to translate: ')
print('\n')

# Process input language
raw_input_choice = input('Translate from: ')
input_choice = raw_input_choice.replace(" ", "")
input_choice = input_choice.capitalize()

if input_choice in langDict:
    langInput = langDict.get(input_choice)
else:
    print('Input language not supported. Please refer to the list of supported languages and try again')
    exit(0)

# Process output language
raw_output_choice = input('Translate to: ')
output_choice = raw_output_choice.replace(" ", "")
output_choice = output_choice.capitalize()
if output_choice in langDict:
    transInput = langDict.get(output_choice)
else:
    print('Output language not supported. Please refer to the list of supported languages and try again')
    exit(0)

# Setting up call parameters and retrieving response
params = dict(key=API_KEY, text=wordInput, lang=langInput + '-' + transInput)
pageResponse = requests.get(url, params=params)

# Checking if the page is working
if pageResponse:
    print('\n')
    print('Your phrase translated from ' + input_choice + ' to ' + output_choice + ': ')
else:
    print('There was an issue loading the response')
    if pageResponse.status_code == 403:
        print('API key is not valid')
    if pageResponse.status_code == 404:
        print('You have used your maximum amount of translations')
    if pageResponse.status_code == 422:
        print('This text cannot be translated')

# Print HTML data
output = open('index.html', 'w')
output.write(pageResponse.text)
output.close()

# Displaying result
json = pageResponse.json()
print(json['text'][0])
print('\n')

