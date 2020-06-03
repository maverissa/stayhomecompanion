import telebot
from telebot import types
import requests
import random
import emoji
import json
import film
import lyricsgenius
bot = telebot.TeleBot('1116307628:AAGco0iC37MG0Yy_J3p7esHABjEpedxu7u0')


@bot.message_handler(commands=["start"])
def general_menu(message):
    bot.send_message(message.chat.id, 'Hello! I will do my best to make your '
                                      'home stay fascinating!')
    markup = types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton
               (text=(emoji.emojize('Games :video_game:', use_aliases=True)),
                callback_data='games'))
    markup.add(
        telebot.types.InlineKeyboardButton
        (text=(emoji.emojize('Music :headphones:', use_aliases=True)),
         callback_data='mus'))
    markup.add(
        telebot.types.InlineKeyboardButton
        (text=(emoji.emojize('Films and series :movie_camera:',
                             use_aliases=True)), callback_data='filmsseries'))
    bot.send_message(message.chat.id, 'What do you want me to recommend you?',
                     reply_markup=markup)


@bot.message_handler(commands=["lyrics"])
def lyrics_handler(message):
    msg = bot.send_message(message.chat.id,
                           'Input the name of a song, an artist.\nFor '
                           'example: Little 15, Depeche Mode')
    bot.register_next_step_handler(msg, song_lyrics)


