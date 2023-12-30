from pyrogram import Client, filters
from pyrogram.errors import BadRequest
import asyncio
api_id = ""
api_hash = ""
bot_token = ""
app = Client(
        "my_bot",
        api_id = api_id, api_hash = api_hash,
        bot_token = bot_token
)
@app.on_message(filters.photo | filters.animation | filters.video | filters.docu
ment)
async def fwd(bot,message):
        try:
                await asyncio.sleep(5)
                await message.forward(chanelid)
        except BadRequest as e:
                print("error : " + str(e))
app.run()
