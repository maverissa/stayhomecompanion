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
genre_button = ['Rock', 'Metal', 'Pop', 'Jazz', 'R&B', 'Indie rock',
                'Electronic', 'Rap']
genre_msg = 'Choose any genre you like:'
mood_button = ['Workout', 'Romance', 'Chill', 'Flashback',
               'I need housework motivation', 'Party', 'Feel good', "I'm sad"]
mood_msg = 'Choose the option which fits your mood now the most:'
mus_menu = [emoji.emojize('Hit parades :chart_with_upwards_trend:',
                          use_aliases=True),
            emoji.emojize('Favourite genre :notes:', use_aliases=True),
            emoji.emojize('Current mood :relieved: ', use_aliases=True)]
mus_menu_msg = 'Do you want me to choose songs from hit parades or' \
               ' according to your favorite genre or current mood?'


def searching_a_song(call, url, n, times):
    i = 0
    while i < times:
        i += 1
        response = json.loads(requests.get(url).text)
        a = random.randint(0, n)
        artist = response["tracks"]["data"][a]["artist"]["name"]
        song = response["tracks"]["data"][a]["title"]
        bot.send_message(call.message.chat.id, artist + " - " + song)
        try:
            bot.send_audio(call.message.chat.id,
                           response["tracks"]["data"][a]['preview'])
        except Exception:
            bot.send_message(call.message.chat.id,
                             "Sorry, I didn't find the preview of that "
                             "song")


def hitparades_song(call):
    if call.data == ht_button[0]:
        bot.send_message(call.message.chat.id,
                         'Enjoy to this song popular worldwide ↓ \nIf you wan'
                         't another five, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/3155776842",
                         99, 5)
    elif call.data == ht_button[1]:
        bot.send_message(call.message.chat.id,
                         'Listen to this song popular in UK ↓ \nIf you want '
                         'another five, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/1111142221",
                         99, 5)
    elif call.data == ht_button[2]:
        bot.send_message(call.message.chat.id,
                         'Listen to this song popular in Russia ↓ \nIf you wan'
                         't another five, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/1116189381",
                         99, 5)
    elif call.data == ht_button[3]:
        bot.send_message(call.message.chat.id,
                         'Listen to this song popular in USA ↓ \nIf you want a'
                         'nother five, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/1313621735",
                         99, 5)
    elif call.data == ht_button[4]:
        bot.send_message(call.message.chat.id,
                         'Listen to this song popular in France ↓ \nIf you wan'
                         't another five, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/1109890291",
                         99, 5)
    elif call.data == ht_button[5]:
        bot.send_message(call.message.chat.id,
                         'Try out this song popular in Brazil ↓ \nIf you wan'
                         't another five, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/1111141961",
                         99, 5)
    elif call.data == ht_button[6]:
        bot.send_message(call.message.chat.id,
                         'Enjoy to this song popular in Japan ↓ \nIf you want'
                         ' another five, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/1362508955",
                         99, 5)


def genre_song(call):
    if call.data == genre_button[5]:
        bot.send_message(call.message.chat.id,
                         'Listen to this indie song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/760160361",
                         59, 1)
    elif call.data == genre_button[4]:
        bot.send_message(call.message.chat.id,
                         'Try out this R&B gold song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/1314725125",
                         49, 1)
    elif call.data == genre_button[7]:
        bot.send_message(call.message.chat.id,
                         'Listen to this song of a rap banger ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/1996494362",
                         50, 1)
    elif call.data == genre_button[3]:
        bot.send_message(call.message.chat.id,
                         'Listen to this classic jazz song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/1615514485",
                         79, 1)
    elif call.data == genre_button[2]:
        bot.send_message(call.message.chat.id,
                         'Listen to this one of the best pop songs ↓ \nIf you '
                         'want another one, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/1963962142",
                         59, 1)
    elif call.data == genre_button[0]:
        bot.send_message(call.message.chat.id,
                         'Listen to this legendary rock song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/4383475142",
                         99, 1)
    elif call.data == genre_button[6]:
        bot.send_message(call.message.chat.id,
                         'Listen to this new electronic song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/2143562442",
                         77, 1)
    elif call.data == genre_button[1]:
        bot.send_message(call.message.chat.id,
                         'Listen to this brutal metal song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song(call, "https://api.deezer.com/playlist/2655390504",
                         99, 1)


def mood_song(call):
    if call.data == mood_button[7]:
        bot.send_message(call.message.chat.id,
                         'Listen to this sad mood song ↓ \nIf you want '
                         'another one, you can click on any mood again!')
        searching_a_song(call, "https://api.deezer.com/playlist/5709525322",
                         399, 1)
    elif call.data == mood_button[6]:
        bot.send_message(call.message.chat.id,
                         'Listen to this good mood song ↓ \nIf you want '
                         'another one, you can click on any mood again!')
        searching_a_song(call, "https://api.deezer.com/playlist/4485213484",
                         39, 1)
    elif call.data == mood_button[2]:
        bot.send_message(call.message.chat.id,
                         'Listen to this relaxing song ↓ \nIf you want '
                         'another one, you can click on any mood again!')
        searching_a_song(call, "https://api.deezer.com/playlist/3338949242",
                         79, 1)
    elif call.data == mood_button[0]:
        bot.send_message(call.message.chat.id,
                         'Try out this song for home workout ↓ \nIf you want'
                         ' another one, you can click on any mood again!')
        searching_a_song(call, "https://api.deezer.com/playlist/2153050122",
                         69, 1)
    elif call.data == mood_button[1]:
        bot.send_message(call.message.chat.id,
                         'Listen to this song for a romantic evening ↓\nIf you'
                         ' want another one, you can click on any mood again!')
        searching_a_song(call, "https://api.deezer.com/playlist/1910878662",
                         99, 1)
    elif call.data == mood_button[3]:
        bot.send_message(call.message.chat.id,
                         'Listen to this 60s song ↓ \nIf you want '
                         'another one, you can click on any mood again!')
        searching_a_song(call, "https://api.deezer.com/playlist/620264073",
                         59, 1)
    elif call.data == mood_button[4]:
        bot.send_message(call.message.chat.id,
                         'Listen to this song for housework motivation ↓ \n'
                         'If you want another one, you can click on any mood '
                         'again!')
        searching_a_song(call, "https://api.deezer.com/playlist/7421024704",
                         69, 1)
    elif call.data == mood_button[5]:
        bot.send_message(call.message.chat.id,
                         'Enjoy this party hit ↓ \nIf you want '
                         'another one, you can click on any mood again!')
        searching_a_song(call, "https://api.deezer.com/playlist/2097558104",
                         78, 1)
