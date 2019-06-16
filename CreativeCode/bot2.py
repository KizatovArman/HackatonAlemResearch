#!/usr/bin/env python
#-*- coding: utf8 -*- 
import random
import pickle

import telebot
from telebot import types
from telebot.types import Message

TOKEN ='503945663:AAHbe-xAAJj5W31FX7tkyoju5KhQEF_Aeos'
STICKER_ID = 'CAADAgADXwMAAgw7AAEKTh8jAAH9Q-gAAQI'
CATEGORY = 'work'
LOCATION = 'RepublicKazakhstan'


bot = telebot.TeleBot(TOKEN)

USERS = set()

@bot.message_handler(commands =['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard =True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['location']])
    msg = bot.send_message(m.chat.id, 'Выбирете локацию',reply_markup=keyboard)
    bot.register_next_step_handler(msg,name)

# def name(m):
#     if m.text == 'location':
#         bot.send_message(m.chat.id, '/Republic Kazakhstan')

def option(bot, update):
    button = [
        [InlineKeyboardButton("Республика Казахстан", callback_data="0"),
         InlineKeyboardButton("г.Астана", callback_data="1")],
         InlineKeyboardButton("г.Астана", callback_data="2")],
         InlineKeyboardButton("г.Астана", callback_data="3"),
         InlineKeyboardButton("г.Астана", callback_data="4"),
        InlineKeyboardButton("г.Алматы", callback_data="5"),
        InlineKeyboardButton("г.Алматы", callback_data="6"),
        InlineKeyboardButton("г.Алматы", callback_data="7"),
        InlineKeyboardButton("г.Алматы", callback_data="8"),
        InlineKeyboardButton("г.Алматы", callback_data="9"),
        InlineKeyboardButton("г.Алматы", callback_data="10"),
        InlineKeyboardButton("г.Алматы", callback_data="11"),
        InlineKeyboardButton("г.Алматы", callback_data="12"),
        InlineKeyboardButton("г.Алматы", callback_data="13"),
        InlineKeyboardButton("г.Алматы", callback_data="14"),
        InlineKeyboardButton("г.Алматы", callback_data="15"),
        InlineKeyboardButton("г.Алматы", callback_data="16"),
        [InlineKeyboardButton("г.Алматы", callback_data="17"),
    ]
    reply_markup = InlineKeyboardMarkup(button)

    bot.send_message(chat_id=update.message.chat_id,
                     text="Choose one option..",
                     reply_markup=reply_markup)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'Hello this bot here to accept your report. Choose /location.')

@bot.message_handler(commands=['work'])
def work(message):
    CATEGORY = "work"
    sent= bot.send_message(message.chat.id, 'Enter your message:')
    bot.register_next_step_handler(sent,f)

def f(message):
    docItem = CATEGORY +'.txt'
    open('./%s'%(LOCATION)+'.txt').write(message.text)
    

def name(m):
    if m.text == 'location':
        bot.reply_to(m, '/РеспубликаКазахстан, ' '/г.Астана, ' '/г. Алматы, ' 'Акмолинская область, ' 'Актюбинская область, ' 'Алматинская область, ' 'Атырауская область, ''Западно-Казахстанская область, ''Жамбылская область, ''Карагандинская область, ''Костанайская область, ''Кызылординская область, ''Мангистауская область, ' 'Южно-Казахстанская область, ''Павлодарская область, ''Северо-Казахстанская область, ''Восточно-Казахстанская область,' 'г. Шымкент')


@bot.message_handler(commands= ['location'])
def command_handler(message: Message):
    bot.reply_to(message, 'Here you are /RepublicKazakhstan')


@bot.message_handler(commands=['RepublicKazakhstan', 'РеспубликаКазахстан'])
def command_handler(message: Message):
    LOCATION == "RepublicKazakhstan"
    bot.reply_to(message,'Now choose /category')




@bot.message_handler(commands= ['category'])
def command_handler(message: Message):
    bot.reply_to(message, '/work')


#@bot.message_handler(content_types =['document'])
#def handle_docs_photos(message):
    #try:
        #chat_id = message.chat.id
        #file_info = bot.get_file(message.document.file_id)
        #downloaded_file = bot.download_file(file_info.file_path)

        #src ='./document/' +message.document.file_name
        #with open(src, 'wb') as new_file:
            #new_file.write(downloaded_file)

        #bot.reply_to(message,"added new file")
    #except Exception as e:
        #bot.reply_to(message,e )

#@bot.message_handler(commands=['start'])
#def start(message):
  #sent = bot.send_message(message.chat.id, 'Message us any info.')
  #bot.register_next_step_handler(sent, hello)

#def hello(message):
    #open('./problem.txt', 'w').write(message.chat.id + ' | ' + message.text + '||')
    #bot.send_message(message.chat.id, 'Thank you!')
    #bot.send_message(ADMIN_ID, message.chat.id + ' | ' + message.text)
 




bot.polling(timeout=60)