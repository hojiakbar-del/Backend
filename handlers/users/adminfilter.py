from aiogram import Router, types, F, filters
from filterlar.admin import AdminFilter

rt = Router()

@rt.message(F.text, AdminFilter(), filters.Command("adinfilter"))
async def admin(msg: types.Message) :
    await msg.reply("Buni faqat adminlar ishlata oladi")







