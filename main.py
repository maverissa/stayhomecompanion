import telebot
from telebot import types
import emoji
import film
import lyricsgenius
import music

bot = telebot.TeleBot('1116307628:AAGco0iC37MG0Yy_J3p7esHABjEpedxu7u0')


def buttons(call, which_buttons, which_msg):
    i = -1
    markup = types.InlineKeyboardMarkup()
    while i < len(which_buttons) - 1:
        i += 1
        markup.add(telebot.types.InlineKeyboardButton
                   (text=which_buttons[i], callback_data=which_buttons[i]))
    bot.send_message(call.message.chat.id, which_msg, reply_markup=markup)


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
        (text=(emoji.emojize('Films:movie_camera:',
                             use_aliases=True)), callback_data='films'))
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
        # work with games API
        pass
    elif call.data == 'mus':
        # work with music API
        buttons(call, music.mus_menu, music.mus_menu_msg)
    if call.data == music.mus_menu[0]:
        buttons(call, music.ht_button, music.ht_msg)
    elif call.data in music.ht_button:
        music.hitparades_song(call)
        buttons(call, music.ht_button, music.ht_msg)
    elif call.data == music.mus_menu[1]:
        buttons(call, music.genre_button, music.genre_msg)
    elif call.data in music.genre_button:
        music.genre_song(call)
        buttons(call, music.genre_button, music.genre_msg)
    elif call.data == music.mus_menu[2]:
        buttons(call, music.mood_button, music.mood_msg)
    elif call.data in music.mood_button:
        music.mood_song(call)
        buttons(call, music.mood_button, music.mood_msg)
    elif call.data == 'films':
        # work with the movie API
        buttons(call, film.film_menu, film.film_menu_msg)
    if call.data == film.film_menu[0]:  # top5
        bot.send_message(call.message.chat.id, 'Here are 5 movies from top '
                                               '250. Enjoy!')
        bot.send_message(call.message.chat.id, film.top5())
    elif call.data == film.film_menu[1]:  # actor
        bot.send_message(call.message.chat.id,
                         emoji.emojize('Write the name of the actor. '
                                       'For the correct selection, please, '
                                       'try to write as correctly and fully'
                                       ' as possible.:revolving_hearts: '
                                       '\nExample: Leonardo DiCaprio'))

        @bot.message_handler(content_types=['text'])
        def send_text(message):
            bot.send_message(call.message.chat.id,
                             film.film_by_actor(message.text))
    elif call.data == film.film_menu[2]:  # rating
        buttons(call, film.rating_button, film.rating_msg)
    elif call.data in film.rating_button:
        if call.data == film.rating_button[0]:
            film.rating(call)
        elif call.data == film.rating_button[1]:
            film.rating(call)
    elif call.data == film.film_menu[3]:  # year
        bot.send_message(call.message.chat.id, 'Write the year:')


bot.polling()

"""
Не получилось
msg = bot.send_message(call.message.chat.id,
                               emoji.emojize(
                                   'Write the name of the actor. '
                                   'For the correct selection, please, '
                                   'try to write as correctly and fully'
                                   ' as possible.:revolving_hearts: '
                                   '\nExample: Leonardo DiCaprio'))
        bot.register_next_step_handler(msg,
                                       film.film_by_actor(message.text, call.message))
"""
