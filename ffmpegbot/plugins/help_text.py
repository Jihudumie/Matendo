from pyrogram import Client, Filters

from ffmpegbot import (HELP_STICKER, MSAADA_TXT, TMP_DOWNLOAD_DIRECTORY)
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler

DONATE_STRING = """*Assalaam Aleykum* Habaari za Saahizi, Hii nisehemu inayo husu Utengenezaji [my creator](t.me/Twuwbaa).\
Khamis Au Hamis Nimtengenezaji Wa Marobot Hapa Telegram Kama una hitaji Kutengenezewa Robot Kama hili onana na Mimia au nitafute Katika @Huduma
"""

@Client.on_message(Filters.command(["start"]))
async def start_text(client, message):
    await message.reply_text(HELP_STICKER, quote=True)

@Client.on_message(Filters.command(["help"]))
async def msaada(client, message):
    await message.reply_text(MSAADA_TXT, quote=True)

khamis_handler = CommandHandler("khamis", donate) migrate_handler = MessageHandler(Filters.status_update.migrate, migrate_chats)

dispatcher.add_handler(khamis_handler)
