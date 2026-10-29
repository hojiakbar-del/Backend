from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("info"))
async def info(msg: types.Message):
    await msg.answer("sizga nima yordam beraolaman?")
    n = "bizning barcha kamandalarimiz:\n"
    n += "/time\n"
    n += "/info\n"
    n += "/car\n"
    n += "/test\n"
    n += "/prezident\n"
    n+="/answer\n"
    n+="/answer_photo\n"
    n+="/answer_location\n"
    n+="/answer_poll\n"
    n+="/answer_dice\n"
    n+="/delete\n"
    n+="/admin\n"
    n+="/forward\n"
    n+="/me\n"
    n+="/kuchuk\n"
    n+="/mushuk\n"
    n+="random_mushuk\n"
    n+="random_kuchuk\n"
    await msg.answer(n)

