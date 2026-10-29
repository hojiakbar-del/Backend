from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("admin"))
async def admin(msg: types.Message):
    await msg.answer_contact("+998930476727", first_name="Hojiakbar/Dev")




