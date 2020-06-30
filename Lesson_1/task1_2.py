import requests
from pprint import pprint
import json

token = ''
main_link = f'https://api.vk.com/method/groups.get'
#main_link = f'https://api.vk.com/method/groups.get?v=5.52&extended=1&access_token={token}'
#main_link = f'https://api.vk.com/method/users.get?v=5.52&access_token={token}'

params = {'v':5.52,
          'extended':1,
          'access_token': token}
response = requests.get(main_link, params=params)
data = response.json()
#pprint(data)
#print(response.status_code)

with open('groups.txt','wb') as f:
     f.write(response.content)

for group in data['response']['items']:
    print(group['name'])