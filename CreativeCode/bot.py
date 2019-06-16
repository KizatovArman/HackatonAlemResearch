#!/usr/bin/env python
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

# @bot.message_handler(commands =['start'])
# def start(m):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard =True)
#     keyboard.add(*[types.KeyboardButton(name) for name in ['location']])
#     msg = bot.send_message(m.chat.id, 'Выбирете локацию',reply_markup=keyboard)
#     bot.register_next_step_handler(msg,name)

# def name(m):
#     if m.text == 'location':
#         bot.send_message(m.chat.id, '/Republic Kazakhstan')

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
    open('').write(message.text)
    


@bot.message_handler(commands= ['location'])
def command_handler(message: Message):
    bot.reply_to(message, 'Here you are /RepublicKazakhstan')


@bot.message_handler(commands=['RepublicKazakhstan'])
def command_handler(message: Message):
    LOCATION = "RepublicKazakhstan"
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
 
# @bot.message_handler(content_types=['text'])
# @bot.edited_message_handler(content_types=['text'])
# def echo_digits(message: Message):
#     print(message.from_user.id)
#     if 'Alex Goodkid' in message.text:
#         bot.reply_to(message, 'Alex is good kid')
#         return
#     reply = str(random.random())
#     if message.from_user.id in USERS:
#         reply += f"  {message.from_user}, hello again"
#     bot.reply_to(message, reply)
#     USERS.add(message.from_user.id)


#@bot.message_handler(content_types=['sticker'])
#def sticker_handler(message: Message):
    #bot.send_sticker(message.chat.id, STICKER_ID)


#@bot.inline_handler(lambda query: query.query)
#def query_text(inline_query):
    #print(inline_query)
    #try:
        #r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        #r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        #bot.answer_inline_query(inline_query.id, [r, r2])
    #except Exception as e:
        #print(e)


bot.polling(timeout=60)