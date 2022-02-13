import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Flare_Robot.events import register
from Flare_Robot import telethn as tbot


PHOTO = "https://telegra.ph/file/75245a9ad3562e636553f.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = "**• Hɪ, I'ᴍ sᴀᴋᴜʀᴀ . ** \n\n"
    TEXT += f"**• I'ᴍ Wᴏʀᴋɪɴɢ Pʀᴏᴘᴇʀʟʏ ** \n\n"
    TEXT += f"**• Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ  : 13.10 ** \n\n"
    TEXT += f"**• Mʏ ʜᴜʙʙʏ: [ haruki](http://t.me/baby_hoii)** \n\n"
    TEXT += f"**• Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ : 1.24.0 ** \n\n"
    TEXT += "**Tʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ , I'ʟʟ sᴇʀᴠᴇ ʏᴏᴜ ᴡᴇʟʟ!**"
    BUTTON = [
        [
            Button.url("📢 Updates", "https://t.me/Sakuraxsupport"),
            Button.url("🚑 Support", "https://t.me/Sakuraxsupport"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
