import telebot
from telebot import types
from bot import Bot
import logging
import sys
import time
from apis.currencyapi import import currency_api_all, currency_api_importants

bot = telebot.TeleBot(Bot.token())


@bot.message_handler(func=lambda mensagem: True if mensagem.text == 'Currency-api' else False)
@bot.message_handler(commands=['currency_api'])
def currency_api(mensagem):
    bot.send_message(mensagem.chat.id, currency_api_importants())
    with open('All-(Currency-api).txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(currency_api_all())
    doc = open('All-(Currency-api).txt', 'rb')
    bot.send_document(mensagem.chat.id, doc)

@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem):
    texto_padrao = """
*MENU INICIAL*\n
Selecione uma das APIs para realizar a consulta
/currency_api
/comando2
/comando3
/comando4
/comando5
    """
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('currency_api')
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
