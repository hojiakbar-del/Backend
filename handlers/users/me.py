from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("me"))
async def me(msg: types.Message):
    n = "o'zinggiz haqingizda malumotni oling:\n"
    n += f"id: {msg.chat.id}\n"
    if msg.chat.first_name:
        n += f"ismingiz: {msg.chat.first_name}\n"
    else:
        n += f"ismingiz: mavjud emas\n"
    if msg.chat.last_name:
        n += f"last name: {msg.chat.last_name}\n"
    else:
        n += f"last name: Mavjud emas\n"
    if msg.chat.username:
        n += f"username: @{msg.chat.username}\n"
    else:
        n += f"username: mavjud emas\n"
    if msg.chat.title:
        n += f"guruh nomi: {msg.chat.title}\n"
    else:
        n += f"guruh nomi: mavjud emas\n"
    if msg.chat.type == "private":
        n += f"siz lichkada yozyapsiz"
    else:
        n += f"siz gurpada yazyapsiz"
    await msg.answer(n)
