from aiogram import Router, filters
rt = Router()
@rt.message(filters.Command('mushuk'))
async def mushuk(msg):
    await msg.answer_photo('https://en.wikipedia.org/wiki/File:Sheba1.JPG')













