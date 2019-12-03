# -*- coding: utf-8 -*-
import types
import requests
import telebot

bot = telebot.TeleBot('1030193418:AAEP9aZ3fs4XZPISr3OBCYu6kyRcDgSd3SE')
result = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')

keyboard = telebot.types.ReplyKeyboardMarkup(True, True, False)
keyboard.row('Info', 'Convert USD in UAH')
keyboard.row('Convert EUR in UAH', 'Convert RUB in UAH')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])

def get_info(message):
    if message.text.lower() == (unicode("Info", "utf-8")).lower():
        for todo_item in result.json():
      	    if todo_item['ccy'] == "BTC":
      	       	bot.send_message(message.from_user.id, todo_item['ccy'] + ':' + todo_item['sale'] + '$')
      	    else :
	 	       	bot.send_message(message.from_user.id, todo_item['ccy'] + ':' + todo_item['sale'])	 			 
    elif message.text.lower() == (unicode("Convert USD in UAH", "utf-8")).lower():
    	bot.send_message(message.from_user.id, "USD: ")
       	bot.register_next_step_handler(message, get_USD)
    elif message.text.lower() == (unicode("Convert EUR in UAH", "utf-8")).lower():
    	bot.send_message(message.from_user.id, "EUR: ")
       	bot.register_next_step_handler(message, get_EUR)
    elif message.text.lower() == (unicode("Convert RUB in UAH", "utf-8")).lower():
    	bot.send_message(message.from_user.id, "RUR: ")
       	bot.register_next_step_handler(message, get_RUB)

def get_USD(message):
	value_USD = float(message.text)
	for todo_item in result.json():
	    if todo_item['ccy'] == "USD":
	        bot.send_message(message.from_user.id, str(value_USD) + '  ' + todo_item['ccy'] + ' = ' + str(float(todo_item['sale'])*value_USD) + '  UAH')

def get_EUR(message):
	value_EUR = float(message.text)
	for todo_item in result.json():
	    if todo_item['ccy'] == "EUR":
	        bot.send_message(message.from_user.id, str(value_EUR) + '  ' + todo_item['ccy'] + ' = ' + str(float(todo_item['sale'])*value_EUR) + '  UAH')

def get_RUB(message):
	value_RUB = float(message.text)
	for todo_item in result.json():
	    if todo_item['ccy'] == "RUR":
	        bot.send_message(message.from_user.id, str(value_RUB) + '  ' + todo_item['ccy'] + ' = ' + str(float(todo_item['sale'])*value_RUB) + '  UAH')	     

bot.polling(none_stop=True, interval=0)