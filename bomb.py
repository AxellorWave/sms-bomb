import telebot
from user_agent import generate_user_agent
from random import randint
from telebot import types
from requests import post
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3 import disable_warnings
import time
import os
from api import *
from db import *
import json

disable_warnings(InsecureRequestWarning)
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def start(message):
    try:
        del_last_mes(message)
    except:
        pass
    print(f'Бот запущен. Пользователь{message.chat.id}')
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn_start = types.InlineKeyboardButton(text='🚀 START', callback_data='btn_start')
    kb.add(btn_start)
    mes = bot.send_photo(message.chat.id,'AgACAgIAAxkBAAIBJ2fEITIpUi2Z3lmckjVVetTikmTIAAIS8TEbSZURSupc2k6E1e10AQADAgADcwADNgQ','👋 Привет! 💣 Это бот-спаммер.\n👇 Нажми кнопку чтобы начать.',reply_markup=kb)
    put(message,'start',mes.id)

def del_last_mes(message):
    level, data , mes_id = give(message)
    bot.delete_message(chat_id = message.chat.id,message_id = mes_id)

def get_number(message,mes_id):
    bot.delete_message(chat_id = message.chat.id,message_id = message.id)
    number = message.text
    if number[0] == '+':
        number = number[1:]
    if len(number) == 11 and number[0] =='8' and number.isdigit():
        number = number.replace('8','7',1)
    elif len(number) == 10 and number.isdigit():
        number =  '7' + number
    elif len(number) == 11 and number[0] =='7' and number.isdigit():
        number = number
    else:
        number = False
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn_start = types.InlineKeyboardButton(text='🚀 START', callback_data='btn_start_spam')
    try:
        with open('whitelist.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            whitelist = data["list"]
    except:
        whitelist = []
    if number and number not in whitelist:
        put(message,'ready_to_spam',mes_id,f'{number}')
        btn_back = types.InlineKeyboardButton(text='🔙 Назад', callback_data='btn_start_b')
        kb.add(btn_start,btn_back)
        bot.edit_message_text(chat_id = message.chat.id,message_id = mes_id,text = f'📞 Номер: +{number}\n❓ Начать спам?',reply_markup=kb)
    else:
        btn_back = types.InlineKeyboardButton(text='🔙 Назад', callback_data='btn_back_to_start')
        kb.add(btn_back)
        bot.edit_message_text(chat_id = message.chat.id,message_id = mes_id,text ='❗ Некорректный номер! Попробуйте снова:',reply_markup=kb)

def edit_n(message,mes_id,n,number,info_text):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn_check = types.InlineKeyboardButton(text='🔴 ЖМИ 🔴', callback_data='btn_check')
    kb.add(btn_check)
    if n%2 == 0:
        em = '💥'
    else:
        em = '💣'
    bot.edit_message_text(chat_id = message.chat.id,message_id =mes_id,text = f'📞 Номер: +{number}\n{em} СПАМ ЗАПУЩЕН 🧨\n📨 Отправлено {n} запросов\n\nПодробнее:\n<blockquote>{info_text}</blockquote>',reply_markup = kb, parse_mode = 'html')

def spam(message,number,mes_id):
    put(message,'spam',mes_id,number)
    bot.edit_message_text(chat_id = message.chat.id,message_id =mes_id,text = f'📞 Номер: +{number}\n💣 СПАМ ЗАПУЩЕН 🧨')
    lst = ['mv(number)','dns(number, is_call=1)','sm_center(number)', 
    'citilink(number)','dns(number)','gorpay(number)','avon(number)',
    'alfabank(number)','zaymer(number)','lenta(number)','wildberries(number)',
    'kviku(number)','moe_online(number)','telegram(number)','mm(number)']
    n=0
    info_text = ''
    for i in lst:
        try:
            t = eval(i)
            info_text = info_text + f'{t}\n'
            n+=1
            edit_n(message,mes_id,n,number,info_text)
        except Exception as e:
            print(e)
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn_start = types.InlineKeyboardButton(text='🏠 В меню', callback_data='btn_back_to_start')
    btn_repeat = types.InlineKeyboardButton(text='💣 Ещё одна атака', callback_data='btn_start_spam')
    btn_another_phone = types.InlineKeyboardButton(text='📞 Изменить телефон', callback_data='btn_start_b')
    kb.add(btn_start, btn_repeat, btn_another_phone)
    bot.edit_message_text(chat_id = message.chat.id,message_id =mes_id,text = f'📞 Номер: +{number}\n🤯 Спам окончен 💥 \n📫 Отправлено {n} запросов\n\n<i><b>Подробнее:</b></i>\n<blockquote expandable>{info_text}</blockquote>',reply_markup = kb, parse_mode = 'html')

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    level, data , mes_id = give(callback.message)
    if callback.data == 'btn_start':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn_back = types.InlineKeyboardButton(text='🔙 Назад', callback_data='btn_back_to_start')
        kb.add(btn_back)
        bot.delete_message(chat_id = callback.message.chat.id,message_id =callback.message.id)
        mes = bot.send_message(chat_id = callback.message.chat.id,text = '✍🏻 Введи номер телефона:',reply_markup=kb)
        put(callback.message,'get_number',mes.id)
    elif callback.data == 'btn_start_b':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn_back = types.InlineKeyboardButton(text='🔙 Назад', callback_data='btn_back_to_start')
        kb.add(btn_back)
        bot.edit_message_text(chat_id = callback.message.chat.id, message_id =callback.message.id, text = '✍🏻 Введи номер телефона:',reply_markup=kb)
        put(callback.message,'get_number',callback.message.id)
    elif callback.data == 'btn_start_spam':
        spam(callback.message,data,mes_id)
    elif callback.data == 'btn_back_to_start':
        bot.delete_message(chat_id = callback.message.chat.id,message_id =callback.message.id)
        start(callback.message)

@bot.message_handler(content_types = ['text','photo' , 'video' ,'sticker' ])
def text(message):
    level, data , mes_id = give(message)
    if level == 'get_number':
        get_number(message, mes_id)
    else:
        bot.delete_message(chat_id = message.chat.id,message_id =message.id)

if __name__ == "__main__":
    bot.polling(non_stop = True)