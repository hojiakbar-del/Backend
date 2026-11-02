from aiogram import  Router, types, F, Bot
from filterlar import admin
rt = Router()


@rt.message(F.text, admin.AdminGroupFilter())
async def admingroup(msg: types.Message):
    async def __call__(self, msg: types.Message, bot:Bot) ->bool:
        user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
        return user.status in ["creator", "administrator"]


    # await msg.reply("bu admingroup filterining test matni")









