import data
import requests
import json

data =[]
for i in range(10):
    result = requests.get('https://randomuser.me/api')
    persons = result.json()
#print(persons['results'][0]['name']['first'])

#going to pull the data down users from the api and store this in a local file
    person = persons['results'][0]
    data.append(person)
#creates file
fh  = open('storage.json', 'wt')
json.dump(data, fh, indent=4)
fh.close()
