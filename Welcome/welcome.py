'''
The Task

Think of a way to store the languages as a database (eg an object). The 
languages are listed below so you can copy and paste!
Write a 'welcome' function that takes a parameter 'language' (always a string),
and returns a greeting - if you have it in your database. It should default to
English if the language is not in the database, or in the event of an invalid 
input.

The Database:
'english': 'Welcome',
'czech': 'Vitejte',
'danish': 'Velkomst',
'dutch': 'Welkom',
'estonian': 'Tere tulemast',
'finnish': 'Tervetuloa',
'flemish': 'Welgekomen',
'french': 'Bienvenue',
'german': 'Willkommen',
'irish': 'Failte',
'italian': 'Benvenuto',
'latvian': 'Gaidits',
'lithuanian': 'Laukiamas',
'polish': 'Witamy',
'spanish': 'Bienvenido',
'swedish': 'Valkommen',
'welsh': 'Croeso'

Possible invalid inputs include:
IP_ADDRESS_INVALID - not a valid ipv4 or ipv6 ip address
IP_ADDRESS_NOT_FOUND - ip address not in the database
IP_ADDRESS_REQUIRED - no ip address was supplied

'''

lang = {
    'english': 'Welcome',
    'czech': 'Vitejte',
    'danish': 'Velkomst',
    'dutch': 'Welkom',
    'estonian': 'Tere tulemast',
    'finnish': 'Tervetuloa',
    'flemish': 'Welgekomen',
    'french': 'Bienvenue',
    'german': 'Willkommen',
    'irish': 'Failte',
    'italian': 'Benvenuto',
    'latvian': 'Gaidits',
    'lithuanian': 'Laukiamas',
    'polish': 'Witamy',
    'spanish': 'Bienvenido',
    'swedish': 'Valkommen',
    'welsh': 'Croeso'
}

possible_inputs = ['IP_ADDRESS_INVALID',
                   'IP_ADDRESS_NOT_FOUND', 'IP_ADDRESS_REQUIRED']


def greet(language):

    if language not in lang:
        return 'Welcome'
    else:
        return lang[language]


# shroter version

def meet(language):
    return lang.get(language, 'Welcome')


# Debug
print(greet('dutch'))
print('Welkom')

print(meet('dutch'))
print('Welkom')
