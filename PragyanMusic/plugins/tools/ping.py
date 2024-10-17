from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from PragyanMusic import app
from PragyanMusic.core.call import PragyanMusic
from PragyanMusic.utils import bot_sys_stats
from PragyanMusic.utils.decorators.language import language
from PragyanMusic.utils.inline import supp_markup
from config import BANNED_USERS
import aiohttp
import asyncio
from io import BytesIO
from PIL import Image, ImageEnhance  # Add these imports

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())

    # Open the image using PIL
    carbon_image = Image.open(image)

    # Increase brightness
    enhancer = ImageEnhance.Brightness(carbon_image)
    bright_image = enhancer.enhance(1.7)  # Adjust the enhancement factor as needed

    # Save the modified image to BytesIO object with increased quality
    output_image = BytesIO()
    bright_image.save(output_image, format='PNG', quality=95)  # Adjust quality as needed
    output_image.name = "carbon.png"
    return output_image

@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    PING_IMG_URL = "https://graph.org/file/b9463a0c5e01efec0c799-b1de962c295a265ea4.jpg"
    captionss = "**🥀𝐏𝐈𝐍𝐆𝐈𝐍𝐆 **"
    response = await message.reply_photo(PING_IMG_URL, caption=(captionss))
    await asyncio.sleep(1)
    await response.edit_caption("**🥀𝐏𝐈𝐍𝐆𝐈𝐍𝐆 **")
    await asyncio.sleep(1)
    await response.edit_caption("**🥀𝐏𝐈𝐍𝐆𝐈𝐍𝐆 .**")
    await asyncio.sleep(1)
    await response.edit_caption("**🥀𝐏𝐈𝐍𝐆𝐈𝐍𝐆 .**")
    await asyncio.sleep(1.5)
    await response.edit_caption("**🥀𝐏𝐈𝐍𝐆𝐈𝐍𝐆 .**")
    await asyncio.sleep(2)
    await response.edit_caption("**🥀𝐏𝐈𝐍𝐆𝐈𝐍𝐆 ..**")
    await asyncio.sleep(2)
    await response.edit_caption("**𝐀𝐍𝐀𝐋𝐘𝐒𝐈𝐍𝐆 !**")
    await asyncio.sleep(3)
    await response.edit_caption("**📩𝐒𝐄𝐍𝐃𝐈𝐍𝐆...**")
    start = datetime.now()
    pytgping = await PragyanMusic.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    text =  _["ping_2"].format(resp, app.name, UP, RAM, CPU, DISK, pytgping)
    carbon = await make_carbon(text)
    captions = "**ㅤ 🏓𝐏𝐈𝐍𝐆 𝐏𝐎𝐍𝐆✨💞**"
    await message.reply_photo((carbon), caption=captions,
    reply_markup=InlineKeyboardMarkup(
            [
                [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="✦ ɢʀᴏᴜᴘ ✦", url=f"https://t.me/CodeSavy",
            ),
            InlineKeyboardButton(
                text="✧ ᴍᴏʀᴇ ✧", url=f"https://t.me/CodeSavy",
            )
        ],
        [
            InlineKeyboardButton(
                text="❅ ʜᴇʟᴘ ❅", callback_data="settings_back_helper"
            )
        ],
    ]
    ),
        )
    await response.delete()