def song_lyrics(message):
    answer = message.text
    genius = lyricsgenius.Genius(
        "-pxwr2wPA_q6ivrxgtD8Yb1BmOM4bUnFQF-6eMG9ROZze-"
        "diXrdoAhLIyxYGd0Hb")
    answer = answer.split(',')
    try:
        song_search = genius.search_song(answer[0], answer[1])
        bot.send_message(message.chat.id, song_search.lyrics)
    except Exception:
        bot.send_message(message.chat.id, "Sorry, I didn't find such a song")


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    def searching_a_song(url, n, times):
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

    if call.data == 'games':
        # работа с API игр
        pass
    elif call.data == 'mus':
        # работа с API музыки
        markup = types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton
                   (text=(emoji.emojize
                          ('Favourite genre :notes:', use_aliases=True)),
                    callback_data='genre'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text=(emoji.emojize
                          ('Current mood :relieved: ', use_aliases=True)),
                    callback_data='mood'))
        bot.send_message(call.message.chat.id,
                         'Do you want me to choose songs from hit parades or '
                         'according to your favorite genre or current mood?',
                         reply_markup=markup)
    if call.data == 'hitparades':
        markup = types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton
                   (text='5 from top 100 World', callback_data='world'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='5 from top 100 UK', callback_data='uk'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='5 from top 100 Russia', callback_data='russia'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='5 from top 100 USA', callback_data='usa'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='5 from top 100 France', callback_data='france'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='5 from top 100 Brazil', callback_data='brazil'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='5 from top 100 Japan', callback_data='japan'))
        bot.send_message(call.message.chat.id,
                         'Do you want to hear worldwide hits or'
                         ' of some country?', reply_markup=markup)
    if call.data == 'world':
        bot.send_message(call.message.chat.id,
                         'Listen to this song popular worldwide ↓ \nIf you wan'
                         't another five, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/3155776842", 99, 5)
    elif call.data == 'uk':
        bot.send_message(call.message.chat.id,
                         'Listen to this song popular in UK ↓ \nIf you want '
                         'another five, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/1111142221", 99, 5)
    elif call.data == 'russia':
        bot.send_message(call.message.chat.id,
                         'Listen to this song popular in Russia ↓ \nIf you wan'
                         't another five, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/1116189381", 99, 5)
    elif call.data == 'usa':
        bot.send_message(call.message.chat.id,
                         'Listen to this song popular in USA ↓ \nIf you want a'
                         'nother five, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/1313621735", 99, 5)
    elif call.data == 'france':
        bot.send_message(call.message.chat.id,
                         'Listen to this song popular in France ↓ \nIf you wan'
                         't another five, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/1109890291", 99, 5)
    elif call.data == 'brazil':
        bot.send_message(call.message.chat.id,
                         'Listen to this song popular in Brazil ↓ \nIf you wan'
                         't another five, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/1111141961", 99, 5)
    elif call.data == 'japan':
        bot.send_message(call.message.chat.id,
                         'Listen to this song popular in Japan ↓ \nIf you want'
                         ' another five, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/1362508955", 99, 5)
    elif call.data == 'genre':
        markup = types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton
                   (text='Rock', callback_data='rock'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='Metal', callback_data='metal'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='Pop', callback_data='pop'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='Jazz', callback_data='jazz'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='R&B', callback_data='rnb'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='Rap', callback_data='rap'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='Indie rock', callback_data='indie'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='Electronic', callback_data='electronic'))
        bot.send_message(call.message.chat.id,
                         'Choose any genre you like:', reply_markup=markup)
    if call.data == 'indie':
        bot.send_message(call.message.chat.id,
                         'Listen to this indie song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/760160361", 60, 1)
    elif call.data == 'rnb':
        bot.send_message(call.message.chat.id,
                         'Listen to this R&B gold song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/1314725125", 50, 1)
    elif call.data == 'rap':
        bot.send_message(call.message.chat.id,
                         'Listen to this song of a rap banger ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/1996494362", 50, 1)
    elif call.data == 'jazz':
        bot.send_message(call.message.chat.id,
                         'Listen to this classic jazz song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/1615514485", 79, 1)
    elif call.data == 'pop':
        bot.send_message(call.message.chat.id,
                         'Listen to this one of the best pop songs ↓ \nIf you '
                         'want another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/1963962142", 59, 1)
    elif call.data == 'rock':
        bot.send_message(call.message.chat.id,
                         'Listen to this legendary rock song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/4383475142", 99, 1)
    elif call.data == 'electronic':
        bot.send_message(call.message.chat.id,
                         'Listen to this new electronic song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/2143562442", 77, 1)
    elif call.data == 'metal':
        bot.send_message(call.message.chat.id,
                         'Listen to this brutal metal song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/2655390504", 99, 1)
    elif call.data == 'mood':
        markup = types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton
                   (text='Workout', callback_data='workout'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='Romance', callback_data='romance'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='Chill', callback_data='chill'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='Flashback', callback_data='flashback'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='Housework motivation', callback_data='home'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='Party', callback_data='party'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text='Feel good', callback_data='good'))
        markup.add(telebot.types.InlineKeyboardButton
                   (text="I'm sad", callback_data='sad'))
        bot.send_message(call.message.chat.id,
                         'Choose the option which fits your'
                         ' mood now the most:', reply_markup=markup)
    if call.data == 'sad':
        bot.send_message(call.message.chat.id,
                         'Listen to this sad mood song ↓ \nIf you want '
                         'another one, you can click on any mood again!')
        searching_a_song("https://api.deezer.com/playlist/5709525322", 399, 1)
    elif call.data == 'good':
        bot.send_message(call.message.chat.id,
                         'Listen to this good mood song ↓ \nIf you want '
                         'another one, you can click on any mood again!')
        searching_a_song("https://api.deezer.com/playlist/4485213484", 39, 1)
    elif call.data == 'chill':
        bot.send_message(call.message.chat.id,
                         'Listen to this relaxing song ↓ \nIf you want '
                         'another one, you can click on any mood again!')
        searching_a_song("https://api.deezer.com/playlist/3338949242", 79, 1)
    elif call.data == 'workout':
        bot.send_message(call.message.chat.id,
                         'Listen to this song for home workout ↓ \nIf you want'
                         ' another one, you can click on any mood again!')
        searching_a_song("https://api.deezer.com/playlist/2153050122", 69, 1)
    elif call.data == 'romance':
        bot.send_message(call.message.chat.id,
                         'Listen to this song for a romantic evening ↓\nIf you'
                         ' want another one, you can click on any mood again!')
        searching_a_song("https://api.deezer.com/playlist/1910878662", 99, 1)
    elif call.data == 'flashback':
        bot.send_message(call.message.chat.id,
                         'Listen to this 60s song ↓ \nIf you want '
                         'another one, you can click on any mood again!')
        searching_a_song("https://api.deezer.com/playlist/620264073", 59, 1)
    elif call.data == 'home':
        bot.send_message(call.message.chat.id,
                         'Listen to this song for housework motivation ↓ \n'
                         'If you want another one, you can click on any mood '
                         'again!')
        searching_a_song("https://api.deezer.com/playlist/7421024704", 69, 1)
    elif call.data == 'party':
        bot.send_message(call.message.chat.id,
                         'Listen to this party hit ↓ \nIf you want '
                         'another one, you can click on any mood again!')
        searching_a_song("https://api.deezer.com/playlist/2097558104", 78, 1)
    elif call.data == 'filmsseries':
        # работа с API кино
        markup = types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Top 5 films',
                                                      callback_data='top'))
        markup.add(telebot.types.InlineKeyboardButton(text='Actor',
                                                      callback_data='actor'))
        markup.add(telebot.types.InlineKeyboardButton(text='Rating',
                                                      callback_data='rating'))
        markup.add(telebot.types.InlineKeyboardButton(text='Released year',
                                                      callback_data='year'))
        bot.send_message(call.message.chat.id,
                         'By what criteria do you want to choose a film?',
                         reply_markup=markup)
    if call.data == 'top':
        bot.send_message(call.message.chat.id, 'Here are 5 movies from top '
                                               '250. Enjoy!')
        bot.send_message(call.message.chat.id, film.top5())
    elif call.data == 'actor':
        bot.send_message(call.message.chat.id, 'Write the name of the actor:')

        @bot.message_handler(content_types=['text'])
        def send_text(message):
            bot.send_message(call.message.chat.id,
                             film.film_by_actor(message.text))
    elif call.data == 'rating':
        bot.send_message(call.message.chat.id, 'Film with rating more than 7:')
        bot.send_message(call.message.chat.id, film.rating())
    elif call.data == 'year':
        bot.send_message(call.message.chat.id, 'Write the film director:')


bot.polling()
