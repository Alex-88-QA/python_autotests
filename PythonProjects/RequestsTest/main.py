import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3fa91832c48eb6357a0c7f0a20983589'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_generate = {
    "name": "generate",
    "photo_id": -1
}

body_change_name = {
    "pokemon_id": "117212",
    "name": "MSI",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": "117212"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json= body_generate)
print(response.text)'''

'''response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json= body_change_name)
print(response.text)'''

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json= body_add_pokeball)
print(response.text)