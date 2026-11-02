from aiogram import Router, types, F
from filterlar.private import PrivateFilter


rt = Router()
@rt.message(F.text, PrivateFilter())
async def private(msg: types.Message) -> bool:
    return msg.chat.type == "group" or msg.chat.type == "supergroup"
    await msg.reply("Bu faqat guruh/superguruhda ishlaydi")
