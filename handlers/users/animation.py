from aiogram import Router, types
rt = Router()
@rt.message()
async def animation(msg: types.Message):
    if msg.sticker:
        print(msg.sticker)
    else:
        print(msg.content_type)








