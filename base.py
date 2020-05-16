import telebot
from telebot import types
import consts
import logging
from messages import *
from keyboards import *
import os

api_token = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(str(api_token))

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message,"💎👓 K◎rBar 👓💎", reply_markup=markup_choos_lang)   

@bot.message_handler(func=lambda message:True)
def all_lang(message):
	if message.text == "🇹🇯TJ":
		bot.reply_to(message, start_message_tj, reply_markup=markup_menu_tj)
	elif message.text == "📜 Хизматрасониҳо":
		bot.reply_to(message, serv_mess_tj, reply_markup=markup_serv_tj)
	elif message.text == "📇 Дар бораи мо":
		bot.reply_to(message, about_mess_tj)
	elif message.text == "🌐Сомонаҳо":
		bot.reply_to(message, web_mess_tj, reply_markup=order_tj)
	elif message.text == "💬Чат-ботҳо":
		bot.reply_to(message, bot_mess_tj, reply_markup=order_tj)
	elif message.text == "💻Десктоп-барономаҳо":
		bot.reply_to(message, gui_mess_tj, reply_markup=order_tj)
	elif message.text == "🎩Логотипҳо":
		bot.reply_to(message, logs_mess_tj, reply_markup=order_tj)
	elif message.text == "🏃Ба қафо":
		bot.reply_to(message, cancel_mess_tj, reply_markup=markup_choos_lang)
	elif message.text == "🇷🇺RU":
		bot.reply_to(message, start_message_ru, reply_markup=markup_menu_ru)
	elif message.text == "📜 Услуги":
		bot.reply_to(message, serv_mess_ru, reply_markup=markup_serv_ru)
	elif message.text == "📇 О нас":
		bot.reply_to(message, about_mess_ru)
	elif message.text == "🌐Сайты":
		bot.reply_to(message, web_mess_ru, reply_markup=order_ru)
	elif message.text == "💬Чат-ботов":
		bot.reply_to(message, bot_mess_ru, reply_markup=order_ru)
	elif message.text == "💻Дектопные приложения":
		bot.reply_to(message, gui_mess_ru, reply_markup=order_ru)
	elif message.text == "🎩Логотипы":
		bot.reply_to(message, logs_mess_ru, reply_markup=order_ru)
	elif message.text == "🏃Назад":
		bot.reply_to(message, cancel_mess_ru, reply_markup=markup_choos_lang)
	elif message.text == "🏴󠁧󠁢󠁥󠁮󠁧󠁿ENG":
		bot.reply_to(message, start_message_eng, reply_markup=markup_menu_eng)
	elif message.text == "📜 Services":
		bot.reply_to(message, serv_mess_eng, reply_markup=markup_serv_eng)
	elif message.text == "📇 About":
		bot.reply_to(message, about_mess_eng)
	elif message.text == "🌐Websites":
		bot.reply_to(message, web_mess_eng, reply_markup=order_eng)
	elif message.text == "💬Chat-Bots":
		bot.reply_to(message, bot_mess_eng, reply_markup=order_eng)
	elif message.text == "💻Desktop(GUI) apps":
		bot.reply_to(message, gui_mess_eng, reply_markup=order_eng)
	elif message.text == "🎩Logotypes":
		bot.reply_to(message, logs_mess_eng, reply_markup=order_eng)
	elif message.text == "🏃Back":
		bot.reply_to(message, cancel_mess_eng, reply_markup=markup_choos_lang)
	else:
		bot.reply_to(message, err_mess_eng)

bot.polling()
