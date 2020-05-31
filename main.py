import deezer
import telebot
from telebot import types
bot = telebot.TeleBot('1116307628:AAGco0iC37MG0Yy_J3p7esHABjEpedxu7u0')


@bot.message_handler(commands=['start'])
def general_menu(message):
    bot.send_message(message.chat.id, 'Hello! I will do my best to make your '
                                      'home stay fascinating!')
    markup = types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Games',
                                                  callback_data='games'))
    markup.add(
        telebot.types.InlineKeyboardButton(text='Music', callback_data='mus'))
    markup.add(
        telebot.types.InlineKeyboardButton(text='Films and series',
                                           callback_data='filmsseries'))
    bot.send_message(message.chat.id, 'What do you want me to recommend you?',
                     reply_markup=markup)


client = deezer.Client()


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'games':
        # работа с API игр
        pass
    elif call.data == 'mus':
        # работа с API музыки
        markup = types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Favourite genre',
                                                      callback_data='genre'))
        markup.add(telebot.types.InlineKeyboardButton(text='Current mood',
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
            bot.send_message(call.message.chat.id,
                             'Choose a genre:', reply_markup=markup)
            print(client.get_playlist(object_id=1514808481))

        elif call.data == 'mood':
            markup = types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton
                       (text='Workout', callback_data='workout'))
            markup.add(telebot.types.InlineKeyboardButton
                       (text='Romance', callback_data='romance'))
            markup.add(telebot.types.InlineKeyboardButton
                       (text='Chill', callback_data='chill'))
            markup.add(telebot.types.InlineKeyboardButton
                       (text='Flashback', callback_data='workout'))
            markup.add(telebot.types.InlineKeyboardButton
                       (text='At home', callback_data='home'))
            markup.add(telebot.types.InlineKeyboardButton
                       (text='Party', callback_data='party'))
            bot.send_message(call.message.chat.id,
                             'Choose the option which fits your'
                             ' mood now the most:', reply_markup=markup)
    elif call.data == 'filmsseries':
        # работа с API кино
        pass


bot.polling()
