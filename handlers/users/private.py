from aiogram import Router, types, F
from filterlar.private import PrivateFilter


rt = Router()
@rt.message(F.text, PrivateFilter())
async def private(msg: types.Message):
    await msg.reply("Bu faqat shaxsiy chatda ishlaydi")
    return msg.chat.type == "private"






