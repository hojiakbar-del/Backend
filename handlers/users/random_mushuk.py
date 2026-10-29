from aiogram import Router, filters
from random import choice
rt = Router()
cats = ['https://en.wikipedia.org/wiki/Cat',"https://en.wikipedia.org/wiki/File:Cat_August_2010-4.jpg","https://en.wikipedia.org/wiki/File:Felis_catus-cat_on_snow.jpg"]

@rt.message(filters.Command('andom_mushuk',prefix='r'))
async def random_mushuk(msg):
    await msg.answer_photo(choice(cats))









