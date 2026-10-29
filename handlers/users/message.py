from aiogram import Router, filters, types,F
rt = Router()
@rt.message(filters.Command("answer"))
async def message(msg: types.Message):
    await msg.answer("Bu oddiy answer")

@rt.message(filters.Command("answer_photo"))
async def answer(msg: types.Message):
    await msg.answer_photo(photo="https://www.google.com/imgres?q=python%20bot%20commands&imgurl=https%3A%2F%2Fmiro.medium.com%2Fv2%2Fresize%3Afit%3A1400%2F1*YzeUNC8Aa778qRWiopKkFw.png&imgrefurl=https%3A%2F%2Ffaun.pub%2Fhow-to-make-a-bot-in-discord-using-python-827994e222e8&docid=fGfAzFbdKzPARM&tbnid=tECdslAhqUTRlM&vet=12ahUKEwj3vqy4p7uXAxXiRPEDHUvpG1cQnPAOegQINhAA..i&w=924&h=744&hcb=2&ved=2ahUKEwj3vqy4p7uXAxXiRPEDHUvpG1cQnPAOegQINhAA", caption="Bu answer_photo javob")

@rt.message(filters.Command("answer_location"))
async def answer(msg: types.Message):
    await msg.answer_location(latitude=38.897957, longitude=-77.036560)
    await msg.reply("Bu answer_location javob")

@rt.message(filters.Command("answer_poll"))
async def answer(msg: types.Message):
    await msg.answer_poll(question="Buglar chiqyabdimi?", options=["ha", "yoq"])
    await msg.reply("Bu answer_poll javob")

@rt.message(filters.Command("answer_dice"))
async def answer(msg: types.Message):
    await msg.answer_dice(emoji="⚽️")
    await msg.reply("Bu answer_dice javob")

@rt.message(filters.Command("delete"))
async def answer(msg: types.Message):
    await msg.delete()
    await msg.answer("Bu answer_delete javob")

@rt.message(filters.Command("forward"))
async def answer(msg: types.Message):
    await msg.forward(chat_id=7935442528)
    await msg.reply("Bu forward javob")
hammasi = [
    "CgACAgQAAxkBAAI3M2rgNcDAG8m0N9t_vSA0l5-2KBCOAAKDAwAC-pKkUoq150fdTkUEPQQ",
    "AgACAgIAAxkBAAI3PGrgNkd0yN9t-5W6dKDWGxqfuHVMAAKRG2sbN9wAAUtcYSol5wTocwEAAwIAA3gAAz0E"
]

@rt.message()
async def f(msg: types.Message):
    await msg.answer_photo(hammasi[1])
    if msg.contact:
        c = msg.contact
        n = "barcha malumotlar:\n"
        n += f"{c.first_name} {c.last_name}\n"
        n += f"{c.phone_number}"
    await msg.answer(n)
    # if msg.contact.user_id == msg.from_user.id:
    #    await msg.answer("bu rostdan sizniki")
    # else:
    #    await msg.answer("bu boshqa insonni nomer")
    # elif msg.dice:
    #    n = f"ushbu {msg.dice.emoji} ning qiymati 100%\n"
    #    n += f"{msg.dice.value} bo'ladi!"
    #     await msg.answer(n)
    # else msg.animation:
    #     print(msg.animation)
# print(msg.photo)


















