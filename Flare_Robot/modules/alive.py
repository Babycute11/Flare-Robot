import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Flare_Robot.events import register
from Flare_Robot import telethn as tbot


PHOTO = "https://telegra.ph/file/9c4cbc290219ff57fd31d.jpg"


@register(pattern=("/void"))
async def awake(event):
    TEXT = "**• Hᴇʏ ɢᴜʏs ᴊᴏɪɴ ᴏᴜʀ ғᴇᴅ ᴜsᴇ ᴛʜᴇ ɪɴsᴛʀᴜᴄᴛɪᴏɴs Bᴇʟʟᴏᴡ . ** \n\n"
    TEXT += f"**• Jᴏɪɴ Fᴇᴅ Usɪɴɢ : /joinfed 7ad20be9-ff75-4e00-847e-7eec6f32f599 ** \n\n"
    TEXT += f"**• Fᴇᴅ ɴᴀᴍᴇ : ᴠᴏɪᴅ ғᴇᴅᴇʀᴀᴛɪᴏɴ ** \n\n"
    TEXT += f"**• Oᴡɴᴇʀ : [× void ×](http://t.me/Voidxtoxic)** \n\n"
    TEXT += f"**• Aᴅᴅ sᴀᴋᴜʀᴀ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ, ᴘʀᴏᴍᴏᴛᴇ ᴀs ᴀᴅᴍɪɴ ᴀɴᴅ ᴜsᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴀʙᴏᴠᴇ   ** \n\n"
    TEXT += "**Aʀɪɢᴀᴛᴏ!**"
    BUTTON = [
        [
            Button.url("× Fᴇᴅᴇʀᴀᴛɪᴏɴ ×", "https://t.me/void_federation"),
            Button.url("× Hᴜʙʙʏ ×", "https://t.me/baby_hoii"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
