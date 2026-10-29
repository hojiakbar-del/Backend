from aiogram import Router, filters
from random import choice
rt = Router()
dogs=["https://en.wikipedia.org/wiki/File:Blue_merle_koolie_short_coat_heading_sheep_(cropped).jpg","https://en.wikipedia.org/wiki/File:Huskiesatrest.jpg","https://en.wikipedia.org/wiki/File:Comparison_of_a_wolf_and_a_pug.png"]
# tasodif= choice(dogs)
@rt.message(filters.Command('andom_kuchuk',prefix='r'))
async def random_kuchuk(msg):
    await msg.answer_photo(choice(dogs))










