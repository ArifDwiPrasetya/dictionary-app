import requests

api_key='eb722de7-f2ad-4d99-91b6-dd63a4eb0710'
word = 'potato'

url=f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)
definitions = res.json()

print(definitions)