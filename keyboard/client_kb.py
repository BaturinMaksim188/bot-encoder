from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Buttons on start_message
b1_1 = KeyboardButton('Матричный')
b1_2 = KeyboardButton('ADFGX')
kb_all = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_all.add(b1_1).add(b1_2)


# kb_start
b2_1 = KeyboardButton('/start')
kb_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_start.add(b2_1)
