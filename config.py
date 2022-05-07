import telebot
from telebot import types
from bot import Bot
import logging
import sys
import time
from apis.currencyapi import currencyapi

bot = telebot.TeleBot(Bot.token())


@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem):
    texto_padrao = """
*MENU INICIAL*\n
/comando1 descrição
/comando2 descrição
/comando3 descrição
/comando4 descrição
/comando5
    """
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('comando1')
    itembtn2 = types.KeyboardButton('comando2')
    itembtn3 = types.KeyboardButton('comando3')
    itembtn4 = types.KeyboardButton('comando4')
    itembtn5 = types.KeyboardButton('comando5')
    markup.row(itembtn1)
    markup.row(itembtn2)
    markup.row(itembtn3)
    markup.row(itembtn4)
    markup.row(itembtn5)
    bot.send_message(mensagem.chat.id, texto_padrao, parse_mode='Markdown', reply_markup=markup)


while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        logging.error(f'{sys.exc_info()[0]}\n({time.ctime()})\n')
        time.sleep(5)
