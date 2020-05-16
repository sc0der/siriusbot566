from telebot import types


markup_choos_lang = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn_tj = types.KeyboardButton('🇹🇯TJ')
btn_ru = types.KeyboardButton("🇷🇺RU")
btn_eng = types.KeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿ENG")
markup_choos_lang.add(btn_tj, btn_ru, btn_eng)

# tj - menu
markup_menu_tj = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_khiz_tj = types.KeyboardButton('📜 Хизматрасониҳо')
btn_about_tj = types.KeyboardButton("📇 Дар бораи мо")
btn_cancel_tj = types.KeyboardButton("🏃 Ба қафо")
markup_menu_tj.add(btn_khiz_tj, btn_about_tj, btn_cancel_tj)

# ru - menu
markup_menu_ru = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_khiz_ru = types.KeyboardButton('📜 Услуги')
btn_about_ru = types.KeyboardButton("📇 О нас")
btn_cancel_ru = types.KeyboardButton("🏃Назад")
markup_menu_ru.add(btn_khiz_ru, btn_about_ru, btn_cancel_ru)

# eng - menu
markup_menu_eng = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_khiz_eng = types.KeyboardButton('📜 Services')
btn_about_eng = types.KeyboardButton("📇 About")
btn_cancel_eng = types.KeyboardButton("🏃 Back")
markup_menu_eng.add(btn_khiz_eng, btn_about_eng, btn_cancel_eng)


# tj - services
markup_serv_tj = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_websites_tj = types.KeyboardButton('🌐Сомонаҳо')
btn_chatbot_tj = types.KeyboardButton("💬Чат-ботҳо")
btn_gui_tj = types.KeyboardButton("💻Десктоп-барономаҳо")
btn_logs_tj = types.KeyboardButton("🎩Логотипҳо")
btn_cancel_tj = types.KeyboardButton("🏃Ба қафо")
markup_serv_tj.row(	btn_websites_tj, btn_chatbot_tj)
markup_serv_tj.row(	btn_gui_tj, btn_logs_tj)
markup_serv_tj.row(	btn_cancel_tj)

# ru - services
markup_serv_ru = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_websites_ru = types.KeyboardButton('🌐Сайты')
btn_chatbot_ru = types.KeyboardButton("💬Чат-ботов")
btn_gui_ru = types.KeyboardButton("💻Дектопные приложения")
btn_logs_ru = types.KeyboardButton("🎩Логотипы")
btn_cancel_ru = types.KeyboardButton("🏃Назад")
markup_serv_ru.row(	btn_websites_ru, btn_chatbot_ru)
markup_serv_ru.row(	btn_gui_ru, btn_logs_ru)
markup_serv_ru.row(	btn_cancel_ru)

# eng - services
markup_serv_eng = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_websites_eng = types.KeyboardButton('🌐Websites')
btn_chatbot_eng = types.KeyboardButton("💬Chat-Bots")
btn_gui_eng = types.KeyboardButton("💻Desktop(GUI) apps")
btn_logs_eng = types.KeyboardButton("🎩Logotypes")
btn_cancel_eng = types.KeyboardButton("🏃Back")
markup_serv_eng.row(btn_websites_eng, btn_chatbot_eng)
markup_serv_eng.row(btn_gui_eng, btn_logs_eng)
markup_serv_eng.row(btn_cancel_eng)


order_tj = types.InlineKeyboardMarkup(row_width=1)
btn_order_tj = types.InlineKeyboardButton(text="Фармоиш додан", url="https://t.me/s1r1us566")
order_tj.add(btn_order_tj)

order_ru = types.InlineKeyboardMarkup(row_width=1)
btn_order_ru = types.InlineKeyboardButton(text="Заказать", url="https://t.me/s1r1us566")
order_ru.add(btn_order_ru)

order_eng = types.InlineKeyboardMarkup(row_width=1)
btn_order_eng = types.InlineKeyboardButton(text="Booking", url="https://t.me/s1r1us566")
order_eng.add(btn_order_eng)