from pyrogram import Client, filters
from pyrogram.errors import BadRequest
import asyncio
api_id = "24928579"
api_hash = "4e8991e8a9ae7aa37d6952d5b7ded2c5"
bot_token = "6746901593:AAFSeoh2rlv6IIxn3roB0D5gKeel9tfn0_A"
app = Client("my_bot",api_id = api_id, api_hash = api_hash,bot_token = bot_token) 
@app.on_message(filters.photo | filters.animation | filters.video | filters.document)
async def fwd(bot,message):
    try:
        await asyncio.sleep(5)
        await message.forward(-1002085625613)
    except BadRequest as e:
        print("error : " + str(e))
app.run()
