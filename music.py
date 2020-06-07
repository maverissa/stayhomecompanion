import telebot
import json
import requests
import random
import emoji
bot = telebot.TeleBot('1116307628:AAGco0iC37MG0Yy_J3p7esHABjEpedxu7u0')
ht_button = ['5 from top 100 World', '5 from top 100 UK',
             '5 from top 100 Russia', '5 from top 100 USA',
             '5 from top 100 France', '5 from top 100 Brazil',
             '5 from top 100 Japan']
ht_msg = 'Do you want to hear worldwide hits or popular songs of some country?'
genre_button, genre_msg = ['Rock', 'Metal', 'Pop', 'Jazz', 'R&B', 'Indie rock',
                           'Electronic', 'Rap'], 'Choose any genre you like:'
mood_button = ['Workout', 'Romance', 'Chill', 'Flashback',
               'I need housework motivation', 'Party', 'Feel good', "I'm sad"]
mood_msg = 'Choose the option which fits your mood now the most:'
mus_menu = [emoji.emojize('Hit parades :chart_with_upwards_trend:',
                          use_aliases=True),
            emoji.emojize('Favourite genre :notes:', use_aliases=True),
            emoji.emojize('Current mood :relieved: ', use_aliases=True)]
mus_menu_msg = 'Do you want me to choose songs from hit parades or' \
               ' according to your favorite genre or current mood?'


def searching_a_song(url, n, times, id):
    i = 0
    while i < times:
        i += 1
        response = json.loads(requests.get(url).text)
        a = random.randint(0, n)
        artist = response["tracks"]["data"][a]["artist"]["name"]
        song = response["tracks"]["data"][a]["title"]
        bot.send_message(id, artist + " - " + song)
        try:
            bot.send_audio(id, response["tracks"]["data"][a]['preview'])
        except Exception:
            bot.send_message(id, "Sorry, I didn't find the preview of that "
                                 "song")


tip = '\nIf you want another five, you can click on any genre again!'
li_ht = [['Enjoy this song popular worldwide ↓' + tip,
          "https://api.deezer.com/playlist/3155776842"],
         ['Listen to this song popular in UK ↓' + tip,
          "https://api.deezer.com/playlist/1111142221"],
         ['Try out this song popular in Russia ↓' + tip,
          "https://api.deezer.com/playlist/1116189381"],
         ['Listen to this song popular in USA ↓' + tip,
          "https://api.deezer.com/playlist/1116189381"],
         ['Listen to this hit from France ↓' + tip,
          "https://api.deezer.com/playlist/1109890291"],
         ['Try out this song popular in Brazil ↓' + tip,
          "https://api.deezer.com/playlist/1111141961"],
         ['Enjoy this song popular in Japan ↓' + tip,
          "https://api.deezer.com/playlist/1362508955"]]
di_ht = dict(zip(ht_button, li_ht))


def hitparades_song(call):
    bot.send_message(call.message.chat.id, di_ht[call.data][0])
    searching_a_song(di_ht[call.data][1], 99, 5, call.message.chat.id)


li_genre = [['Enjoy this legendary rock song ↓' + tip,
             "https://api.deezer.com/playlist/4383475142", 99],
            ['Listen to this brutal metal song ↓' + tip,
             "https://api.deezer.com/playlist/2655390504", 99],
            ['Try out one of the best pop songs ↓' + tip,
             "https://api.deezer.com/playlist/1963962142", 59],
            ['Enjoy this classic jazz song ↓' + tip,
             "https://api.deezer.com/playlist/1615514485", 79],
            ['Try out this R&B gold song ↓' + tip,
             "https://api.deezer.com/playlist/1314725125", 49],
            ['Listen to this indie song ↓' + tip,
             "https://api.deezer.com/playlist/760160361", 59],
            ['Listen to this new electronic song ↓' + tip,
             "https://api.deezer.com/playlist/2143562442", 77],
            ['Listen to this song of a rap banger ↓' + tip,
             "https://api.deezer.com/playlist/1996494362", 50]]
di_genre = dict(zip(genre_button, li_genre))


def genre_song(call):
    bot.send_message(call.message.chat.id, di_genre[call.data][0])
    searching_a_song(di_genre[call.data][1], di_genre[call.data][2], 1,
                     call.message.chat.id)


li_mood = [['Try out this song for a home workout ↓' + tip,
            "https://api.deezer.com/playlist/2153050122", 69],
           ['Enjoy this song for a romantic evening ↓' + tip,
            "https://api.deezer.com/playlist/1910878662", 99],
           ['Chill out to this relaxing song ↓' + tip,
            "https://api.deezer.com/playlist/3338949242", 79],
           ['Feel nostalgic to this 60s song ↓' + tip,
            "https://api.deezer.com/playlist/620264073", 59],
           ['Listen to this song for housework motivation ↓' + tip,
            "https://api.deezer.com/playlist/7421024704", 69],
           ['Enjoy this party hit ↓' + tip,
            "https://api.deezer.com/playlist/2097558104", 78],
           ['Listen to this good mood song ↓' + tip,
            "https://api.deezer.com/playlist/4485213484", 39],
           ['Listen to this sad mood song ↓' + tip,
            "https://api.deezer.com/playlist/5709525322", 399]]
di_mood = dict(zip(mood_button, li_mood))


def mood_song(call):
    bot.send_message(call.message.chat.id, di_mood[call.data][0])
    searching_a_song(di_mood[call.data][1], di_mood[call.data][2],
                     1, call.message.chat.id)
