from aiogram import filters, Router

rt = Router()
@rt.message(filters.Command("prezident"))
async def prezident(msg):
    await msg.answer_photo("https://www.google.com/imgres?q=Sh.%20Mirziyoyev&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F5%2F54%2FShavkat_Mirziyoyev_official_portrait.jpg%3Futm_source%3Duz.wikipedia.org%26utm_campaign%3Dindex%26utm_content%3Doriginal&imgrefurl=https%3A%2F%2Fuz.wikipedia.org%2Fwiki%2FShavkat_Mirziyoyev&docid=-LHIIod86CdeyM&tbnid=kJZNAmkRxs5zSM&vet=12ahUKEwiksNrEoruXAxUiTqQEHTdBPNIQnPAOegQIMxAA..i&w=1028&h=1200&hcb=2&ved=2ahUKEwiksNrEoruXAxUiTqQEHTdBPNIQnPAOegQIMxAA")


























