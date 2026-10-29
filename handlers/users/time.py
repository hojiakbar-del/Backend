from aiogram import types, filters, Router
from datetime import timezone, timedelta
rt = Router()
TASHKENT=timezone(timedelta(hours=5))
@rt.message(filters.Command("time"))
async def time(msg: types.Message):
    await msg.answer(str(f"{TASHKENT}"))





