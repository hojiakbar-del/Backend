from aiogram import types, filters, Bot

class AdminGroupFilter(filters.BaseFilter):
    async def __call__(self, msg: types.Message, bot:Bot) -> bool:
        if msg.chat.type != "group" or msg.chat.type != "supergroup":
            return False
        user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
        return user.status == "administrator" or user.status == "creator"










