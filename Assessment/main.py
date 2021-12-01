import requests
import json
from requests import get
print('Найти покемона по имени: 1')
print('Получить из списка первых 50 покемонов: 2')
print('Введите 1/2')
startanswer = int(input())
if startanswer == 1:
    print('Введите имя строчными буквами на латинице')
    name = input()

class BasePokemon:
    def __init__(self):
        pass

class Pokemon:
    def __init__(self):
        pass



class PokeAPI:
    def __init__(self):
        pass

    @get_all
    def get_all:
        url = 'https://pokeapi.co/api/v2/pokemon?limit=50'






    print('Введите имя строчными буквами на латинице')
    name = input()
    url = f'https://pokeapi.co/api/v2/pokemon/{name}/'
    resp = get(url)
    if resp.status_code == 200:
        pokemon = resp.json()
        poke_name = pokemon['name']
        poke_id = pokemon['id']
        poke_height = pokemon['height']
        poke_weight = pokemon['weight']
        answer = {'Name': poke_name,
                  'Id': poke_id,
                  'Height': poke_height,
                  'Weight': poke_weight
                  }
        print(answer)
    else:
        print('Error caught in API response')
        quit(1)

elif startanswer == 2:
    print('func2')
else:
    print('Error: wrong function id')
