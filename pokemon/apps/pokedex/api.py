from django.http import response
import requests



#estructura para obtener los datos 
def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()


#Obtener todos los pokemos
def getpokemons(offset = 0):

    args = {'offset':offset} if offset else {}
    response = generate_request('https://pokeapi.co/api/v2/pokemon-form/',args)
    
    
    if response:

         pokemon = response.get('results', [] )

         return pokemon


#Obtener datos especificos de Pokemon
def getpokemon(url):

    response = generate_request(url)

    return response
         
