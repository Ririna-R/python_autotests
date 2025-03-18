import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '792b34cbfddaca190b78274c51b55de5'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}


#1. Создание покемона

body_create_pokemon= {"name": "generate",
    "photo_id": -1
    }

response1=requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create_pokemon)
print(response1.text)
my_pokemon_id=response1.json()['id']

#2 Смена имени покемона

body_rename= {
    "pokemon_id": "id",
    "name": "BigBossik"
}

response2=requests.patch(url=f'{URL}/pokemons', headers=HEADER, json=body_rename)
print(response2.text)

#Поймать покемона в покебол

body_pokemon_in_pokeball={
    "pokemon_id": "id"
}

response3=requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokemon_in_pokeball)
print(response3.text)
