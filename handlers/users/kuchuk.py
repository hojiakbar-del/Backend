from aiogram import Router, filters
rt = Router()
@rt.message(filters.Command('kuchuk'))
async def kuchuk(msg):
    await msg.answer_photo('https://en.wikipedia.org/wiki/File:Black_Labrador_Retriever_-_Male_IMG_3323_(cropped).jpg')













