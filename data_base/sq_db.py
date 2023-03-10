import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('telegram_cars_db')
    cur = base.cursor()
    if base:
        print("База данных успешно подключена!")
    base.execute("CREATE TABLE IF NOT EXISTS cars(img TEXT, name TEXT, description TEXT, price TEXT)")
    base.commit()


async def command_sql_add(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO cars VALUES (?, ?, ?, ?)", tuple(data.values()))
        base.commit()


async def command_sql_read_for_client(message):
    for ret in cur.execute("SELECT * FROM cars").fetchall():
        await bot.send_photo(message.chat.id, ret[0], f"{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}")


async def command_sql_read_for_admin_delete():
    return cur.execute("SELECT * FROM cars").fetchall()


async def command_sql_delete(data):
    cur.execute("DELETE FROM cars WHERE name == ?", (data,))
    base.commit()
