import telebot
from telebot import types
import emoji
import film
import lyricsgenius
import music
import os
import game
import time
subscribers = []
bot = telebot.TeleBot('1116307628:AAGco0iC37MG0Yy_J3p7esHABjEpedxu7u0')


def buttons(call, which_buttons, which_msg):
    i = -1
    markup = types.InlineKeyboardMarkup()
    while i < len(which_buttons) - 1:
        i += 1
        markup.add(telebot.types.InlineKeyboardButton
                   (text=which_buttons[i], callback_data=which_buttons[i]))
    bot.send_message(call.message.chat.id, which_msg, reply_markup=markup)


def updating_subscribers():
    with open('subscribers.txt', 'r', encoding='utf-8') as s:
        for line in s:
            line = line.split('\n')
            if line[0] not in subscribers:
                subscribers.append(line[0])


@bot.message_handler(commands=["start"])
def greetings(message):
    bot.send_message(message.chat.id, 'Hello! I will do my best to make your '
                                      'home stay fascinating!')
    bot.send_message(message.chat.id, 'You can use such commands:'
                                      '\n/start - when you use the bot for th'
                                      'e first time or if you want to get the '
                                      'message with commands.\n/recommendation'
                                      's - to get an advice on games, films or'
                                      ' music.\n/lyrics - to get the lyrics of'
                                      ' any song.\n/weekly_mailing - to subscr'
                                      'ibe or unsubscribe to our weekly compil'
                                      'ations of fresh sapid games, films and '
                                      'series or music for you.')


@bot.message_handler(commands=["weekly_mailing"])
def defining_a_subscription(message):
    global subscribers
    updating_subscribers()
    if str(message.chat.id) not in subscribers or \
            os.stat("subscribers.txt").st_size == 0:
        markup = types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Yes',
                                                      callback_data='Yes'))
        markup.add(telebot.types.InlineKeyboardButton(text='No',
                                                      callback_data='No'))
        bot.send_message(message.chat.id,
                         'Do you want to subscribe to our weekly mailing?',
                         reply_markup=markup)
    if str(message.chat.id) in subscribers:
        markup = types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Yes',
                                                      callback_data='yes'))
        markup.add(telebot.types.InlineKeyboardButton(text='No',
                                                      callback_data='no'))
        bot.send_message(message.chat.id,
                         'You are already subscribed to the mailing. Do you wa'
                         'nt to stop receiving it?', reply_markup=markup)


@bot.message_handler(commands=["NTcddme4C5"])
def mailing(message):
    subscribers_li = []
    with open('subscribers.txt', 'r', encoding='utf-8') as s:
        for line in s:
            subscribers_li.append(line)
        for i in subscribers_li:
            bot.send_message(i, "Enjoy our weekly compilation!\nLatest music:")
            music.searching_a_song('https://api.deezer.com/playlist/7131475044'
                                   '', 74, 3, i)
            bot.send_message(i, 'Here is a hot new game:\n' +
                             game.random_game_year())
            bot.send_message(i, 'Here is one of the best movies of 19-20s:\n')
            film.film_subscription(i)


@bot.message_handler(commands=["lyrics"])
def lyrics_handler(message):
    msg = bot.send_message(message.chat.id,
                           'Input the name of a song, an artist.\nFor '
                           'example: Little 15, Depeche Mode')
    bot.register_next_step_handler(msg, song_lyrics)


def song_lyrics(message):
    answer = message.text
    genius = lyricsgenius.Genius("-pxwr2wPA_q6ivrxgtD8Yb1BmOM4bUnFQF-6eMG9ROZz"
                                 "e-diXrdoAhLIyxYGd0Hb")
    answer = answer.split(',')
    try:
        song_search = genius.search_song(answer[0], answer[1])
        bot.send_message(message.chat.id, song_search.lyrics)
    except Exception:
        bot.send_message(message.chat.id, emoji.emojize(
            "Sorry, I didn't find such a song :cry:", use_aliases=True))


