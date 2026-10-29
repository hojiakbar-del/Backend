from aiogram import  filters, Router, types
rt =Router()
@rt.message(filters.Command("car"))
async def car(msg: types.Message):
    await msg.answer("Car - is the one of the most used methods of transports")



