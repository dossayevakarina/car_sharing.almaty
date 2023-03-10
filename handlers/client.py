from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from create_bot import bot, dp
from random import randrange
from keyboards import client_kb
from data_base import sq_db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton








class FSMclient(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()









@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '/start':
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgQAAxkBAAEH-U9kAc5fGqD3fMh3-BKfr3GIx688HwACSRgAAqbxcR7zOpD5Pmgbri4E")

        await bot.send_message(chat_id=message.chat.id,
                               text="Привет привет!👋 \n\nМеня зовут Никита 🤖, я бот занимающийся арендой автомобилей и не только 🚘 Наш офис открыт для тебя с 08:00 до 22:00 ежедневно. Welcome! 🙌 \n\nМы всегда рады видеть вас у нас для подробной консультации 🌊 ",
                               reply_markup=client_kb)

        await bot.send_message(chat_id=message.chat.id,
                               text="Cпасибо, что ты с нами! 🚀 \n\nСовсем скоро я смогу рассказать о программе лояльности, рассмотреть все твои предпочтения по выбору авто, расскажу о новинках в мире аренды авто 🤩 ",
                               reply_markup=client_kb)

        await bot.send_message(chat_id=message.chat.id,
                               text="🤖 Я еще обучаюсь новым алгоритмам, но кое-что я уже умею 😎 \n\nВыбери меню и нажми кнопку👇🏼",
                               reply_markup=client_kb)


    elif message.text == '🚘Авто в наличии':
        await sq_db.command_sql_read_for_client(message)
    elif message.text == '🚀Загрузить свое авто':
        await FSMclient.photo.set()
        await message.answer("Загрузи фото своей машины! 🚘")

    elif message.text == '☎️Контакты':
        await message.answer('📍  Наш адрес: город Алматы, ЖК Gagarin Terrace, проспект Гагарина, 244 помещение 2 \n\n☎️ Наш телефон: +7‒777-777-7777')
    elif message.text == '💡Часы работы':
        await message.answer('Мы работаем с 8:00 до 22:00 ежедневно. Ждем тебя на подробную консультацию с нашим менеджером 🫶🏻')
    elif message.text == '📍Наша локация':
        await message.answer('📍  Наш адрес: город Алматы, ЖК Gagarin Terrace, проспект Гагарина, 244 помещение 2')
    elif message.text == '🌟Оставить отзыв':
        await message.reply("Привет, уважаемый клиент! \n\n🤖 Совсем недавно я видел тебя у нас. Как ты оцениваешь работу нашего менеджера?👇 ", reply_markup=keyboard_inline)
    elif message.text == '📨Предложить':
        await message.answer('🤖 Предложи идею, я передам ее людям, которые меня создали ✨ \n\nЗаписываю ⌨️')
    elif message.text == '💯Акции':
        await message.answer('На данный момент эта плюшка находится в разработке:)')




async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        await FSMclient.next()
        await message.reply("Теперь введи марку своей машины! 🚗")

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await FSMclient.next()
        await message.reply("Ого, то что надо😎, а теперь напиши подробное описание машины!")

async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        await FSMclient.next()
        await message.reply("А теперь необходимо ввести сумму, за которую ты хочешь сдавать свою машину в сутки💵")

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
        await sq_db.command_sql_add(state)
        await message.answer("Объявление успешно добавлено 🌟")
        await state.finish()

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del'))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sq_db.command_sql_delete(callback_query.data.replace("del ", ""))
    await callback_query.answer(text=f"{callback_query.data.replace('del ', '')} удалена успешно.", show_alert=True)

# @dp.message_handler(commands=['delete'])
async def command_delete(message: types.Message):
    read = await sq_db.command_sql_read_for_admin_delete()
    for ret in read:
        await bot.send_photo(message.chat.id, ret[0], f"{ret[1]}\nОписание: {ret[2]}\n Цена: {ret[-1]}")
        await bot.send_message(message.chat.id, text="Удалить вышерасположенный объект ⬆️", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"Удалить {ret[1]}",callback_data=f"del {ret[1]}")))


button1 = InlineKeyboardButton(text="👎", callback_data="dislike")
button2 = InlineKeyboardButton(text="👎👎", callback_data="dislike")
button3 = InlineKeyboardButton(text="👌👌👌", callback_data="its ok")
button4 = InlineKeyboardButton(text="👍👍👍👍", callback_data="like")
button5 = InlineKeyboardButton(text="❤️❤️❤️❤️❤️", callback_data="excellent")

keyboard_inline = InlineKeyboardMarkup().add(button1).add(button2).add(button3).add(button4).add(button5)
















def registration_client_handlers(disp: Dispatcher):
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMclient.photo)
    dp.register_message_handler(load_name, state=FSMclient.name)
    dp.register_message_handler(load_description, state=FSMclient.description)
    dp.register_message_handler(load_price, state=FSMclient.price)
    dp.register_message_handler(command_delete, commands=['delete'])




