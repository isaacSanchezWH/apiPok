from os import name
from django.conf.urls import url
from django.shortcuts import render
from django.views.generic.base import TemplateView
from apps.pokedex.api import getpokemons,getpokemon
import requests

# Create your views here.

#Index de la pagina
class Index(TemplateView):
    template_name = 'index.html'


#vista donde se listan todos los pokemons 
def list_pokemon(request):

    pokemons = getpokemons()

    #variables que seviran para guardar contenido
    dictionary  = {}
    context     = {}
    index       = 0
    
    #for para obtener todos los pokemos con su foto 
    for pokemon in pokemons:

        index += 1
    #extraccion de nombre y url ->(para obtener la foto)
        url     = pokemon['url']
        name    = pokemon['name'].capitalize()

    #Obtencion de foto e id

        result  = getpokemon(url)

        id      = result.get('id')
        sprites = result.get('sprites')
        photo   = sprites.get('front_shiny')

        dictionary = {
        'Name':     name,
        'Photo':    photo,
        'Id':       id

        }
        context[index] = dictionary

    return render(request, 'listar_pokemon.html', {'Pokemons': context})

#vista de detalles de pokemon
def pokemon(request,id):

    #Ingresamos a la url con id pasando a id en formato string
    pokemon = getpokemon('https://pokeapi.co/api/v2/pokemon/{}'.format(id) )

    #declaramos variable futuras
    dictionary_type = {}
    context_type    = {}
    list_move       = []
    list_abilities  = []
    context         = {}
    index           = 0

    #obtenemos datos 
    name        = pokemon.get('name').capitalize()
    sprites     = pokemon.get('sprites')
    photo       = sprites.get('front_shiny')
    weight      = pokemon.get('weight')
    height      = pokemon.get('height')
    types       = pokemon.get('types')
    abilities   = pokemon.get('abilities')
    moves       = pokemon.get('moves')


    #ciclos para obter el datos de pokemon que sean mas de 1 
    for values in types:
        index   += 1
        type     = values.get('type')['name'] 

        #obtenemos la url para entrar al tipo y obtener el id 
        url     = values.get('type')['url'] 
        result  = getpokemon(url)
        id      = result.get('id')

        dictionary_type = {
         'type':        type,
         'id':          id,
        }
        context_type[index] = dictionary_type
    
    for values in abilities:
        ability = values.get('ability')['name'] 
        list_abilities.append(ability)

    for values in moves:
        move = values.get('move')['name'] 
        list_move.append(move)

        

    context ={
        'Name':         name,
        'Photo':        photo,
        'weight':       weight, 
        'height':       height, 
        'abilities':    list_abilities,
        'moves':        list_move,
        'types':         context_type,
    }   


    return render(request, 'pokemon.html', context)

#vista con los pokemon que hay de ese tipo
def types_pokemon(request,id):

    pokemons = getpokemon('https://pokeapi.co/api/v2/type/{}/'.format(id) )

    
    #declaramos variable futuras
    dictionary  = {}
    context     = {}
    index       = 0

    pokemon = pokemons.get('pokemon')

    for values in pokemon:

        index  += 1
        name = values.get('pokemon')['name'].capitalize() 
        url = values.get('pokemon')['url'] 

        #Obtener de foto e if
        result  = getpokemon(url)

        sprites = result.get('sprites')
        photo   = sprites.get('front_shiny')

        #Obtencion de foto e id

        result  = getpokemon(url)

        id      = result.get('id')
        sprites = result.get('sprites')
        photo   = sprites.get('front_shiny')

        dictionary = {
        'Name':     name,
        'Photo':    photo,
        'Id':       id

        }
        context[index] = dictionary



    
    return render(request, 'listar_pokemon.html', {'Pokemons': context})


def paginado_pokemon(request,offset):

    pokemons = getpokemons(offset)

    #variables que seviran para guardar contenido
    dictionary  = {}
    context     = {}
    index       = 0
    
    #for para obtener todos los pokemos con su foto 
    for pokemon in pokemons:

        index += 1
    #extraccion de nombre y url ->(para obtener la foto)
        url     = pokemon['url']
        name    = pokemon['name'].capitalize()

    #Obtencion de foto e id

        result  = getpokemon(url)

        id      = result.get('id')
        sprites = result.get('sprites')
        photo   = sprites.get('front_shiny')

        dictionary = {
        'Name':     name,
        'Photo':    photo,
        'Id':       id

        }
        context[index] = dictionary

    return render(request, 'listar_pokemon.html', {'Pokemons': context})