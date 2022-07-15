import random

import telebot
import sqlite3
# Создаем экземпляр бота

connection = sqlite3.connect("anek.db")

bot = telebot.TeleBot('5575492053:AAGb_CuE9UuDVtzzqyLCUILjZuGCugtt22k')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, "Я на связи. Смогу рассмешить любого своими анекдотами!\nНапиши:\n/help - я помагаю. \nанекдоты - высылаю анекдот")
  #     bot.send_message(m.chat.id, "Я на связи. Напиши мне что-нибудь")
@bot.message_handler(commands=["help"])
def handle_text(message):
    bot.send_message(message.chat.id, "Напиши: привет")
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if(message.text == "привет"):
        bot.send_message(message.chat.id, "Привет, я бот анекдотов!")
    elif(message.text == "анекдот" or message.text == "Анекдот" or message.text == "анек"):
        connection = sqlite3.connect("anek.db")
        cursor = connection.cursor()
        cursor.execute('''SELECT anekdot FROM anek''')
        an = cursor.fetchall()[:130478]
        bot.send_message(message.chat.id, random.choice(an)[0].replace('\\n','\n'))
        connection.commit()
        connection.close()
    elif(message.text == "анекдот!" or message.text == "Анекдот!"):
        connection = sqlite3.connect("anek.db")
        cursor = connection.cursor()
        cursor.execute('''SELECT anekdot FROM anek''')
        an = cursor.fetchall()[:130478]
        bot.send_message(message.chat.id, random.choice(an)[0].replace('\\n','\n'))
        connection.commit()
        connection.close()
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю напишите /help")
# Запускаем бота
bot.polling(none_stop=True, interval=0)
