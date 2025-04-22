import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '21654fb504b65566ed1aeeecd01c14ef'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change = {
    "pokemon_id": "298335",
    "name": "Хачапури"
}

body_pokeball = {
    "pokemon_id": "298335"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)