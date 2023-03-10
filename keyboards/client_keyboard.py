from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


client_kb = ReplyKeyboardMarkup(resize_keyboard=True)
client_button_1 = KeyboardButton('🚘Авто в наличии')
client_button_2 = KeyboardButton('🚀Загрузить свое авто')
client_button_3 = KeyboardButton('☎️Контакты')
client_button_4 = KeyboardButton('💡Часы работы')
client_button_5 = KeyboardButton('📍Наша локация')
client_button_6 = KeyboardButton('🌟Оставить отзыв')
client_button_7 = KeyboardButton('📨Предложить')
client_button_8 = KeyboardButton('💯Акции')

client_kb.add(client_button_1).insert(client_button_2).add(client_button_3).insert(client_button_4).add(client_button_5).insert(client_button_6).add(client_button_7).insert(client_button_8)

button1 = InlineKeyboardButton(text="👎", callback_data="randomvalue_of10")
button2 = InlineKeyboardButton(text="👎👎", callback_data="randomvalue_of10")
button3 = InlineKeyboardButton(text="👌👌👌", callback_data="randomvalue_of10")
button4 = InlineKeyboardButton(text="👍👍👍👍", callback_data="randomvalue_of10")
button5 = InlineKeyboardButton(text="❤️❤️❤️❤️❤️", callback_data="randomvalue_of10")

keyboard_inline = InlineKeyboardMarkup().add(button1).add(button2).add(button3).add(button4).add(button5)

lang_button1 = InlineKeyboardButton(text="English🇺🇸", callback_data="Eng")
lang_button2 = InlineKeyboardButton(text="Русский 🇷🇺", callback_data="Ru")
lang_button3 = InlineKeyboardButton(text="Қазақша 🇰🇿", callback_data="Kz")

lang_keyboard_inline = InlineKeyboardMarkup().add(lang_button1).insert(lang_button2).insert(lang_button3)

