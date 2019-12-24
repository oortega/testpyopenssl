# -*- coding: utf-8 -*-
import requests
import json
import ast

# Create your views here.

endpoint = "https://pokeapi.co/api/v2/pokemon/?limit=10"
response = requests.get(url=endpoint)
response_dumps = json.dumps(response.content)
response_dict = json.loads(response_dumps)
response_dict = json.loads(response_dict)
pokemons = response_dict.get('results')
print pokemons