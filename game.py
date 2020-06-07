import requests
import json
import random
import re
import html
buttons, msg = ['Games with rating >3.0', 'Random game', 'Action game',
                'RPG game', 'Arcade game'], "Choose one:"


# This is def for using html symbols
def html_decode(s):
    htmlcodes = (
        ("'", '&#39;'),
        ('"', '&quot;'),
        ('>', '&gt;'),
        ('<', '&lt;'),
        ('&', '&amp;')
    )
    for code in htmlcodes:
        s = s.replace(code[1], code[0])
    return s


# This is a def for getting a random game.
def random_game():
    while True:
        # Here we take all information from the api site of a random game.
        response = json.loads(requests.get
                              (f'https://api.rawg.io/api/games/'
                               f'{str(random.randint(1, 10000))}').text)
        if "slug" in response:
            b = 'Genre is not defined.'
            try:
                if 'genres' in response and bool(response['genres']) is True:
                    dic_1 = (response['genres'][0])
                    b = (dic_1['name'])
            except IndexError:
                pass
            dxd = 'Name| ' + response["slug"]
            dxd = dxd + '\nGenre| ' + b
            dxd = dxd + '\nReleased| ' + str(response['released'])
            dxd = dxd + '\nRating| ' + str(response['rating'])
            dxd = dxd + '\nAchievements| ' + str(response
                                                 ["achievements_count"])
            dxd = dxd + '\nWebsite| ' + response['website']
            dxd = dxd + '\nMetacritics| ' + str(response['metacritic'])
            c = html.unescape(response['description'])
            unescaped = html_decode(c)
            bb = re.sub(r'\<[A-Za-z\/][^>#]*\>', '', unescaped)
            dxd = dxd + '\nDescription| ' + bb
            return dxd


# This is a def for getting a random game with rating higher than 3.0.
def random_game_rating():
    while True:
        # Here we take all information from the api site of a random game.
        response = json.loads(requests.get(f'https://api.rawg.io/api/games/'
                                           f'{str(random.randint(1, 10000))}'
                                           f'').text)
        if "slug" in response and "rating" in response and response['rating'] \
                > 3.0:
            b = 'Genre is not defined.'
            try:
                if 'genres' in response and bool(response['genres']) is True:
                    dic_1 = (response['genres'][0])
                    b = (dic_1['name'])
            except IndexError:
                pass
            dxd = 'Name| ' + response["slug"]
            dxd = dxd + '\nGenre| ' + b
            dxd = dxd + '\nReleased| ' + str(response['released'])
            dxd = dxd + '\nRating| ' + str(response['rating'])
            dxd = dxd + '\nAchievements| ' + str(response
                                                 ["achievements_count"])
            dxd = dxd + '\nWebsite| ' + response['website']
            dxd = dxd + '\nMetacritics| ' + str(response['metacritic'])
            c = html.unescape(response['description'])
            unescaped = html_decode(c)
            bb = re.sub(r'\<[A-Za-z\/][^>#]*\>', '', unescaped)
            dxd = dxd + '\nDescription| ' + bb
            return dxd


# This is a def for getting a random action game.
def random_game_action():
    while True:
        # Here we take all information from the api site of a random game.
        response = json.loads(requests.get(f'https://api.rawg.io/api/games/'
                                           f'{str(random.randint(1, 10000))}'
                                           ).text)
        b = 'Genre is not defined.'
        if "slug" in response and "genres" in response and \
                bool(response['genres']) is True:
            dic_1 = (response['genres'][0])
            b = (dic_1['name'])
        if b == 'Action':
            dxd = 'Name| ' + response["slug"]
            dxd = dxd + '\nGenre| ' + b
            dxd = dxd + '\nReleased| ' + str(response['released'])
            dxd = dxd + '\nRating| ' + str(response['rating'])
            dxd = dxd + '\nAchievements| ' + str(response
                                                 ["achievements_count"])
            dxd = dxd + '\nWebsite| ' + response['website']
            dxd = dxd + '\nMetacritics| ' + str(response['metacritic'])
            c = html.unescape(response['description'])
            unescaped = html_decode(c)
            bb = re.sub(r'\<[A-Za-z\/][^>#]*\>', '', unescaped)
            dxd = dxd + '\nDescription| ' + bb
            return dxd


