
import os
import requests
from pyrogram import Client, filters

bot = Client(
    "logo bot",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)


@bot.on_message(filters.command(["logo"]))
async def logo(bot, update):
    try:      
        name = update.text.split(None, 1)[1]
        req = requests.get(f"https://sd-logo-api.herokuapp.com/?logo={name}")
        IMG = req.text
        await update.reply_photo(IMG) 
    except Exception as e:
        await update.reply_text(f"Error: {e}")
      
bot.run()
