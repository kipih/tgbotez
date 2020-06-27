import telebot

bot = telebot.TeleBot ('929805114:AAF2C14Cw8fBvLJYkRMAUJNpWqftvdMCQvk')


@bot.message_handler(commands=['start'])
def start_comant(message):
    bot.send_message(message.chat.id, 'Привет ты написал старт.')


bot.polling()