# This is a def for getting a random rpg game.
def random_game_rpg():
    while True:
        # Here we take all information from the api site of a random game.
        response = json.loads(requests.get
                              (f'https://api.rawg.io/api/games/'
                               f'{str(random.randint(1, 10000))}').text)
        b = 'Genre is not defined.'
        if "slug" in response and "genres" in response and \
                bool(response['genres']) is True:
            dic_1 = (response['genres'][0])
            b = (dic_1['name'])
        if b == 'RPG':
            dxd = 'Name| ' + response["slug"]
            dxd = dxd + '\nGenre| ' + b
            dxd = dxd + '\nReleased| ' + str(response['released'])
            dxd = dxd + '\nRating| ' + str(response['rating'])
            dxd = dxd + '\nAchievements| ' + str(response
                                                 ["achievements_count"])
            dxd = dxd + '\nWebsite| ' + response['website']
            dxd = dxd + '\nMetacritics| ' + str(response['metacritic'])
            c = html.unescape(response['description'])
            unescaped = html_decode(c)
            bb = re.sub(r'\<[A-Za-z\/][^>#]*\>', '', unescaped)
            dxd = dxd + '\nDescription| ' + bb
            return dxd


# This is a def for getting a random arcade game.
def random_game_arcade():
    while True:
        # Here we take all information from the api site of a random game.
        response = json.loads(requests.get
                              (f'https://api.rawg.io/api/games/'
                               f'{str(random.randint(1, 10000))}').text)
        b = 'Genre is not defined.'
        if "slug" in response and "genres" in response and \
                bool(response['genres']) is True:
            dic_1 = (response['genres'][0])
            b = (dic_1['name'])
        if b == 'Arcade':
            dxd = 'Name| ' + response["slug"]
            dxd = dxd + '\nGenre| ' + b
            dxd = dxd + '\nReleased| ' + str(response['released'])
            dxd = dxd + '\nRating| ' + str(response['rating'])
            dxd = dxd + '\nAchievements| ' + str(response
                                                 ["achievements_count"])
            dxd = dxd + '\nWebsite| ' + response['website']
            dxd = dxd + '\nMetacritics| ' + str(response['metacritic'])
            c = html.unescape(response['description'])
            unescaped = html_decode(c)
            bb = re.sub(r'\<[A-Za-z\/][^>#]*\>', '', unescaped)
            dxd = dxd + '\nDescription| ' + bb
            return dxd


def random_game_year():
    while True:
        # Here we take all information from the api site of a random game.
        response = json.loads(requests.get
                              (f'https://api.rawg.io/api/games/'
                               f'{str(random.randint(1, 1000000))}').text)
        if "slug" in response and "released" in response and \
                bool(response['released']) is True:
            a = response['released']
            a = a.split('-')
            x = a[0]
            x = int(x)
            b = 'Genre is not defined.'
            if x >= 2019:
                try:
                    if 'genres' in response and \
                            bool(response['genres']) is True:
                        dic_1 = (response['genres'][0])
                        b = (dic_1['name'])
                except IndexError:
                    pass
                dxd = 'Name| ' + response["slug"]
                dxd = dxd + '\nGenre| ' + b
                dxd = dxd + '\nReleased| ' + str(response['released'])
                dxd = dxd + '\nRating| ' + str(response['rating'])
                dxd = dxd + '\nAchievements| ' + \
                    str(response["achievements_count"])
                dxd = dxd + '\nWebsite| ' + response['website']
                dxd = dxd + '\nMetacritics| ' + str(response['metacritic'])
                c = html.unescape(response['description'])
                unescaped = html_decode(c)
                bb = re.sub(r'\<[A-Za-z\/][^>#]*\>', '', unescaped)
                dxd = dxd + '\nDescription| ' + bb
                return dxd