@bot.message_handler(commands=["recommendations"])
def general_menu(message):
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
        (text=(emoji.emojize('Сinematograph :movie_camera:',
                             use_aliases=True)), callback_data='films'))
    bot.send_message(message.chat.id, 'What do you want me to recommend you?',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'games':  # work with games API
        buttons(call, game.buttons, game.msg)
    if call.data == game.buttons[0]:
        bot.send_message(call.message.chat.id, 'Here is a random game! ')
        bot.send_message(call.message.chat.id, game.random_game())

    elif call.data == game.buttons[1]:
        bot.send_message(call.message.chat.id, 'Here is a random game with '
                                               'high rating! ')
        bot.send_message(call.message.chat.id, game.random_game_rating())

    elif call.data == game.buttons[2]:
        bot.send_message(call.message.chat.id, 'Here is a random action game!')
        bot.send_message(call.message.chat.id, game.random_game_action())

    elif call.data == game.buttons[3]:
        bot.send_message(call.message.chat.id, 'Here is a random rpg game! ')
        bot.send_message(call.message.chat.id, game.random_game_rpg())

    elif call.data == game.buttons[4]:
        bot.send_message(call.message.chat.id, 'Here is a random arcade game!')
        bot.send_message(call.message.chat.id, game.random_game_arcade())
    elif call.data == 'mus':  # work with music API
        buttons(call, music.mus_menu, music.mus_menu_msg)
    if call.data == music.mus_menu[0]:  # hit parades
        buttons(call, music.ht_button, music.ht_msg)
    elif call.data in music.ht_button:
        music.hitparades_song(call)
        buttons(call, music.ht_button, music.ht_msg)
    elif call.data == music.mus_menu[1]:  # genre
        buttons(call, music.genre_button, music.genre_msg)
    elif call.data in music.genre_button:
        music.genre_song(call)
        buttons(call, music.genre_button, music.genre_msg)
    elif call.data == music.mus_menu[2]:  # mood
        buttons(call, music.mood_button, music.mood_msg)
    elif call.data in music.mood_button:
        music.mood_song(call)
        buttons(call, music.mood_button, music.mood_msg)
    elif call.data == 'films':  # work with the movie API
        buttons(call, film.film_menu, film.film_menu_msg)
    if call.data == film.film_menu[0]:  # top5
        bot.send_message(call.message.chat.id, 'Here are 5 movies from top '
                                               '250. Enjoy!')
        bot.send_message(call.message.chat.id, film.top5())
        buttons(call, film.film_menu, film.film_menu_msg)
    elif call.data == film.film_menu[1]:  # actor
        bot.send_message(call.from_user.id,
                         emoji.emojize('Write the name of the actor. '
                                       'For the correct selection, please, '
                                       'try to write as correctly and fully'
                                       ' as possible.:revolving_hearts: '
                                       '\nExample: Leonardo DiCaprio'))

        @bot.message_handler(content_types=['text'])
        def send_text(message):
            bot.send_message(message.chat.id,
                             film.film_by_actor(message.text))
    elif call.data == film.film_menu[2]:  # rating
        buttons(call, film.rating_button, film.rating_msg)
    elif call.data in film.rating_button:
        film.rating(call)
        buttons(call, film.rating_button, film.rating_msg)
    elif call.data == film.film_menu[3]:  # year
        buttons(call, film.year_button, film.year_msg)
    elif call.data in film.year_button:
        film.by_year(call)
        buttons(call, film.year_button, film.year_msg)
    if call.data == 'Yes':  # subscription
        updating_subscribers()
        subscribers.append(str(call.from_user.id))
        with open('subscribers.txt', 'w', encoding='utf-8') as s:
            for i in subscribers:
                s.write(str(i) + '\n')
        bot.send_message(call.message.chat.id,
                         'From this moment every week you will receive '
                         'fascinating games, films and music fresh compilation'
                         's from us!')
    elif call.data == 'No':
        bot.send_message(call.message.chat.id,
                         'OK. But keep in mind that you can miss really cool '
                         'compilations from us.')
    elif call.data == 'yes':
        subscribers.remove(str(call.from_user.id))
        with open('subscribers.txt', 'w', encoding='utf-8') as s:
            for i in subscribers:
                s.write(str(i) + '\n')
        bot.send_message(call.message.chat.id,
                         'From this moment you will not get our fascinatin'
                         'g games, films and music fresh '
                         'compilations every week')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, "OK. Hope you enjoy it!")


bot.polling()
