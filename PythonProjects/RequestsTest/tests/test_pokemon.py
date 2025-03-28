import requests
import pytest_

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '792b34cbfddaca190b78274c51b55de5'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID= '22716'
def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code==200

    def test_part_of_response():
        response_get = requests.get(url=f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_id"]== 22716