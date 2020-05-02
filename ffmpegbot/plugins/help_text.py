from pyrogram import Client, Filters

from ffmpegbot import (HELP_STICKER, MSAADA, TMP_DOWNLOAD_DIRECTORY)

@Client.on_message(Filters.command(["start"]))
async def start_text(client, message):
    await message.reply_message(HELP_STICKER, quote=True)

@Client.on_message(Filters.command(["help"]))
async def msaada(client, message):
    await message.reply_message(MSAADA, quote=True)
