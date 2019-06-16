import random
import pickle
import telebot
from telebot import types
from telebot.types import Message

TOKEN ='503945663:AAHbe-xAAJj5W31FX7tkyoju5KhQEF_Aeos'
CATEGORY = ''
LOCATION = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'Hello this bot here to accept your report. Choose  /location.')



bot.polling(timeout=60)