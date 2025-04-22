import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '21654fb504b65566ed1aeeecd01c14ef'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '30647'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_par_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Lana'