from aiogram import Router, types
rt = Router()
@rt.message()

async def test(msg: types.Message):
    if msg.contact:
        await msg.answer("Contact qabul qilindi")
    else:
        await msg.answer(text="<b>CONTACT</b> TASHAAAAAAAAAA!", parse_mode="HTML")














