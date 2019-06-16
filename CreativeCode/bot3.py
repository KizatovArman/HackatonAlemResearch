#!/usr/bin/env python
import random
import pickle
import telebot
from telebot import types
from telebot.types import Message

TOKEN ='503945663:AAHbe-xAAJj5W31FX7tkyoju5KhQEF_Aeos'
CATEGORY = ''
LOCATION = ''


bot = telebot.TeleBot(TOKEN)

USERS = set()

@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'Hello this bot here to accept your report. Choose  /location.')
    
@bot.message_handler(commands= ['location'])
def command_handler(message: Message):
    bot.reply_to(message, 'Here you are /RepublicKazakhstan /Akmola_region /Aktyubinsk_region /Almaty /Almaty_region /Astana /Atyrau_region /East_Kazakhstan_region /Karaganda_region /Kostanai_region /Kyzylorda_region /Mangistau_region /North_Kazakhstan_region /Pavlodar_region /Shymkent /West_Kazakhstan_region /Zhambyl_region')


@bot.message_handler(commands=['RepublicKazakhstan'])
def command_handler(message: Message):
    LOCATION = 'RepublicKazakhstan'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['Akmola_region'])
def command_handler(message: Message):
    LOCATION = 'Akmola_region'
    print(LOCATION)
    bot.reply_to(message,'Now choose  /category')

@bot.message_handler(commands=['Aktyubinsk_region'])
def command_handler(message: Message):
    LOCATION = 'Aktyubinsk_region'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['Almaty'])
def command_handler(message: Message):
    LOCATION = 'Almaty'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['Almaty_region'])
def command_handler(message: Message):
    LOCATION = 'Almaty_region'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['Astana'])
def command_handler(message: Message):
    LOCATION = 'Astana'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['Atyrau_region'])
def command_handler(message: Message):
    LOCATION = 'Atyrau_region'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['East_Kazakhstan_region'])
def command_handler(message: Message):
    LOCATION = 'East_Kazakhstan_region'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['Karaganda'])
def command_handler(message: Message):
    LOCATION = 'Karaganda'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['Kostanai_regon'])
def command_handler(message: Message):
    LOCATION = 'Kostanai_regon'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['Kyzyloda_region'])
def command_handler(message: Message):
    LOCATION = 'Kyzyloda_region'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['Mangistau_region'])
def command_handler(message: Message):
    LOCATION = 'Mangistau_region'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['North_Kazakhstan_region'])
def command_handler(message: Message):
    LOCATION = 'North_Kazakhstan_region'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['Pavlodar_region'])
def command_handler(message: Message):
    LOCATION = 'Pavlodar_region'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['Shymkent'])
def command_handler(message: Message):
    LOCATION = 'Shymkent'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['South_Kazakhstan_region'])
def command_handler(message: Message):
    LOCATION = 'South_Kazakhstan_region'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['West_Kazakhstan_region'])
def command_handler(message: Message):
    LOCATION = 'West_Kazakhstan_region'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands=['Zhambyl'])
def command_handler(message: Message):
    LOCATION = 'Zhambyl'
    print(LOCATION)
    bot.reply_to(message,'Now choose /category')

@bot.message_handler(commands= ['category'])
def command_handler(message: Message):
    bot.reply_to(message, '/business /corporation /drugoe /ecology /education /governmentcontrol /healthissues /infrastructure /MERO /publictransport /security /SPS /trudobyeotnosheniya /work /zemelnyeontosheniya /ZKH')

@bot.message_handler(commands=['work'])
def work(message):
    CATEGORY = 'work'
    print(CATEGORY)
    sent= bot.send_message(message.chat.id, 'Enter your message:')
    bot.register_next_step_handler(sent,f)

def f(message):
    docItem = CATEGORY +'.txt'
    open('./' + LOCATION+'/' +docItem, 'w').write(message.text)

@bot.message_handler(commands=['business'])
def work(message):
    CATEGORY = 'business'
    print(CATEGORY)
    sent= bot.send_message(message.chat.id, 'Enter your message:')
    bot.register_next_step_handler(sent,f)

def f(message):
    docItem = CATEGORY +'.txt'
    open('./' + LOCATION+'/' +docItem, 'w').write(message.text)

@bot.message_handler(commands=['corporation'])
def work(message):
    CATEGORY = 'corporation'
    print(CATEGORY)
    sent= bot.send_message(message.chat.id, 'Enter your message:')
    bot.register_next_step_handler(sent,f)

def f(message):
    docItem = CATEGORY +'.txt'
    open('./' + LOCATION+'/' +docItem, 'w').write(message.text)

@bot.message_handler(commands=['drugoe'])
def work(message):
    CATEGORY = 'drugoe'
    print(CATEGORY)
    sent= bot.send_message(message.chat.id, 'Enter your message:')
    bot.register_next_step_handler(sent,f)

def f(message):
    docItem = CATEGORY +'.txt'
    open('./' + LOCATION+'/' +docItem, 'w').write(message.text)

@bot.message_handler(commands=['ecology'])
def work(message):
    CATEGORY = 'ecology'
    print(CATEGORY)
    sent= bot.send_message(message.chat.id, 'Enter your message:')
    bot.register_next_step_handler(sent,f)

def f(message):
    docItem = CATEGORY +'.txt'
    open('./' + LOCATION+'/' +docItem, 'w').write(message.text)

@bot.message_handler(commands=['education'])
def work(message):
    CATEGORY = 'education'
    print(CATEGORY)
    sent= bot.send_message(message.chat.id, 'Enter your message:')
    bot.register_next_step_handler(sent,f)

def f(message):
    docItem = CATEGORY +'.txt'
    open('./' + LOCATION+'/' +docItem, 'w').write(message.text)

@bot.message_handler(commands=['governmentcontrol'])
def work(message):
    CATEGORY = 'governmetcontrol'
    print(CATEGORY)
    sent= bot.send_message(message.chat.id, 'Enter your message:')
    bot.register_next_step_handler(sent,f)

def f(message):
    docItem = CATEGORY +'.txt'
    open('./' + LOCATION+'/' +docItem, 'w').write(message.text)

@bot.message_handler(commands=['governmentcontrol'])
def work(message):
    CATEGORY = 'governmetcontrol'
    print(CATEGORY)
    sent= bot.send_message(message.chat.id, 'Enter your message:')
    bot.register_next_step_handler(sent,f)


def f(message):
    docItem = CATEGORY +'.txt'
    open('./' + LOCATION+'/' +docItem, 'w').write(message.text)






# @bot.message_handler(content_types =['document'])
# def handle_docs_photos(message):
#     try:
#         chat_id = message.chat.id
#         file_info = bot.get_file(message.document.file_id)
#         downloaded_file = bot.download_file(file_info.file_path)

#         src ='./'+LOCATION+"/"+CATEGORY+message.document.file_name
#         with open(src, 'wb') as new_file:
#             new_file.write(downloaded_file)

#         bot.reply_to(message,"added new file")
#     except Exception as e:
#         bot.reply_to(message,e )

#@bot.message_handler(commands=['start'])
#def start(message):
  #sent = bot.send_message(message.chat.id, 'Message us any info.')
  #bot.register_next_step_handler(sent, hello)

#def hello(message):
    #open('./problem.txt', 'w').write(message.chat.id + ' | ' + message.text + '||')
    #bot.send_message(message.chat.id, 'Thank you!')
    #bot.send_message(ADMIN_ID, message.chat.id + ' | ' + message.text)
 
bot.polling(timeout=60)