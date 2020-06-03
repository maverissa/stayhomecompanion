import telebot
from telebot import types
import requests
import random
import emoji
import json
import film
import lyricsgenius
import music
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
    if call.data == 'games':
        # работа с API игр
        pass
    elif call.data == 'mus':
        # работа с API музыки
        music.buttons(call, music.mus_menu, music.mus_menu_msg)
    if call.data == music.mus_menu[0]:
        music.buttons(call, music.ht_button, music.ht_msg)
    elif call.data in music.ht_button:
        music.hitparades_song(call)
        music.buttons(call, music.ht_button, music.ht_msg)
    elif call.data == music.mus_menu[1]:
        music.buttons(call, music.genre_button, music.genre_msg)
    elif call.data in music.genre_button:
        music.genre_song(call)
        music.buttons(call, music.genre_button, music.genre_msg)
    elif call.data == music.mus_menu[2]:
        music.buttons(call, music.mood_button, music.mood_msg)
    elif call.data in music.mood_button:
        music.mood_song(call)
        music.buttons(call, music.mood_button, music.mood_msg)
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
