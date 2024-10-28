import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3fa91832c48eb6357a0c7f0a20983589'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '7994'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == '7994'