import requests
from pprint import pprint

user_name = 'MityaSorokin'
main_link = f'https://api.github.com/users/{user_name}/repos'

response = requests.get(main_link)
data = response.json()
#pprint(data)

for repo in data:
#    print(repo['name'])
    print(repo['html_url'])

