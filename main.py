import telebot
from telebot import types
import requests
import random
import emoji
import json
import film

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


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    def searching_a_song(url, n):
        response = json.loads(requests.get(url).text)
        a = random.randint(0, n)
        artist = response["tracks"]["data"][a]["artist"]["name"]
        song = response["tracks"]["data"][a]["title"]
        bot.send_message(call.message.chat.id, artist + " - " + song)
        bot.send_audio(call.message.chat.id, response["tracks"]["data"][a]
        ['preview'])

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
                         'Do you want me to choose songs according to your'
                         ' favorite genre or current mood?',
                         reply_markup=markup)
    if call.data == 'genre':
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
                         'Choose a genre:', reply_markup=markup)
    if call.data == 'indie':
        bot.send_message(call.message.chat.id,
                         'Listen to this indie song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/760160361", 60)
    if call.data == 'rnb':
        bot.send_message(call.message.chat.id,
                         'Listen to this R&B gold song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/1314725125", 50)
    if call.data == 'rap':
        bot.send_message(call.message.chat.id,
                         'Listen to this song of a rap banger ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/1996494362", 50)
    if call.data == 'jazz':
        bot.send_message(call.message.chat.id,
                         'Listen to this classic jazz song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/1615514485", 79)
    if call.data == 'pop':
        bot.send_message(call.message.chat.id,
                         'Listen to this one of the best pop songs ↓ \nIf you '
                         'want another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/1963962142", 59)
    if call.data == 'rock':
        bot.send_message(call.message.chat.id,
                         'Listen to this legendary rock song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/4383475142", 99)
    if call.data == 'electronic':
        bot.send_message(call.message.chat.id,
                         'Listen to this new electronic song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/2143562442", 77)
    if call.data == 'metal':
        bot.send_message(call.message.chat.id,
                         'Listen to this brutal metal song ↓ \nIf you want '
                         'another one, you can click on any genre again!')
        searching_a_song("https://api.deezer.com/playlist/2655390504", 99)
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
        searching_a_song("https://api.deezer.com/playlist/5709525322", 399)
    if call.data == 'good':
        bot.send_message(call.message.chat.id,
                         'Listen to this good mood song ↓ \nIf you want '
                         'another one, you can click on any mood again!')
        searching_a_song("https://api.deezer.com/playlist/4485213484", 39)
    if call.data == 'chill':
        bot.send_message(call.message.chat.id,
                         'Listen to this relaxing song ↓ \nIf you want '
                         'another one, you can click on any mood again!')
        searching_a_song("https://api.deezer.com/playlist/3338949242", 79)
    if call.data == 'workout':
        bot.send_message(call.message.chat.id,
                         'Listen to this song for home workout ↓ \nIf you want'
                         ' another one, you can click on any mood again!')
        searching_a_song("https://api.deezer.com/playlist/2153050122", 69)
    if call.data == 'romance':
        bot.send_message(call.message.chat.id,
                         'Listen to this song for a romantic evening ↓\nIf you'
                         ' want another one, you can click on any mood again!')
        searching_a_song("https://api.deezer.com/playlist/1910878662", 99)
    if call.data == 'flashback':
        bot.send_message(call.message.chat.id,
                         'Listen to this 60s song ↓ \nIf you want '
                         'another one, you can click on any mood again!')
        searching_a_song("https://api.deezer.com/playlist/620264073", 59)
    if call.data == 'home':
        bot.send_message(call.message.chat.id,
                         'Listen to this song for housework motivation ↓ \n'
                         'If you want another one, you can click on any mood '
                         'again!')
        searching_a_song("https://api.deezer.com/playlist/7421024704", 69)
    if call.data == 'party':
        bot.send_message(call.message.chat.id,
                         'Listen to this party hit ↓ \nIf you want '
                         'another one, you can click on any mood again!')
        searching_a_song("https://api.deezer.com/playlist/2097558104", 78)
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
