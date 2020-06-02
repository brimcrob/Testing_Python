import json
import random

fh = open('storage.json', 'rt')
customers = json.load(fh)

customer = random.choice(customers)
print(" {} {}".format(customer['name']['first'],customer['name']['last']))
