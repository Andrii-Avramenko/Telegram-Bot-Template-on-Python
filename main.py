import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start']) # Команда start
def start(message):
  bot.send_message(message.chat.id, '') # Відповідь на команду

bot.polling(none_stop=True) 
