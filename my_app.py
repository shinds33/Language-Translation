import requests

API_KEY = 'trnsl.1.1.20191112T215743Z.477a420465e8c67b.7999c06a217a0d6aa13d11c2c65535b6683da6d9'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


# Get word/phrase and languages to translate from and to
wordInput = input('Enter a phrase you want to translate: ')

# Process input language
def process_input(user_in):
    user_in.strip()
    if user_in == 'English' or user_in == 'english':
        user_in = 'en'
        return user_in
    if user_in == 'Spanish' or user_in == 'spanish':
        user_in = 'es'
        return user_in
    if user_in == 'French' or user_in == 'french':
        user_in = 'fr'
        return user_in
    if user_in == 'Italian' or user_in == 'italian':
        user_in = 'it'
        return user_in
    if user_in == 'German' or user_in == 'german':
        user_in = 'de'
        return user_in
    if user_in == 'Arabic' or user_in == 'arabic':
        user_in = 'ar'
        return user_in
langInput = input('Enter the base language: ')
langInput = process_input(langInput)

# Process output language
def process_output(user_out):
    user_out.strip()
    if user_out == 'English' or user_out == 'english':
        user_out = 'en'
        return user_out
    if user_out == 'Spanish' or user_out == 'spanish':
        user_out = 'es'
        return user_out
    if user_out == 'French' or user_out == 'french':
        user_out = 'fr'
        return user_out
    if user_out == 'Italian' or user_out ==  'italian':
        user_out = 'it'
        return user_out
    if user_out == 'German' or user_out ==  'german':
        user_out = 'de'
        return user_out
    if user_out == 'Arabic' or user_out ==  'arabic':
        user_out = 'ar'
        return user_out
transInput = input('Enter the language to translate to: ')
transInput = process_output(transInput)

# Setting up call parameters
params = dict(key=API_KEY, text=wordInput, lang=langInput + '-' + transInput)

# Retrieving response
pageResponse = requests.get(url, params=params)

# Checking if the page is working
if pageResponse:
    print('Your phrase translated from ' + langInput + ' to ' + transInput + ' is: ')
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

# Displaying JSON object
json = pageResponse.json()
print(json['text'][0])







