# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 09:19:36 2023

@author: geron
"""

# using the json.load() function to work with json files - java script files - must import json


import json
 
with open('purchase_14781239.json') as purchase_json:
  purchase_data = json.load(purchase_json)
 
print(purchase_data['user'])
# Prints 'ellen_greg'




import json

with open('message.json') as message_json:
  message = json.load(message_json)
print(message['text'])


# using .dump with write a json file

turn_to_json = {
  'eventId': 674189,
  'dateTime': '2015-02-12T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}

import json
 
with open('output.json', 'w') as json_file:
  json.dump(turn_to_json, json_file)
  


data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)








